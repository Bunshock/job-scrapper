# Job Scrapper


## Objective:

With this app, I wanted to reduce the time and effort put in searching for a specific job. I found myself spending too much time repeating the same process of looking for a job, every day (enter a website, input desired job keywords, check if I've already applied to them, repeat..). The idea is to provide the app with a website and a set of keywords, to let it scrap that website for jobs that include the words provided in it's title or description. For now, it's only functional for the 'Computrabajo' website. (see: https://ar.computrabajo.com/)

The scrapper has two operation modes:
- Manual: you can prompt the scrapper to manually look for jobs.
- Automatic: every 10 minutes, the scrapper will fetch the wanted jobs from the website.

As a result, the app shows only the newest jobs (excluding the ones that it has already found in previous searches).

You can view all the fetched jobs from each category (keyword) in chronological order. Or you can just choose to see every fetched job (regardless of category), also in chronological order.


## How to use:

- Run the script with `python src/python_scrapper_app.py`
- You will be prompted to input the set of keywords, separated by a comma ','
- Now, you can decide to:
    - Fetch the jobs manually with `run`
    - Start the scheduled search (every 10 minutes) with `start`
    - TO IMPLEMENT: View all searched jobs (by category or unfiltered) with `view {grouped | all}`
    - Exit the script with `exit`


## Future plans:
- Make the app usable in any job-search related website.
- Implement profiles, so you don't have to load the website and keywords every time you run the app.
- Be able to decide if the keywords should be looked for only in the job's title, or both in the title and the description.
