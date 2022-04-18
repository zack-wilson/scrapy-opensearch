# scrapy-opensearch

The scrapy-opensearch is a scrapy extension to send scrapy items to
opensearch.

## Installation

Install scrapy-opensearch using `pip`:

    $ pip install scrapy-opensearch

## Configuration

First, you need to enable and include the extension in the `ITEM_PIPELINES` dict in
`settings.py`, e.g.:

    OPENSEARCH_ENABLED = True

    ITEM_PIPELINES = {
        ...
        'scrapy_opensearch.OpensearchExtension': 123,
        ...
    }

## Settings

### Required Settings

To enable the extension, set:

    OPENSEARCH_ENABLED = True

To configure host(s) settings, you can adjust the following:

    OPENSEARCH_HOSTS = 'https://0:9200'

The default endpoint for sending items to opensearch is:

    https://0:9200

Periodic logging is enabled by default but you can disable it, in which
case the items will be logged only once, when a spider is closed.

Set the desired index, e.g.:

    OPENSEARCH_INDEX = 'scrapy'
### Optional Settings

    OPENSEARCH_DOC_TYPE = None
    OPENSEARCH_ID = None
    OPENSEARCH_USERNAME = OPENSEARCH_PASSWORD = "admin"
    OPENSEARCH_USE_SSL = True
    OPENSEARCH_VERIFY_CERTS = False
    OPENSEARCH_SSL_SHOW_WARN = False
    OPENSEARCH_HTTP_COMPRESS = True
    OPENSEARCH_CA_CERTS = None
    OPENSEARCH_CLIENT_CERT = None
    OPENSEARCH_CLIENT_KEY = None

<!-- You can specify which indexes you want logged if you don't want all
scrapy opensearch items. The default is an empty list which indicates that
all opensearch items should be logged. You can, for example, log only
downloader and robotstxt exception opensearch items by setting
`OPENSEARCH_LOG_ONLY` to `['downloader', 'robotstxt.exception_count']`.

    OPENSEARCH_LOG_ONLY = []

You can also specify indexes to ignore the same way using
`OPENSEARCH_IGNORE`:

    OPENSEARCH_IGNORE = []

## Tags

Certain platforms such as datadog and influxdb offer tagging options.

To enable tagging set `OPENSEARCH_TAGGING` to `True`, it is disabled by
default:

    OPENSEARCH_TAGGING = False

Then, you can set custom tags using `OPENSEARCH_TAGS`. Currently, only
`spider_name_tag` is supported and setting it to True will add the
spider's as a tag on all items:

    OPENSEARCH_TAGS = {
        'spider_name_tag': True
    }

You can also set custom tags by setting `OPENSEARCH_TAGS` attribute on
each spider. This must be a dictionary containing tag names as keys and
tag values as dictionary values. -->
