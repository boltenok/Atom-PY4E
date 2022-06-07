score = input("Please, enter your score: \n")
try:
    score_float = float(score)
except:
    print("Bad data")
    quit()
if score_float > 1.0 or score_float < 0.0:
    print("Bad data")
else:
    if score_float >= 0.9:
        print("A")
    elif score_float >= 0.8:
        print("B")
    elif score_float >= 0.7:
        print("C")
    elif score_float >= 0.6:
        print("D")
    else:
        print("F")
