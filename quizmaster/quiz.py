# quizmaster/quiz.py

from dataclasses import dataclass
from typing import List
from .question import Question
from .utils import safe_int_input
import random

@dataclass
class QuizResult:
    total: int
    score: int

    @property
    def percent(self) -> float:
        return (self.score / self.total) * 100 if self.total else 0.0

class Quiz:
    """
    Runs a quiz for a given category with a list of Question objects.
    Expects Question.correct_option to be 1-based (1..n).
    """
    def __init__(self, category: str, questions: List[Question], shuffle_questions: bool = True, shuffle_options: bool = True):
        self.category = category
        self.questions = list(questions)
        self.score = 0
        self.shuffle_questions = shuffle_questions
        self.shuffle_options = shuffle_options

    def _ask_question(self, idx: int, q: Question):
        print(f"\nQ{idx}. {q.question_text}\n")

        # Prepare options; we will preserve original indices (1-based)
        option_pairs = [{"text": opt, "orig_index": i + 1} for i, opt in enumerate(q.options)]

        # Optionally shuffle options while keeping orig_index to check correctness
        if self.shuffle_options:
            random.shuffle(option_pairs)

        # Display options with displayed index (1..n based on display order)
        for disp_i, pair in enumerate(option_pairs, start=1):
            print(f"  {disp_i}. {pair['text']}")

        # Map displayed index -> original index
        valid_range = range(1, len(option_pairs) + 1)
        chosen_display = safe_int_input(f"\nEnter your choice (1-{len(option_pairs)}): ", valid_range=valid_range)

        # Convert displayed choice to original index to compare with q.correct_option
        chosen_pair = option_pairs[chosen_display - 1]
        chosen_orig_index = chosen_pair["orig_index"]

        if q.is_correct(chosen_orig_index):
            print("\n✅ Correct!\n")
            self.score += 1
        else:
            correct_text = q.options[q.correct_option - 1] if 1 <= q.correct_option <= len(q.options) else "Unknown"
            print(f"\n❌ Wrong! Correct answer: {q.correct_option}. {correct_text}\n")

    def start_quiz(self) -> QuizResult:
        print(f"\n=== Starting Quiz: {self.category} ===")
        if self.shuffle_questions:
            random.shuffle(self.questions)

        for idx, q in enumerate(self.questions, start=1):
            self._ask_question(idx, q)

        return self.show_result()

    def show_result(self) -> QuizResult:
        total = len(self.questions)
        result = QuizResult(total=total, score=self.score)
        percent = result.percent
        print("\n---- RESULT ----")
        print(f"Score: {self.score}/{total} ({percent:.2f}%)")

        if percent == 100:
            print("🏆 Excellent! Perfect score!")
        elif percent >= 70:
            print("👏 Good job, keep it up!")
        elif percent >= 40:
            print("🙂 Keep practicing!")
        else:
            print("💡 Try Again, practice more!")

        print()
        return result
