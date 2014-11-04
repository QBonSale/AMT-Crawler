# Scrapy settings for mturk project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mturk'

SPIDER_MODULES = ['mturk.spiders']
NEWSPIDER_MODULE = 'mturk.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mturk (+http://www.yourdomain.com)'

# COOKIES_DEBUG = True
COOKIES_ENABLED = True

ITEM_PIPELINES = {
    'mturk.pipelines.MturkPipeline': 300,
}