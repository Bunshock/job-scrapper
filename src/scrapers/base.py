from abc import ABC, abstractmethod

class JobScraperBase(ABC):
    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0.0.0 Safari/537.36"
        )
    }
    
    def __init__(self):
        self.search_keywords = []
        self.location = None
        self.fetched_jobs = []
        self.new_jobs = []

    def prompt_for_configuration(self):
        raw_keywords_input = input("Enter job search keywords (comma-separated) (leave blank to search any job): ").split(',')
        search_keywords = [keyword.strip() for keyword in raw_keywords_input if keyword.strip()]

        location = input("Enter desired location (leave blank to search anywhere): ").strip()
        location = location if location else None

        return search_keywords, location

    @abstractmethod
    def initialize_scraper(self):
        pass

    @abstractmethod
    def fetch_jobs(self):
        pass

    def get_new_jobs(self):
        # Fetch the latest jobs
        previous_jobs_links = {job['link'] for job in self.fetched_jobs}
        self.fetch_jobs()

        # Filter jobs that are new (not in previous fetched_jobs)
        self.new_jobs = [job for job in self.fetched_jobs if job['link'] not in previous_jobs_links]

    def clear_jobs(self):
        self.jobs = []

    def print_job_list(self, job_list):
        # We asume job_list is not empty
        for job in job_list:
            print("-" * 40)
            print(f"Title: {job['title']}")
            print(f"Company: {job['company']}  ({job['company_link']})")
            print(f"Location: {job['location']}")
            print(f"Link: {job['link'] if job['link'] else 'No link found'}")
            print(f"Source: {job['source']}")
            print(f"Fetched at: {job['fetched_at']}")

    def print_fetched_jobs(self):
        if not self.fetched_jobs:
            print("No jobs fetched yet.")
            return
        
        print("-" * 40)
        print("Fetched Jobs:")
        self.print_job_list(self.fetched_jobs)

    def print_new_jobs(self):
        if not self.new_jobs:
            print("No new jobs found.")
            return
        
        print("-" * 40)
        print("New Jobs:")
        self.print_job_list(self.new_jobs)