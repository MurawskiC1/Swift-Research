#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:42:09 2023

@author: catermurawski
"""

import tkinter as tk
from tkinter import messagebox
import random as rng


class BurstGUI:
    def __init__(self):
        # Create GUI
        self.window = tk.Tk()
        self.window.title("Burst Chaser")


        #send the game to the menue screen
        self.menu()

        

    def menue():
        '''
        Menu Page:
            Title 
            By Carter 
            Options:
                Pulse Shapes
                Pulse Nois
                Where are the Pulses
        '''
    def PulseShapes():
        '''
        Pulse Shapes:
            Export 
            Filter 
            Repeats



    def run(self):
        self.window.mainloop()
        

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
