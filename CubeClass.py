#Falling Facts / Falling Number Game Revised Version
#Assessment 3.46
#Ruben Nithyaganesh
#21/4/19

from GlobalVariables import *
from ColumnClass import *

#CubeClass

class Cube:
    def __init__(self, canvas, c1, c2, number_val, game_over, speed):
        #create a square inside the canvas of the column it is being created in, fill with passed in number value
        self.canvas = canvas
        colour = c1
        text_colour = c2
        self.square = self.canvas.create_rectangle(2, 0-col_WIDTH, col_WIDTH+1, -1, fill = colour)
        self.num_text = self.canvas.create_text(col_WIDTH / 2, 0-col_WIDTH/2, text=number_val, fill=text_colour, font=("Calibri", 12))
        self.number_val = number_val
        self.status = True #as long as this variable is True, the loop for animating the falling square runs
        #sets the speed of cube to a random speed within a range of 3
        self.speed = random.randint(speed, speed+3)
        #defines the game_over function from the control class
        self.game_over = game_over
        #starts the animation loop for the square
        self.move_square()



    def check_number(self, user_answer, multiple):
        #checks the user answer, if correct return true and stop the cube moving
        if self.number_val / multiple == user_answer:
            return True
            self.speed = 0
        #if incorrect, return false
        else:
            return False




    def move_square(self):
        #get coordinates of the square on canvas, store in list
        cube_pos = self.canvas.coords(self.square)

        self.update_position() #run the function that moves square
        if self.status == True: #this statement prevents an infinite loop occuring
            if cube_pos[3] >= HEIGHT-2: #if the lowest point of the cube is touching the bottom of column, run game over function
                self.game_over()
            
                self.status = False
                return False
            else:
                
                
                root.after(30, self.move_square) #if the cube hasnt reached the bottom, wait 30ms and run this function again
                return True

    def update_position(self):
        #moves square and number text down by self.speed pixels
        self.canvas.move(self.square, 0, self.speed)
        self.canvas.move(self.num_text, 0, self.speed)

    def delete_rectangle(self, canvas):
        #delete square and number from GUI
        self.status = False
        canvas.delete(self.square)
        canvas.delete(self.num_text)

    def stop(self):
        #set speed to 0, set status to false (stops loop in the move_square function)
        self.speed = 0
        self.status = False

