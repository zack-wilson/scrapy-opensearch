# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import logging
from sqlite3 import adapt
from typing import Dict, List, Optional, Union

import scrapy
from itemadapter import ItemAdapter
from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.exceptions import NotConfigured

from . import defaults

logger = logging.getLogger(__name__)


class OpenSearchPipeline:
    def __init__(
        self,
        opensearch_index: str,
        opensearch_hosts: Union[str, List[Dict[str, int]]],
        opensearch_enabled: Optional[bool] = None,
        opensearch_username: Optional[str] = None,
        opensearch_password: Optional[str] = None,
        opensearch_use_ssl: Optional[str] = None,
        opensearch_verify_certs: Optional[str] = None,
        opensearch_ca_certs: Optional[Dict[str, str]] = None,
        opensearch_client_cert: Optional[str] = None,
        opensearch_client_key: Optional[str] = None,
        opensearch_http_compress: Optional[str] = None,
        opensearch_id: Optional[str] = None,
    ):
        if not opensearch_enabled:
            raise NotConfigured
        else:
            self.opensearch_index = opensearch_index
            self.opensearch_hosts = opensearch_hosts
            self.opensearch_username = opensearch_username
            self.opensearch_password = opensearch_password
            self.opensearch_use_ssl = opensearch_use_ssl
            self.opensearch_verify_certs = opensearch_verify_certs
            self.opensearch_ca_certs = opensearch_ca_certs
            self.opensearch_client_cert = opensearch_client_cert
            self.opensearch_client_key = opensearch_client_key
            self.opensearch_http_compress = opensearch_http_compress
            self.opensearch_id = opensearch_id

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        settings = crawler.settings
        ext = cls(
            opensearch_enabled=settings.getbool(
                "OPENSEARCH_ENABLED", defaults.OPENSEARCH_ENABLED
            ),
            opensearch_index=settings.get(
                "OPENSEARCH_INDEX", defaults.OPENSEARCH_INDEX
            ),
            opensearch_hosts=settings.get(
                "OPENSEARCH_HOSTS", defaults.OPENSEARCH_HOSTS
            ),
            opensearch_username=settings.get(
                "OPENSEARCH_USERNAME", defaults.OPENSEARCH_USERNAME
            ),
            opensearch_password=settings.get(
                "OPENSEARCH_PASSWORD", defaults.OPENSEARCH_PASSWORD
            ),
            opensearch_use_ssl=settings.getbool(
                "OPENSEARCH_USE_SSL", defaults.OPENSEARCH_USE_SSL
            ),
            opensearch_verify_certs=settings.getbool(
                "OPENSEARCH_VERIFY_CERTS", defaults.OPENSEARCH_VERIFY_CERTS
            ),
            opensearch_ca_certs=settings.get(
                "OPENSEARCH_CA_CERTS", defaults.OPENSEARCH_CA_CERTS
            ),
            opensearch_client_cert=settings.get(
                "OPENSEARCH_CLIENT_CERT", defaults.OPENSEARCH_CLIENT_CERT
            ),
            opensearch_client_key=settings.get(
                "OPENSEARCH_CLIENT_KEY", defaults.OPENSEARCH_CLIENT_KEY
            ),
            opensearch_http_compress=settings.getbool(
                "OPENSEARCH_HTTP_COMPRESS", defaults.OPENSEARCH_HTTP_COMPRESS
            ),
            opensearch_id=settings.get("OPENSEARCH_ID", defaults.OPENSEARCH_ID),
        )
        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)

        return ext

    def open_spider(self, spider: scrapy.Spider):
        try:
            from opensearchpy import OpenSearch
        except ImportError:
            raise NotConfigured("scrapy-opensearch requires installing opensearch-py")
        self.client: OpenSearch = OpenSearch(
            hosts=self.opensearch_hosts,
            http_auth=(self.opensearch_username, self.opensearch_password),
            use_ssl=self.opensearch_use_ssl,
            verify_certs=self.opensearch_verify_certs,
            ca_certs=self.opensearch_ca_certs,
            client_key=self.opensearch_client_cert,
            client_cert=self.opensearch_client_key,
            http_compress=self.opensearch_http_compress,
        )

    def close_spider(self, spider):
        self.client.close()

    def spider_opened(self, spider):
        logger.info("opened spider %s", spider.name)

    def spider_closed(self, spider):
        logger.info("closed spider %s", spider.name)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        body = adapter.asdict()
        self.client.index(
            index=self.opensearch_index,
            body=body,
            id=body.get(self.opensearch_id),
        )
        return item
