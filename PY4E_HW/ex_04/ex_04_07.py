score = input("Please, enter your score: \n")
try:
    score_float = float(score)
except:
    print("Bad data")
    quit()
def computegrade(score_float):
    if score_float > 1.0 or score_float < 0.0:
        return "Bad data"
    else:
        if score_float >= 0.9:
            return "A"
        elif score_float >= 0.8:
            return "B"
        elif score_float >= 0.7:
            return "C"
        elif score_float >= 0.6:
            return "D"
        else:
            return "F"
print (computegrade(score_float))
