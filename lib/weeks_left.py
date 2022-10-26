import datetime

# lastDat should have the object structure{'year': int, 'month': int, 'day': 'int'}
def getWeeksLeft(lastDay, weeksOff = 0):
    today = datetime.datetime.today()
    lastDayFormatted = datetime.datetime(lastDay['year'], lastDay['month'], lastDay['day'])
    print((lastDayFormatted - today).days)


def main():
    pass

if __name__ == '__main__':
    main()