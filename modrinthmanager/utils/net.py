import requests
from PySide6.QtWidgets import QApplication


def get_html(url: str, headers=None, params=None, json=None, cookies=None, content_type=None):
    """
        Sends an HTTP GET request to the specified URL with the given headers, query parameters, and cookies.

        :param url: The URL to request.
        :param headers: Optional dictionary of request headers.
        :param params: Optional dictionary of query parameters.
        :param json: Optional dictionary of json to include in the request.
        :param cookies: Optional dictionary of cookies to include in the request.
        :param content_type: Optional string indicating the expected content type of the response ('content' or 'json').
        :return: If content_type is 'content', returns the raw response content (bytes).
                 If content_type is 'json', returns the JSON-decoded response.
                 Otherwise, returns the full requests.Response object.
                 Returns None if there was an error.
        """
    if headers is None:
        print("No headers")
    if "test" in QApplication.arguments():
        return
    try:
        response = requests.get(url, headers=headers, params=params, json=json, cookies=cookies)
        response.raise_for_status()
        if content_type == 'content':
            return response.content
        elif content_type == 'json':
            return response.json()
        elif content_type == 'text':
            return response.text
        else:
            return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url}")
        print(f"  Reason: {e}")
        print(f"  Headers: {headers}")
        print(f"  Params: {params}")
        print(f"  Cookies: {cookies}")
        print(f"  Json: {json}")
        return
