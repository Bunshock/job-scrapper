class JobScraper:
    def __init__(self, search_keywords):
        self.search_keywords = search_keywords
        self.jobs = []

    def fetch_jobs(self):
        raise NotImplementedError("Subclasses should implement this method to fetch jobs.")

    def get_new_jobs(self):
        new_jobs = [job for job in self.jobs if self.is_new_job(job)]
        return new_jobs

    def is_new_job(self, job):
        # Logic to determine if a job is new
        pass

    def clear_jobs(self):
        self.jobs = []