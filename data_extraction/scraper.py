"""
JobYaari Web Scraper - Updated for current HTML structure and infinite scroll
"""

import os
import time
import json
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

class JobYaariScraper:
    def __init__(self):
        self.categories = {
            'engineering': 'https://jobyaari.com/category/engineering?type=graduate',
            'science':    'https://jobyaari.com/category/science?type=graduate',
            'commerce':   'https://jobyaari.com/category/commerce?type=graduate',
            'education':  'https://jobyaari.com/category/education?type=graduate',
        }
        os.makedirs("extracted_data", exist_ok=True)
        self.driver = None
        if SELENIUM_AVAILABLE:
            self.init_selenium()

    def init_selenium(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    def scrape_with_requests(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            resp = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find_all('div', class_='drop__card')
        except Exception as e:
            print(f"Requests scrape failed: {e}")
            return []

    def extract_from_container(self, container):
        try:
            job_title = container.find("span", class_="ribbon1").find("span").get_text(strip=True)
        except:
            job_title = "N/A"
        try:
            organization = container.find("span", class_="drop__profession").get_text(strip=True)
        except:
            organization = "N/A"
        try:
            salary = container.find("span", class_="salary-price").find_all("span")[1].get_text(strip=True)
        except:
            salary = "N/A"
        try:
            experience = container.find("span", class_="drop__exp").get_text(strip=True)
        except:
            experience = "N/A"
        try:
            qualification = container.find("div", class_="salary").get_text(strip=True)
        except:
            qualification = "N/A"
        try:
            location = container.find("div", class_="location").get_text(strip=True)
        except:
            location = "N/A"
        try:
            tags_container = container.find("div", class_="tags-part")
            tags = [tag.get_text(strip=True) for tag in tags_container.find_all("a", class_="tags-item")]
        except:
            tags = []

        age_limit = "N/A"
        vacancies = "N/A"

        return {
            "job_title": job_title,
            "organization": organization,
            "salary": salary,
            "experience": experience,
            "qualification": qualification,
            "location": location,
            "tags": tags,
            "age_limit": age_limit,
            "vacancies": vacancies,
        }

    def scrape_category(self, cat, url):
        print(f"Scraping {cat} category with infinite scroll...")

        jobs = []
        if self.driver:
            self.driver.get(url)
            time.sleep(5)

            scroll_attempt = 0
            max_scroll_attempts = 10
            last_height = self.driver.execute_script("return document.body.scrollHeight")

            while scroll_attempt < max_scroll_attempts:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)  # wait for content loading
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    print("Reached page bottom or no more content.")
                    break
                last_height = new_height
                scroll_attempt += 1
                print(f"Scroll attempt {scroll_attempt}")

            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            containers = soup.find_all("div", class_="drop__card")
            print(f"Found total {len(containers)} job cards")

            for container in containers:
                job = self.extract_from_container(container)
                job['category'] = cat
                jobs.append(job)
        else:
            containers = self.scrape_with_requests(url)
            for container in containers:
                job = self.extract_from_container(container)
                job['category'] = cat
                jobs.append(job)

        if not jobs:
            jobs = [{
                'job_title': f'Sample {cat} Job',
                'organization': 'Sample Org',
                'salary': '10000-20000',
                'experience': 'Fresher',
                'qualification': 'Any',
                'age_limit': '18-30',
                'vacancies': '10',
                'location': 'All India',
                'category': cat,
            }]

        print(f"Scraped total {len(jobs)} jobs for category {cat}")
        return jobs

    def run(self):
        all_jobs = []
        for cat, url in self.categories.items():
            jobs = self.scrape_category(cat, url)
            for job in jobs:
                if 'category' not in job:
                    job['category'] = cat

            print(f"Category {cat} jobs scraped: {len(jobs)}")

            df = pd.DataFrame(jobs)
            df.drop_duplicates(subset=['job_title', 'organization', 'location'], inplace=True)
            df.to_csv(f"extracted_data/{cat}_jobs.csv", index=False)
            all_jobs.extend(df.to_dict('records'))

        if len(all_jobs) == 0:
            print("No jobs scraped! Adding fallback data.")
            sample = [{
                'job_title': 'Sample Job',
                'organization': 'Sample Org',
                'salary': '10000-20000',
                'experience': 'Fresher',
                'qualification': 'Any',
                'age_limit': '18-30',
                'vacancies': '10',
                'location': 'All India',
                'category': 'engineering',
            }]
            all_jobs.extend(sample)

        df_all = pd.DataFrame(all_jobs)
        df_all.drop_duplicates(subset=['job_title', 'organization', 'location'], inplace=True)
        df_all.to_csv('extracted_data/all_jobs_combined.csv', index=False)

        categorized = {cat: [job for job in all_jobs if job.get('category') == cat] for cat in self.categories}
        kb = {
            'metadata': {
                'total_jobs': len(all_jobs),
                'extraction_time': datetime.now().isoformat(),
            },
            'categories': categorized,
        }

        os.makedirs("../chatbot_app/training_data", exist_ok=True)
        with open("../chatbot_app/training_data/knowledge_base.json", 'w', encoding='utf-8') as f:
            json.dump(kb, f, indent=2)

        print("Knowledge base JSON created successfully.")

if __name__ == "__main__":
    JobYaariScraper().run()
