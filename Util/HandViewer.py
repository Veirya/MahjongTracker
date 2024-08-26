# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:48:55 2024

@author: giova

Class to encapsulate the section of the app where the saved hands are displayed
"""
import tkinter as tk
from Util.HandFrame import HandFrame

class HandViewer:
    def __init__(self, master, bg, bd=0, relief='solid'):
        self.bg = bg
        self.outerFrame = tk.Frame(master, bg=self.bg, borderwidth=bd,
                                   relief=relief)
        self.canvas = tk.Canvas(self.outerFrame)
        self.scroll = tk.Scrollbar(self.outerFrame, orient=tk.VERTICAL,
                                       command=self.canvas.yview,
                                       troughcolor=self.bg)
        self.innerFrame = tk.Frame(self.canvas, bg=self.bg)
        self.canvasWindow = self.canvas.create_window((0,0),
                                                      window=self.innerFrame,
                                                      anchor='nw')
        self.loadedHands = []
        self.__setup_subframes()

    '''
    Return the outer frame for organization in the master
    '''
    def get_outer(self):
        return self.outerFrame
    
    '''
    Converts a list of hand data into corresponding HandFrames and arranges
    them in the inner display frame.
    '''
    def import_hands(self, handData, tiles):
        # Wipe out existing frames
        if len(self.loadedHands):
            [frame.get_frame().destroy() for frame in self.loadedHands]
        # Load in the frames
        self.loadedHands = [HandFrame(self.innerFrame, hand, tiles,
                                  self.bg, bd=1) for hand in handData]
        # Arrange them in the inner frame
        for i, frame in enumerate(self.loadedHands):
            frame.get_frame().grid(row=i, column=0, sticky='news')
        # end for
    # End def
    
    '''
    Exports currently loaded hands as JSON data.
    '''
    def export_hands(self):
        return [hand.get_data() for hand in self.loadedHands]
    
    '''
    Arrange all of the sub frames and their scaling in the viewer frame
    '''
    def __setup_subframes(self):
        self.canvas.grid(row=0, column=0, sticky='news')
        self.scroll.grid(row=0, column=1, sticky='ns')
        # Canvas should fill width not occupied by the scrollbar, both should
        # fill the available vertical space.
        self.outerFrame.grid_columnconfigure(0, weight=1)
        self.outerFrame.grid_rowconfigure(0, weight=1)
        self.innerFrame.grid_columnconfigure(0, weight=1)
        # Needed for Scrolling to work
        self.canvas.config(yscrollcommand = self.scroll.set)
        self.canvas.bind('<Configure>', self.__canvas_on_config)
    # end def
    
    '''
    Binded to canvas' Configure events. Allows for scrolling of the canvas
    and expands the canvas window into any empty space within the canvas.
    '''
    def __canvas_on_config(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.itemconfig(self.canvasWindow, width=event.width-1)
    
# end class