# -*- coding: utf-8 -*-
CONJURED_MANA_CAKE = "Conjured Mana Cake"
HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
TICKETS = "Backstage passes to a TAFKAL80ETC concert"
MIN_QUALITY = 0
MAX_QUALITY = 50


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != HAND_OF_RAGNAROS:
                item.sell_in = item.sell_in - 1
            if item.name != AGED_BRIE and item.name != TICKETS:
                if item.quality > MIN_QUALITY and item.name != HAND_OF_RAGNAROS:
                    self.decrease_quality(item)
                    if item.name == CONJURED_MANA_CAKE:
                        self.decrease_quality(item)
            else:
                if item.quality < MAX_QUALITY:
                    self.increase_quality(item)
                    if item.name == TICKETS and item.quality < MAX_QUALITY:
                        if item.sell_in < 11:
                            self.increase_quality(item)
                        if item.sell_in < 6:
                            self.increase_quality(item)

            if item.sell_in < 0:
                if item.name != AGED_BRIE:
                    if item.name != TICKETS:
                        if item.quality > MIN_QUALITY and item.name != HAND_OF_RAGNAROS:
                            self.decrease_quality(item)
                            if item.name == CONJURED_MANA_CAKE:
                                self.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < MAX_QUALITY:
                        self.increase_quality(item)

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