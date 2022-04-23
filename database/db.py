from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = "postgres+psycopg2://postgres:password@localhost:5432/adnetwork"

db = create_engine(DATABASE_URI)
base = declarative_base()


class AdNetwork(base):
    __tablename__ = "daily_report"
    id = Column(Integer, primary_key=True)
    date = Column(String)
    app = Column(String)
    platform = Column(String)
    requests = Column(Integer)
    impressions = Column(Integer)
    revenue = Column(Float)

    def __repr__(self):
        return "<adNetwork(date='{}', app='{}', platform={}, requests={}, impressions={}, revenue={})>".format(
            self.date,
            self.app,
            self.platform,
            self.requests,
            self.impressions,
            self.revenue,
        )


def recreate_database():
    base.metadata.drop_all(db)
    base.metadata.create_all(db)


Session = sessionmaker(bind=db)
session = Session()

# Create
ad_network = AdNetwork(
    date="15/9/2017",
    app="Talking Ben",
    platform="iOS",
    requests=1051,
    impressions=175,
    revenue=0.7,
)
session.add(ad_network)
session.commit()


# Read
ad_network = session.query(AdNetwork)
for ad in ad_network:
    print(ad.platform)

# Update
ad_network.app = "iOS"
session.commit()

# Delete
session.delete(ad_network)
session.commit()

session.close()
