#Global Variables
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import time
import random

global root
root = Tk()
root.title("Falling Facts")
root.resizable(0, 0)



HEIGHT = 750
WIDTH=750
COL_NUM = 12
col_WIDTH = WIDTH / COL_NUM

INSTRUCTION_TEXT = "Falling Numbers is a game that trains your basic facts."\
                   "\nOn the screen are twelve numbered columns. Numbers will fall in each column"\
                   "\nthat are divisible by the number of the column that it is falling in. To eliminate the number"\
                   "\nenter the answer to the division equation formed. The aim of the game is to eliminate as many"\
                   "\nnumbers as possible. You have three lives if you get a question incorrect, if your lives run out or"\
                   "\na number hits the bottom of the screen, the game is over. As the game goes on, the numbers will"\
                   "\nfall progressively faster signalled by changing colours. Good luck!"

CON_LIVES = 3

TITLE_COL = "green"
BUTTON_COL = "orange"
BUTTON_TEXT = "green"


col_C1 = "blue"
col_C2 = "yellow"


cube_C1_1 = "white"
cube_C2_1 = "black"

cube_C1_2 = "skyblue"
cube_C2_2 = "black"

cube_C1_3 = "darkblue"
cube_C2_3 = "white"

cube_C1_4 = "black"
cube_C2_4 = "white"


THRESHOLD1 = 15
THRESHOLD2 = 40
THRESHOLD3 = 60

SPEED1 = 1
SPEED2 = 3
SPEED3 = 6
SPEED4 = 9

WHITE_PERCENTAGE = 50
SKYBLUE_PERCENTAGE = 25
DARKBLUE_PERCENTAGE = 10

SPEED_VARIATION = False
'''Set SPEED_VARIATION to True if you want higher speed cubes to come at seperate times,
dependent on score, or to False to have all speed types randomly generate at increasing rarity.'''


 
