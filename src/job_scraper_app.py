# job_scraper_app.py

import time
from jobs.computrabajo import ComputrabajoScraper
from scheduler import JobScheduler

def main():
    search_keywords = input("Enter job search keywords (comma-separated): ").split(',')
    search_keywords = [keyword.strip() for keyword in search_keywords]

    scraper = ComputrabajoScraper(search_keywords)
    scheduler = JobScheduler(scraper)

    while True:
        user_input = input("Type 'run' to fetch jobs manually, 'start' to schedule" \
        " automatic fetching, or 'exit' to quit: ").strip().lower()
        
        if user_input == 'run':
            new_jobs = scraper.get_new_jobs()
            if new_jobs:
                print("New jobs found:")
                for job in new_jobs:
                    print(job)
            else:
                print("No new jobs found.")
        
        elif user_input == 'start':
            interval = 10  # Fetch jobs every 10 minutes
            print(f"Starting automatic job fetching every {interval} minutes...")
            scheduler.start(interval)
        
        elif user_input == 'exit':
            print("Exiting the program.")
            scheduler.stop()
            break
        
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()