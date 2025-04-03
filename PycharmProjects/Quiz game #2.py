#Quiz game 2

questions= ("How many countries are in the European Union?: ",
            "What's the smallest country?: ",
            "Which country's flag has an eagle and a snake on it?: ",
            "What's the world's largest ocean?: ",
            "Poland's flag is red, and which other color?: ")
options= (("A. 20", "B. 27", "C. 32", "D. 35"),
          ("A. Vatican City", "B. Italy", "C. Japan", "D. New Zealand"),
          ("A. USA", "B. Mexico", "C. North Korea", "D. Zimbabwe"),
          ("A. Pacific", "B. Atlantic", "C. Artic", "D. Indian"),
          ("A. White", "B. Blue", "C. Yellow", "D. Green"))


answers = ("B", "A", "B", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter A. B. C. D. ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print ("Congrats!")
    else:
        print ("Sorry, maybe next time!")
        print(f"IF you WERE SMArT YOUd know iT WaS {answers[question_num]}")

    question_num += 1

print("$$$$$$$$$")
print(" Results ")
print("$$$$$$$$$")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
score = int(score / len(questions) * 100)
print(f"your final score is: {score}%")
print("now fuck off")




