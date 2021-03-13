import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Region, Service
from flask_cors import CORS
import sys

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    #CORS(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

    # -----------------------------------------------------------------------------------------
    # ROUTE FOR GET all regions
    # GET /regions
    # -----------------------------------------------------------------------------------------
    '''
    ROUTE FOR GET /regions
    No request Payload
    Sample Success Response is below
    {
        "regions": [
            {
                "city": "Chennai",
                "country": "India",
                "name": "West Mambalam",
                "regionhead": "Anitha",
                "state": "Tamil Nadu"
            },
            {
                "city": "Chennai",
                "country": "India",
                "name": "Vadapalani",
                "regionhead": "Amutha",
                "state": "Tamil Nadu"
            }
        ],
        "success": true
    }
    '''

    @app.route('/regions', methods=['GET'])
    def get_regions():
        all_regions = Region.query.order_by(Region.id).all()
        total_no_regions = len(all_regions)
        if (total_no_regions == 0):
            abort(404)

        region_array = []
        for region in all_regions:
            region_array.append({
                "id": region.id,
                "name": region.name,
                "city": region.city,
                "state": region.state,
                "country": region.country,
                "regionhead": region.regionhead
            })
        return jsonify({
            'regions': region_array,
            'success':True
        })

    # -----------------------------------------------------------------------------------------
    # ROUTE to GET a specific region
    # GET / regions/<region_id>
    # -----------------------------------------------------------------------------------------
    '''
    ROUTE FOR GET /regions
    No request Payload
    Sample Success Response is below
    {
    "city": "Chennai",
    "country": "India",
    "id": 1,
    "name": "West Mambalam",
    "regionhead": "Anitha",
    "state": "Tamil Nadu"
    }    '''

    @app.route('/regions/<region_id>', methods=['GET'])
    def get_region_by_id(region_id):
        try:
            region = Region.query.filter(Region.id == region_id).one_or_none()
            if region is None:
                abort(404)
            return jsonify(Region.format(region)),200
        except:
            print(sys.exc_info())
            abort(422)

    # -----------------------------------------------------------------------------------------
    # ROUTE to create a new region
    #  POST /regions
    # -----------------------------------------------------------------------------------------

    '''
    ROUTE FOR POST /regions
    Sample Request Payload in Expected Format:
    {
    'name': 'West Mambalam',
    'city': 'Chennai',
    'state': 'Tamil Nadu',
    'country': 'India',
    'regionhead': 'Anitha'
    }
    
    Sample Successful JSON Response
    {
    "created": 2,
    "success": true
    }
    '''

    @app.route('/regions', methods=['POST'])
    def create_region():
        try:
            body = request.get_json()
            name = body.get('name', None)
            city = body.get('city', None)
            state = body.get('state', None)
            country = body.get('country', None)
            regionhead = body.get('regionhead', None)

            if (name is None) or (city is None) or (state is None) or (regionhead is None):
                abort(422)

            new_region = Region(name=name, city=city, state=state, regionhead=regionhead, country=country)
            new_region.insert()
            return jsonify({
                'success': True,
                'created': new_region.id
            }), 200
        except:
            print(sys.exc_info())
            abort(500)

    # -----------------------------------------------------------------------------------------
    # ROUTE to update a region
    # PATCH /regions/<region_id>
    # -----------------------------------------------------------------------------------------

    '''
    ROUTE TO UPDATE Regions
    PATCH /regions/<region_id>
    
    Sample Successful JSON Response
    {
    "created": 2,
    "success": true
    }
    '''

    @app.route('/regions/<region_id>', methods=['PATCH'])
    def update_region(region_id):
        body = request.get_json()
        print(str(body))
        try:
            name = body.get('name', None)
            print('---------'+str(body))
            city = body.get('city', None)
            state = body.get('state', None)
            country = body.get('country', None)
            regionhead = body.get('regionhead', None)

            if (name is None) and (city is None) and (state is None) and (regionhead is None):
                abort(422)

            region = Region.query.get(region_id)
            if (region is None):
                abort(402)

            if name is not None:
                region.name = name
            if city is not None:
                region.city = city
            if state is not None:
                region.state = state
            if country is not None:
                region.country = country
            if regionhead is not None:
                region.regionhead = regionhead

            Region.update(region)
            return jsonify({
                'success': True,
                'updated': region.id
            }), 200
        except:
            print(sys.exc_info())
            abort(500)

    '''
    ROUTE TO DELETE Region BY ID
    DELETE /regions/<region_id>

    Sample Successful JSON Response
    {
    "deleted": 2,
    "success": true
    }
    '''
    @app.route('/regions/<region_id>', methods=['DELETE'])
    def delete_region(region_id):

        region = Region.query.get(region_id)

        if region is None:
            abort(404)
        try:
            Region.delete(region)
            return jsonify({
                'success': True,
                'deleted': region.id
            }), 200
        except:
            abort(422)

    '''
    ROUTE FOR APPLICATION ROOT
    '''
    @app.route('/')
    def welcome():
        return "Welcome to Environment Services Portal"

    # ----------------------------------------------------------------------------#
    # Error Handlers
    # ----------------------------------------------------------------------------#
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(422)
    def request_unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'request is unprocessable'
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
