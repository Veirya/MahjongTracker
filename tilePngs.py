# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:15:56 2024

@author: Giovanni "Veirya" Oliver

Imports the tile images for MahjongTracker as tkinter PhotoImages.
Image credits to FluffyStuff @github
https://github.com/FluffyStuff/riichi-mahjong-tiles/tree/master
"""

from tkinter import PhotoImage
import os
import re
LOC = "Resources/Tile_Graphics"

# Note that 'scale' is a downscaling factor.
def gen_img_table(scale=1):
    directory = os.fsencode(LOC)
    res = {'z':{},
                   'm':{},
                   'p':{},
                   's':{},
                   'b':{}
                  }
    
    for file in os.listdir(directory):
        fn = os.fsdecode(file)  # Get file name
        cat = fn[0].lower()     # Tile category
        # Tile number
        num = '1' if fn[0] == 'B' else re.search(r'\d', fn).group()
        # Generate a PhotoImage for the file assigned to the tile code
        print("Adding {}/{} as {}{}".format(LOC, fn, cat, num))
        res[cat][num] = PhotoImage(file="{}/{}".format(LOC, fn)).subsample(scale)
    # end for

    return res
# end def