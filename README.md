# Job Scraper


## Objective:

With this app, I wanted to reduce the time and effort put in searching for a specific job. I found myself spending too much time repeating the same process of looking for a job, every day (enter a website, input desired job keywords, check if I've already applied to them, repeat..). The idea is to provide the app with a website and a set of keywords, to let it scrap that website for jobs that include the words provided in it's title or description. For now, it's only functional for the 'Computrabajo' website. (see: https://ar.computrabajo.com/)

The scraper has two operation modes:
- Manual: you can prompt the scraper to manually look for jobs.
- Automatic: every 10 minutes, the scraper will fetch the wanted jobs from the website.

As a result, the app shows only the newest jobs (excluding the ones that it has already found in previous searches).

You can view all the fetched jobs from each category (keyword) in chronological order. Or you can just choose to see every fetched job (regardless of category), also in chronological order.


## How to use:

### First-time setup:
- Clone this repository: `git clone https://github.com/Bunshock/job-scrapper`
- Move to repository folder: `cd job-scrapper` (or `dir .\job-scrapper` in Windows shell)
- Create a virtual environment: `python -m venv .venv`
- Activate the environment: `./.venv/Scripts/activate`
- Install required dependencies: `pip install -r requirements.txt`

### Run the script:
- Activate the virtual environment (if not already activated): `./.venv/Scripts/activate`. (You can exit the environment with: `deactivate`)
- Run the script with `python src/python_scraper_app.py`
- Select the source website to scrap
- Configure the scraper:
    - You will be prompted to input the set of desired keywords, separated by a comma ','
    - Configure the job search location
    - Depending on website search rules, you might have to fulfill some conditions (e.g., you might not be able to keep both parameters empty)
- You will also be prompted to configure the time between searches for automatic mode.
- Now, you can decide to:
    - Fetch the jobs manually with `run`
    - Start the scheduled search (every 10 minutes) with `start`
    - TO IMPLEMENT: View all searched jobs (by category or unfiltered) with `view {grouped | all}`
    - Exit the script with `exit`


## Future plans:
- (DONE) Make the app usable in any job-search related website.
- Implement profiles:
    - When running the app, pass the profile as an argument.
    - If running with a profile, you are given the option add or remove a keyworkd, and change location.
    - Save searched jobs for each profile.
- Be able to decide if the keywords should be looked for only in the job's title, or both in the title and the description.
- Input location manually, or select from a group of pre-defined locations.
