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
                company_link = base_url.rstrip("/") + company_link_tag["href"]

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
                link = base_url.rstrip("/") + link_tag["href"]
            
            jobs.append({
                "title": title,
                "company": company,
                "company_link": company_link,
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

        if new_jobs:
            print("-" * 40)
            print("New jobs found:")
            for job in new_jobs:
                print("-" * 40)
                print(f"Title: {job['title']}")
                print(f"Company: {job['company']}  ({job['company_link']})")
                print(f"Location: {job['location']}")
                print(f"Link: {job['link'] if job['link'] else 'No link found'}")
        else:
            print("No new jobs found.")
        print("-" * 40)
        
        return new_jobs