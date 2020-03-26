from azure.storage.blob import BlockBlobService
import json


def main():
    # https://stackoverflow.com/questions/41978833/upload-csv-file-into-microsoft-azure-storage-account-using-python
    block_blob_service = BlockBlobService(
        account_name='storageaccountazure8ed8',
        account_key='jz9uITvczqYowa9oKJnL3h/4pISy+lxwilNNFRkC5GWdbzWPKMp8ClRjv4iPM5r7xCHvnYAF3HxonnD4ROf0MA=='
    )

    block_blob_service.get_blob_to_path('samples-workitems', '0001.pdf', '/tmp/file.pdf')
    block_blob_service.create_blob_from_path('raster-derived', '0001.pdf', '/tmp/file.pdf')

if __name__ == '__main__':
    main()