from bs4 import BeautifulSoup
import requests

class ComputrabajoScraper:
    def __init__(self, search_keywords, location):
        self.search_keywords = search_keywords
        self.location = location
        self.fetched_jobs = []

    def fetch_jobs(self):
        # Logic to scrape job listings from the Computrabajo website
        # based on self.search_keywords and self.location

        if not self.search_keywords:
            print("No search keywords provided.")
            return
        
        # Construct the search URL based on keywords and location
        base_url = "https://ar.computrabajo.com/"
        query = "+".join(self.search_keywords)
        if self.location:
            location_query = self.location.replace(" ", "-").lower()
            search_url = f"{base_url}trabajo-de-{query}-en-{location_query}"
        else:
            search_url = f"{base_url}trabajo-de-{query}"

        # Print the configured URL
        print(f"Fetching jobs from: {search_url}")
        
        # Fetch the job listings
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            print(response.content)
            print("Failed to fetch jobs from Computrabajo.")
            return

        # Parse the response content
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []
        for job_card in soup.select("article.box_offer"):
            title = job_card.select_one("a.js-o-link").get_text(strip=True)
            company = job_card.select_one("a.emp").get_text(strip=True) if job_card.select_one("a.emp") else ""
            location = job_card.select_one("p.location").get_text(strip=True) if job_card.select_one("p.location") else ""
            link = base_url.rstrip("/") + job_card.select_one("a.js-o-link")["href"]
            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "link": link
            })

        # Update the fetched jobs
        self.fetched_jobs = jobs

    def get_new_jobs(self):
        # Logic to filter and return only new job postings

        # Fetch the latest jobs
        previous_jobs_links = {job['link'] for job in self.fetched_jobs}
        self.fetch_jobs()

        # Filter jobs that are new (not in previous fetched_jobs)
        new_jobs = [job for job in self.fetched_jobs if job['link'] not in previous_jobs_links]
        return new_jobs