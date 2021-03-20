import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Region, Service
from flask_cors import CORS
import sys
from auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
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
    "region": {
        "city": "Chennai",
        "country": "India",
        "id": 1,
        "name": "West Mambalam",
        "regionhead": "Anitha",
        "state": "Tamil Nadu"
    },
    "success": true
    }    '''

    @app.route('/regions/<region_id>', methods=['GET'])
    def get_region_by_id(region_id):
        try:
            region = Region.query.filter(Region.id == region_id).one_or_none()
            if region is None:
                abort(404)
            return jsonify({
                "region": Region.format(region),
                "success": True
            }),200
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
    @requires_auth('post:regions')
    def create_region(jwt):
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
            abort(422)

    # -----------------------------------------------------------------------------------------
    # ROUTE to update a region
    # PATCH /regions/<region_id>
    # -----------------------------------------------------------------------------------------


    '''
    ROUTE TO UPDATE Regions
    PATCH /regions/<region_id>
    
    Sample Successful JSON Response
    {
    "updated": 2,
    "success": true
    }
    '''

    @app.route('/regions/<region_id>', methods=['PATCH'])
    @requires_auth('patch:regions')
    def update_region(jwt,region_id):
        body = request.get_json()
        print(str(body))
        try:
            name = body.get('name', None)
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
    @requires_auth('delete:regions')
    def delete_region(jwt, region_id):

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
            print(sys.exc_info())
            abort(422)


# ========================================================
    '''
    ROUTE FOR POST /services
    Sample Request Payload in Expected Format:
    {
    'name': 'SS Resource Management Services',
    'type': 'Resource Management Service',
    'address': '3, Brinda Street, West Mambalam, Tamil Nadu',
    'region_id': 1,
    'email': 'info@ssrms.com',
    'phone': '+91-1112223344',
    'website': 'www.ssrms.com' 
    }

    Sample Successful JSON Response
    {
    "created": 1,
    "success": true
    }
    '''

    @app.route('/services', methods=['POST'])
    @requires_auth('post:services')
    def create_service(jwt):
        body = request.get_json()
        try:
            name = body.get('name', None)
            type = body.get('type', None)
            address = body.get('address', None)
            region_id = body.get('region_id', None)
            email = body.get('email', None)
            phone = body.get('phone', None)
            website = body.get('website', None)
            image = body.get('image', None)

            if (name is None) or (type is None) or (address is None) or (region_id is None):
                print('Something is none')
                abort(422)

            new_service = Service(name=name, type=type, address=address,
                                  region_id=region_id, email=email,
                                  phone=phone, website=website, image=image)
            new_service.insert()
            return jsonify({
                'success': True,
                'created': new_service.id
            }), 200
        except:
            print(sys.exc_info())
            abort(422)

    # -----------------------------------------------------------------------------------------
    # ROUTE FOR GET all regions
    # GET /regions
    # -----------------------------------------------------------------------------------------
    '''
    ROUTE FOR GET /services
    No request Payload
    Sample Success Response is below:
    {
    "services": [
        {
            "address": "3 Brinda StreetWest MambalamTamil Nadu",
            "email": "info@ssrms.com",
            "id": 1,
            "image": null,
            "name": "SS Resource Management Services",
            "phone": "911112223344",
            "region_id": 1,
            "type": "Resource Management Service",
            "website": "www.ssrms.com"
        },
        {
            "address": "3 Van Street, West Mambalam, Tamil Nadu",
            "email": "info@mmrms.com",
            "id": 3,
            "image": null,
            "name": "MM Resource Management Services",
            "phone": "911112223355",
            "region_id": 2,
            "type": "Resource Management Service",
            "website": "www.mmrms.com"
        }
    ],
    "success": true
}
    '''

    @app.route('/services', methods=['GET'])
    def get_services():
        all_services = Service.query.order_by(Service.id).all()
        total_no_services = len(all_services)
        if (total_no_services == 0):
            abort(404)

        services_array = []
        for service in all_services:
            services_array.append({
                "id": service.id,
                "name": service.name,
                "type": service.type,
                "address": service.address,
                "region_id": service.region_id,
                "email": service.email,
                "phone": service.phone,
                "website": service.website,
                "image": service.image,
            })
        return jsonify({
            'services': services_array,
            'success':True
        })

    # -----------------------------------------------------------------------------------------
    # ROUTE to GET a specific region
    # GET /services/<service_id>
    # -----------------------------------------------------------------------------------------
    '''
    ROUTE FOR GET /services/1
    No request Payload
    Sample Success Response is below
    {
    "service": {
        "address": "3 Brinda StreetWest MambalamTamil Nadu",
        "email": "info@ssrms.com",
        "id": 1,
        "image": null,
        "name": "SS Resource Management Services",
        "phone": "911112223344",
        "region_id": 1,
        "type": "Resource Management Service",
        "website": "www.ssrms.com"
    },
    "success": true
}    '''

    @app.route('/services/<service_id>', methods=['GET'])
    def get_service_by_id(service_id):
        try:
            service = Service.query.filter(Service.id == service_id).one_or_none()
            if service is None:
                abort(404)
            return jsonify({
                "service": Service.format(service),
                "success": True
            }),200
        except:
            print(sys.exc_info())
            abort(422)

    # -----------------------------------------------------------------------------------------
    # ROUTE to update a service
    # PATCH /services/<service_id>
    # -----------------------------------------------------------------------------------------

    '''
    ROUTE TO UPDATE Services
    PATCH /services/<service_id>

    Sample Successful JSON Response
    {
    "updated": 2,
    "success": true
    }
    '''

    @app.route('/services/<service_id>', methods=['PATCH'])
    @requires_auth('patch:services')
    def update_service(jwt, service_id):
        body = request.get_json()
        print(str(body))
        try:
            name = body.get('name', None)
            type = body.get('type', None)
            address = body.get('address', None)
            region_id = body.get('region_id', None)
            email = body.get('email', None)
            phone = body.get('phone', None)
            website = body.get('website', None)
            image = body.get('image', None)

            if (name is None) and (type is None) and (address is None) \
                    and (region_id is None) and (email is None) and (phone is None)\
                    and (website is None) and (image is None):
                abort(422)

            service = Service.query.get(service_id)
            if (service is None):
                abort(402)

            if name is not None:
                service.name = name
            if type is not None:
                service.type = type
            if address is not None:
                service.address = address
            if region_id is not None:
                service.region_id = region_id
            if email is not None:
                service.email = email
            if phone is not None:
                service.phone = phone
            if image is not None:
                service.image = image
            if website is not None:
                service.website = website

            Service.update(service)
            return jsonify({
                'success': True,
                'updated': service.id
            }), 200
        except:
            print(sys.exc_info())
            abort(500)

    '''
    ROUTE TO DELETE Service BY ID
    DELETE /services/<service_id>

    Sample Successful JSON Response
    {
    "deleted": 2,
    "success": true
    }
    '''

    @app.route('/services/<service_id>', methods=['DELETE'])
    @requires_auth('delete:services')
    def delete_service(jwt, service_id):

        service = Service.query.get(service_id)

        if service is None:
            print(sys.exc_info())
            abort(404)
        try:
            Service.delete(service)
            return jsonify({
                'success': True,
                'deleted': service.id
            }), 200
        except:
            print(sys.exc_info())
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

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        return jsonify({
            "success": False,
            "error": ex.status_code,
            'message': ex.error
        }), 401

    return app

app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080, debug=True)
