xyear = int(input("Enter a year: "))

def chkLeapYr(xyear):
    isLeap = False
    if (xyear%4==0 and xyear%100!=0) or (xyear%400==0):
        isLeap = True
    else:
        isLeap = False
    return isLeap

print(chkLeapYr(xyear))