#!/usr/bin/env python
from flask import (Flask, render_template, request, jsonify)
from models.saloon import Saloon
from models.user import User
from peewee import IntegrityError
import bootstrap
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)
bootstrap.initialize()


@app.route('/')
def index():
    return "List of products"


@app.route('/user/register', methods=['POST'])
def register_user():
    user_data = dict(request.form.items())
    result = {}
    try:
        User.create(
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            email=user_data.get('email')
        )
        result = {
            'status': 'success',
            'message': '{} registered'.format(user_data.get('first_name'))}
        return jsonify(result)
    except IntegrityError:
        result = {
            'status': 'failed',
            'message': '{} is not unique'.format(user_data.get('email'))}
        return jsonify(result)


@app.route('/user')
def list_users():
    users = User.select()
    results = []
    for user in users:
        results.append(
            {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }
        )
    return jsonify(results)


@app.route('/saloon/add',  methods=['POST'])
def add_saloon():
    saloon_data = dict(request.form.items())
    Saloon.create(
        name=saloon_data.get('name', 'Anonymous'),
        business_number=saloon_data.get('business_number'),
        opening_time=saloon_data.get('opening_time'),
        closing_time=saloon_data.get('closing_time'),
        description=saloon_data.get('description'),
        services=saloon_data.get('services'),
        user_id=1
    )
    result = {'status': 'success'}
    return jsonify(result)


@app.route('/saloon',  methods=['GET'])
def list_saloons():
    saloons = Saloon.select()
    results = []
    for saloon in saloons:
        results.append(
            {
                'name': saloon.name,
                'business_number': saloon.business_number
             }
            )
    return jsonify(results)

if __name__ == '__main__':
    app.run(**app_start_config)
