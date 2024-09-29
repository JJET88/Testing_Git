def GetScore():
    # Get the number of students
    num_students = int(input("Enter the number of students: "))
    scores = []

    for i in range(num_students):
        
        score = float(input(f"Enter score for student {i + 1} (0-100): "))
        if 0 <= score <= 100:
            scores.append(score)
            
        else:
            print("Score must be between 0 and 100. Please try again.")
    
    return scores

def Total(scores):
    return sum(scores)

def Average(scores):
    if scores:
        return Total(scores) / len(scores)
    else:
        return 0

def Max(scores):
    if scores:
        return max(scores) 
    else:
        return 0

def Min(scores):
    if scores:
        return min(scores) 
    else:
        return 0

def Passed(scores):
    pass_student=0
    for s in scores:
        if s>=50:
            pass_student+=1
    return pass_student

def Failed(scores):
    fail_student=0
    for s in scores:
        if s<50:
            fail_student+=1
    return fail_student


def main():
    scores = []
    while True:
        print("\nMenu:")
        print("1. Input students' scores")
        print("2. Display the number of students")
        print("3. Display total score")
        print("4. Display average score")
        print("5. Display maximum score")
        print("6. Display minimum score")
        print("7. Display number of students who passed the exam")
        print("8. Display number of students who failed the exam")
        print("9. Exit program")
        
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            scores = GetScore()
        elif choice == '2':
            print(f"Number of students: {len(scores)}")
        elif choice == '3':
            print(f"Total score: {Total(scores)}")
        elif choice == '4':
            print(f"Average score: {Average(scores)}")
        elif choice == '5':
            print(f"Maximum score: {Max(scores)}")
        elif choice == '6':
            print(f"Minimum score: {Min(scores)}")
        elif choice == '7':
            print(f"Number of students passed: {Passed(scores)}")
        elif choice == '8':
            print(f"Number of students failed: {Failed(scores)}")
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


main()
        

