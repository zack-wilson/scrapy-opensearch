from typing import Optional
OPENSEARCH_CA_CERTS: Optional[str] = None
OPENSEARCH_CLIENT_CERT: Optional[str] = None
OPENSEARCH_CLIENT_KEY: Optional[str] = None
OPENSEARCH_ENABLED: bool = False
OPENSEARCH_HOSTS: str = "https://localhost:9200"
OPENSEARCH_HTTP_COMPRESS: bool = True  # enables gzip compression for request bodies
OPENSEARCH_ID: Optional[str] = None  # An item's primary key field, e.g., "item_id". Automatically generated when set to `None`.
OPENSEARCH_INDEX: str = "scrapy_opensearch"
OPENSEARCH_SSL_SHOW_WARN: bool = False
OPENSEARCH_USE_SSL: bool = True
OPENSEARCH_USERNAME: str = "admin"
OPENSEARCH_PASSWORD: str = "admin"
OPENSEARCH_VERSION: Optional[str] = None
OPENSEARCH_VERIFY_CERTS: bool = False
