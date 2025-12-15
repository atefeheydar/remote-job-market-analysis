# Remote Job Market Analysis (Python)

## Overview
This project collects and analyzes remote developer job listings using the RemoteOK public API.
The goal is to identify in-demand skills and trends in the remote job market.

## Features
- Data collection via public API
- Data cleaning and preprocessing
- Skill frequency analysis
- Visualization of top skills

## Tech Stack
- Python
- Requests
- Pandas
- Matplotlib

## Project Structure
remote-job-market-analysis/
├── data/
│ ├── remoteok_jobs.csv
│ └── top_skills.csv
│
├── src/
│ ├── remoteok_api_scraper.py
│ ├── analysis.py
│ └── visualize.py
│
├── requirements.txt
└── .gitignore


## How to Run
```bash
pip install -r requirements.txt
python src/remoteok_api_scraper.py
python src/analysis.py
python src/visualize.py

Output

remoteok_jobs.csv: raw job data

top_skills.csv: skill frequency

Chart of top 10 skills


Why This Project?

This project demonstrates real-world data collection, analysis, and visualization skills
using Python, suitable for Data Analyst / Junior Data Scientist roles.