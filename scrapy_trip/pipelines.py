import os
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings
from urllib.parse import quote_plus


Base = declarative_base()

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(String)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String)
    price = Column(String)
    image_urls = Column(String)

class TripPipeline:
    def __init__(self):
        settings = get_project_settings()
        db_settings = settings.get('DATABASE')
        password = quote_plus(db_settings['password'])
        db_url = f"{db_settings['drivername']}://{db_settings['username']}:{password}@{db_settings['host']}:{db_settings['port']}/{db_settings['database']}"
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        
        # Create tables
        Base.metadata.create_all(self.engine)

    def process_item(self, item, spider):
        session = self.Session()
        trip = Trip(**item)

        try:
            spider.logger.info(f"Processing item: {item}")
            session.add(trip)
            session.commit()
            spider.logger.info(f"Item successfully stored in database: {item['title']}")
        except Exception as e:
            session.rollback()
            spider.logger.error(f"Error storing item in database: {e}")
        finally:
            session.close()
        return item


class TripImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item.get('image_urls', []):
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = ','.join(image_paths)
        return item