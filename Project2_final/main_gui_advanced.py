# ============================================================
# app.py
# Academic Computer Hardware Assessment
# Modern Tkinter GUI
# ============================================================

import tkinter as tk
from tkinter import ttk, messagebox
import re

from database import get_db
from crud import create_user, list_questions
from models import User, Questions, Choice


# ============================================================
# DESIGN SYSTEM
# ============================================================

COLORS = {
    "navy": "#0B1F33",
    "navy_light": "#16324F",
    "blue": "#1769AA",
    "blue_hover": "#12578E",
    "accent": "#2F80ED",

    "background": "#F4F6F8",
    "surface": "#FFFFFF",
    "surface_soft": "#F8FAFC",

    "border": "#DDE3EA",
    "border_dark": "#CBD3DC",

    "text": "#17212B",
    "text_secondary": "#5B6875",
    "text_muted": "#8995A3",

    "success": "#19734A",
    "success_bg": "#EAF7F0",

    "warning": "#A86500",
    "warning_bg": "#FFF7E8",

    "danger": "#B42318",

    "selected_bg": "#EAF3FB",
    "selected_border": "#1769AA",
}


FONT = "Arial"


# ============================================================
# DATABASE
# ============================================================

db = get_db()


# ============================================================
# MAIN APPLICATION
# ============================================================

class AcademicQuizApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # ----------------------------------------------------
        # WINDOW
        # ----------------------------------------------------

        self.title("Academic Assessment Portal")
        self.geometry("1180x760")
        self.minsize(1050, 700)

        self.configure(bg=COLORS["background"])

        # Center window
        self.center_window()

        # ----------------------------------------------------
        # EXAM STATE
        # ----------------------------------------------------

        self.user = None
        self.questions = []

        self.current_question_index = 0

        # stores:
        # {
        #     question_id: choice_id
        # }
        self.answers = {}

        self.selected_choice = tk.IntVar(value=-1)

        # ----------------------------------------------------
        # STYLE
        # ----------------------------------------------------

        self.setup_styles()

        # ----------------------------------------------------
        # ROOT CONTAINER
        # ----------------------------------------------------

        self.container = tk.Frame(
            self,
            bg=COLORS["background"]
        )

        self.container.pack(
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # START
        # ----------------------------------------------------

        self.show_welcome_page()

        self.protocol(
            "WM_DELETE_WINDOW",
            self.close_application
        )


    # ========================================================
    # WINDOW CENTER
    # ========================================================

    def center_window(self):

        width = 1180
        height = 760

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.geometry(
            f"{width}x{height}+{x}+{y}"
        )


    # ========================================================
    # TTK STYLES
    # ========================================================

    def setup_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        # -----------------------------------------
        # Main Button
        # -----------------------------------------

        style.configure(
            "Primary.TButton",
            font=(FONT, 11, "bold"),
            foreground="white",
            background=COLORS["blue"],
            padding=(18, 12),
            borderwidth=0
        )

        style.map(
            "Primary.TButton",
            background=[
                ("active", COLORS["blue_hover"]),
                ("pressed", COLORS["navy"])
            ],
            foreground=[
                ("active", "white")
            ]
        )

        # -----------------------------------------
        # Secondary Button
        # -----------------------------------------

        style.configure(
            "Secondary.TButton",
            font=(FONT, 11, "bold"),
            foreground=COLORS["navy"],
            background="#E9EEF3",
            padding=(18, 12),
            borderwidth=0
        )

        style.map(
            "Secondary.TButton",
            background=[
                ("active", "#DDE5EC")
            ]
        )

        # -----------------------------------------
        # Entry
        # -----------------------------------------

        style.configure(
            "Academic.TEntry",
            font=(FONT, 12),
            padding=10
        )

        # -----------------------------------------
        # Progress Bar
        # -----------------------------------------

        style.configure(
            "Academic.Horizontal.TProgressbar",
            troughcolor="#E6EBF0",
            background=COLORS["blue"],
            thickness=7,
            borderwidth=0
        )


    # ========================================================
    # HELPER
    # ========================================================

    def clear_page(self):

        for widget in self.container.winfo_children():
            widget.destroy()


    # ========================================================
    # INSTITUTION HEADER
    # ========================================================

    def create_header(self, parent, compact=False):

        height = 78 if compact else 90

        header = tk.Frame(
            parent,
            bg=COLORS["navy"],
            height=height
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)

        inner = tk.Frame(
            header,
            bg=COLORS["navy"]
        )

        inner.pack(
            fill="both",
            expand=True,
            padx=42
        )

        # ----------------------------------------------------
        # LEFT
        # ----------------------------------------------------

        brand = tk.Frame(
            inner,
            bg=COLORS["navy"]
        )

        brand.pack(
            side="left",
            fill="y"
        )

        logo_box = tk.Frame(
            brand,
            bg="white",
            width=44,
            height=44
        )

        logo_box.pack(
            side="left",
            pady=20
        )

        logo_box.pack_propagate(False)

        tk.Label(
            logo_box,
            text="A",
            bg="white",
            fg=COLORS["navy"],
            font=(FONT, 22, "bold")
        ).pack(
            expand=True
        )

        brand_text = tk.Frame(
            brand,
            bg=COLORS["navy"]
        )

        brand_text.pack(
            side="left",
            padx=(14, 0)
        )

        tk.Label(
            brand_text,
            text="ACADEMIC ASSESSMENT PORTAL",
            bg=COLORS["navy"],
            fg="white",
            font=(FONT, 13, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            brand_text,
            text="Computer Hardware Fundamentals",
            bg=COLORS["navy"],
            fg="#AFC1D2",
            font=(FONT, 10)
        ).pack(
            anchor="w",
            pady=(3, 0)
        )

        # ----------------------------------------------------
        # RIGHT
        # ----------------------------------------------------

        right = tk.Frame(
            inner,
            bg=COLORS["navy"]
        )

        right.pack(
            side="right"
        )

        tk.Label(
            right,
            text="ASSESSMENT ENVIRONMENT",
            bg=COLORS["navy"],
            fg="#8EACC5",
            font=(FONT, 9, "bold")
        ).pack(
            anchor="e"
        )

        tk.Label(
            right,
            text="Secure Session",
            bg=COLORS["navy"],
            fg="white",
            font=(FONT, 11)
        ).pack(
            anchor="e",
            pady=(3, 0)
        )

        return header


    # ========================================================
    # WELCOME / REGISTRATION PAGE
    # ========================================================

    def show_welcome_page(self):

        self.clear_page()

        self.create_header(
            self.container
        )

        content = tk.Frame(
            self.container,
            bg=COLORS["background"]
        )

        content.pack(
            fill="both",
            expand=True
        )

        center = tk.Frame(
            content,
            bg=COLORS["background"]
        )

        center.place(
            relx=0.5,
            rely=0.48,
            anchor="center"
        )

        # ====================================================
        # INTRO
        # ====================================================

        tk.Label(
            center,
            text="Computer Hardware Assessment",
            bg=COLORS["background"],
            fg=COLORS["text"],
            font=(FONT, 28, "bold")
        ).pack()

        tk.Label(
            center,
            text=(
                "Candidate Registration & Examination Access"
            ),
            bg=COLORS["background"],
            fg=COLORS["text_secondary"],
            font=(FONT, 12)
        ).pack(
            pady=(7, 28)
        )

        # ====================================================
        # CARD
        # ====================================================

        card = tk.Frame(
            center,
            bg=COLORS["surface"],
            width=670,
            height=470,
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )

        card.pack()

        card.pack_propagate(False)

        inside = tk.Frame(
            card,
            bg=COLORS["surface"]
        )

        inside.pack(
            fill="both",
            expand=True,
            padx=48,
            pady=35
        )

        # -----------------------------------------
        # Section header
        # -----------------------------------------

        tk.Label(
            inside,
            text="CANDIDATE INFORMATION",
            bg=COLORS["surface"],
            fg=COLORS["blue"],
            font=(FONT, 10, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            inside,
            text="Enter your information to begin.",
            bg=COLORS["surface"],
            fg=COLORS["text"],
            font=(FONT, 18, "bold")
        ).pack(
            anchor="w",
            pady=(6, 7)
        )

        tk.Label(
            inside,
            text=(
                "Your information will be registered before "
                "the assessment begins."
            ),
            bg=COLORS["surface"],
            fg=COLORS["text_secondary"],
            font=(FONT, 10)
        ).pack(
            anchor="w",
            pady=(0, 25)
        )

        # ====================================================
        # NAME
        # ====================================================

        self.create_form_label(
            inside,
            "Full Name"
        )

        self.name_entry = ttk.Entry(
            inside,
            style="Academic.TEntry"
        )

        self.name_entry.pack(
            fill="x",
            pady=(7, 18)
        )

        # ====================================================
        # EMAIL
        # ====================================================

        self.create_form_label(
            inside,
            "Email Address"
        )

        self.email_entry = ttk.Entry(
            inside,
            style="Academic.TEntry"
        )

        self.email_entry.pack(
            fill="x",
            pady=(7, 25)
        )

        # ====================================================
        # INFORMATION BOX
        # ====================================================

        notice = tk.Frame(
            inside,
            bg="#F0F5FA",
            highlightbackground="#D8E5F0",
            highlightthickness=1
        )

        notice.pack(
            fill="x",
            pady=(0, 25)
        )

        tk.Label(
            notice,
            text="i",
            bg=COLORS["blue"],
            fg="white",
            font=(FONT, 10, "bold"),
            width=3
        ).pack(
            side="left",
            fill="y"
        )

        tk.Label(
            notice,
            text=(
                "The assessment contains multiple-choice questions. "
                "Select one answer for each question."
            ),
            bg="#F0F5FA",
            fg=COLORS["text_secondary"],
            font=(FONT, 9),
            wraplength=470,
            justify="left"
        ).pack(
            side="left",
            padx=12,
            pady=11
        )

        # ====================================================
        # BUTTON
        # ====================================================

        ttk.Button(
            inside,
            text="Continue to Assessment",
            style="Primary.TButton",
            command=self.start_assessment
        ).pack(
            fill="x"
        )

        self.bind(
            "<Return>",
            lambda event: self.start_assessment()
        )

        self.name_entry.focus()


    # ========================================================
    # FORM LABEL
    # ========================================================

    def create_form_label(self, parent, text):

        tk.Label(
            parent,
            text=text,
            bg=COLORS["surface"],
            fg=COLORS["text"],
            font=(FONT, 10, "bold")
        ).pack(
            anchor="w"
        )


    # ========================================================
    # EMAIL VALIDATION
    # ========================================================

    def is_valid_email(self, email):

        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        return re.match(
            pattern,
            email
        ) is not None


    # ========================================================
    # START ASSESSMENT
    # ========================================================

    def start_assessment(self):

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name:

            messagebox.showwarning(
                "Candidate Information",
                "Please enter your full name."
            )

            return

        if not email:

            messagebox.showwarning(
                "Candidate Information",
                "Please enter your email address."
            )

            return

        if not self.is_valid_email(email):

            messagebox.showwarning(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return

        # ----------------------------------------------------
        # DATABASE USER
        # ----------------------------------------------------

        try:

            self.user = create_user(
                db,
                name=name,
                email=email
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                f"Unable to register candidate.\n\n{error}"
            )

            return

        # ----------------------------------------------------
        # QUESTIONS
        # ----------------------------------------------------

        try:

            self.questions = list_questions(db)

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                f"Unable to load assessment questions.\n\n{error}"
            )

            return

        if not self.questions:

            messagebox.showwarning(
                "Assessment Unavailable",
                "No questions are available in the database."
            )

            return

        self.current_question_index = 0
        self.answers = {}

        self.show_exam_page()


    # ========================================================
    # GET CHOICES
    # ========================================================

    def get_question_choices(self, question):

        # Supports both versions of your model:

        if hasattr(question, "choices"):
            return list(question.choices)

        if hasattr(question, "choice"):
            return list(question.choice)

        return []


    # ========================================================
    # EXAM PAGE
    # ========================================================

    def show_exam_page(self):

        self.clear_page()

        self.create_header(
            self.container,
            compact=True
        )

        # ====================================================
        # TOP EXAM INFORMATION
        # ====================================================

        status_bar = tk.Frame(
            self.container,
            bg="white",
            height=60,
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )

        status_bar.pack(
            fill="x"
        )

        status_bar.pack_propagate(False)

        status_inner = tk.Frame(
            status_bar,
            bg="white"
        )

        status_inner.pack(
            fill="both",
            expand=True,
            padx=42
        )

        # candidate
        candidate_name = getattr(
            self.user,
            "name",
            "Candidate"
        )

        tk.Label(
            status_inner,
            text=f"Candidate:  {candidate_name}",
            bg="white",
            fg=COLORS["text"],
            font=(FONT, 10, "bold")
        ).pack(
            side="left"
        )

        tk.Label(
            status_inner,
            text="Computer Hardware Fundamentals",
            bg="white",
            fg=COLORS["text_secondary"],
            font=(FONT, 10)
        ).pack(
            side="right"
        )

        # ====================================================
        # BODY
        # ====================================================

        body = tk.Frame(
            self.container,
            bg=COLORS["background"]
        )

        body.pack(
            fill="both",
            expand=True,
            padx=38,
            pady=28
        )

        # ====================================================
        # LEFT SIDEBAR
        # ====================================================

        sidebar = tk.Frame(
            body,
            bg=COLORS["surface"],
            width=245,
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)

        # ====================================================
        # MAIN AREA
        # ====================================================

        main = tk.Frame(
            body,
            bg=COLORS["background"]
        )

        main.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(24, 0)
        )

        self.create_question_sidebar(
            sidebar
        )

        self.create_question_panel(
            main
        )


    # ========================================================
    # SIDEBAR
    # ========================================================

    def create_question_sidebar(self, parent):

        total = len(self.questions)

        answered = len(self.answers)

        # -----------------------------------------
        # Header
        # -----------------------------------------

        tk.Label(
            parent,
            text="ASSESSMENT",
            bg="white",
            fg=COLORS["blue"],
            font=(FONT, 9, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(24, 6)
        )

        tk.Label(
            parent,
            text="Question Navigator",
            bg="white",
            fg=COLORS["text"],
            font=(FONT, 15, "bold")
        ).pack(
            anchor="w",
            padx=22
        )

        # -----------------------------------------
        # Progress
        # -----------------------------------------

        progress_text = tk.Frame(
            parent,
            bg="white"
        )

        progress_text.pack(
            fill="x",
            padx=22,
            pady=(25, 5)
        )

        tk.Label(
            progress_text,
            text="Progress",
            bg="white",
            fg=COLORS["text_secondary"],
            font=(FONT, 9)
        ).pack(
            side="left"
        )

        tk.Label(
            progress_text,
            text=f"{answered}/{total}",
            bg="white",
            fg=COLORS["text"],
            font=(FONT, 9, "bold")
        ).pack(
            side="right"
        )

        progress = ttk.Progressbar(
            parent,
            style="Academic.Horizontal.TProgressbar",
            maximum=total,
            value=answered
        )

        progress.pack(
            fill="x",
            padx=22
        )

        # -----------------------------------------
        # Divider
        # -----------------------------------------

        tk.Frame(
            parent,
            bg=COLORS["border"],
            height=1
        ).pack(
            fill="x",
            padx=22,
            pady=22
        )

        # -----------------------------------------
        # Question grid
        # -----------------------------------------

        grid = tk.Frame(
            parent,
            bg="white"
        )

        grid.pack(
            padx=18,
            anchor="w"
        )

        for index, question in enumerate(self.questions):

            number = index + 1

            is_current = (
                index == self.current_question_index
            )

            is_answered = (
                question.id in self.answers
            )

            if is_current:

                bg = COLORS["navy"]
                fg = "white"

            elif is_answered:

                bg = COLORS["success_bg"]
                fg = COLORS["success"]

            else:

                bg = COLORS["surface_soft"]
                fg = COLORS["text_secondary"]

            button = tk.Button(
                grid,
                text=str(number),
                bg=bg,
                fg=fg,
                activebackground=COLORS["navy_light"],
                activeforeground="white",
                relief="flat",
                font=(FONT, 10, "bold"),
                width=4,
                height=2,
                cursor="hand2",
                command=lambda i=index: self.go_to_question(i)
            )

            row = index // 4
            col = index % 4

            button.grid(
                row=row,
                column=col,
                padx=4,
                pady=4
            )

        # -----------------------------------------
        # Legend
        # -----------------------------------------

        tk.Frame(
            parent,
            bg=COLORS["border"],
            height=1
        ).pack(
            fill="x",
            padx=22,
            pady=(25, 18)
        )

        self.create_legend_item(
            parent,
            COLORS["navy"],
            "Current question"
        )

        self.create_legend_item(
            parent,
            COLORS["success_bg"],
            "Answered"
        )

        self.create_legend_item(
            parent,
            COLORS["surface_soft"],
            "Not answered"
        )

        # -----------------------------------------
        # Academic integrity
        # -----------------------------------------

        integrity = tk.Frame(
            parent,
            bg="#F7F9FB",
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )

        integrity.pack(
            side="bottom",
            fill="x",
            padx=18,
            pady=18
        )

        tk.Label(
            integrity,
            text="ASSESSMENT POLICY",
            bg="#F7F9FB",
            fg=COLORS["text_secondary"],
            font=(FONT, 8, "bold")
        ).pack(
            anchor="w",
            padx=12,
            pady=(10, 3)
        )

        tk.Label(
            integrity,
            text=(
                "Review your answers before final submission."
            ),
            bg="#F7F9FB",
            fg=COLORS["text_secondary"],
            font=(FONT, 8),
            wraplength=185,
            justify="left"
        ).pack(
            anchor="w",
            padx=12,
            pady=(0, 10)
        )


    # ========================================================
    # LEGEND
    # ========================================================

    def create_legend_item(self, parent, color, text):

        row = tk.Frame(
            parent,
            bg="white"
        )

        row.pack(
            fill="x",
            padx=22,
            pady=3
        )

        indicator = tk.Frame(
            row,
            bg=color,
            width=13,
            height=13
        )

        indicator.pack(
            side="left"
        )

        indicator.pack_propagate(False)

        tk.Label(
            row,
            text=text,
            bg="white",
            fg=COLORS["text_secondary"],
            font=(FONT, 8)
        ).pack(
            side="left",
            padx=8
        )


    # ========================================================
    # QUESTION PANEL
    # ========================================================

    def create_question_panel(self, parent):

        q = self.questions[
            self.current_question_index
        ]

        question_number = (
            self.current_question_index + 1
        )

        total_questions = len(
            self.questions
        )

        # restore previous answer

        previous_answer = self.answers.get(
            q.id,
            -1
        )

        self.selected_choice.set(
            previous_answer
        )

        # ====================================================
        # QUESTION META
        # ====================================================

        meta = tk.Frame(
            parent,
            bg=COLORS["background"]
        )

        meta.pack(
            fill="x",
            pady=(0, 12)
        )

        tk.Label(
            meta,
            text=f"QUESTION {question_number}",
            bg=COLORS["background"],
            fg=COLORS["blue"],
            font=(FONT, 10, "bold")
        ).pack(
            side="left"
        )

        tk.Label(
            meta,
            text=f"{question_number} of {total_questions}",
            bg=COLORS["background"],
            fg=COLORS["text_secondary"],
            font=(FONT, 10)
        ).pack(
            side="right"
        )

        # ====================================================
        # QUESTION CARD
        # ====================================================

        card = tk.Frame(
            parent,
            bg="white",
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )

        card.pack(
            fill="both",
            expand=True
        )

        inside = tk.Frame(
            card,
            bg="white"
        )

        inside.pack(
            fill="both",
            expand=True,
            padx=42,
            pady=34
        )

        # -----------------------------------------
        # Instruction
        # -----------------------------------------

        tk.Label(
            inside,
            text="Select the best answer.",
            bg="white",
            fg=COLORS["text_muted"],
            font=(FONT, 9)
        ).pack(
            anchor="w"
        )

        # -----------------------------------------
        # Question
        # -----------------------------------------

        tk.Label(
            inside,
            text=q.text,
            bg="white",
            fg=COLORS["text"],
            font=(FONT, 19, "bold"),
            wraplength=700,
            justify="left"
        ).pack(
            anchor="w",
            pady=(12, 28)
        )

        # -----------------------------------------
        # Answer separator
        # -----------------------------------------

        tk.Frame(
            inside,
            bg=COLORS["border"],
            height=1
        ).pack(
            fill="x",
            pady=(0, 20)
        )

        # ====================================================
        # ANSWERS
        # ====================================================

        choices = self.get_question_choices(q)

        letters = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F"
        ]

        self.answer_widgets = []

        for index, choice in enumerate(choices):

            letter = (
                letters[index]
                if index < len(letters)
                else str(index + 1)
            )

            self.create_answer_option(
                inside,
                letter,
                choice
            )

        # ====================================================
        # BOTTOM NAVIGATION
        # ====================================================

        nav = tk.Frame(
            parent,
            bg=COLORS["background"]
        )

        nav.pack(
            fill="x",
            pady=(18, 0)
        )

        # Previous

        if self.current_question_index > 0:

            ttk.Button(
                nav,
                text="← Previous",
                style="Secondary.TButton",
                command=self.previous_question
            ).pack(
                side="left"
            )

        # Right buttons

        right = tk.Frame(
            nav,
            bg=COLORS["background"]
        )

        right.pack(
            side="right"
        )

        if (
            self.current_question_index
            < total_questions - 1
        ):

            ttk.Button(
                right,
                text="Save & Continue →",
                style="Primary.TButton",
                command=self.next_question
            ).pack(
                side="right"
            )

        else:

            ttk.Button(
                right,
                text="Review & Submit",
                style="Primary.TButton",
                command=self.submit_assessment
            ).pack(
                side="right"
            )


    # ========================================================
    # ANSWER OPTION
    # ========================================================

    def create_answer_option(
        self,
        parent,
        letter,
        choice
    ):

        option = tk.Frame(
            parent,
            bg=COLORS["surface_soft"],
            highlightbackground=COLORS["border"],
            highlightthickness=1,
            cursor="hand2"
        )

        option.pack(
            fill="x",
            pady=6
        )

        # ----------------------------------------------------
        # Letter box
        # ----------------------------------------------------

        letter_box = tk.Label(
            option,
            text=letter,
            width=3,
            bg="#E9EEF3",
            fg=COLORS["navy"],
            font=(FONT, 10, "bold")
        )

        letter_box.pack(
            side="left",
            fill="y",
            padx=(0, 14)
        )

        # ----------------------------------------------------
        # Radio button
        # ----------------------------------------------------

        radio = tk.Radiobutton(
            option,
            text=choice.text,
            variable=self.selected_choice,
            value=choice.id,
            command=self.answer_selected,
            bg=COLORS["surface_soft"],
            activebackground=COLORS["surface_soft"],
            fg=COLORS["text"],
            font=(FONT, 11),
            anchor="w",
            justify="left",
            selectcolor="white",
            wraplength=650,
            padx=4,
            pady=14
        )

        radio.pack(
            fill="x",
            expand=True
        )

        # make frame clickable

        def select_option(event=None):

            self.selected_choice.set(
                choice.id
            )

            self.answer_selected()

        option.bind(
            "<Button-1>",
            select_option
        )

        letter_box.bind(
            "<Button-1>",
            select_option
        )

        self.answer_widgets.append(
            (
                option,
                letter_box,
                radio,
                choice.id
            )
        )

        self.refresh_answer_styles()


    # ========================================================
    # ANSWER SELECTION
    # ========================================================

    def answer_selected(self):

        q = self.questions[
            self.current_question_index
        ]

        choice_id = (
            self.selected_choice.get()
        )

        if choice_id != -1:

            self.answers[q.id] = choice_id

        self.refresh_answer_styles()


    # ========================================================
    # REFRESH ANSWER UI
    # ========================================================

    def refresh_answer_styles(self):

        if not hasattr(
            self,
            "answer_widgets"
        ):
            return

        selected = (
            self.selected_choice.get()
        )

        for (
            frame,
            letter,
            radio,
            choice_id
        ) in self.answer_widgets:

            if choice_id == selected:

                frame.configure(
                    bg=COLORS["selected_bg"],
                    highlightbackground=COLORS["selected_border"],
                    highlightthickness=2
                )

                letter.configure(
                    bg=COLORS["blue"],
                    fg="white"
                )

                radio.configure(
                    bg=COLORS["selected_bg"],
                    activebackground=COLORS["selected_bg"]
                )

            else:

                frame.configure(
                    bg=COLORS["surface_soft"],
                    highlightbackground=COLORS["border"],
                    highlightthickness=1
                )

                letter.configure(
                    bg="#E9EEF3",
                    fg=COLORS["navy"]
                )

                radio.configure(
                    bg=COLORS["surface_soft"],
                    activebackground=COLORS["surface_soft"]
                )


    # ========================================================
    # QUESTION NAVIGATION
    # ========================================================

    def go_to_question(self, index):

        self.save_current_answer()

        self.current_question_index = index

        self.show_exam_page()


    def previous_question(self):

        self.save_current_answer()

        if self.current_question_index > 0:

            self.current_question_index -= 1

            self.show_exam_page()


    def next_question(self):

        if self.selected_choice.get() == -1:

            answer = messagebox.askyesno(
                "Question Not Answered",
                (
                    "You have not selected an answer.\n\n"
                    "Would you like to continue anyway?"
                )
            )

            if not answer:
                return

        self.save_current_answer()

        if (
            self.current_question_index
            < len(self.questions) - 1
        ):

            self.current_question_index += 1

            self.show_exam_page()


    # ========================================================
    # SAVE ANSWER
    # ========================================================

    def save_current_answer(self):

        if not self.questions:
            return

        q = self.questions[
            self.current_question_index
        ]

        selected = (
            self.selected_choice.get()
        )

        if selected != -1:

            self.answers[q.id] = selected


    # ========================================================
    # SUBMIT
    # ========================================================

    def submit_assessment(self):

        self.save_current_answer()

        unanswered = (
            len(self.questions)
            - len(self.answers)
        )

        if unanswered > 0:

            message = (
                f"You still have {unanswered} unanswered "
                f"question(s).\n\n"
                "Do you want to submit the assessment anyway?"
            )

        else:

            message = (
                "You have answered all questions.\n\n"
                "Submit your assessment now?"
            )

        confirm = messagebox.askyesno(
            "Final Submission",
            message
        )

        if confirm:

            self.show_results_page()


    # ========================================================
    # CALCULATE SCORE
    # ========================================================

    def calculate_score(self):

        correct = 0

        for question in self.questions:

            selected_id = self.answers.get(
                question.id
            )

            if selected_id is None:
                continue

            for choice in self.get_question_choices(
                question
            ):

                if (
                    choice.id == selected_id
                    and choice.is_correct
                ):

                    correct += 1
                    break

        total = len(self.questions)

        percentage = (
            correct / total * 100
            if total > 0
            else 0
        )

        return (
            correct,
            total,
            percentage
        )


    # ========================================================
    # RESULT PAGE
    # ========================================================

    def show_results_page(self):

        self.clear_page()

        self.create_header(
            self.container
        )

        correct, total, percentage = (
            self.calculate_score()
        )

        # ====================================================
        # BACKGROUND
        # ====================================================

        content = tk.Frame(
            self.container,
            bg=COLORS["background"]
        )

        content.pack(
            fill="both",
            expand=True
        )

        # ====================================================
        # TITLE
        # ====================================================

        title_area = tk.Frame(
            content,
            bg=COLORS["background"]
        )

        title_area.pack(
            pady=(38, 22)
        )

        tk.Label(
            title_area,
            text="Assessment Results",
            bg=COLORS["background"],
            fg=COLORS["text"],
            font=(FONT, 28, "bold")
        ).pack()

        tk.Label(
            title_area,
            text="Computer Hardware Fundamentals",
            bg=COLORS["background"],
            fg=COLORS["text_secondary"],
            font=(FONT, 11)
        ).pack(
            pady=(6, 0)
        )

        # ====================================================
        # RESULT CARD
        # ====================================================

        card = tk.Frame(
            content,
            bg="white",
            width=700,
            height=430,
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )

        card.pack()

        card.pack_propagate(False)

        inside = tk.Frame(
            card,
            bg="white"
        )

        inside.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=32
        )

        # ====================================================
        # STATUS
        # ====================================================

        if percentage >= 80:

            result_title = "Excellent Performance"
            result_text = (
                "You demonstrated a strong understanding "
                "of computer hardware fundamentals."
            )

        elif percentage >= 60:

            result_title = "Satisfactory Performance"
            result_text = (
                "You demonstrated a good understanding, "
                "with some areas available for improvement."
            )

        else:

            result_title = "Further Review Recommended"
            result_text = (
                "Additional study of computer hardware "
                "fundamentals is recommended."
            )

        tk.Label(
            inside,
            text="ASSESSMENT COMPLETED",
            bg="white",
            fg=COLORS["success"],
            font=(FONT, 9, "bold")
        ).pack()

        tk.Label(
            inside,
            text=result_title,
            bg="white",
            fg=COLORS["text"],
            font=(FONT, 20, "bold")
        ).pack(
            pady=(8, 4)
        )

        tk.Label(
            inside,
            text=result_text,
            bg="white",
            fg=COLORS["text_secondary"],
            font=(FONT, 10),
            wraplength=500,
            justify="center"
        ).pack()

        # ====================================================
        # SCORE
        # ====================================================

        score_frame = tk.Frame(
            inside,
            bg=COLORS["surface_soft"],
            highlightbackground=COLORS["border"],
            highlightthickness=1
        )

        score_frame.pack(
            fill="x",
            pady=28
        )

        # Percentage

        percentage_box = tk.Frame(
            score_frame,
            bg=COLORS["surface_soft"]
        )

        percentage_box.pack(
            side="left",
            expand=True,
            fill="both",
            pady=20
        )

        tk.Label(
            percentage_box,
            text=f"{percentage:.0f}%",
            bg=COLORS["surface_soft"],
            fg=COLORS["navy"],
            font=(FONT, 33, "bold")
        ).pack()

        tk.Label(
            percentage_box,
            text="FINAL SCORE",
            bg=COLORS["surface_soft"],
            fg=COLORS["text_muted"],
            font=(FONT, 8, "bold")
        ).pack()

        # Divider

        tk.Frame(
            score_frame,
            bg=COLORS["border"],
            width=1
        ).pack(
            side="left",
            fill="y",
            pady=18
        )

        # Correct

        correct_box = tk.Frame(
            score_frame,
            bg=COLORS["surface_soft"]
        )

        correct_box.pack(
            side="left",
            expand=True,
            fill="both",
            pady=20
        )

        tk.Label(
            correct_box,
            text=f"{correct} / {total}",
            bg=COLORS["surface_soft"],
            fg=COLORS["text"],
            font=(FONT, 24, "bold")
        ).pack()

        tk.Label(
            correct_box,
            text="CORRECT ANSWERS",
            bg=COLORS["surface_soft"],
            fg=COLORS["text_muted"],
            font=(FONT, 8, "bold")
        ).pack()

        # ====================================================
        # CANDIDATE
        # ====================================================

        candidate_name = getattr(
            self.user,
            "name",
            ""
        )

        candidate_email = getattr(
            self.user,
            "email",
            ""
        )

        tk.Label(
            inside,
            text=f"Candidate: {candidate_name}",
            bg="white",
            fg=COLORS["text"],
            font=(FONT, 10, "bold")
        ).pack()

        tk.Label(
            inside,
            text=candidate_email,
            bg="white",
            fg=COLORS["text_secondary"],
            font=(FONT, 9)
        ).pack(
            pady=(3, 20)
        )

        # ====================================================
        # ACTIONS
        # ====================================================

        buttons = tk.Frame(
            inside,
            bg="white"
        )

        buttons.pack()

        ttk.Button(
            buttons,
            text="Take Assessment Again",
            style="Secondary.TButton",
            command=self.restart_assessment
        ).pack(
            side="left",
            padx=6
        )

        ttk.Button(
            buttons,
            text="Exit",
            style="Primary.TButton",
            command=self.close_application
        ).pack(
            side="left",
            padx=6
        )


    # ========================================================
    # RESTART
    # ========================================================

    def restart_assessment(self):

        self.user = None
        self.questions = []
        self.answers = {}

        self.current_question_index = 0

        self.selected_choice.set(-1)

        self.show_welcome_page()


    # ========================================================
    # CLOSE
    # ========================================================

    def close_application(self):

        try:
            db.close()

        except:
            pass

        self.destroy()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    app = AcademicQuizApp()

    app.mainloop()