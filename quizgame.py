# ==============================
#        QUIZ GAME
# ==============================

questions = [
    {
        "question": "What is the capital of India?",
        "options": [
            "A. Mumbai",
            "B. New Delhi",
            "C. Kolkata",
            "D. Chennai"
        ],
        "answer": "B"
    },

    {
        "question": "Which language are we learning?",
        "options": [
            "A. Java",
            "B. C++",
            "C. Python",
            "D. HTML"
        ],
        "answer": "C"
    },

    {
        "question": "Which data type is used to store True or False?",
        "options": [
            "A. String",
            "B. Boolean",
            "C. Integer",
            "D. Float"
        ],
        "answer": "B"
    },

    {
        "question": "Which keyword is used to create a function in Python?",
        "options": [
            "A. function",
            "B. func",
            "C. define",
            "D. def"
        ],
        "answer": "D"
    }
]


# Starting score
score = 0

print("==============================")
print("         QUIZ GAME")
print("==============================")


# Go through each question
for i, question in enumerate(questions, start=1):

    print(f"\nQuestion {i}: {question['question']}")

    # Display options
    for option in question["options"]:
        print(option)

    # Ask until the user gives a valid option
    while True:

        user = input("Select option A, B, C, or D: ").upper()

        if user in ("A", "B", "C", "D"):
            break

        print("Invalid input! Please choose A, B, C, or D.")


    # Check the answer
    if user == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")


# Final result
print("\n==============================")
print("          QUIZ OVER")
print("==============================")

print(f"Your score: {score}/{len(questions)}")

percentage = score / len(questions) * 100

print(f"Your percentage: {percentage:.2f}%")