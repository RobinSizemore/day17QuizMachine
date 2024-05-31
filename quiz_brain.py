class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1  # Incrementing now to fix question number display below.
        response = input(f"Q.{self.question_number}: {question.question_text} (True/False)? ").lower()
        while not (response == "true" or response == "false"):
            print("Invalid response.")
            response = input(f"Q.{self.question_number}: {question.question_text} (True/False)?  ").lower()
        self.check_answer(response, question.answer)

    def still_has_questions(self):
        return not self.question_number >= len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("That's the correct answer.")
            self.user_score += 1
        else:
            print("I'm sorry, that's the incorrect answer.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.user_score}/{self.question_number}\n\n")


