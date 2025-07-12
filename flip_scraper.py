import requests
from bs4 import BeautifulSoup
import time
import random
import json
import re
from datetime import datetime
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class FlipScraper:
    def __init__(self):
        self.base_url = "https://flipkart.com"
        self.search_url = "https://www.flipkart.com/search"
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        self.stats = {
            'total_searches': 0,
            'total_coupons_found': 0,
            'last_search': None,
            'errors': []
        }
        
    def _get_chrome_driver(self):
        """Initialize Chrome driver for dynamic content"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"--user-agent={self.ua.random}")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    
    def _extract_price(self, price_text):
        """Extract numeric price from text"""
        if not price_text:
            return None
        
        # Remove currency symbols and extract numbers
        price_match = re.search(r'[\d,]+\.?\d*', price_text.replace(',', ''))
        if price_match:
            return float(price_match.group().replace(',', ''))
        return None
    
    def _extract_discount(self, discount_text):
        """Extract discount percentage from text"""
        if not discount_text:
            return None
        
        discount_match = re.search(r'(\d+)%', discount_text)
        if discount_match:
            return int(discount_match.group(1))
        return None
    
    def search_coupons(self, category, limit=10):
        """Search for coupons based on category/product"""
        try:
            self.stats['total_searches'] += 1
            self.stats['last_search'] = datetime.now().isoformat()
            
            # Construct search URL
            search_params = {
                'q': category,
                'otracker': 'search',
                'otracker1': 'search',
                'marketplace': 'FLIPKART',
                'as-show': 'on',
                'as': 'off',
                'as-pos': '1',
                'as-type': 'HISTORY'
            }
            
            response = self.session.get(self.search_url, params=search_params)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            coupons = []
            
            # Look for product cards
            product_cards = soup.find_all('div', {'class': '_1AtVbE'})
            
            for card in product_cards[:limit]:
                try:
                    # Extract product information
                    title_elem = card.find('div', {'class': '_4rR01T'})
                    title = title_elem.get_text().strip() if title_elem else "N/A"
                    
                    # Extract price
                    price_elem = card.find('div', {'class': '_30jeq3'})
                    price = self._extract_price(price_elem.get_text()) if price_elem else None
                    
                    # Extract original price
                    original_price_elem = card.find('div', {'class': '_3I9_wc'})
                    original_price = self._extract_price(original_price_elem.get_text()) if original_price_elem else price
                    
                    # Extract discount
                    discount_elem = card.find('div', {'class': '_3Ay6Sb'})
                    discount = self._extract_discount(discount_elem.get_text()) if discount_elem else None
                    
                    # Extract rating
                    rating_elem = card.find('div', {'class': '_3LWZlK'})
                    rating = float(rating_elem.get_text()) if rating_elem else None
                    
                    # Extract reviews count
                    reviews_elem = card.find('span', {'class': '_2_R_DZ'})
                    reviews = reviews_elem.get_text().strip() if reviews_elem else "0"
                    
                    # Extract product link
                    link_elem = card.find('a', {'class': '_1fQZEK'})
                    product_link = self.base_url + link_elem.get('href') if link_elem else None
                    
                    # Extract image
                    img_elem = card.find('img', {'class': '_396cs4'})
                    image_url = img_elem.get('src') if img_elem else None
                    
                    coupon_data = {
                        'title': title,
                        'current_price': price,
                        'original_price': original_price,
                        'discount_percentage': discount,
                        'rating': rating,
                        'reviews': reviews,
                        'product_link': product_link,
                        'image_url': image_url,
                        'category': category,
                        'scraped_at': datetime.now().isoformat()
                    }
                    
                    coupons.append(coupon_data)
                    
                except Exception as e:
                    self.stats['errors'].append(f"Error parsing product card: {str(e)}")
                    continue
            
            self.stats['total_coupons_found'] += len(coupons)
            return coupons
            
        except Exception as e:
            self.stats['errors'].append(f"Search error: {str(e)}")
            raise e
    
    def get_lowest_price(self, product):
        """Get the lowest price for a specific product"""
        try:
            coupons = self.search_coupons(product, limit=50)
            
            if not coupons:
                return None
            
            # Filter out items without price
            valid_coupons = [c for c in coupons if c['current_price'] is not None]
            
            if not valid_coupons:
                return None
            
            # Find the lowest price
            lowest_coupon = min(valid_coupons, key=lambda x: x['current_price'])
            
            return {
                'product': product,
                'lowest_price': lowest_coupon['current_price'],
                'title': lowest_coupon['title'],
                'discount_percentage': lowest_coupon['discount_percentage'],
                'product_link': lowest_coupon['product_link'],
                'image_url': lowest_coupon['image_url'],
                'found_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.stats['errors'].append(f"Lowest price error: {str(e)}")
            raise e
    
    def get_top_cheapest(self, product, limit=10):
        """Get top N cheapest coupons for a product"""
        try:
            coupons = self.search_coupons(product, limit=100)
            
            if not coupons:
                return []
            
            # Filter out items without price
            valid_coupons = [c for c in coupons if c['current_price'] is not None]
            
            if not valid_coupons:
                return []
            
            # Sort by price and return top N
            sorted_coupons = sorted(valid_coupons, key=lambda x: x['current_price'])
            
            return sorted_coupons[:limit]
            
        except Exception as e:
            self.stats['errors'].append(f"Top cheapest error: {str(e)}")
            raise e
    
    def get_available_categories(self):
        """Get available categories from Flipkart"""
        categories = [
            "Electronics",
            "Fashion",
            "Home & Kitchen",
            "Beauty & Personal Care",
            "Sports & Fitness",
            "Books & Media",
            "Automotive",
            "Toys & Games",
            "Health & Wellness",
            "Grocery & Gourmet",
            "Baby Products",
            "Pet Supplies",
            "Office Products",
            "Tools & Hardware",
            "Jewelry",
            "Watches",
            "Luggage & Bags",
            "Shoes",
            "Clothing",
            "Accessories"
        ]
        return categories
    
    def get_stats(self):
        """Get scraping statistics"""
        return self.stats
    
    def save_to_csv(self, coupons, filename=None):
        """Save coupons to CSV file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"flip_coupons_{timestamp}.csv"
        
        df = pd.DataFrame(coupons)
        df.to_csv(filename, index=False)
        return filename
    
    def save_to_json(self, coupons, filename=None):
        """Save coupons to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"flip_coupons_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(coupons, f, indent=2, ensure_ascii=False)
        
        return filename 