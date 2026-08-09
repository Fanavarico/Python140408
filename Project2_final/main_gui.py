# app.py
# Professional Mini Quiz GUI using Tkinter

import tkinter as tk
from tkinter import ttk, messagebox
import re

from database import get_db
from crud import create_user, list_questions
from models import User, Questions, Choice


# ============================================================
# DATABASE
# ============================================================

db = get_db()


# ============================================================
# MAIN APPLICATION
# ============================================================

class QuizApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Window settings
        # -----------------------------
        self.title("Mini Quiz")
        self.geometry("900x620")
        self.minsize(800, 580)

        # Main background
        self.configure(bg="#F3F5F9")

        # -----------------------------
        # Quiz variables
        # -----------------------------
        self.user = None

        self.questions = []
        self.current_question = 0

        self.score = 0

        self.selected_choice = tk.IntVar(value=-1)

        # -----------------------------
        # Setup ttk styles
        # -----------------------------
        self.setup_styles()

        # -----------------------------
        # Main container
        # -----------------------------
        self.container = tk.Frame(
            self,
            bg="#F3F5F9"
        )

        self.container.pack(
            fill="both",
            expand=True
        )

        # Start from login page
        self.show_login_page()


    # ========================================================
    # STYLE
    # ========================================================

    def setup_styles(self):

        style = ttk.Style()

        # Use a theme available on most systems
        try:
            style.theme_use("clam")
        except:
            pass

        # ----------------------------
        # Buttons
        # ----------------------------

        style.configure(
            "Primary.TButton",
            font=("Arial", 13, "bold"),
            padding=12
        )

        style.configure(
            "Secondary.TButton",
            font=("Arial", 11),
            padding=10
        )

        # ----------------------------
        # Progress bar
        # ----------------------------

        style.configure(
            "Quiz.Horizontal.TProgressbar",
            thickness=12
        )


    # ========================================================
    # CLEAR CURRENT PAGE
    # ========================================================

    def clear_page(self):

        for widget in self.container.winfo_children():
            widget.destroy()


    # ========================================================
    # LOGIN PAGE
    # ========================================================

    def show_login_page(self):

        self.clear_page()

        # ---------------------------------------
        # Center Card
        # ---------------------------------------

        card = tk.Frame(
            self.container,
            bg="white",
            highlightbackground="#E3E7EE",
            highlightthickness=1
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=520,
            height=480
        )

        # ---------------------------------------
        # Logo
        # ---------------------------------------

        logo = tk.Label(
            card,
            text="🧠",
            font=("Arial", 52),
            bg="white"
        )

        logo.pack(
            pady=(35, 5)
        )

        # ---------------------------------------
        # Title
        # ---------------------------------------

        title = tk.Label(
            card,
            text="Mini Quiz",
            font=("Arial", 28, "bold"),
            bg="white",
            fg="#222831"
        )

        title.pack()

        subtitle = tk.Label(
            card,
            text="Test your computer hardware knowledge",
            font=("Arial", 12),
            bg="white",
            fg="#7A8493"
        )

        subtitle.pack(
            pady=(5, 30)
        )

        # ---------------------------------------
        # Name
        # ---------------------------------------

        name_label = tk.Label(
            card,
            text="Full Name",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#333333",
            anchor="w"
        )

        name_label.pack(
            fill="x",
            padx=60
        )

        self.name_entry = ttk.Entry(
            card,
            font=("Arial", 13)
        )

        self.name_entry.pack(
            fill="x",
            padx=60,
            pady=(6, 18),
            ipady=7
        )

        # ---------------------------------------
        # Email
        # ---------------------------------------

        email_label = tk.Label(
            card,
            text="Email",
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#333333",
            anchor="w"
        )

        email_label.pack(
            fill="x",
            padx=60
        )

        self.email_entry = ttk.Entry(
            card,
            font=("Arial", 13)
        )

        self.email_entry.pack(
            fill="x",
            padx=60,
            pady=(6, 25),
            ipady=7
        )

        # ---------------------------------------
        # Start Button
        # ---------------------------------------

        start_button = ttk.Button(
            card,
            text="Start Quiz →",
            style="Primary.TButton",
            command=self.start_quiz
        )

        start_button.pack(
            fill="x",
            padx=60
        )

        # Enter key
        self.bind(
            "<Return>",
            lambda event: self.start_quiz()
        )

        self.name_entry.focus()


    # ========================================================
    # VALIDATE EMAIL
    # ========================================================

    def valid_email(self, email):

        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        return re.match(
            pattern,
            email
        ) is not None


    # ========================================================
    # START QUIZ
    # ========================================================

    def start_quiz(self):

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        # ---------------------------------------
        # Validation
        # ---------------------------------------

        if not name:

            messagebox.showwarning(
                "Missing Name",
                "Please enter your name."
            )

            return

        if not email:

            messagebox.showwarning(
                "Missing Email",
                "Please enter your email."
            )

            return

        if not self.valid_email(email):

            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return

        # ---------------------------------------
        # Create user in database
        # ---------------------------------------

        try:

            self.user = create_user(
                db,
                name=name,
                email=email
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                f"Could not create user:\n\n{error}"
            )

            return

        # ---------------------------------------
        # Load questions
        # ---------------------------------------

        try:

            self.questions = list_questions(db)

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                f"Could not load questions:\n\n{error}"
            )

            return

        if not self.questions:

            messagebox.showwarning(
                "No Questions",
                "There are currently no questions in the database."
            )

            return

        # reset quiz

        self.current_question = 0
        self.score = 0

        self.show_quiz_page()


    # ========================================================
    # QUIZ PAGE
    # ========================================================

    def show_quiz_page(self):

        self.clear_page()

        q = self.questions[self.current_question]

        # reset selected answer

        self.selected_choice.set(-1)

        # ====================================================
        # HEADER
        # ====================================================

        header = tk.Frame(
            self.container,
            bg="#18212F",
            height=85
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        # app name

        tk.Label(
            header,
            text="MINI QUIZ",
            font=("Arial", 18, "bold"),
            bg="#18212F",
            fg="white"
        ).pack(
            side="left",
            padx=40
        )

        # user

        user_name = getattr(
            self.user,
            "name",
            "Student"
        )

        tk.Label(
            header,
            text=f"👤  {user_name}",
            font=("Arial", 12),
            bg="#18212F",
            fg="#DCE3EA"
        ).pack(
            side="right",
            padx=40
        )

        # ====================================================
        # MAIN
        # ====================================================

        main = tk.Frame(
            self.container,
            bg="#F3F5F9"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=70,
            pady=35
        )

        # ====================================================
        # QUESTION NUMBER
        # ====================================================

        question_number = self.current_question + 1

        total_questions = len(self.questions)

        tk.Label(
            main,
            text=f"QUESTION {question_number} OF {total_questions}",
            font=("Arial", 11, "bold"),
            fg="#6C7585",
            bg="#F3F5F9"
        ).pack(
            anchor="w"
        )

        # ====================================================
        # PROGRESS BAR
        # ====================================================

        progress = ttk.Progressbar(
            main,
            style="Quiz.Horizontal.TProgressbar",
            maximum=total_questions,
            value=question_number
        )

        progress.pack(
            fill="x",
            pady=(8, 25)
        )

        # ====================================================
        # QUESTION CARD
        # ====================================================

        question_card = tk.Frame(
            main,
            bg="white",
            highlightbackground="#E0E5EC",
            highlightthickness=1
        )

        question_card.pack(
            fill="both",
            expand=True
        )

        # question ID

        tk.Label(
            question_card,
            text=f"Question #{q.id}",
            font=("Arial", 10),
            fg="#929BAA",
            bg="white"
        ).pack(
            anchor="w",
            padx=35,
            pady=(30, 8)
        )

        # question text

        tk.Label(
            question_card,
            text=q.text,
            font=("Arial", 18, "bold"),
            fg="#222831",
            bg="white",
            wraplength=700,
            justify="left"
        ).pack(
            anchor="w",
            padx=35,
            pady=(0, 25)
        )

        # ====================================================
        # GET CHOICES
        # ====================================================

        choices = self.get_question_choices(q)

        # ====================================================
        # ANSWER OPTIONS
        # ====================================================

        letters = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F"
        ]

        for index, choice in enumerate(choices):

            option_frame = tk.Frame(
                question_card,
                bg="#F8F9FB",
                highlightbackground="#E4E8EF",
                highlightthickness=1
            )

            option_frame.pack(
                fill="x",
                padx=35,
                pady=6
            )

            letter = (
                letters[index]
                if index < len(letters)
                else str(index + 1)
            )

            radio = tk.Radiobutton(
                option_frame,
                text=f"  {letter}.   {choice.text}",
                variable=self.selected_choice,
                value=choice.id,
                font=("Arial", 13),
                bg="#F8F9FB",
                activebackground="#F8F9FB",
                fg="#303641",
                anchor="w",
                padx=15,
                pady=12
            )

            radio.pack(
                fill="x"
            )

        # ====================================================
        # NEXT BUTTON
        # ====================================================

        button_text = "Finish Quiz"

        if self.current_question < total_questions - 1:
            button_text = "Next Question →"

        next_button = ttk.Button(
            question_card,
            text=button_text,
            style="Primary.TButton",
            command=self.submit_answer
        )

        next_button.pack(
            anchor="e",
            padx=35,
            pady=25
        )


    # ========================================================
    # GET QUESTION CHOICES
    # ========================================================

    def get_question_choices(self, question):

        """
        Supports both:

        question.choice

        and:

        question.choices
        """

        if hasattr(question, "choices"):

            return question.choices

        elif hasattr(question, "choice"):

            return question.choice

        else:

            return []


    # ========================================================
    # SUBMIT ANSWER
    # ========================================================

    def submit_answer(self):

        selected_id = self.selected_choice.get()

        if selected_id == -1:

            messagebox.showwarning(
                "Select an Answer",
                "Please select an answer before continuing."
            )

            return

        q = self.questions[self.current_question]

        choices = self.get_question_choices(q)

        # ---------------------------------------
        # Find selected choice
        # ---------------------------------------

        selected_choice = None

        for choice in choices:

            if choice.id == selected_id:

                selected_choice = choice
                break

        # ---------------------------------------
        # Check answer
        # ---------------------------------------

        if (
            selected_choice is not None
            and selected_choice.is_correct
        ):

            self.score += 1

        # ---------------------------------------
        # Move to next question
        # ---------------------------------------

        self.current_question += 1

        if self.current_question < len(self.questions):

            self.show_quiz_page()

        else:

            self.show_result_page()


    # ========================================================
    # RESULT PAGE
    # ========================================================

    def show_result_page(self):

        self.clear_page()

        total_questions = len(self.questions)

        percentage = (
            self.score / total_questions
        ) * 100

        # ====================================================
        # CARD
        # ====================================================

        card = tk.Frame(
            self.container,
            bg="white",
            highlightbackground="#E0E5EC",
            highlightthickness=1
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=570,
            height=500
        )

        # ====================================================
        # ICON
        # ====================================================

        if percentage >= 80:

            icon = "🏆"
            message = "Excellent Work!"

        elif percentage >= 60:

            icon = "👏"
            message = "Good Job!"

        elif percentage >= 40:

            icon = "📚"
            message = "Keep Practicing!"

        else:

            icon = "💪"
            message = "Try Again!"

        tk.Label(
            card,
            text=icon,
            font=("Arial", 65),
            bg="white"
        ).pack(
            pady=(35, 5)
        )

        # ====================================================
        # TITLE
        # ====================================================

        tk.Label(
            card,
            text="Quiz Completed!",
            font=("Arial", 27, "bold"),
            bg="white",
            fg="#222831"
        ).pack()

        tk.Label(
            card,
            text=message,
            font=("Arial", 14),
            bg="white",
            fg="#77808F"
        ).pack(
            pady=(5, 25)
        )

        # ====================================================
        # SCORE
        # ====================================================

        tk.Label(
            card,
            text=f"{percentage:.0f}%",
            font=("Arial", 54, "bold"),
            bg="white",
            fg="#2563EB"
        ).pack()

        tk.Label(
            card,
            text=f"{self.score} correct answers out of {total_questions}",
            font=("Arial", 13),
            bg="white",
            fg="#6D7685"
        ).pack(
            pady=(5, 30)
        )

        # ====================================================
        # BUTTONS
        # ====================================================

        buttons = tk.Frame(
            card,
            bg="white"
        )

        buttons.pack(
            fill="x",
            padx=60
        )

        restart_button = ttk.Button(
            buttons,
            text="Restart Quiz",
            style="Primary.TButton",
            command=self.restart_quiz
        )

        restart_button.pack(
            fill="x",
            pady=5
        )

        exit_button = ttk.Button(
            buttons,
            text="Exit",
            style="Secondary.TButton",
            command=self.close_app
        )

        exit_button.pack(
            fill="x",
            pady=5
        )


    # ========================================================
    # RESTART QUIZ
    # ========================================================

    def restart_quiz(self):

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.selected_choice.set(-1)

        self.show_login_page()


    # ========================================================
    # CLOSE
    # ========================================================

    def close_app(self):

        try:
            db.close()

        except:
            pass

        self.destroy()


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app = QuizApp()

    app.protocol(
        "WM_DELETE_WINDOW",
        app.close_app
    )

    app.mainloop()