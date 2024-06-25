import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import time


class scrap:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def get_contents(self, url):
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            },
        )
        soup = BeautifulSoup(response.content, "html.parser")
        return soup


class Job(scrap):
    def __init__(self, title, company, position, url):
        super().__init__(self)
        self.title = title
        self.company = company
        self.position = position
        self.url = url


class ScrapBerlin(Job):
    def __init__(self):
        super().__init__(self)
        self.berlin_url = "https://berlinstartupjobs.com/skill-areas/"
        self.jobs = {}

    def get_job_list(self, soup):
        return soup.find("ul", class_="jobs-list-items").find_all(
            "li", class_="bjs-jlid"
        )

    def get_job_meta(self, job):
        meta = job.find("div", class_="bjs-jlid__header").find(
            "div", class_="bjs-jlid__meta"
        )
        position_meta = meta.find("h4", class_="bjs-jlid__h")
        return {
            "Company": meta.find("a", class_="bjs-jlid__b").text,
            "Position": position_meta.text,
            "Link": position_meta.find("a")["href"],
        }

    def extract_jobs(self, keyword):
        soup = self.get_contents(f"{self.berlin_url}{keyword}")
        job_list = self.get_job_list(soup)
        for job in job_list:
            job_meta = self.get_job_meta(job)
        self.jobs.update(job_meta)
