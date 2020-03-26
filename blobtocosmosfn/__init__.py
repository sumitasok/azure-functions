import logging

import azure.functions as func
from azure.storage.blob import BlockBlobService
import json


def main(myblob: func.InputStream, doc: func.Out[func.Document], myOutblob: func.Out[func.InputStream]):
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

    # block_blob_service = BlockBlobService(
    #     account_name='storageaccountazure8ed8',
    #     account_key='jz9uITvczqYowa9oKJnL3h/4pISy+lxwilNNFRkC5GWdbzWPKMp8ClRjv4iPM5r7xCHvnYAF3HxonnD4ROf0MA=='
    # )

    # block_blob_service.get_blob_to_path('samples-workitems', '0002.pdf', '/tmp/file.pdf')
    # block_blob_service.create_blob_from_path('raster-derived', '0002.pdf', '/tmp/file.pdf')