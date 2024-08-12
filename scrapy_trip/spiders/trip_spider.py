import scrapy
from scrapy_trip.items import TripItem
import re
import json
import random

class TripSpider(scrapy.Spider):
    name = 'trip'
    start_urls = ['https://uk.trip.com/hotels/?locale=en-GB&curr=GBP']

    def parse(self, response):
        # Extract the script tag content containing 'window.IBU_HOTEL'
        script_content = response.xpath('//script[contains(text(), "window.IBU_HOTEL")]/text()').get()
        
        if script_content:
            # Use regex to find the JSON-like object within the script content
            json_data_match = re.search(r'window\.IBU_HOTEL\s*=\s*({.*?});', script_content, re.DOTALL)

            if json_data_match:
                # Extract the matched JSON-like string
                json_data_str = json_data_match.group(1)

                try:
                    # Convert the JSON-like string to a Python dictionary
                    json_data = json.loads(json_data_str)

                    # Extract hotel data
                    htlsData = json_data.get('initData', {}).get('htlsData', [])

                    # Select three random categories
                    categories = ['inboundCities', 'outboundCities', 'fiveStarHotels', 'cheapHotels', 'hostelHotels']
                    selected_categories = random.sample(categories, 3)

                    self.logger.info(f"Selected categories: {selected_categories}")

                    for category in selected_categories:
                        # Extract hotel data for each selected category
                        category_data = htlsData.get(category, [])
                        hotels = category_data[0].get('recommendHotels', []) if category_data else []

                        for hotel in hotels:
                            item = TripItem()
                            item['title'] = hotel.get('hotelName')
                            item['rating'] = hotel.get('rating')
                            item['location'] = hotel.get('fullAddress')
                            item['latitude'] = hotel.get('lat')
                            item['longitude'] = hotel.get('lon')
                            item['room_type'] = "Standard"  # Modify as per available data or further scraping logic
                            item['price'] = hotel.get('prices', {}).get('priceInfos', [{}])[0].get('price')
                            
                            # Handling single image URL from 'imgUrl'
                            base_url = 'https://ak-d.tripcdn.com/images'
                            image_urls = [base_url + hotel.get('imgUrl', '')]
                            
                            item['image_urls'] = image_urls
                            
                            yield item

                except json.JSONDecodeError as e:
                    self.logger.error(f"Failed to decode JSON: {e}")
