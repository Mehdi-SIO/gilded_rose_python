# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_quality_decreases_by_one_at_the_end_of_the_day(self):
        items = [Item(name="Elixir of the Mongoose", sell_in=5, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_quality_decreases_by_two_at_the_end_of_the_day_if_expired(self):
        items = [Item(name="Elixir of the Mongoose", sell_in=-1, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)

    def test_sell_in_value_decreases_by_one_each_day(self):
        items = [Item(name="Elixir of the Mongoose", sell_in=5, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_quality_increases_by_one_at_the_end_of_the_day_aged_brie(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_quality_increases_twice_as_fast_when_sell_in_date_has_passed(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_quality_cannot_be_higher_than_50(self):
        items = [Item(name="Aged Brie", sell_in=3, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_quality_of_sulfura_never_decreases(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sell_in_of_sulfura_never_decreases(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)

    def test_quality_of_backstage_passes_increases_by_one_if_expires_above_ten_days(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_quality_of_backstage_passes_increases_by_two_if_expires_within_ten_days(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_quality_of_backstage_passes_increases_by_three_if_expires_within_five_days(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_quality_of_backstage_passes_drops_to_zero_if_expired(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()