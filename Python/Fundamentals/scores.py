import random

# def scoresAndGrades(reps):
#     print "Scores and Grades"
#     for x in range(0, reps):
#         score = random.randint(60,101)
#         if score >= 60 and score <= 69:
#             print "Score", score, ": your grade is a D"
#         elif score >=70 and score <= 79:
#             print "Score", score, ": your grade is a C"
#         elif score >= 80 and score <= 89:
#             print "Score", score, ": your grade is a B"
#         elif score >=90 and score <= 100:
#             print "Score", score, ": your grade is an A"
#         else:
#             print "You failed. Sorry"
#     print "End of program, bye."
# scoresAndGrades(10)

def coinToss(reps):
    attempt_count = 1
    head_count = 0
    tail_count = 0
    result = ""
    result_string_complete = ""

    for x in range(1, reps):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            result = "heads"
            head_count += 1
            print "Attempt #", attempt_count, " :Throwing a coin... It's a", result, "! Got", head_count, "head(s) so far and ", tail_count, "tail(s) so far"
        else:
            result = "tails"
            tail_count += 1
            print "Attempt #", attempt_count, " :Throwing a coin... It's a", result, "! Got", tail_count, "tail(s) so far and ", head_count, "head(s) so far"
        attempt_count += 1
        
    
coinToss(5001)
    

    

    