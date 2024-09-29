def GetScore():
    # Get the number of students
    num_students = int(input("Enter the number of students: "))
    scores = []

    for i in range(num_students):
        
        score = float(input(f"Enter score for student {i + 1} (0-100): "))
        if 0 < score < 100:
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
    scores = GetScore()
    
    print(f"Total score: {Total(scores)}")
    print(f"Average score: {Average(scores)}")
    print(f"Maximum score: {Max(scores)}")
    print(f"Minimum score: {Min(scores)}")
    print(f"Number of students passed: {Passed(scores)}")
    print(f"Number of students failed: {Failed(scores)}")

main()
