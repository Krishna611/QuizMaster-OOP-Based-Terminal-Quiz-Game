# quizmaster/question.py

class Question:
    """
    Represents a single multiple-choice question.
    correct_option is expected to be 1..n (1-based index).
    """
    def __init__(self, question_text: str, options: list[str], correct_option: int):
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option  # 1-based

    def is_correct(self, choice: int) -> bool:
        """Return True if user's choice (1-based) matches the correct option."""
        return choice == self.correct_option
