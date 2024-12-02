import logging
from requests import Response


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)

    if response.request.body:
        if isinstance(response.request.body, bytes):
            body = response.request.body.decode('utf-8')
        else:
            body = str(response.request.body)
        logging.info("INFO Request body: " + body)

    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code: " + str(response.status_code))
    logging.info("Response: " + response.text)
