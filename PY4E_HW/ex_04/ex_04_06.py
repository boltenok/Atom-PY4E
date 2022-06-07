# inputs
sh = input ("Enter Hours: ")
sr = input ("Enter Pay Rate: ")

# converting inputs to float numbers
try:
    fh = float (sh)
    fr = float (sr)
except:
    print ("Error, please enter numeric input")
    quit()

#compute (fh, fr)
def computepay (fh, fr):
    if fh > 40:
    #overtime
        reg = fh * fr
        otp = (fh - 40)*(fr * 0.5)
        xp = reg + otp
    else:
    #regular Pay
        xp = fh * fr
    return xp
# x = computepay  (fh, fr)
print ("Pay", computepay  (fh, fr))
