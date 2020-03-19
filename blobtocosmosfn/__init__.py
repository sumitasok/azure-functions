import logging

import azure.functions as func
import json


def main(myblob: func.InputStream, doc: func.Out[func.Document]):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 f"URI: {myblob.uri}")

    outdata = {
        "file": {
            "name": myblob.name,
            "size_in_bytes": myblob.length,
            "uri": myblob.uri
        }
    }
    doc.set(func.Document.from_json(json.dumps(outdata)))
