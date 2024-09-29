def TotalScore(Scores):
    Total =0
    for score in Scores:
        Total += score
    return Total

Scores=[56,75,64,82,77,68]
Total = TotalScore(Scores)
Average = Total/len(Scores)

print(f"Total = {Total}, Average = {Average}")
    