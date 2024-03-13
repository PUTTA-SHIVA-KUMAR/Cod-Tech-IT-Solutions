import random

# Define questions and answers for each category
questions = {
    "History": {
        "What year did World War II end?": ["1945"],
        "Who was the first president of the United States?": ["George Washington"],
        "What city was the capital of the Roman Empire?": ["Rome"]
    },
    "Science": {
        "What is the chemical symbol for water?": ["H2O"],
        "Who developed the theory of relativity?": ["Albert Einstein"],
        "What is the largest organ in the human body?": ["Skin"]
    },
    "Geography": {
        "What is the capital of France?": ["Paris"],
        "Which continent is the largest by land area?": ["Asia"],
        "What is the longest river in the world?": ["Nile"]
    }
}

def quiz():
    score = 0
    
    # Iterate over each category
    for category, category_questions in questions.items():
        print(f"\n{category} Questions:")
        print("----------------------------")
        
        # Shuffle the order of questions
        shuffled_questions = random.sample(category_questions.items(), len(category_questions))
        
        # Iterate over each question in the shuffled order
        for question, answers in shuffled_questions:
            print(question)
            user_answer = input("Your answer: ").strip().capitalize()
            
            # Check if the user's answer matches any of the correct answers
            if user_answer in answers:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
                print("Correct answer(s):", ", ".join(answers))
                
    print("\nQuiz complete!")
    print("Your score:", score, "/", len(questions))
    print("Thank you for playing!")

# Run the quiz
quiz()
