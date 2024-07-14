from question import Question


class Quiz:

    def __init__(self, questions):
        self.current_question = Question("", "")
        self.total_questions_processed = 0
        self.questions = questions
        self.current_answer = ""
        self.current_score = 0
        self.start_quiz(questions)

    def get_current_question(self, question_i):
        self.current_question = Question(question_i['text'], question_i['answer'])
        print(self.current_question.question)

    def get_current_answer(self):
        self.current_answer = input("Enter the answer to the question with 'T' for True" +
                                    " and 'F' for False." +
                                    " To skip to the next question, type 'S'.\n")
        self.validate_current_answer()

    def validate_current_answer(self):
        if self.current_answer is None or self.current_answer == "":
            print("No answer detected. Let's try the next one")
            return
        elif (self.current_answer.upper()[0] != 'F' or self.current_answer.upper()[0] != 'S' or
              self.current_answer.upper()[0] != 'T'):
            print("No answer detected. Let's try the next one")
            return
        elif self.current_answer.upper() == "S":
            return
        elif self.current_question.answer.upper()[0] == self.current_answer.upper()[0]:
            print("Correct Answer")
            self.current_score += 1
        else:
            print("Not quite! Let's try the next one")

    def start_quiz(self, questions):
        while len(self.questions) > self.total_questions_processed:
            for question_i in questions:
                self.get_current_question(question_i)
                self.get_current_answer()
                self.total_questions_processed += 1

                if len(self.questions) != self.total_questions_processed:
                    print("Next Question:")

        print("Quiz ended!\n")
        print(f'Your score is {self.current_score}\n')
        print("Congratulations! (or not, lol)")
