# quizmaster/manager.py

import json
from typing import Dict, List
from .question import Question
from .quiz import Quiz
from .utils import clear_screen, safe_int_input

class QuizManager:
    """
    Handles loading questions from a JSON file, category selection,
    and launching a Quiz instance.
    """
    def __init__(self, filename: str):
        self.filename = filename
        self.categories: Dict[str, List[Question]] = {}

    def load_questions(self) -> None:
        with open(self.filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        loaded = {}
        for category, qs in data.items():
            questions = []
            for q in qs:
                question_text = q.get("question", "").strip()
                options = q.get("options", [])
                answer = q.get("answer", 1)  # expecting 1-based answer in JSON
                # Validate
                if (not question_text) or (not isinstance(options, list)) or len(options) == 0:
                    continue
                if not isinstance(answer, int) or answer < 1 or answer > len(options):
                    continue
                questions.append(Question(question_text, options, answer))
            if questions:
                loaded[category] = questions

        self.categories = loaded

    def choose_category(self) -> str:
        if not self.categories:
            raise RuntimeError("No categories loaded. Please check your questions file.")

        print("Available Categories:")
        cats = list(self.categories.keys())
        for i, cat in enumerate(cats, start=1):
            print(f"{i}. {cat}")
        choice = safe_int_input("Select category: ", valid_range=range(1, len(cats) + 1)) - 1
        return cats[choice]

    def start(self, shuffle_questions: bool = True, shuffle_options: bool = True) -> None:
        clear_screen()
        selected = self.choose_category()
        quiz = Quiz(selected, self.categories[selected], shuffle_questions=shuffle_questions, shuffle_options=shuffle_options)
        quiz.start_quiz()
