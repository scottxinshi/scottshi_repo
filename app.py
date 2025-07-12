from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import random

app = Flask(__name__)

# Mock data for Canadian retailers
mock_coupons = {
    "pepsi": [
        {
            "title": "Pepsi 2L Bottle",
            "current_price": 2.99,
            "original_price": 4.49,
            "discount_percentage": 33,
            "rating": 4.2,
            "reviews": "1,234",
            "product_link": "https://www.walmart.ca/en/ip/pepsi-2l/6000195499267",
            "image_url": "https://via.placeholder.com/100x100?text=Pepsi+2L",
            "category": "Beverages",
            "retailer": "Walmart Canada",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "title": "Pepsi 12 Pack Cans (355ml)",
            "current_price": 5.99,
            "original_price": 7.99,
            "discount_percentage": 25,
            "rating": 4.1,
            "reviews": "856",
            "product_link": "https://www.amazon.ca/Pepsi-Cola-Regular-Soda-355ml/dp/B08N5KJ9X1",
            "image_url": "https://via.placeholder.com/100x100?text=Pepsi+Cans",
            "category": "Beverages",
            "retailer": "Amazon Canada",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "title": "Pepsi 1L Bottle",
            "current_price": 1.99,
            "original_price": 2.99,
            "discount_percentage": 33,
            "rating": 4.0,
            "reviews": "567",
            "product_link": "https://www.loblaw.ca/en/pepsi-1l",
            "image_url": "https://via.placeholder.com/100x100?text=Pepsi+1L",
            "category": "Beverages",
            "retailer": "Loblaws",
            "scraped_at": datetime.now().isoformat()
        }
    ],
    "electronics": [
        {
            "title": "Samsung Galaxy A54 5G (128GB)",
            "current_price": 599.99,
            "original_price": 749.99,
            "discount_percentage": 20,
            "rating": 4.3,
            "reviews": "2,456",
            "product_link": "https://www.bestbuy.ca/en-ca/product/samsung-galaxy-a54-5g-128gb/17340125",
            "image_url": "https://via.placeholder.com/100x100?text=Samsung+Phone",
            "category": "Electronics",
            "retailer": "Best Buy Canada",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "title": "Apple iPhone 15 (128GB)",
            "current_price": 1099.99,
            "original_price": 1199.99,
            "discount_percentage": 8,
            "rating": 4.5,
            "reviews": "1,789",
            "product_link": "https://www.apple.com/ca/iphone-15/",
            "image_url": "https://via.placeholder.com/100x100?text=iPhone+15",
            "category": "Electronics",
            "retailer": "Apple Canada",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "title": "Sony WH-1000XM5 Wireless Headphones",
            "current_price": 399.99,
            "original_price": 499.99,
            "discount_percentage": 20,
            "rating": 4.4,
            "reviews": "892",
            "product_link": "https://www.amazon.ca/Sony-WH-1000XM5-Canceling-Headphones-PlayStation/dp/B09Y2MYL5C",
            "image_url": "https://via.placeholder.com/100x100?text=Sony+Headphones",
            "category": "Electronics",
            "retailer": "Amazon Canada",
            "scraped_at": datetime.now().isoformat()
        }
    ],
    "fashion": [
        {
            "title": "Men's Cotton T-Shirt (H&M)",
            "current_price": 14.99,
            "original_price": 24.99,
            "discount_percentage": 40,
            "rating": 4.0,
            "reviews": "892",
            "product_link": "https://www2.hm.com/en_ca/productpage.0984564001.html",
            "image_url": "https://via.placeholder.com/100x100?text=H%26M+T-Shirt",
            "category": "Fashion",
            "retailer": "H&M Canada",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "title": "Women's Winter Boots (Sorel)",
            "current_price": 129.99,
            "original_price": 199.99,
            "discount_percentage": 35,
            "rating": 4.2,
            "reviews": "456",
            "product_link": "https://www.sorel.com/ca/en/womens-boots/",
            "image_url": "https://via.placeholder.com/100x100?text=Sorel+Boots",
            "category": "Fashion",
            "retailer": "Sorel",
            "scraped_at": datetime.now().isoformat()
        }
    ],
    "grocery": [
        {
            "title": "Maple Syrup 500ml (Pure)",
            "current_price": 8.99,
            "original_price": 12.99,
            "discount_percentage": 31,
            "rating": 4.6,
            "reviews": "234",
            "product_link": "https://www.loblaw.ca/en/maple-syrup",
            "image_url": "https://via.placeholder.com/100x100?text=Maple+Syrup",
            "category": "Grocery",
            "retailer": "Loblaws",
            "scraped_at": datetime.now().isoformat()
        },
        {
            "title": "Tim Hortons Coffee Beans 1kg",
            "current_price": 15.99,
            "original_price": 19.99,
            "discount_percentage": 20,
            "rating": 4.3,
            "reviews": "567",
            "product_link": "https://www.timhortons.ca/ca/en/shop/coffee-beans",
            "image_url": "https://via.placeholder.com/100x100?text=Tim+Hortons+Coffee",
            "category": "Grocery",
            "retailer": "Tim Hortons",
            "scraped_at": datetime.now().isoformat()
        }
    ]
}

