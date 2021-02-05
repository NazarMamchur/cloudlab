import connexion
import six

from swagger_server import util


def health_check():  # noqa: E501
    """Provides an indication about the health of the API

     # noqa: E501


    :rtype: None
    """
    response = {
        "detail": f"API is healthy",
        "status": 200,
        "title": "",
        "type": ""
    }
    return response
