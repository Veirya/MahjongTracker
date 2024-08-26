# -*- coding: utf-8 -*-

"""
Created on Sat Aug 24 22:48:55 2024

@author: giova

Class to encapsulate the section of the app where the input widgets live.
"""
import tkinter as tk
from tkinter.font import Font as tkFont

class InputFrame:
    def __init__(self, master, bg, bd=0, relief='solid'):
        self.font = tkFont(size=12)
        self.frame = tk.Frame(master, bg=bg, bd=bd, relief=relief)
        self.handLabel = tk.Label(self.frame, bg=bg, text='Final Hand',
                                  font=self.font)
        self.handInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.startLabel = tk.Label(self.frame, bg=bg, text='Dealt Hand',
                                  font=self.font)
        self.startInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.doraLabel = tk.Label(self.frame, bg=bg, text='Revealed Dora',
                                  font=self.font)
        self.doraInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.acceptLabel = tk.Label(self.frame, bg=bg, text='Accepts/Wait',
                                    font=self.font)
        self.acceptInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.shantenLabel = tk.Label(self.frame, bg=bg, text='Shanten',
                                     font=self.font)
        self.shantenInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.yakuLabel = tk.Label(self.frame, bg=bg, text='Yaku', font=self.font)
        self.yakuInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.wonLabel = tk.Label(self.frame, bg=bg, text='Won?', font=self.font)
        self.wonInput = tk.Checkbutton(self.frame, bg=bg)
        self.furiLabel = tk.Label(self.frame, bg=bg, text='Furiten?',
                                  font=self.font)
        self.furiInput = tk.Checkbutton(self.frame, bg=bg)
        self.rtnLabel = tk.Label(self.frame, bg=bg, text='Ron/Tsumo?',
                                 font=self.font)
        self.rtnInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.whereLabel = tk.Label(self.frame, bg=bg, text='Where?',
                                   font=self.font)
        self.whereInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        self.leftLabel = tk.Label(self.frame, bg=bg, text='# Left',
                                  font=self.font)
        self.leftInput = tk.Entry(self.frame, font=self.font, exportselection=0)
        
        # Convenience
        self.widgets = [[self.handLabel,  self.doraLabel,   self.shantenLabel, self.wonLabel,  self.rtnLabel, self.leftLabel],
                        [self.handInput,  self.doraInput,   self.shantenInput, self.wonInput,  self.rtnInput, self.leftInput],
                        [self.startLabel, self.acceptLabel, self.yakuLabel,    self.furiLabel, self.whereLabel],
                        [self.startInput, self.acceptInput, self.yakuInput,    self.furiInput, self.whereInput]]
        
        self.__setup_widgets()
        
    def get_frame(self):
        return self.frame
    
    def __setup_widgets(self):
        # The input section will be subdivided into 2 rows that are also
        # subdivided into two: the top for the widget label, and the bottom for
        # the actual widget.
        
        # Place the widgets into the grid
        for i in range(len(self.widgets)):
            sticky = 'ew' if i%2 else 'sw'
            for j, widget in enumerate(self.widgets[i]):
                widget.grid(row=i, column=j, sticky=sticky, padx=5)
                if i == 3:
                    widget.grid(pady=(0,5))
                # end if
            # end for
        # end for        
        # Overwrite grid configs for won and furi
        '''
        self.handLabel.grid(sticky='sw', padx=5)
        self.handInput.grid(sticky='ew', padx=5)
        self.startLabel.grid(sticky='sw', padx=5)
        self.startInput.grid(sticky='ew', padx=5, pady=(0,5))
        self.doraLabel.grid(sticky='sw', padx=5)
        self.doraInput.grid(sticky='ew', padx=5)
        self.acceptLabel.grid(sticky='sw', padx=5)
        self.acceptInput.grid(sticky='ew', padx=5, pady=(0,5))
        self.shantenLabel.grid(sticky='s')
        self.yakuLabel.grid(sticky='s', padx=5)
        self.yakuInput.grid(sticky='ew', padx=5, pady=(0,5))
        '''
        self.wonLabel.grid(sticky='s')
        self.furiLabel.grid(sticky='s')
        self.furiInput.grid(padx=0)
        '''
        self.rtnLabel.grid(sticky='s')
        self.rtnInput.grid(sticky='news')
        self.whereLabel.grid(sticky='s')
        self.whereInput.grid(sticky='news', padx=5, pady=(0,5))
        self.leftLabel.grid(sticky='s')
        self.leftInput.grid(sticky='ew', padx=5)
        '''
        
        # Set grid weights
        [self.frame.grid_rowconfigure(i, weight=1) for i in range(len(
                                                                self.widgets))]
        self.frame.grid_columnconfigure(0, weight=3)
        self.frame.grid_columnconfigure(1, weight=1)
    # end def
# end class