from peewee import (Model, CharField, DateTimeField, TextField, IntegerField)
import config
import datetime
DATABASE = config.DATABASE


class Appointment(Model):
    user_id = IntegerField()
    time_appointment = DateTimeField(default=datetime.datetime.now)
    saloon_id = IntegerField()
    services = TextField()

    class Meta:
        database = DATABASE
