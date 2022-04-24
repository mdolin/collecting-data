from platform import platform

from requests import request
from database.models import connect_db, AdNetwork
from sqlalchemy.orm import sessionmaker

db=connect_db()
Session = sessionmaker(bind=db)
session = Session()

def save_to_database(dataframe=None, session=session):
    for _, row in dataframe.iterrows():
        db_dict = dict(
            date = row['Date'],
            app = row['App'],
            platform=row['Platform'],
            requests=row['Requests'],
            impressions=row['Impressions'],
            revenue=row['Revenue'],
        )

        adn = AdNetwork(**db_dict)

        session.add(adn)
        session.commit()

    session.close()
