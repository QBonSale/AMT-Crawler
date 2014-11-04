#!/bin/sh
cd /home/mcqb/mturk
NOW=$(date +"%m-%d_%H-%M_%Y")
scrapy crawl AMT -o ${NOW}_raw.json
python cleanup.py -i ${NOW}_raw.json -o ${NOW}.json
