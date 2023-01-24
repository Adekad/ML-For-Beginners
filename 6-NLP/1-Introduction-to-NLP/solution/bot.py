import nltk
nltk.download('punkt')
import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["C'est assez intéressant, s'il vous plaît dites-m'en plus.",
                    "Je vois. Continuez.",
                    "Pourquoi dites-vous cela?",
                    "Drôle de temps que nous avons eu, n'est-ce pas ?",
                    "Changeons de sujet.",
                    "Avez-vous vu le match hier soir ?"]

print("Bonjour, je suis Marvin, le robot simple.")
print("Vous pouvez mettre fin à cette conversation à tout moment en tapant 'bye'")
print("Après avoir tapé chaque réponse, appuyez sur 'enter'")
print("Comment vas-tu aujourd'hui?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "bye":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("It was nice talking to you, goodbye!")
