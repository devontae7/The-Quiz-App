from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.score.config(padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        # background_img = PhotoImage(file="background.png")
        # canvas.create_image(150, 207, image=background_img)
        self.quote_text = self.canvas.create_text(
            150,
            125,
            text="Kanye Quote Goes HERE",
            width=280,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_img = PhotoImage(file="images/true.png")
        self.check_bt = Button(image=check_img, highlightthickness=0, command=self.check_button)
        self.check_bt.grid(row=2, column=0)

        # the cross and check_img variables are not self., because self. make a variable a property
        # which could be used outside of class. we do not need these images to be used anywhere else
        # so we do not make it self.check_img.

        cross_img = PhotoImage(file="images/false.png")
        self.cross_bt = Button(image=cross_img, highlightthickness=0, command=self.cross_button)
        self.cross_bt.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quote_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quote_text, text=f"You have reached to the end of the Quiz. You Scored {self.quiz.score}")
            self.cross_bt.config(state='disabled')
            self.check_bt.config(state='disabled')


    def cross_button(self):
        # this two lines and check_bt one do the same.
        is_right = self.quiz.check_answer('false')
        self.show_result(is_right)

    def check_button(self):
        self.show_result(self.quiz.check_answer('true'))

    def show_result(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)
