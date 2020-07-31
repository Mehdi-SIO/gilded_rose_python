# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_sell_in_decreases_by_one_at_the_end_of_the_day(self):
        items = [Item("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)

    def test_quality_decreases_by_one_at_the_end_of_the_day(self):
        items = [Item("foo", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)

    def test_quality_decreases_by_two_when_sell_in_has_passed_at_the_end_of_the_day(self):
        items = [Item("foo", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item("foo", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_of_aged_brie_increases_at_the_end_of_day(self):
        #Given
        items = [Item("Aged Brie", 10, 0)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertGreater(items[0].quality, 0)

    def test_quality_of_aged_brie_increases_twice_as_fast_if_expired_at_the_end_of_day(self):
        #Given
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(items[0].quality, 12)

    def test_quality_is_never_above_fifty(self):
        #Given
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(50, items[0].quality)

    def test_sell_in_of_sulfura_never_decreases(self):
        #Given
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 50)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(10, items[0].sell_in)

    def test_quality_of_sulfura_never_decreases(self):
        #Given
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 50)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(50, items[0].quality)

    def test_quality_of_tickets_increases_by_one_at_the_end_of_day_if_sell_greater_than_ten_days(self):
        #Given
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(21, items[0].quality)

    def test_quality_of_tickets_increases_by_two_at_the_end_of_day_if_sell_is_less_than_ten_days(self):
        #Given
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(22, items[0].quality)

    def test_quality_of_tickets_increases_by_three_at_the_end_of_day_if_sell_is_less_than_5_days(self):
        #Given
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(23, items[0].quality)

    def test_quality_of_tickets_drops_to_zero_after_the_concert(self):
        #Given
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(0, items[0].quality)

    def test_quality_of_conjured_objects_decreases_by_two_at_the_of_day(self):
        #Given
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(4, items[0].quality)

    def test_quality_of_conjured_objects_decreases_by_four_if_expired_at_the_of_day(self):
        #Given
        items = [Item("Conjured Mana Cake", 0, 6)]
        gilded_rose = GildedRose(items)
        #When
        gilded_rose.update_quality()
        #Then
        self.assertEqual(2, items[0].quality)



class ItemTest(unittest.TestCase):
    def test_item_parameters_are_correctly_attributed_to_the_item(self):
        #GIVEN
        name = "foo"
        sell_in = 5
        quality = 10
        #WHEN
        item = Item(name, sell_in, quality)
        #THEN
        self.assertEqual(name, item.name)
        self.assertEqual(sell_in, item.sell_in)
        self.assertEqual(quality, item.quality)


if __name__ == '__main__':
    unittest.main()