# Technology_scraper
# Overview
This project is a web scraper built in Python to extract information from websites. The scraper focuses on retrieving contact numbers, emails, and identifying technologies used by a given website.

# Features
Contact Information Extraction:

Extracts contact numbers from anchor tags with 'tel:' in the href attribute.
Extracts email addresses from anchor tags with 'mailto:' in the href attribute.
Technology Identification:

Utilizes Wappalyzer to analyze the web page and identify the technologies used.
Data Storage:

Extracted information can be stored in a suitable format, such as a CSV file or a database.
# Prerequisites
Python 3.x
Install required libraries by running: pip install -r requirements.txt
# Usage
Clone the repository: git clone https://github.com/riteeshinfo/Technology_scraper.git
Navigate to the project directory: cd web-scraper
Run the scraper: python scraper.py https://example.com
# Configuration
Modify config.py to customize the behavior of the scraper, such as output format and storage options.
