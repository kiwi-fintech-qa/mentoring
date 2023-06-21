from requests import request, Response
from typing import Dict, Any

# Docs: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
API_URL = "https://restful-booker.herokuapp.com"


# API endpoints
def health_check() -> Response:
	url = API_URL + ""
	response = request(url=url, method="GET")
	return response


def create_booking(request_payload: Dict[str, Any]) -> Response:
	url = ""
	response = request(url=url, method="", data=request_payload)
	return response


def delete_booking(booking_id: str, headers: Dict[str, str]) -> Response:
	url = ""
	response = request(url=url, method="", headers=headers)
	return response


def get_booking_by_id():
	pass


def get_list_of_bookings():
	pass


# You can have two separate functions to call different update-endpoints or one to handle both based on a condition
def update_booking():
	pass

