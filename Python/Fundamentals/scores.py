import random

def scoresAndGrades(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60,101)
        if score >= 60 and score <= 69:
            print "Score", score, ": your grade is a D"
        elif score >=70 and score <= 79:
            print "Score", score, ": your grade is a C"
        elif score >= 80 and score <= 89:
            print "Score", score, ": your grade is a B"
        elif score >=90 and score <= 100:
            print "Score", score, ": your grade is an A"
        else:
            print "You failed. Sorry"
    print "End of program, bye."
scoresAndGrades(10)