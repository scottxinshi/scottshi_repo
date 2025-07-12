# Canadian Coupon Collector 🍁

A modern web application to collect and analyze deals from major Canadian retailers. Find the lowest prices, top cheapest deals, and browse available categories across Canadian e-commerce sites.

## Features

- 🔍 **Smart Search**: Search for deals by product name or category
- 💰 **Lowest Price Finder**: Find the absolute lowest price for any product
- 🏆 **Top Cheapest**: Get the top N cheapest deals for a product
- 📂 **Category Browser**: Browse available categories and search within them
- 🏪 **Canadian Retailers**: Search across major Canadian stores
- 📊 **Real-time Statistics**: Track your search history and results
- 🎨 **Modern UI**: Beautiful, responsive interface with Canadian theme
- 📱 **Mobile Friendly**: Works perfectly on all devices

## Screenshots

The application features a modern, Canadian-themed design with:
- Clean search interface with maple leaf accents
- Tabbed results display
- Product cards with Canadian pricing (CAD)
- Real-time statistics dashboard
- Responsive design for all screen sizes

## Installation

### Prerequisites

- Python 3.8 or higher
- Chrome browser (for web scraping)
- Internet connection

### Setup

1. **Clone or download the project**
   ```bash
   cd flip-coupon-collector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## Usage

### Basic Search
1. Enter a product name or category (e.g., "Pepsi", "Electronics", "Maple Syrup")
2. Set the number of results you want (1-50)
3. Click "Search" to find deals

### Find Lowest Price
1. Enter a specific product name (e.g., "Pepsi 2L")
2. Click "Find Lowest Price"
3. Get the absolute cheapest option available

### Top Cheapest
1. Enter a product name
2. Set the number of results
3. Click "Top Cheapest"
4. View the cheapest options sorted by price

### Browse Categories
1. Click "Browse Categories"
2. Select from available categories
3. Automatically search within that category

### Canadian Retailers
1. Click "Canadian Retailers" tab
2. View all supported Canadian stores
3. See which retailers are being searched

## API Endpoints

The application provides RESTful API endpoints:

- `POST /search` - Search for deals
- `POST /lowest-price` - Find lowest price for a product
- `POST /top-cheapest` - Get top cheapest deals
- `GET /categories` - Get available categories
- `GET /retailers` - Get Canadian retailers
- `GET /stats` - Get scraping statistics

### Example API Usage

```bash
# Search for Pepsi deals
curl -X POST http://localhost:5000/search \
  -H "Content-Type: application/json" \
  -d '{"category": "pepsi", "limit": 10}'

# Find lowest price for Pepsi
curl -X POST http://localhost:5000/lowest-price \
  -H "Content-Type: application/json" \
  -d '{"product": "pepsi"}'
```

## Features in Detail

### Smart Scraping
- Uses both requests and Selenium for comprehensive data extraction
- Handles dynamic content loading
- Respects website structure and rate limits
- Extracts product images, prices, discounts, and ratings

### Data Processing
- Automatic price extraction and formatting in Canadian dollars (CAD)
- Discount percentage calculation
- Rating and review parsing
- Product link generation

### User Experience
- Real-time loading indicators
- Error handling and user feedback
- Responsive design for all devices
- Tabbed interface for organized results

## Canadian Retailers Supported

The application searches across major Canadian retailers:
- Amazon Canada
- Walmart Canada
- Best Buy Canada
- Canadian Tire
- Loblaws
- Shoppers Drug Mart
- H&M Canada
- Apple Canada
- Tim Hortons
- Sobeys
- No Frills
- Costco Canada
- Home Depot Canada
- Staples Canada
- Sport Chek
- The Bay
- Indigo
- Michaels Canada

## Available Categories

The application supports searching across major categories:
- Electronics
- Fashion
- Home & Kitchen
- Beauty & Personal Care
- Sports & Fitness
- Books & Media
- Automotive
- Toys & Games
- Health & Wellness
- Grocery & Gourmet
- Baby Products
- Pet Supplies
- Office Products
- Tools & Hardware
- Jewelry
- Watches
- Luggage & Bags
- Shoes
- Clothing
- Accessories

## Technical Details

### Architecture
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Scraping**: BeautifulSoup4, Selenium
- **Data Processing**: Pandas
- **Styling**: Custom CSS with Canadian theme and maple leaf accents

### Key Components
- `app.py` - Main Flask application
- `flip_scraper.py` - Web scraping logic
- `templates/index.html` - Frontend interface
- `requirements.txt` - Python dependencies

### Data Structure
Each deal contains:
```json
{
  "title": "Product Name",
  "current_price": 2.99,
  "original_price": 4.49,
  "discount_percentage": 33,
  "rating": 4.2,
  "reviews": "1,234",
  "product_link": "https://retailer.ca/product-url",
  "image_url": "https://image-url.jpg",
  "category": "Beverages",
  "retailer": "Walmart Canada",
  "scraped_at": "2024-01-01T12:00:00"
}
```

## Troubleshooting

### Common Issues

1. **Chrome Driver Issues**
   - The app automatically downloads ChromeDriver
   - Ensure Chrome browser is installed
   - Check internet connection for driver download

2. **No Results Found**
   - Try different search terms
   - Check if the product exists on Canadian retailers
   - Verify internet connection

3. **Slow Performance**
   - Reduce the number of results requested
   - Check your internet speed
   - The app includes delays to respect rate limits

### Error Handling
- The application logs all errors
- User-friendly error messages are displayed
- Statistics track error counts
- Graceful degradation for network issues

## Legal Notice

This application is for educational and personal use only. Please respect:
- Canadian retailers' Terms of Service
- Rate limiting and robots.txt
- Copyright and intellectual property rights
- Website usage policies

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving the UI/UX
- Optimizing the scraping logic
- Adding more Canadian retailers

## License

This project is open source and available under the MIT License.

## Support

For support or questions:
- Check the troubleshooting section
- Review the code comments
- Ensure all dependencies are installed correctly

---

**Happy Canadian Deal Hunting! 🍁🇨🇦**
