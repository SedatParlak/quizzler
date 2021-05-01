from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#264653"
CANVAS_COLOR = "#e9c46a"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(width=600, height=500)
        self.window.resizable(False, False)
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.canvas = Canvas(width=500, height=300, bg=CANVAS_COLOR, highlightthickness=0)
        self.text = self.canvas.create_text(250, 150, text="asd", font=("Arial", 20, "italic"), width=450)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.score_label = Label(text=f"Score : 0 ", font=("Arial", 15, "bold"), fg="white", pady=20, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.image_true = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.image_true, highlightthickness=0, borderwidth=0,
                                  command=self.true_pressed)
        self.button_true.grid(row=2, column=0, pady=20)

        self.image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.image_false, highlightthickness=0, borderwidth=0,
                                   command=self.false_pressed)
        self.button_false.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="#e9c46a")
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"End of the quiz. Your score : {self.quiz.score}")
            self.button_false.config(state="disable")
            self.button_true.config(state="disable")

    def true_pressed(self):
        is_right = (self.quiz.check_answer("True"))
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#40916c")
        else:
            self.canvas.config(bg="#c71f37")
        self.window.after(500, self.get_next_question)
