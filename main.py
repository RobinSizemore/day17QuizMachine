from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question_datum in question_data:
    question_bank.append(Question(question_datum["text"], question_datum["answer"]))

brainiac = QuizBrain(question_bank)
while brainiac.still_has_questions():
    brainiac.next_question()

print(f"You've completed the quiz.\nYour final score was {brainiac.user_score}/{brainiac.question_number}")