# job_scraper_app.py

import time
from scheduler import JobScheduler
from scrapers.scraper_registry import SCRAPER_CLASSES

def main():
    print("-" * 40 + "\nWelcome to the Job Scraper App!\n" + "-" * 40)

    # Prompt user to select scraper class
    print("Available scrapers:", ", ".join(SCRAPER_CLASSES.keys()))
    while True:
        scraper_name = input("Enter the job site to scrape: ").strip().lower()
        if scraper_name in SCRAPER_CLASSES:
            break
        else:
            print("Invalid scraper name. Please choose from:", ", ".join(SCRAPER_CLASSES.keys()))

    scraper = SCRAPER_CLASSES[scraper_name]()
    scraper.initialize_scraper()
    print("\nScraper initialized successfully.\n" + "-" * 40)

    # TODO: Load previously fetched jobs from a file or database if needed

    # Prompt for interval in minutes
    print("You can set an interval for automatic job fetching.")
    while True:
        try:
            interval_minutes = int(input("Enter interval in minutes between searches (minimum 5): ").strip())
            if interval_minutes >= 5:
                break
            else:
                print("Please enter a value of 5 or more.")
        except ValueError:
            print("Please enter a valid integer.")

    print(f"Automatic job fetching will occur every {interval_minutes} minutes.")
    scheduler = JobScheduler(interval_minutes * 60, scraper)
    print("\nJob Scheduler created successfully.\n" + "-" * 40)

    while True:
        user_input = input("Type 'run' to fetch jobs manually, 'start' to schedule" \
        " automatic fetching, 'view' to see all fetched jobs, or 'exit' to quit: ").strip().lower()
        
        if user_input == 'run':
            scraper.get_new_jobs()
            scraper.print_new_jobs()
        
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

        elif user_input == 'clear':
            print("Clearing fetched jobs.")
            scraper.clear_jobs()
            print("Fetched jobs cleared successfully.")

        elif user_input == 'view':
            print("Currently fetched jobs:")
            scraper.print_fetched_jobs()
        
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()