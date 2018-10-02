#!/usr/bin/env python
from flask import (Flask, render_template, request, jsonify)
from models.saloon import Saloon
app_start_config = {'debug': True, 'port': 8080, 'host': '0.0.0.0'}
app = Flask(__name__)


@app.route('/')
def index():
    return "List of products"


@app.route('/user/register', methods=['POST'])
def register_user():
    result = {'status': 'success'}
    return jsonify(result)


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
