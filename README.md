# GSMArena Image Scraper

This script scrapes mobile phone images from GSMArena's website for various brands and saves them locally. It uses Python's `requests` and `BeautifulSoup` libraries to fetch and parse web pages, and implements user-agent rotation to minimize the chance of being blocked by the server.

## Features

- **Multi-brand scraping:** Supports multiple phone brands.
- **Pagination:** Automatically navigates through pages to fetch all images.
- **User-Agent Rotation:** Uses random user-agents to avoid being flagged as a bot.
- **Duplicate Prevention:** Skips downloading images already saved locally.
- **Error Handling:** Handles HTTP errors and missing elements gracefully.

## Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gsmarena-image-scraper.git
   cd gsmarena-image-scraper
 ## Install dependencies:
  `pip install -r requirements.txt`

Create the output folder: The script automatically creates folders for each brand under a directory named gsmarena_images.

 ## Usage:
Edit the script: Update the brands dictionary in the script to include the brands and their respective GSMArena URLs you want to scrape.

 ## Run the script:

`python MobileThumb.py`

 ## Find the images:
Images are saved in the gsmarena_images folder, organized by brand.

Example Output

Directory structure:
gsmarena_images

    ├── Apple/
    │   ├── image1.jpg
    │   ├── image2.jpg
    ├── sony/
    │   ├── image1.jpg
    │   ├── image2.jpg
    ├── samsung/
    │   ├── image1.jpg
    │   ├── image2.jpg
    
### Notes:
Be respectful of GSMArena's terms of service.
Avoid overwhelming their servers with too many requests in a short time. You can introduce a delay between requests using time.sleep.

### Contributing:
Contributions are welcome! Feel free to submit a pull request or create an issue for feature suggestions or bug reports.

### License:
This project is licensed under the MIT License. See the LICENSE file for details.

### Disclaimer:
This tool is for educational purposes only. The developer is not responsible for any misuse of the script.
