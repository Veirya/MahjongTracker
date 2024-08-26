# -*- coding: utf-8 -*-
"""
Created on Sun Aug 2 15:19:45 2024

@author: Giovanni "Veirya" Oliver

Class to represent a frame for a particular mahjong hand. The handData keys
in init also serves as the template for json data for a given hand.
"""
import tkinter as tk
import re

class HandFrame:
    def __init__(self, master, handData, images, bg, bd=0, relief='solid'):
        # Load the Basics
        self.images = images    # Tile PNGs
        self.bg = bg            # BG Color
        self.frame = tk.Frame(master, bg=bg, bd=bd, relief=relief)  # Own tkinter frame
        self.rawHand = handData["hand"]     # MPSZ notation string for hand
        self.hand = self._read_hand(self.rawHand)   # Labels for hand
        self.rawDora = handData["dora"]     # MPSZ notation string for doras
        self.dora = self._read_hand(self.rawDora)   # Labels for doras
        self.shanten = handData["shanten"]  # Shanten of hand
        self.accepts = handData["accepts"]  # Tiles that reduce shanten 
        self.yaku = handData["yaku"]    # Main Yaku intended for hand
        self.furiten = handData["furiten"]  # In Furiten?
        self.won = handData["won"]  # Did you win the hand?
        self.rtn = handData["rtn"]  # Ron/Tsumo/Neither
        self.left = handData["left"]    # How many tiles left in the wall
        self.where = handData["where"]  # Where was what you needed (tenpai)
        self.start = handData["start"]  # Dealt hand + first draw
        
        # Then do arrangements
        self._arrange_hand()
        
    def get_frame(self):
        return self.frame
    
    '''
    Back out the hand's data for JSON packaging
    '''
    def get_data(self):
        data = {}
        data["hand"] = self.rawHand
        data["dora"] = self.rawDora
        data["shanten"] = self.shanten
        data["accepts"] = self.accepts
        data["yaku"] = self.yaku
        data["furiten"] = self.furiten
        data["won"] = self.won
        data["rtn"] = self.won
        data["left"] = self.left
        data["where"] = self.where
        data["start"] = self.start
        
        return data
    # end def
    
    '''
    Read a MPSZ notation string and return a list of Labels with the respective
    tile images ordered as listed in the string. Called tiles should be
    separated by a space, and face-down tiles from Kan as 'b1'.
    Input: String in MPSZ notation
    Output: List of tkinter laberls
    '''
    def _read_hand(self, input):
        res = []
        matches = re.findall(r'[mpszb][0-9]*| ', input)
        for mtch in matches:
            # Spacer for called tiles
            if mtch == ' ':
                label = tk.Label(self.frame, width=5)
                label.configure(background=self.bg)
                res.append(label)
            else:
                for d in mtch[1:]:
                    # Assign the label's image according to tile
                    img = self.images[mtch[0]][d]
                    label = tk.Label(self.frame, image=img)
                    label.configure(background=self.bg)
                    res.append(label)
                # end for
            # end if
        # end for
        return res
    # end def
    
    # Arrange the parts of the hand in the frame
    def _arrange_hand(self):
        # Arrange the labels according to position in list
        for i, label in enumerate(self.hand):
            label.grid(row=0, column = i, columnspan = 1)
        # end for
    # end def
# end class
