#Falling Facts / Falling Number Game Revised Version
#Assessment 3.46
#Ruben Nithyaganesh
#21/4/19

from ColumnClass import *
from GlobalVariables import *




#Control Class

class Control:
    def __init__(self, root):
        self.root = root
        self.username = StringVar()
        self.initialise_page()
        self.menu()
        
    def initialise_page(self):       
        self.canvas = Canvas(self.root, height=HEIGHT+50, width=WIDTH+(COL_NUM*4))
        self.canvas.grid(row=1, column=0, rowspan=2)

        self.header = tk.Frame(self.root)
        self.header.grid(row=0, column=0)
        
        self.window = tk.Frame(self.root)
        self.window.grid(row=1, column=0)

        self.title_frame = tk.Frame(self.window)
        self.title_frame.grid(column=0, sticky="N")
        
        self.main_frame = tk.Frame(self.window)
        self.main_frame.grid(row=1, column=0)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.grid(row=2, column=0)

    def menu(self):
        self.initialise_page()

        self.title = tk.Label(self.title_frame, text="FALLING FACTS", font=("Calibri", 30), fg=TITLE_COL)
        self.title.grid(row=0, column=0, pady=50)
        
        self.play = tk.Button(self.main_frame, text="PLAY", command=self.user_entry, width=15, bg=BUTTON_COL, fg=BUTTON_TEXT)
        self.play.grid(row=0, column=0, pady=1)

        instructions = tk.Button(self.main_frame, text="HOW TO PLAY", command=self.instructions, width=15, bg=BUTTON_COL, fg=BUTTON_TEXT)
        instructions.grid(row=1, column=0, pady=1)

        self.quit = tk.Button(self.main_frame, text="QUIT", command=quit, width=15, bg=BUTTON_COL, fg=BUTTON_TEXT)
        self.quit.grid(row=2, column=0, pady=1)

        self.flow = tk.Label(self.header, text="Flow Computing 2019", fg="#777b82")
        self.flow.grid(row=1, column=0)
        

    def instructions(self):
        self.initialise_page()

        self.main_frame.destroy()
        self.instruct_frame = tk.Frame(self.window)
        self.instruct_frame.grid(row=1, column=0)

        self.title = tk.Label(self.title_frame, text="INSTRUCTIONS", font=("Calibri", 30), fg=TITLE_COL)
        self.title.grid(row=0, column=0, pady=50)

        instructions = Label(self.instruct_frame, text=INSTRUCTION_TEXT)
        instructions.grid(row=1, column=0)

        entry = tk.Button(self.instruct_frame, text="MENU", command=self.menu, bg=BUTTON_COL, fg=BUTTON_TEXT)
        entry.grid(row=2, column=0, pady=50)

        
    def user_entry(self):
        self.initialise_page()
        self.userentry = StringVar()
        self.userentry.set("")
        title = tk.Label(self.main_frame, text="ENTER A USERNAME", font=("Calibri", 18), fg=TITLE_COL)
        title.grid(row=0, column=0, columnspan=2)
        
        entry = Entry(self.main_frame, textvariable = self.userentry)
        entry.grid(row=1, column=0)
        entry.focus()

        error_message = tk.Label(self.main_frame, text="", fg="red")
        error_message.grid(row=2, column=0)

        def enter(event):
            self.process_user()
        root.bind("<Return>", enter)

        submit = tk.Button(self.main_frame, text="ENTER", command=self.process_user, bg=BUTTON_COL, fg=BUTTON_TEXT)
        submit.grid(row=1, column=1)

    def process_user(self):
        self.username = self.userentry.get()
        if len(self.username) <= 2 or len(self.username) > 20 or (" " in self.username) == True:
            self.userentry.set("")
            error_message = tk.Label(self.main_frame, text="Invalid username", fg="red")
            error_message.grid(row=2, column=0)
        else:
            self.start_game()
        

    def start_game(self):
        def enter(event):
            self.check_answer()
        root.bind("<Return>", enter)
        
        self.input_frame.destroy()
        self.window.destroy()
        self.initialise_page()

        self.status = True
        
        self.player_score = 0
        self.player_lives = CON_LIVES
        
        self.game_frame = tk.Frame(self.main_frame, bg="black")
        self.game_frame.grid(row=0, column=0)

        self.user_input = IntVar()
        self.user_input.set("")

        self.score = tk.Label(self.input_frame, text="SCORE: {}".format(self.player_score), fg=TITLE_COL)
        self.score.grid(row=0, column=0)

        self.entry = Entry(self.input_frame, textvariable=self.user_input, width=10, state="disabled")
        self.entry.grid(row=0, column=1)

        self.start = tk.Button(self.input_frame, height=1, width=8, text="START", command=self.create_square_setup, bg=TITLE_COL, fg="white")
        self.start.grid(row=1, column=1)

        self.lives = tk.Label(self.input_frame, text="LIVES: {}".format(self.player_lives), fg=TITLE_COL)
        self.lives.grid(row=0, column=2)



        self.C1 = col_C1
        self.C2 = col_C2
        
        self.column_cube = []
        self.create_column()

    def destroy_input(self):
        self.game_over()
        self.input_frame.destroy()
        self.menu()

    def enter(event):
        self.check_answer()
        
    def create_column(self):
        self.column_index = 0
        self.column_list = []
        for i in range (COL_NUM):
            column = Column(self.column_index, self.game_frame, self.C1, self.C2, self.game_over)
            self.column_list.append(column)
            self.column_index += 1

    def create_square_setup(self):
        self.start = tk.Button(self.input_frame, width=8, text="EXIT", command=self.destroy_input, bg=TITLE_COL, fg="white")
        self.start.grid(row=1, column=1)
        self.entry['state'] = "active"
        self.entry.focus()
        self.create_square()

    def create_square(self):
        if self.status == True:
            col_number = random.randint(1, COL_NUM) - 1
            new_cube = self.column_list[col_number]
            self.column_cube.append(new_cube)
            self.column_list[col_number].create_square()
            root.after(1000, self.create_square)            

    def check_answer(self):
        check = False
        try:
            user_answer = self.user_input.get()

            for i in range (COL_NUM):
                
                status = self.column_list[i].check_square(user_answer)
                if status == True:
                    self.add_playerscore()
                    check = True
            
            if check == False:
                self.subtract_lives()

            
        except ValueError:
            pass

        self.user_input.set("")

    
    
    def add_playerscore(self):
        self.player_score += 1
        self.score = Label(self.input_frame, text="SCORE: {}".format(self.player_score))
        self.score.grid(row=0, column=0)

        
        for i in range(0, len(self.column_list)):
            self.column_list[i].change_colour(self.player_score)

    def subtract_lives(self):
        self.player_lives -= 1
        self.lives = Label(self.input_frame, text="LIVES: {}".format(self.player_lives))
        self.lives.grid(row=0, column=2)
        if self.player_lives == 0:
            self.game_over()

    def game_over(self):
        self.status = False
        for i in range (COL_NUM):
            self.column_list[i].stop_square()

        end_screen = tk.Canvas(self.game_frame, height=HEIGHT/2, width= WIDTH/1.5)
        end_screen.grid(row=0, column=0, columnspan = COL_NUM)
        gameover_text = end_screen.create_text((WIDTH/1.5)/2, HEIGHT/10, text="GAME OVER", font = ("Arial", 20))
        player_stats_text = end_screen.create_text((WIDTH/1.5)/2, HEIGHT/3, \
                                                   text="{} eliminated {} squares.".format(self.username.strip(), self.player_score))

        self.entry['state'] = "disabled"

        if self.player_lives == 0:
             death_info = end_screen.create_text((WIDTH/1.5)/2, HEIGHT/4, \
                                                   text="Out of lives!")
        else:
            death_info = end_screen.create_text((WIDTH/1.5)/2, HEIGHT/4, \
                                                   text="A square got to the bottom!")
            
            
