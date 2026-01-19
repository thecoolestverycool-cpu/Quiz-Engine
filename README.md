# Quiz-Engine
This Python script has a Quiz Engine using Object Oriented Programming to make clean, readable code. It asks either type or multiple choice questions one by one, defined by the user.

To define a question, you can create a Question object using either the MultipleChoiceQuestion class or TypeQuestion class. The TypeQuestion takes in a question and a correct (both must be strings). The MultipleChoice Question class takes in a question, answers (a tuple) and a correct (string) which is the number of the correct answer. For example, you could have q1 = MultipleChoiceQuestion('Question', ('answer 1', 'answer 2', 'answer 3), '3').

To make a quiz, simply create a Quiz object passing in a tuple of questions. Then, call the run methond on your Quiz object.
