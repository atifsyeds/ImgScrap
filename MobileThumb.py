import os
import requests
from bs4 import BeautifulSoup

# Base URLs for the brands
brands = {
            "sony": "https://www.gsmarena.com/sony-phones-7.php",
            "samsung": "https://www.gsmarena.com/samsung-phones-9.php",
            "apple": "https://www.gsmarena.com/apple-phones-48.php",
            "huawei": "https://www.gsmarena.com/huawei-phones-58.php",
            "nokia": "https://www.gsmarena.com/nokia-phones-1.php",
            "sony": "https://www.gsmarena.com/sony-phones-7.php",
            "lg": "https://www.gsmarena.com/lg-phones-20.php",
            "htc": "https://www.gsmarena.com/htc-phones-45.php",
            "motorola": "https://www.gsmarena.com/motorola-phones-4.php",
            "lenovo": "https://www.gsmarena.com/lenovo-phones-73.php",
            "xiaomi": "https://www.gsmarena.com/xiaomi-phones-80.php",
            "google": "https://www.gsmarena.com/google-phones-107.php",
            "honor": "https://www.gsmarena.com/honor-phones-121.php",
            "oppo": "https://www.gsmarena.com/oppo-phones-82.php",
            "realme": "https://www.gsmarena.com/realme-phones-118.php",
            "oneplus": "https://www.gsmarena.com/oneplus-phones-95.php",
            "nothing": "https://www.gsmarena.com/nothing-phones-128.php",
            "vivo": "https://www.gsmarena.com/vivo-phones-98.php",
            "meizu": "https://www.gsmarena.com/meizu-phones-74.php",
            "asus": "https://www.gsmarena.com/asus-phones-46.php",
            "alcatel": "https://www.gsmarena.com/alcatel-phones-5.php",
            "zte": "https://www.gsmarena.com/zte-phones-62.php",
            "microsoft": "https://www.gsmarena.com/microsoft-phones-64.php",
            "umidigi": "https://www.gsmarena.com/umidigi-phones-135.php",
            "coolpad": "https://www.gsmarena.com/coolpad-phones-105.php",
            "cat": "https://www.gsmarena.com/cat-phones-89.php",
            "sharp": "https://www.gsmarena.com/sharp-phones-23.php",
            "micromax": "https://www.gsmarena.com/micromax-phones-66.php",
            "infinix": "https://www.gsmarena.com/infinix-phones-119.php",
            "ulefone_": "https://www.gsmarena.com/ulefone_-phones-124.php",
            "tecno": "https://www.gsmarena.com/tecno-phones-120.php",
            "doogee": "https://www.gsmarena.com/doogee-phones-129.php",
            "blackview": "https://www.gsmarena.com/blackview-phones-116.php",
            "cubot": "https://www.gsmarena.com/cubot-phones-130.php",
            "oukitel": "https://www.gsmarena.com/oukitel-phones-132.php",
            "itel": "https://www.gsmarena.com/itel-phones-131.php",
            "tcl": "https://www.gsmarena.com/tcl-phones-123.php"

}
# List of User-Agent strings for rotation
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36',
]

# Function to download images from a page
def download_images_from_page(brand_name, page_url, output_folder):
    headers = {
        'User-Agent': random.choice(user_agents)
    }

    try:
        response = requests.get(page_url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {page_url}: {e}")
        return False

    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate phone thumbnails in the "makers" class
    makers_div = soup.find('div', class_='makers')
    if not makers_div:
        print(f"No makers div found on {page_url}")
        return False

    img_tags = makers_div.find_all('img')  # Find all images in the makers div
    downloaded = 0
    for img_tag in img_tags:
        img_url = img_tag.get('src') or img_tag.get('data-src')  # Get the image URL
        if img_url:
            if img_url.startswith('/'):  # Handle relative URLs
                img_url = f"https://www.gsmarena.com{img_url}"

            img_name = img_url.split("/")[-1]
            img_path = os.path.join(output_folder, img_name)
            
            if not os.path.exists(img_path):  # Avoid duplicate downloads
                try:
                    img_data = requests.get(img_url, headers=headers).content
                    with open(img_path, 'wb') as f:
                        f.write(img_data)
                    downloaded += 1
                    print(f"Downloaded: {img_name}")
                except Exception as e:
                    print(f"Error downloading {img_url}: {e}")
    return downloaded > 0

# Function to scrape images across multiple pages
def scrape_brand_images(brand_name, base_url):
    print(f"Scraping images for {brand_name}...")
    output_folder = os.path.join("gsmarena_images", brand_name)
    os.makedirs(output_folder, exist_ok=True)

    current_url = base_url
    while True:
        print(f"Fetching: {current_url}")
        if not download_images_from_page(brand_name, current_url, output_folder):
            print(f"No more images found on {current_url}. Stopping.")
            break

        # Check if there's a "Next" button to proceed to the next page
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(current_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_button = soup.find('a', class_='prevnextbutton', title='Next page')
        if next_button:
            next_url = next_button.get('href')
            if next_url:
                current_url = f"https://www.gsmarena.com/{next_url}"  # Construct the full URL
            else:
                print(f"No valid URL found in 'Next' button. Stopping.")
                break
        else:
            print(f"No 'Next' button found. Completed scraping for {brand_name}.")
            break

# Main script to iterate through all brands
def main():
    for brand_name, base_url in brands.items():
        scrape_brand_images(brand_name, base_url)

if __name__ == "__main__":
    main()
