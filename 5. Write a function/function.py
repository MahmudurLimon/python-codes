xyear = int(input("Enter a year: "))

def chkLeapYr(xyear):
    if (xyear%4==0 and xyear%100!=0) or (xyear%400==0):
        isLeap = "true"
        print(isLeap)
    else:
        isLeap = "false"
        print(isLeap)

chkLeapYr(xyear)