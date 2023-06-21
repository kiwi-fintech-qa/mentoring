from restful_booker_API import health_check, create_booking


# API tests
def test_health_check():
	response = health_check()
	assert response.status_code == 201


def test_create_booking():
	payload = {}
	json_response = create_booking(request_payload=payload).json()
	assert json_response
