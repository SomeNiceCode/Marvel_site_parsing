# Marvel Characters Scraper

This project is a **Python-based web scraper** that extracts detailed information about Marvel characters directly from the official [Marvel website](https://www.marvel.com/characters).  
It leverages the **Marvel API** and **BeautifulSoup** to collect structured data such as character names, links, images, and biography stats, saving them into a CSV file for further analysis.

## 🚀 Features
- Fetches all Marvel characters (over 2800 entries) using the official API.
- Extracts:
  - Character name and alias
  - Direct link to the character’s page
  - Image link
  - Biography stats (height, weight, powers, etc.)
- Saves results into a clean CSV file for easy use in data analysis or portfolio projects.

## 🛠️ Tech Stack
- **Python 3**
- **Requests** — for API calls
- **BeautifulSoup (bs4)** — for HTML parsing
- **CSV module** — for structured data export

Spider-Man, /characters/spider-man-peter-parker, Height: 5'10", Weight: 167 lbs



## ⚙️ Installation
```bash
git clone https://github.com/SomeNiceCode/Marvel_site_parsing.git
cd Marvel_site_parsing
pip install -r requirements.txt
python Marvel_parsing.py



