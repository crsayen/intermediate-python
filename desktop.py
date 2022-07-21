import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from madlib.data import Data
from madlib.madlib import Madlib


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.rowconfigure(0, minsize=800, weight=1, pad=10)
        self.columnconfigure(1, minsize=800, weight=1, pad=10)

        self.title("Mad Libs")

        self.home_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def home_screen(self):
        self.start_button = ttk.Button(self, text="start new game")
        self.start_button["command"] = self.new_game_clicked
        self.start_button.pack()

    def start_game(self):
        self.data = Data()
        story = self.data.get_random_story()
        self.madlib = Madlib(story)
        for prompt in self.madlib.prompt_iterator:
            print(prompt)
            answer = simpledialog.askstring(
                "input", prompt
            ) or self.data.get_random_word(prompt)
            self.madlib.give_next_answer(answer)
        self.show_result()

    def show_result(self):
        self.home_screen()
        self.result = tk.Label(self, text=self.madlib.solve(), wraplength=400)
        self.result.pack()

    def new_game_clicked(self):
        self.clear_screen()
        self.start_game()


if __name__ == "__main__":
    app = App()
    app.mainloop()
