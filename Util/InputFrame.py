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
        self.wonCheck = tk.IntVar()     # Control variable for won Checkbutton
        self.furiCheck = tk.IntVar()    # Control variable for furi Checkbutton
        self.frame = tk.Frame(master, bg=bg, bd=bd, relief=relief)
        
        # There is a label and some form of input widget for each JSON key.
        # The input widgets' "name" kw are set to match the JSON.
        self.handLabel = tk.Label(self.frame, bg=bg, text='Final Hand',
                                  font=self.font)
        self.handInput = tk.Entry(self.frame, font=self.font, name="hand",
                                  exportselection=0)
        self.startLabel = tk.Label(self.frame, bg=bg, text='Dealt Hand',
                                  font=self.font)
        self.startInput = tk.Entry(self.frame, font=self.font, name="start",
                                   exportselection=0)
        self.doraLabel = tk.Label(self.frame, bg=bg, text='Revealed Dora',
                                  font=self.font)
        self.doraInput = tk.Entry(self.frame, font=self.font, name="dora",
                                  exportselection=0)
        self.acceptLabel = tk.Label(self.frame, bg=bg, text='Accepts/Wait',
                                    font=self.font)
        self.acceptInput = tk.Entry(self.frame, font=self.font, name="accepts",
                                    exportselection=0)
        self.shantenLabel = tk.Label(self.frame, bg=bg, text='Shanten',
                                     font=self.font)
        self.shantenInput = tk.Entry(self.frame, font=self.font, name="shanten",
                                     exportselection=0)
        self.yakuLabel = tk.Label(self.frame, bg=bg, text='Yaku', font=self.font)
        self.yakuInput = tk.Entry(self.frame, font=self.font, name="yaku",
                                  exportselection=0)
        self.wonLabel = tk.Label(self.frame, bg=bg, text='Won?', font=self.font)
        self.wonInput = tk.Checkbutton(self.frame, bg=bg, name="won",
                                       variable=self.wonCheck)
        self.furiLabel = tk.Label(self.frame, bg=bg, text='Furiten?',
                                  font=self.font)
        self.furiInput = tk.Checkbutton(self.frame, bg=bg, name="furiten",
                                        variable=self.furiCheck)
        self.rtnLabel = tk.Label(self.frame, bg=bg, text='Ron/Tsumo?',
                                 font=self.font)
        self.rtnInput = tk.Entry(self.frame, font=self.font, name="rtn",
                                 exportselection=0)
        self.whereLabel = tk.Label(self.frame, bg=bg, text='Where?',
                                   font=self.font)
        self.whereInput = tk.Entry(self.frame, font=self.font, name="where",
                                   exportselection=0)
        self.leftLabel = tk.Label(self.frame, bg=bg, text='# Left',
                                  font=self.font)
        self.leftInput = tk.Entry(self.frame, font=self.font, name="left",
                                  exportselection=0)
        
        # Convenience
        self.widgets = [[self.handLabel,  self.doraLabel,   self.shantenLabel, self.wonLabel,  self.rtnLabel, self.leftLabel],
                        [self.handInput,  self.doraInput,   self.shantenInput, self.wonInput,  self.rtnInput, self.leftInput],
                        [self.startLabel, self.acceptLabel, self.yakuLabel,    self.furiLabel, self.whereLabel],
                        [self.startInput, self.acceptInput, self.yakuInput,    self.furiInput, self.whereInput]]
        
        # Set up the widgets
        self.__setup_widgets()
        
    def get_frame(self):
        return self.frame
    
    '''
    Get and check the input for each widget, turning the label's color red if
    the input is improper for that widget. Returns -1 if an input was invalid,
    or the inputs from the widgets if all are valid
    '''
    def get_input(self):
        # Set the labels all back to black
        for label in self.widgets[0] + self.widgets[2]:
            label['foreground'] = "black"
        
        fail = False
        res = []; keyMap = []
        # Check the first row's inputs
        for i, widget in enumerate(self.widgets[1]):
            inp = widget.get().lower().strip() if type(widget)==tk.Entry else self.wonCheck.get()
            valid = True    # Applicable for Won
            match i:
                # Hand should be MSPZ valid
                case 0:
                    valid = inp and self.mpsz_valid(inp)
                # Dora should be MSPZ valid and not contain spaces
                case 1:
                    valid = inp and self.mpsz_valid(inp) and not ' ' in inp
                # Shanten and Left should be integers (negative is valid for
                # Shanten, but not checked for Left)
                case 2 | 5:
                    try:
                        if inp == '':
                            raise ValueError
                        inp = int(inp)
                    except ValueError:
                        valid = False
                # Ron/Tsumo/Hit/NA are the only valid options, as well as their
                # short codes
                case 4:
                    valid = inp in {'r','ron','t','tsumo','h','hit','n','na',
                                   'n/a'}
            # end match
            if not valid:
                self.widgets[0][i]['foreground'] = "red"
                fail = True
            res.append(inp); keyMap.append(widget.winfo_name())
        # end for
        
        # Check the second row's inputs
        for i, widget in enumerate(self.widgets[3]):
            inp = widget.get().lower().strip() if type(widget)==tk.Entry else self.furiCheck.get()
            valid = True    # Applicable for Furi
            match i:
                # Start and Accept should be MPSZ valid
                # TODO: Accept will need special formatting
                case 0 | 1:
                    valid = inp and self.mpsz_valid(inp)
                # Yaku and Where just needs to have something
                case 2 | 4:
                    valid = inp
                # end case
            # end match
            if not valid:
                self.widgets[2][i]['foreground'] = "red"
                fail = True
            res.append(inp); keyMap.append(widget.winfo_name())
        # end for
        return -1 if fail else zip(res, keyMap)
    # end def
    
    '''
    Checks for valid MSPZ input, namely that at least one of those letters are
    present and that the # of digits meets or exceeds the # of those letters.
    Spaces and 'b' are also accepted. Not perfect, but solid.
    '''
    def mpsz_valid(self, string):
        string = string.lower()
        valLetters = 0; digs = 0;
        if not string[-1].isnumeric():
            return False
        for i,l in enumerate(string):
            if l in set('mpszb'):
                valLetters += 1
                if not string[i+1].isnumeric():
                    return False
            elif l.isnumeric():
                digs += 1
            elif l != ' ':
                return False
            # end if
        # end for
        return False if valLetters > digs else True
    # end def
    
    '''
    Places each of the widgets and sets up their scaling behavior.
    '''
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
        self.wonLabel.grid(sticky='s')
        self.furiLabel.grid(sticky='s')
        self.furiInput.grid(padx=0)
        
        # Set grid weights
        [self.frame.grid_rowconfigure(i, weight=1) for i in range(len(
                                                                self.widgets))]
        self.frame.grid_columnconfigure(0, weight=3)
        self.frame.grid_columnconfigure(1, weight=1)
    # end def
# end class