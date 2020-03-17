from rio_cogeo.cogeo import cog_translate
from rio_cogeo.profiles import cog_profiles
import boto3
import botocore
import os
import logging
import uuid

@profile
def _translate(src_path, dst_path, profile="lzw", profile_options={}, **options):
    """Convert image to COG."""
    # Format creation option (see gdalwarp `-co` option)
    output_profile = cog_profiles.get(profile)
    output_profile.update(dict(BIGTIFF="IF_SAFER"))
    output_profile.update(profile_options)

    # Dataset Open option (see gdalwarp `-oo` option)
    config = dict(
        GDAL_NUM_THREADS="ALL_CPUS",
        GDAL_TIFF_INTERNAL_MASK=True,
        GDAL_TIFF_OVR_BLOCKSIZE="128",
    )

    cog_translate(
        src_path,
        dst_path,
        output_profile,
        config=config,
        in_memory=False,
        quiet=True,
        **options,
    )
    return True

def cog_path_from_file_path(file_path):
    p = os.path.splitext(file_path)
    l = list(p[0:-1])
    l.append('-cog'+p[-1])
    return ''.join(l)

if __name__ == '__main__':
    _UUID = str(uuid.uuid4())

    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('SECRET_KEY'),
        region_name=os.environ.get('REGION'),
        )

    BUCKET = os.environ.get('BUCKET')
    KEY = os.environ.get('FILE_PATH')

    # # mode = 0o666
    # os.mkdir('/data/%s' % _UUID)

    # s3.download_file(BUCKET, KEY, '/data/%s/file.tif' % _UUID)


    print('starting...')
    _translate(KEY, cog_path_from_file_path(KEY))

    # try:
    #     response = s3.upload_file('/data/%s/cog.tif' % _UUID, BUCKET, cog_path_from_file_path(KEY))
    # except botocore.exceptions.ClientError as e:
    #     logging.error(e)%