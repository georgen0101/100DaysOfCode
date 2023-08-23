# Create a class called QuizBrain
class QuizBrain:
    # Write an __init__() method
    def __init__(self, question_list):
        # Initialise the question_number to 0
        self.question_number = 0
        # Initialise the question_list to an input
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Return False if there is no more questions, otherwise True."""
        return len(self.question_list) > self.question_number

    def next_question(self):
        # Retrieve the item at the current question_number from the question_list.
        question_object = self.question_list[self.question_number]
        self.question_number += 1
        # Show the Question text and ask for the user's answer.
        # question_text = question_object.text
        user_answer = input(f"Q.{self.question_number}: {question_object.text} (True/False)?: ")
        # print(self.question_number) # The question number.
        # print(self.question_list) # List of objects
        # print(question_object) # The object
        # print(question_text) # Question text access with object.attribute
        self.check_answer(user_answer=user_answer, correct_answer=question_object.answer)

    def check_answer(self, user_answer, correct_answer):
        # Safety check use .lower()
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}\n")

