from scrapy import Spider

from scrapy_opensearch import defaults
from scrapy_opensearch.pipelines import OpenSearchPipeline

from scrapy_project.spiders.dummy_spider import DummySpiderSpider

spider = DummySpiderSpider()


def test_opensearch_pipeline():
    # TODO: This test requires an opensearch connection, we could mock or use docker
    opensearch_pipeline = OpenSearchPipeline(
        opensearch_index="scrapy_opensearch_test_index",
        opensearch_hosts="https://admin:admin@opensearch:9200",
        opensearch_enabled=True,
        opensearch_username="admin",
        opensearch_password="admin",
    )
    opensearch_pipeline.open_spider(spider=spider)
    assert opensearch_pipeline.process_item({"item": "test_item"}, spider=spider)
