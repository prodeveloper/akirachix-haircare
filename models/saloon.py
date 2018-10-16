from peewee import (Model, CharField,IntegrityError, TextField)
import config

DATABASE = config.DATABASE


class Saloon(Model):
    name = CharField(max_length=100, unique=True)
    business_number = CharField(max_length=100)
    opening_time = CharField(max_length=100)
    closing_time = CharField(max_length=200)
    description = TextField()
    services = TextField()
    user_id = CharField(max_length=200)
    location = TextField()

    class Meta:
        database = DATABASE


DATABASE.create_tables([Saloon], safe=True)
