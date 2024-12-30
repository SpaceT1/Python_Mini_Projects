questions = ("Who carried Harry in the beginning of the first movie?",
             "Who opened chamber of secrets for the first time?",
             "Why Severus replaced Lupin for some of the classes",
             "How many forbidden curses are there?",
             "Who died in the end of the fifth movie?")

options = (("A.Dumbledore", "B.Minerva", "C.Hargid", "D.Harry himself"),
           ("A.Tom Riddle", "B.Hagrid", "C.Harry", "D.Jinny"),
           ("A.He hates Lupin", "B.Lupin died", "C.Dumbledore told to", "D.Lupin is werewolf"),
           ("A.1", "B.2", "C.3", "D.4"),
           ("A.Harry", "B.Ron", "C.Hermine", "D.Sirius"))

answers = ("C", "A", "D", "C", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print ("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------------")
print("         RESULTS           ")
print("---------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your final score is {score}%")