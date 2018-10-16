from models.user import User
from models.saloon import Saloon
from models.appointment import Appointment
from peewee import IntegrityError
import datetime
import config

DATABASE = config.DATABASE


def initialize():
    DATABASE.create_tables([User, Saloon, Appointment], safe=True)
    try:
        User.create(
            first_name="Felicia",
            last_name="Mueni",
            email="john@doe.com"
        )
    except IntegrityError:
        pass

    try:
        Saloon.create(
            name="Mrembo",
            business_number="9897",
            opening_time="10:00 am",
            closing_time="5:00 pm",
            description="Urembo services",
            services="Manicure, Pedicure, Haircare",
            user_id=1,
            location="George Padimore Lane"
        )
    except IntegrityError:
        pass
    try:
        Appointment.create(
                user_id=1,
                saloon_id=1,
                services="Manicure, Pedicure",
                time_appointment=datetime.datetime.now()
        )
    except IntegrityError:
        pass