stats = {
    'total_searches': 0,
    'total_coupons_found': 0,
    'last_search': None,
    'errors': []
}

@app.route('/')
def index():
    """Main page with search interface"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_coupons():
    """Search for coupons based on category/product"""
    try:
        data = request.get_json()
        category = data.get('category', '').strip().lower()
        limit = data.get('limit', 10)
        
        if not category:
            return jsonify({'error': 'Category is required'}), 400
        
        stats['total_searches'] += 1
        stats['last_search'] = datetime.now().isoformat()
        
        # Search in mock data
        coupons = []
        for key, items in mock_coupons.items():
            if category in key or any(category in item['title'].lower() for item in items):
                coupons.extend(items)
        
        # Limit results
        coupons = coupons[:limit]
        
        # Add some random variation for demo
        for coupon in coupons:
            coupon['current_price'] = round(coupon['current_price'] * random.uniform(0.95, 1.05), 2)
        
        stats['total_coupons_found'] += len(coupons)
        
        return jsonify({
            'success': True,
            'coupons': coupons,
            'total_found': len(coupons),
            'search_term': category
        })
        
    except Exception as e:
        stats['errors'].append(str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/lowest-price', methods=['POST'])
def get_lowest_price():
    """Get the lowest price for a specific product"""
    try:
        data = request.get_json()
        product = data.get('product', '').strip().lower()
        
        if not product:
            return jsonify({'error': 'Product name is required'}), 400
        
        # Search in mock data
        all_coupons = []
        for items in mock_coupons.values():
            all_coupons.extend(items)
        
        matching_coupons = [c for c in all_coupons if product in c['title'].lower()]
        
        if not matching_coupons:
            return jsonify({'error': 'No products found'}), 404
        
        # Find lowest price
        lowest_coupon = min(matching_coupons, key=lambda x: x['current_price'])
        
        return jsonify({
            'success': True,
            'lowest_price': {
                'product': product,
                'lowest_price': lowest_coupon['current_price'],
                'title': lowest_coupon['title'],
                'discount_percentage': lowest_coupon['discount_percentage'],
                'product_link': lowest_coupon['product_link'],
                'image_url': lowest_coupon['image_url'],
                'retailer': lowest_coupon['retailer'],
                'found_at': datetime.now().isoformat()
            }
        })
        
    except Exception as e:
        stats['errors'].append(str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/top-cheapest', methods=['POST'])
def get_top_cheapest():
    """Get top N cheapest coupons for a product"""
    try:
        data = request.get_json()
        product = data.get('product', '').strip().lower()
        limit = data.get('limit', 10)
        
        if not product:
            return jsonify({'error': 'Product name is required'}), 400
        
        # Search in mock data
        all_coupons = []
        for items in mock_coupons.values():
            all_coupons.extend(items)
        
        matching_coupons = [c for c in all_coupons if product in c['title'].lower()]
        
        if not matching_coupons:
            return jsonify({'error': 'No products found'}), 404
        
        # Sort by price and return top N
        sorted_coupons = sorted(matching_coupons, key=lambda x: x['current_price'])
        
        return jsonify({
            'success': True,
            'cheapest_coupons': sorted_coupons[:limit],
            'total_found': len(sorted_coupons[:limit])
        })
        
    except Exception as e:
        stats['errors'].append(str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/categories')
def get_categories():
    """Get available categories"""
    try:
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
        return jsonify({
            'success': True,
            'categories': categories
        })
    except Exception as e:
        stats['errors'].append(str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/retailers')
def get_retailers():
    """Get available Canadian retailers"""
    try:
        retailers = [
            "Amazon Canada",
            "Walmart Canada", 
            "Best Buy Canada",
            "Canadian Tire",
            "Loblaws",
            "Shoppers Drug Mart",
            "H&M Canada",
            "Apple Canada",
            "Tim Hortons",
            "Sobeys",
            "No Frills",
            "Costco Canada",
            "Home Depot Canada",
            "Staples Canada",
            "Sport Chek",
            "The Bay",
            "Indigo",
            "Michaels Canada"
        ]
        return jsonify({
            'success': True,
            'retailers': retailers
        })
    except Exception as e:
        stats['errors'].append(str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/stats')
def get_stats():
    """Get scraping statistics"""
    try:
        return jsonify({
            'success': True,
            'stats': stats
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 