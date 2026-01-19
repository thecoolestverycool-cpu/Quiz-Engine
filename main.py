import math

class Question:
    def __init__(self, question, answers, correct):
        self.question = question
        self.answers = answers
        self.correct = correct

    def check(self, answer):
        if self.correct == answer:
            return True

        return False

class TypeQuestion(Question):
    def __init__(self, question, correct):
        super().__init__(question, None, correct)

    def __str__(self):
        question = f"{self.question}\n"
        question += "Type your answer below\n"
        return question

class MultipleChoiceQuestion(Question):
    def __init__(self, question, answers, correct):
        super().__init__(question, answers, correct)

    def __str__(self):
        spacing = 0
        question = f"{self.question}\n"

        for answer in self.answers:
            spacing += 1

            if spacing % 2 == 0:
                question += f"{spacing}. {answer}\n"
                continue

            question += f"{spacing}. {answer}, "

        question += "Type the number corresponding to your answer below"

        return question

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.total = len(questions)

        self.score = 0
        self.current_question = None
        self.question_number = -1

        self.push()

    def push(self):
        self.question_number += 1
        if self.question_number < self.total:
            self.current_question = self.questions[self.question_number]

        else:
            self.current_question = None

    def run(self):
        while self.current_question:
            print(self.current_question)
            correct = self.current_question.check(input(""))

            if correct:
                self.score += 1

            self.push()

        print(f"You got {self.score} question{'s' if self.score != 1 else ''} correct out of {self.total} question{'s' if self.total != 1 else ''} ({math.floor(self.score / self.total * 100)}%).")
