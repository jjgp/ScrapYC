output:
	mkdir $@

output/items.json: ITEM_ID ?= 30878761
output/items.json: | output
	scrapy crawl items -a item_id=$(ITEM_ID) -o $@
