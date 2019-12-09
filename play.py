import hangman
import random

answers = ["apple",
          "banana",
          "peach",
          "lemon",
          "ichigiku",
          "beef"
          ]

hangman.hangman(random.choice(answers))
