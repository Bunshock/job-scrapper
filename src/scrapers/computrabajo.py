from datetime import datetime
from bs4 import BeautifulSoup
import requests
from scrapers.base import JobScraperBase

class ComputrabajoScraper(JobScraperBase):
    BASE_URL = "https://ar.computrabajo.com/"

    def __init__(self):
        super().__init__()

    def initialize_scraper(self):
        print("-" * 40)
        print("Configuration setup for Computrabajo scraper:")
        print("You can set search keywords and location when initializing the scraper.")
        print("Example:\n    keywords: 'developer, python', location: 'Buenos Aires'")
        print("You can also leave them blank to search for any job in any location.")
        print("But you must provide at least one keyword or a location to search (they cannot both be empty).")
        print("-" * 40)

        while True:
            self.search_keywords, self.location = self.prompt_for_configuration()
            if len(self.search_keywords) > 0 or self.location != None:
                break
            print("\nERROR: You must provide at least keywords or a location. Please try again.\n" + "-" * 40)
    
    def fetch_jobs(self):
        # Logic to scrape job listings from the Computrabajo website
        # based on self.search_keywords and self.location
        
        # Construct the search URL based on keywords and location
        query = "+".join(self.search_keywords)
        location_query = self.location.replace(" ", "-") if self.location else ""

        if not query and location_query:
            search_url = f"{self.BASE_URL}empleos-en-{location_query}"
        elif query and not location_query:
            search_url = f"{self.BASE_URL}trabajo-de-{query}"
        elif query and location_query:
            search_url = f"{self.BASE_URL}trabajo-de-{query}-en-{location_query}"
        else:
            print("Error: You must provide at least keywords or a location.")
            return

        # Print the configured URL
        print("-" * 40)
        print(f"Fetching jobs from: {search_url}")
        
        # Fetch the job listings
        response = requests.get(search_url, headers=self.HEADERS)
        if response.status_code != 200:
            print(response.content)
            print("Failed to fetch jobs from Computrabajo.")
            return

        # Parse the response content
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = []
        for job_card in soup.select("article.box_offer"):
            
            # Title
            title_tag = job_card.select_one("a.js-o-link")
            title = title_tag.get_text(strip=True) if title_tag else "No title found"

            # Company
            company_tag = job_card.select_one("a.fc_base.t_ellipsis")
            company = company_tag.get_text(strip=True) if company_tag else "No company found"

            # Company link
            company_link_tag = job_card.select_one("a.fc_base.t_ellipsis")
            company_link = "No company link found"
            if company_link_tag and company_link_tag.has_attr("href"):
                company_link = self.BASE_URL.rstrip("/") + company_link_tag["href"]

            # Location
            location_tag = job_card.select("p.fs16.fc_base.mt5 span.mr10")
            location = "No location found"
            # Both the company rating and location are in the same tag structure
            # so we need to check for the class 'mr10' to get the location
            for loc in location_tag:
                if loc.get('class') == ['mr10']:
                    location = loc.get_text(strip=True)
                    break

            # Link
            link_tag = job_card.select_one("a.js-o-link")
            link = "No link found"
            if link_tag and link_tag.has_attr("href"):
                link = self.BASE_URL.rstrip("/") + link_tag["href"]
            
            jobs.append({
                "title": title,
                "company": company,
                "company_link": company_link,
                "location": location,
                "link": link,
                "source": "Computrabajo",
                "fetched_at": datetime.now()
            })

        # Update the fetched jobs
        self.fetched_jobs = self.fetched_jobs + jobs