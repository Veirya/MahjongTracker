# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 12:29:45 2024

@author: Giovanni "Veirya" Oliver

MahjongTracker
---------------------------------
Pythong tool to help keep track of various mahjong hands I've had and how I
lost/won the hand.
"""

import tkinter as tk
from tilePngs import gen_img_table
import re

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
    # end def

    def get_root(self):
        return self.root
    
    '''
    Read a mahjong hand represented by an MPSZ notation string and returns
    a list of Labels with the respective tile image ordered as listed in the
    string. Called tiles should be separated by a space, and face-down tiles
    from Kan as 'b1'.
    Input: String in MPSZ notation
    Output: List of tkinter laberls
    '''
    def _read_hand(self, input):
        res = []
        matches = re.findall(r'[mpszb][0-9]*| ', input)
        for mtch in matches:
            # Spacer for called tiles
            if mtch == ' ':
                label = tk.Label(self.root, width=5)
                label.configure(background = 'gray66')
                res.append(label)
            else:
                for d in mtch[1:]:
                    # Assign the label's image according to tile
                    img = self.TILE_IMAGES[mtch[0]][d]
                    label = tk.Label(self.root, image = img)
                    label.configure(background = 'gray66')
                    res.append(label)
                # end for
            # end if
        # end for
        return res
    # end def
    
    '''
    Function scripting the current feature under test.
    '''
    def current_test(self):
        # Read in a test input and display it
        test = 'm123p406s55789 z666'
        handLabels = self._read_hand(test)

        # Arrange the labels according to position in list
        for i, label in enumerate(handLabels):
            label.grid(row=1, column = i, columnspan = 1)
        # end for
    #end def
#end class
    
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = MahjongTracker(root)
        app.current_test()
        app.get_root().mainloop()
    except Exception as e:
        print(e)
        root.destroy()
#end if

