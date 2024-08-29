# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:29:45 2024

@author: Giovanni "Veirya" Oliver

MahjongTracker
---------------------------------
Pythong tool to help keep track of various mahjong hands I've had and how I
lost/won the hand.
"""

import json
import traceback
import tkinter as tk
from tkinter.font import Font as tkFont
from pathlib import Path
from Util.tilePngs import gen_img_table
from Util.HandViewer import HandViewer
from Util.InputFrame import InputFrame

'''
Core of the app, requiring a base tkinter window/root to use
'''
class MahjongTracker:
    def __init__(self, master, tiles, sf, bg='gray66'):
        self.master = master
        self.tiles = tiles      # Map of tile images to MPSZ notation
        self.sf = sf            # Save file for hands
        self.bg = bg            # Background color
        self.addStatText = ''   # Used to set status text when adding hands
        self.buttonFont = tkFont(size=20, weight='bold')
        
        # Initialize sub-frames and their widgets
        ## Hand Display ##
        # Displays the hands that have been loaded
        self.handViewer = HandViewer(self.master, self.bg, bd=2)
        
        ## Control Frame ##
        # Hosts the control buttons. Not encapsulated in its own class as the
        # controls regularly interface with the main app.
        self.controlFrame = tk.Frame(self.master,bg=self.bg, bd=2,
                                     relief='solid')
        self.quitButton = tk.Button(
                                    self.controlFrame, bg='red', text='Quit',
                                    command=self._exit_app, height=2,
                                    font=self.buttonFont
                                    )
        self.saveButton = tk.Button(
                                    self.controlFrame, bg='light gray',
                                    text='Save', command=self._save_hands,
                                    height=2, font=self.buttonFont
                                    )
        self.reloadButton = tk.Button(
                                      self.controlFrame, bg='light gray',
                                      text='Reload', command=self._load_hands,
                                      height=2, font=self.buttonFont
                                      )
        self.addStatus = tk.Label(
                                  self.controlFrame, bg=self.bg,
                                  textvariable=self.addStatText
                                  )
        self.addButton = tk.Button(
                                   self.controlFrame, bg='light gray',
                                   text='Add Hand', command=self._add_hand,
                                   height=2, font=self.buttonFont,
                                   )
        
        ## Input Frame ##
        # Hosts the input fields, boxes, and buttons
        self.inputFrame = InputFrame(self.master, bg=self.bg, bd=2)
        
        # Load any saved hands
        self._load_hands()
        # Arrange and setup scaling for sub-frames
        self.__setup_subframes()

    def get_root(self):
        return self.master
    
    '''
    Loads previously saved hand data and creates frames for it.
    '''
    def _load_hands(self):
        try:
            print("Loading hands...")
            with open(self.sf, 'r') as f:
                data = json.load(f)
            self.handViewer.import_hands(data, self.tiles)
            print("Hands loaded.")
        except FileNotFoundError:
            Path.mkdir("Data", exist_ok=True)
            open(self.sf, 'w').close()
            print("Save file not found. Intialized save file and directory.")
    # end def
    
    '''
    Save all loaded hands as JSON list. Overwrites the current save.
    '''
    def _save_hands(self):
        print("Writing loaded hands to " + self.sf + "...")
        handData = self.handViewer.export_hands()
        with open(self.sf, 'w') as f:
            json.dump(handData, f, indent=4)
        # end with
        print("Write complete.")
    # end def
    
    '''
    Add a hand specified in the input section to the loaded hands.
    '''
    def _add_hand(self):
        # Get the raw input and key map from the input frame
        rawData = self.inputFrame.get_input()
        # Don't do the rest if it failed and note the failure
        if rawData == -1:
            # TODO: Add label for fail status
            return
        # Pack it the way HandFrame wants it
        handData = {}
        for inp, key in rawData:
            handData[key] = inp
        # end for
        
        self.handViewer.add_hand(handData, self.tiles)
    # end def
    
    '''
    Arrange the child frames and their grid scaling.
    '''
    def __setup_subframes(self):
        # The grid is planned to be 10x13
        ## Hand Display ##
        self.handViewer.get_outer().grid(row=0, column=0, rowspan=8,
                                         columnspan=11, sticky='news')
        
        self.controlFrame.grid(row=0, column=11, rowspan=10, columnspan=2,
                               sticky='news')
        self.quitButton.pack(fill='both', side='top', expand=0)
        self.saveButton.pack(fill='both', side='top', expand=0)
        self.reloadButton.pack(fill='both', side='top', expand=0)
        self.addButton.pack(fill='both', side='bottom', expand=0, pady=(0,5))
        
        self.inputFrame.get_frame().grid(row=8, column=0, rowspan=2,
                                         columnspan=11, sticky='news')
    # end def
    
    def _exit_app(self):
        print("Saving hands and exiting app...")
        self._save_hands()
        self.master.destroy()
    
#end class
    
if __name__ == "__main__":
    try:
        # Initialize and set up the root window
        SAVE_FILE = "Data/saved_hands.json"
        root = tk.Tk()
        root.title("MahjongTracker")
        root.configure(background='gray66')
        root.minsize(1900, 1080)
        # Have the columns and rows for the hand viewer expand
        [root.grid_rowconfigure(i, weight=1) for i in range(8)]
        [root.grid_columnconfigure(i, weight=1) for i in range(12)]
        app = MahjongTracker(root, gen_img_table(10), SAVE_FILE)
        root.mainloop()
    except Exception:
        # This T/E makes errors while running in the IDE much more tolerable
        print(traceback.format_exc())
        root.destroy()
#end if

