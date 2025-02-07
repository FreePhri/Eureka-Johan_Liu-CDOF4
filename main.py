# -*- coding: utf-8 -*-
"""main

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sn2hwLupM_dSQ0QStzZxj5uLnfjf19TX
"""

import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        user_answer = input("Votre réponse (entrez le numéro de l'option) : ")
        return int(user_answer)

    def run(self):
        random.shuffle(self.questions)
        for question in self.questions:
            user_answer = self.display_question(question)
            correct_answer = question['correct_option']
            if user_answer == correct_answer:
                print("Correct !\n")
                self.score += 1
            else:
                print(f"Faux. La réponse correcte était l'option {correct_answer}.\n")

        print(f"Votre score final : {self.score}/{len(self.questions)}")

# Liste de questions
questions = [
    {
        'question': 'Quelle est la capitale de la France ?',
        'options': ['Berlin', 'Paris', 'Londres', 'Madrid'],
        'correct_option': 2
    },
    {
        'question': 'Quel est le plus grand océan du monde ?',
        'options': ['Océan Atlantique', 'Océan Pacifique', 'Océan Indien', 'Océan Arctique'],
        'correct_option': 1
    },
    {
        'question': 'Quel est le symbole chimique de l\'or ?',
        'options': ['O', 'Au', 'Ag', 'Fe'],
        'correct_option': 2
    },
    {
        'question': 'Qui a écrit "Roméo et Juliette" ?',
        'options': ['William Shakespeare', 'Jane Austen', 'Charles Dickens', 'F. Scott Fitzgerald'],
        'correct_option': 1
    },
    {
        'question': 'Quel est le plus grand désert du monde ?',
        'options': ['Désert du Sahara', 'Désert de Gobi', 'Désert d\'Atacama', 'Antarctique'],
        'correct_option': 4
    },
    # Ajoutez autant de questions que vous le souhaitez
]

# Créer une instance du jeu et le lancer
quiz = QuizGame(questions)
quiz.run()