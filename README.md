 ##📸 ImgScrap
 
This script scrapes mobile phone images from GSMArena's website for various brands and saves them locally. It uses Python's `requests` and `BeautifulSoup` libraries to fetch and parse web pages, and implements user-agent rotation to minimize the chance of being blocked by the server.


 ##🚀 Features

- **Multi-brand scraping:** Scrapes phone images from GSMArena for multiple brands.
- **Pagination:** Automatically navigates through pages to fetch all images.
- **User-Agent Rotation:** Uses random user-agents to avoid being flagged as a bot.
- **Save Images:** Saves images to organized folders by brand.
- **Duplicate Prevention:** Skips downloading images already saved locally.
- **Error Handling:** Handles HTTP errors and missing elements gracefully.


##📂 Directory Structure
ImgScrap/
- **├── scraper.py            # Main scraping script
- **├── requirements.txt      # Dependencies list
- **├── README.md             # Documentation
- **├── .gitignore            # Ignored files
- **├── LICENSE               # Project license

## Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/atifsyeds/ImgScrap/
   cd gsmarena-image-scraper
   
 ## Install dependencies:
  `pip install -r requirements.txt`

📜 License
This project is licensed under the MIT License.

📫 Contact
Author: Atif Syed
Email: *****@gmail.com

    
### Notes:
Be respectful of GSMArena's terms of service.
Avoid overwhelming their servers with too many requests in a short time. You can introduce a delay between requests using time.sleep.

### Contributing:
Contributions are welcome! Feel free to submit a pull request or create an issue for feature suggestions or bug reports.

### Disclaimer:
This tool is for educational purposes only. The developer is not responsible for any misuse of the script.
