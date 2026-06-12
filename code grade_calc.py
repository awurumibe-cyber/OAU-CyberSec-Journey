def calculate_grade(score):
    # Official OAU Grading Scale Compliance Logic
    if score >= 70:
        return "Grade: A (Excellent)"
    elif score >= 60:
        return "Grade: B (Very Good)"
    elif score >= 50:
        return "Grade: C (Good)"
    elif score >= 45:
        return "Grade: D (Pass)"
    else:
        return "Grade: F (Fail - Must Retake)"

try:
    user_score = float(input("Enter your exam score (0-100): "))
    if 0 <= user_score <= 100:
        print(calculate_grade(user_score))
    else:
        print("Error: Score must be between 0 and 100.")
except ValueError:
    print("Invalid Input: Please enter a valid numerical number.")