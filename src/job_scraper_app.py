# job_scraper_app.py

import time
from jobs.computrabajo import ComputrabajoScraper
from scheduler import JobScheduler

def main():
    search_keywords = input("Enter job search keywords (comma-separated) (leave blank to search any job): ").split(',')
    search_keywords = [keyword.strip() for keyword in search_keywords]

    location = input("Enter desired location (leave blank to search anywhere): ").strip()
    location = location if location else None

    while True:
        try:
            interval_minutes = int(input("Enter interval in minutes between searches (minimum 5): ").strip())
            if interval_minutes >= 5:
                break
            else:
                print("Please enter a value of 5 or more.")
        except ValueError:
            print("Please enter a valid integer.")

    scraper = ComputrabajoScraper(search_keywords, location)
    scheduler = JobScheduler(interval_minutes * 60, scraper)

    while True:
        user_input = input("Type 'run' to fetch jobs manually, 'start' to schedule" \
        " automatic fetching, or 'exit' to quit: ").strip().lower()
        
        if user_input == 'run':
            scraper.get_new_jobs()
        
        elif user_input == 'start':
            print(f"Starting automatic job fetching every {interval_minutes} minutes...")
            scheduler.start()

        elif user_input == 'stop':
            print("Stopping automatic job fetching.")
            scheduler.stop()
        
        elif user_input == 'exit':
            print("Exiting the program.")
            scheduler.stop()
            break
        
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()