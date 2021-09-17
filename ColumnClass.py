#Falling Facts / Falling Number Game Revised Version
#Assessment 3.46
#Ruben Nithyaganesh
#21/4/19

#import global variables and other classes
from GlobalVariables import *
from ControlClass import *
from CubeClass import *

class Column:
    def __init__(self, column_value, frame, c1, c2, game_over):

    #create column, place in grid
        self.column_space = tk.Canvas(frame, height=HEIGHT, width = col_WIDTH, bg= c1)
        self.column_space.grid(row=0, column=column_value, padx=0, pady=0)
        self.col_number = column_value + 1
        self.column_space.create_text(col_WIDTH / 2, HEIGHT / 2, text=self.col_number, fill=c2, font=("Calibri", 15))
    #create a list for created cubes, define self variables with passed in values
        self.column_value = column_value
        self.cube_list = []
        self.game_over = game_over
        self.c1 = cube_C1_1
        self.c2 = cube_C2_1
        self.cube_speed = SPEED1


        
    def create_square(self):
        if len(self.cube_list) <= 0: #limits a cube being made if a cube is already in the column
            #create a random number to put inside square
            num = random.randint(1,12)
            self.column_multiple = self.column_value + 1
            number_val = (self.column_multiple) * num
            #create instance of cube class, passing in values for colour, the number value, and the canvas of the column
            cube=Cube(self.column_space, self.c1, self.c2, number_val,\
                      self.game_over, self.cube_speed)
            #add created instance to the cube list
            self.cube_list.append(cube)
                
                


    def check_square(self, user_answer):
        #for loop, runs through all cubes in column
        for i in range(0, len(self.cube_list)):
            #runs the check number function from the created cube class, which returns true or false
            status = self.cube_list[i].check_number(user_answer, self.column_multiple)

            if status == True: #if user answer is correct (return true), delete the square and return true
                self.delete_square(i)
                return True
            else: #if incorrect, return false, do not delete square
                return False
                
    def delete_square(self, i):
        #deletes the GUI representation of cube class, than deletes instance of the class
        self.cube_list[i].delete_rectangle(self.column_space)
        del self.cube_list[i]

    def stop_square(self):
        #sets the speed of cube to 0
        for i in range(0, len(self.cube_list)):
            self.cube_list[i].stop()

    def change_colour(self, score):
        #depending on user score, change cube speed and colour
        if score == THRESHOLD1:
            self.c1 = cube_C1_2
            self.c2 = cube_C2_2
            self.cube_speed = SPEED2
        elif score == THRESHOLD2:
            self.c1 = cube_C1_3
            self.c2 = cube_C2_3
            self.cube_speed = SPEED3
        elif score == THRESHOLD3:
            self.c1 = cube_C1_4
            self.c2 = cube_C2_4
            self.cube_speed = SPEED4
        
            
