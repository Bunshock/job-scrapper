class JobScheduler:
    def __init__(self, interval, job_fetcher):
        self.interval = interval
        self.job_fetcher = job_fetcher
        self.running = False

    def start(self):
        import time
        import threading

        self.running = True

        def run():
            while self.running:
                self.job_fetcher.fetch_jobs()
                time.sleep(self.interval)

        threading.Thread(target=run).start()

    def stop(self):
        self.running = False