# main.py (place at project root QuizMaster-Python/main.py)

from quizmaster.manager import QuizManager
from quizmaster.utils import pause, clear_screen

def main():
    config = {
        "shuffle_questions": True,
        "shuffle_options": True,
        "questions_file": "questions.json",
    }

    mgr = QuizManager(config["questions_file"])
    try:
        mgr.load_questions()
    except FileNotFoundError:
        print("questions.json not found. Put questions.json next to main.py.")
        return

    while True:
        clear_screen()
        print("=== QUIZMASTER ===")
        print("1. Start Quiz")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            clear_screen()
            mgr.start(shuffle_questions=config["shuffle_questions"], shuffle_options=config["shuffle_options"])
            pause()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            pause()

if __name__ == "__main__":
    main()
