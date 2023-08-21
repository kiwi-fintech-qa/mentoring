from typing import Any, Dict, Optional
from requests import Response, request

API_URL = ""
API_KEY = ""


class TestAPI:
    @classmethod
    def _api_request(
        cls,
        url: str,
        headers: Dict[str, Any],
        method: str,
        timeout: int = 100,
        json: Optional[Dict[str, Any]] = None,
    ) -> Response:
        url = f"{API_URL}/{url}"
        return request(
            method=method,
            url=url,
            timeout=timeout,
            headers=headers,
            json=json,
        )

    @classmethod
    def _add_headers(cls, auth_method: Optional[str] = None) -> Dict[str, str]:
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if auth_method == "api_key":
            pass
        elif auth_method == "cookie_token":
            pass
        return headers

    @classmethod
    def _get_auth_token(cls) -> str:
        url = "auth"
        response = cls._api_request(
            url=url,
            headers=cls._add_headers(),
            method="POST",
            json={"username": "admin", "password": "password123"},
        )
        return response.json()["token"]

    @classmethod
    def create_booking(cls, request_payload: Dict[str, Any]) -> Response:
        url = "booking"
        response = cls._api_request(
            url=url, headers=cls._add_headers(), method="POST", json=request_payload
        )
        return response

    @classmethod
    def list_booking_ids(cls):
        pass

    @classmethod
    def get_booking_by_id(cls):
        pass

    @classmethod
    def update_booking(cls):
        pass

    @classmethod
    def delete_booking(cls):
        pass

    @classmethod
    def ping_api(cls):
        pass
