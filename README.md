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
   git clone https://github.com/yourusername/trip-scraper.git
   cd trip-scraper
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

## Troubleshooting

If you encounter any issues:

1. Check the console output for error messages
2. Verify your database connection settings
3. Ensure you have the necessary permissions to write to the project directory
4. If you're getting blocked by the website, try adjusting the `DOWNLOAD_DELAY` in `settings.py`

## Contributing to Trip.com Scraper

To contribute to Trip.com Scraper, follow these steps:

1. Fork this repository
2. Create a branch: `git checkout -b <branch_name>`
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me, you can reach me at `<your_email@example.com>`.

## License

This project uses the following license: [MIT License](<link_to_license>).