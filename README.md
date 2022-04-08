# scrapy-opensearch

The scrapy-opensearch is a scrapy extension to send scrapy items to
opensearch.

## Installation

Install scrapy-opensearch using `pip`:

    $ pip install scrapy-opensearch

## Configuration

First, you need to include the extension to your `EXTENSIONS` dict in
`settings.py`, e.g.:

    OPENSEARCH_ENABLED = True

    EXTENSIONS = {
        ...
        'scrapy_opensearch_extension.OpensearchExtension': 123,
        ...
    }

## Settings

To configure host settings, you can adjust the following:

    OPENSEARCH_HOSTS = 'https://localhost:9200'

The default endpoint for sending opensitemsarch will be:

    http://localhost:9200

To enable the extension you must set:

    OPENSEARCH_ENABLED = True

Periodic logging is enabled by default but you can disable it, in which
case the items will be logged only once, when a spider is closed.

Set the desired index:

    OPENSEARCH_INDEX = 'scrapy'

You can specify which indexes you want logged if you don't want all
scrapy opensitemsarch. The default is an empty list which indicates that
all opensitemsarch should be logged. You can, for example, log only
downloader and robotstxt exception opensitemsarch by setting
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
tag values as dictionary values.
