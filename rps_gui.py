from tkinter import *
from random import randint
from tkinter import ttk

class GUI:
    def __init__(self, window):
        self.window = window

        self.human_label_name = Label(
            self.window,
            bg='#69cdd6',
            text='Human',
            font=('Arial', 24)
            )
        self.human_label_name.place(x=120, y=10)

        self.computer_label_name = Label(
            self.window,
            bg='#69cdd6',
            text='Computer',
            font=('Arial', 24)
            )
        self.computer_label_name.place(x=750, y=10)

        self.rock = PhotoImage(file='C:/Users/chrho/Desktop/pythonProject3_2_modified/images/rock.png')
        self.paper = PhotoImage(file='C:/Users/chrho/Desktop/pythonProject3_2_modified/images/paper.png')
        self.scissors = PhotoImage(file='C:/Users/chrho/Desktop/pythonProject3_2_modified/images/scissors.png')
        self.image_list = [self.rock, self.paper, self.scissors]
        self.pick_number = randint(0,2)

        self.computer_label_image = Label(self.window, image=self.image_list[self.pick_number])
        self.computer_label_image.place(x = 680, y=75)

        self.human_label_image = Label(self.window, image=self.image_list[0])
        self.human_label_image.place(x = 40, y=75)

        self.human_score = Label(
            self.window,
            bg='#69cdd6',
            text='0',
            font=('Arial', 24)
            )
        self.human_score.place(x=160, y=280)

        self.computer_score = Label(
            self.window,
            bg='#69cdd6',
            text='0',
            font=('Arial', 24)
            )
        self.computer_score.place(x=810, y=280)

        # Make choice
        self.user_choice_label = Label(self.window, bg='#69cdd6', text="Choose Your Weapon!", font=("Arial", 18))
        self.user_choice_label.pack(pady=10)
        self.user_choice = ttk.Combobox(self.window, value=("Rock", "Paper", "Scissors"))
        self.user_choice.current(0)
        self.user_choice.pack(pady=15)

        # Create button to play
        self.pick_button = Button(self.window, text="Let's Play!", command=self.choose)
        self.pick_button.pack(pady=15)

        # Label for showing if human won or not
        self.win_lose_label = Label(self.window, bg='#69cdd6', text='Results:', font=("Arial", 18))
        self.win_lose_label.pack(pady=50)


    def choose(self):
        self.pick_number = randint(0, 2)
        self.computer_label_image.config(image=self.image_list[self.pick_number])

    # Convert Dropdown choice to a number
        if self.user_choice.get() == "Rock":
            self.user_choice_value = 0
            self.human_label_image.config(image=self.image_list[0])

        if self.user_choice.get() == "Paper":
            self.user_choice_value = 1
            self.human_label_image.config(image=self.image_list[1])

        if self.user_choice.get() == "Scissors":
            self.user_choice_value = 2
            self.human_label_image.config(image=self.image_list[2])

    # Determine if human won or lost
        if self.user_choice_value == 0: # Rock
            if self.pick_number == 0: # Rock
                self.win_lose_label.config(text="It's A Tie!\n Try Again!")
            elif self.pick_number == 1: # Paper
                self.win_lose_label.config(text="Paper Covers Rock!\n You Lose!")
                self.update_computer_score()
            elif self.pick_number == 2: # Scissors
                self.win_lose_label.config(text="Rock Smashes Scissors!\n You Win!")
                self.update_human_score()

        if self.user_choice_value == 1: # Paper
            if self.pick_number == 0: # Rock
                self.win_lose_label.config(text="Paper covers Rock!\n You Win!")
                self.update_human_score()
            elif self.pick_number == 1: # Paper
                self.win_lose_label.config(text="It's A Tie!\n Try Again!")
            elif self.pick_number == 2: # Scissors
                self.win_lose_label.config(text="Scissors Cut Paper!\n You Lose!")
                self.update_computer_score()

        if self.user_choice_value == 2: # Scissors
            if self.pick_number == 0: # Rock
                self.win_lose_label.config(text="Rock Smashes Scissors!\n You Lose!")
                self.update_computer_score()
            elif self.pick_number == 1: # Paper
                self.win_lose_label.config(text="Scissors Cut Paper!\n You Win!")
                self.update_human_score()
            elif self.pick_number == 2: # Scissors
                self.win_lose_label.config(text="It's A Tie!\n Try Again!")

    def update_human_score(self):
        self.score_x = int(self.human_score["text"])
        self.score_x += 1
        self.human_score["text"] = str(self.score_x)
        self.human_counter = self.score_x

    def update_computer_score(self):
        self.score_y = int(self.computer_score["text"])
        self.score_y += 1
        self.computer_score["text"] = str(self.score_y)

def score_keeper(score_x, score_y):
    score_x = int(score_x)
    score_y = int(score_y)
    if score_x < 0:
        raise ValueError('Invalid input')
    else:
        total_wins = score_x + score_y
        return total_wins