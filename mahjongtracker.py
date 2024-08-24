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
from tilePngs import gen_img_table
from Util.HandFrame import HandFrame
'''
Core of the app, requiring a base tkinter window/root to use
'''
class MahjongTracker:
    def __init__(self, root):
        # Set up root tk window
        self.root = root
        self.root.title("MahjongTracker")
        self.MAIN_BG = "gray66"
        self.root.configure(background='gray66')
        self.root.minsize(1900, 1080)
        # Import tile images at 1/X scale
        self.TILE_IMAGES = gen_img_table(10)
        self.loadedHands = []

    def get_root(self):
        return self.root
    
    '''
    Loads previously saved hand data and creates frames for it.
    '''
    def _load_hands(self):
        try:
            with open("Data/saved_hands.json", 'r') as f:
                data = json.load(f)
            self.loadedHands = [HandFrame(self.root, hand, self.TILE_IMAGES,
                                      self.MAIN_BG) for hand in data]
        except FileNotFoundError:
            print("No save file was found. Skipping Load.")
    # end def
    
    '''
    Save all loaded hands as JSON list. Overwrites the current save.
    '''
    def _save_hands(self):
        with open("Data/saved_hands.json", 'w') as f:
            handData = [hand.get_data() for hand in self.loadedHands]
            json.dump(handData, f, indent=4)
        # end with
    # end def
    
    '''
    Function scripting the current feature under test.
    '''
    # TODO: Remove when system is more interactable
    def current_test(self):
        # Load hands from the current data
        self._load_hands()
        #self._save_hands()
        for i, hand in enumerate(self.loadedHands):
            hand.get_frame().grid(row=i, column=0, sticky='ew')
        root.grid_columnconfigure(0, weight=1)
    #end def
#end class
    
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MahjongTracker(root)
        app.current_test()
        root.mainloop()
    except Exception:
        # This T/E makes errors while running in the IDE much more tolerable
        print(traceback.format_exc())
        root.destroy()
#end if

