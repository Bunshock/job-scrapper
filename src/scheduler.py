import threading
from utils import log

class JobScheduler:
    def __init__(self, interval, job_fetcher):
        self.interval = interval
        self.job_fetcher = job_fetcher
        self.running = False
        self.thread = None

    def start(self):
        import time

        if self.running:
            print("Scheduler is already running.")
            return

        self.running = True

        def run():
            while self.running:
                log("Fetching new jobs...")
                self.job_fetcher.get_new_jobs()
                time.sleep(self.interval)

        self.thread = threading.Thread(target=run, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=1)
            self.thread = None