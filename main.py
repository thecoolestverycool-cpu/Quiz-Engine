import math

import inquirer

print("--- QuizPy 2.0 ---")

class MultipleChoiceQuestion:
    def __init__(self, question, answers, answer):
        self.question = question
        self.answers = answers
        self.answer = answer

    def query(self):
        prompt = [
            inquirer.List(
                "q",
                message=self.question,
                choices=self.answers,
            ),
        ]

        user_answer = inquirer.prompt(prompt)
        if user_answer["q"] == self.answer:
            return 1

        return 0

class TextQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

    def query(self):
        prompt = [inquirer.Text('q', message=self.question)]

        user_answer = inquirer.prompt(prompt)

        if user_answer["q"] in self.answers:
            return 1

        return 0

class CheckboxQuestion:
    def __init__(self, question, answers, correct: list):
        self.question = question
        self.answers = answers
        self.correct = correct

    def query(self):
        prompt = [inquirer.Checkbox('q', message=self.question, choices=self.answers)]

        user_answer = inquirer.prompt(prompt)

        if user_answer["q"] == self.correct:
            return 1

        return 0

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.idx = -1
        self.current_q = None

    def push(self):
        self.idx += 1

        if self.idx < len(self.questions):
            self.current_q = self.questions[self.idx]
            return True

        else:
            self.current_q = None
            return False

    def run(self):
        while self.push():
            self.score += self.current_q.query()

        print(f"You got {self.score} point{'' if self.score != 1 else 's'} out of {len(self.questions)} question{'' if len(self.questions) != 1 else 's'} with a rate of {math.floor(self.score / len(self.questions) * 100)}%")
