from datetime import datetime as dt
from datetime import timedelta as td

def main():
    startstring = "01/01/1901"
    endstring = "12/31/2000"
    sd = dt.strptime(startstring, '%m/%d/%Y')
    sdd = sd
    ed = dt.strptime(endstring, '%m/%d/%Y')
    daydelt = td(1)
    count = 0
    while sd <= ed:
        if sd.day == 1 and sd.weekday() == 6:
            count+=1
        sd+=daydelt
    print(count)
    return sdd, ed

if __name__ == '__main__':
    main()
