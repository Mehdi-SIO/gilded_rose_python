# -*- coding: utf-8 -*-
LAST_DATE_LIMI_FOR_TICKETS = 6
FIRST_DATE_LMIT_FOR_TICKETS = 11
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONCERT = "Backstage passes to a TAFKAL80ETC concert"
BRIE = "Aged Brie"
MIN_QUALITY = 0
MAX_QUALITY = 50


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            #1st if level
            if item.name != BRIE and item.name != CONCERT:
                #2nd if level
                if item.quality > MIN_QUALITY:
                    #3rd if level
                    if item.name != SULFURAS:
                        self.decrease_quality(item)
            else:
                #2nd if level
                if item.quality < MAX_QUALITY:
                    self.increase_quality(item)
                    #3rd if level
                    if item.quality < MAX_QUALITY:
                        if item.name == CONCERT:
                            if item.sell_in < FIRST_DATE_LMIT_FOR_TICKETS:
                                self.increase_quality(item)
                            if item.sell_in < LAST_DATE_LIMI_FOR_TICKETS:
                                self.increase_quality(item)
            #1st if level
            if item.name != SULFURAS:
                self.go_to_next_day(item)
            # 1st if level
            if item.sell_in < 0:
                #2nd if level
                if item.name != BRIE:
                    #3rd if level
                    if item.name != CONCERT:
                        #4th if level
                        if item.quality > MIN_QUALITY:
                            #5th if level
                            if item.name != SULFURAS:
                                self.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < MAX_QUALITY:
                        self.increase_quality(item)

    def go_to_next_day(self, item):
        item.sell_in = item.sell_in - 1

    def decrease_quality(self, item):
        item.quality = item.quality - 1

    def increase_quality(self, item):
        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)