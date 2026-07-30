class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def still_has_question(self):
        if self.question_number <= len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question= self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}:{current_question.text}(True/False):").lower()
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer==correct_answer.lower():
            print("You are Correct")
            self.score+=1

        else:
            print("You are Wrong")
        print(f"Correct Answer: {correct_answer}")
        print(f"Your correct score is {self.score}/{self.question_number}.")
        print()
