import logging

import azure.functions as func

import numpy as np


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    return func.HttpResponse(f"Hello {str(np.array([1,2,3,4]))}!")