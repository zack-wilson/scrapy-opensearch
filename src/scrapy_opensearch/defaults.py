OPENSEARCH_CA_CERTS = None
OPENSEARCH_CLIENT_CERT = None
OPENSEARCH_CLIENT_KEY = None
OPENSEARCH_ENABLED = False
OPENSEARCH_HOSTS = [{"host": "localhost", "port": 9200}]
OPENSEARCH_HTTP_COMPRESS = True  # enables gzip compression for request bodies
OPENSEARCH_ID = None  # An item's primary key field, e.g., "item_id". Automatically generated when set to `None`.
OPENSEARCH_INDEX = "scrapy"
OPENSEARCH_SSL_SHOW_WARN = False
OPENSEARCH_DOC_TYPE = None  # e.g., "_doc"
OPENSEARCH_USE_SSL = True
OPENSEARCH_USERNAME = OPENSEARCH_PASSWORD = "admin"
OPENSEARCH_VERSION = None
OPENSEARCH_VERIFY_CERTS = False

try:
    from local_settings import *
except ImportError:
    pass
