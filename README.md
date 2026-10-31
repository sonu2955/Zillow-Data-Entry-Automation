# Zillow Data Entry Automation 🏠

A Python web scraping and browser automation project that collects property listing information from a practice Zillow-clone website and automatically enters the collected data into a Google Form.

## Features

- Scrapes property prices using BeautifulSoup.
- Extracts property addresses.
- Collects individual property listing URLs.
- Uses Selenium to automate browser interactions.
- Automatically fills and submits Google Forms.
- Processes multiple property listings in sequence.

## Tech Stack

- Python
- Requests
- BeautifulSoup
- Selenium
- Chrome WebDriver

## Getting Started

### Prerequisites

- Python 3.x
- Google Chrome
- Compatible ChromeDriver (if not managed automatically by Selenium)

Install dependencies:

```bash
pip install requests beautifulsoup4 selenium
```

### Run the application

```bash
git clone https://github.com/YOUR_USERNAME/zillow-data-entry-automation.git
cd zillow-data-entry-automation
python main.py
```

## How It Works

1. Sends an HTTP request to the practice property listing website.
2. Parses the HTML response using BeautifulSoup.
3. Extracts property prices, addresses, and listing links.
4. Launches Chrome using Selenium.
5. Opens the configured Google Form.
6. Enters the corresponding property details and submits the form.
7. Repeats the process for the collected listings.

## What I Learned

- Web scraping and HTML parsing.
- Extracting information using CSS classes and HTML elements.
- Browser automation using Selenium.
- Locating web elements using XPath.
- Automating repetitive data entry tasks.
- Combining web scraping with browser automation.

## Current Limitations

- Uses a specific practice Zillow-clone website.
- Google Form URL and element XPath selectors are hardcoded.
- The submission loop is configured for 44 listings.
- Website structure changes may require updating the selectors.

This project demonstrates how web scraping and browser automation can be combined to reduce repetitive manual data entry.
