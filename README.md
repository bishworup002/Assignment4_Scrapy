# Trip.com Scraper

This Scrapy project is designed to scrape hotel data from trip.com, store it in a PostgreSQL database, and download associated images.

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 3.7 or later
* You have installed PostgreSQL 12 or later
* You have basic knowledge of Python and web scraping

## Installing Trip.com Scraper

To install the Trip.com Scraper, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/bishworup002/Assignment4_Scrapy.git
  
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database:
   - Ensure PostgreSQL is running on port 5433
   - Create a new database named 'trip':
     ```
     createdb -h localhost -p 5433 -U postgres trip
     ```
   - If you need to use different database settings, update the `DATABASE` configuration in `settings.py`

   ```
   DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': 'your port',
    'username': 'Your username',
    'password': 'password',
    'database': 'database_name'
   }
   ```

## Configuration

Before running the scraper, check the following configuration files:

1. `settings.py`: 
   - Verify the database settings under the `DATABASE` variable
   - Adjust the `CONCURRENT_REQUESTS`, `DOWNLOAD_DELAY`, and other settings as needed

2. `spiders/trip_spider.py`:
   - If you want to scrape a different URL, update the `start_urls` list in the `TripSpider` class

## Running the Trip.com Scraper

To run the Trip.com Scraper, follow these steps:

1. Ensure you're in the project directory and your virtual environment is activated (if you're using one)

2. Run the spider:
   ```
   python run_spider.py
   ```

3. The scraper will start running, and you should see output in the console indicating its progress

4. Once complete, you can check your PostgreSQL database to see the scraped data

5. Downloaded images will be stored in the `images` directory


## Contact

If you want to contact me, you can reach me at `<bishworupmollik@gmail.com>`.

## License

This project uses the following license: [MIT License](<link_to_license>).