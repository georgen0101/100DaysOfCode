from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
# Write a for loop to iterate over the question_data
for question in question_data:
    # Access the dictionary values -- Test
    # print(dic["text"])
    # print(dic["answer"])
    # Best practice?
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # Create a Question object from each entry in question_data
    new_question = Question(q_text=question_text, q_answer=question_answer)
    # Append each Question (object) to the question_bank
    question_bank.append(new_question)

quiz = QuizBrain(question_list=question_bank)


while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

