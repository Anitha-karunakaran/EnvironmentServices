import string
import random


def generate_region_payload():
    # generate random name for region
    region_name = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=7))
    test_payload = {
        "name": region_name,
        "city": "Chennai",
        "state": "Tamil Nadu",
        "country": "India",
        "regionhead": "Anitha"
    }
    return test_payload


def generate_service_payload(created_region_id):
    # generate random name for region
    service_name = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=7))
    test_payload = {
        "name": service_name,
        "type": "Test Service Type ",
        "address": "Test Address",
        "region_id": created_region_id,
        "email": "info@ssrms.com",
        "phone": "+91-1112223344",
        "website": "www.ssrms.com"
    }
    return test_payload
