from lib import sheets
from lib import scrape_data
from lib import weeks_left

# TODO: figure out how to find the amount of weeks off there are left
# TODO: figure out how to scrape data from beacon card website
# TODO: figure out how to get account balance from citizens bank API

def main():
    weeks_left.getWeeksLeft({'year': 2023, 'month': 5, 'day': 23}, 6)
    pass

if __name__ == "__main__":
    main()