MturkCrawler
============

A Crawler for Amazon Mechanical Turkey based on [Scrapy](http://scrapy.org/)


Specification: The "data collection" part in the paper which could be found [here](http://archive.nyu.edu/bitstream/2451/29801/4/CeDER-10-04.pdf)


`scrapy crawl AMT` to scrape, followed by `-o foo.json/csv/xml` for output

`cron` `crawl.sh` to crawl


``merge.py` -> `fix.py` -> `simplify.py` for afterwards processing