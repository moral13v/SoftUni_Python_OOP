from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Test")

    def test_constructor(self):
        self.assertEqual("Test", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_if_quantity_zero_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Pedigree", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_if_quantity_negative_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Pedigree", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food(self):
        self.pet_shop.add_food("Pedigree", 100)
        self.pet_shop.add_food("Pedigree", 50)
        self.pet_shop.add_food("Whiskas", 70)
        expected = {"Pedigree": 150, "Whiskas": 70}
        self.assertEqual(expected, self.pet_shop.food)

    def test_add_food_return_message(self):
        food_name = "Pedigree"
        food_quantity = 100
        result = self.pet_shop.add_food(food_name, food_quantity)
        expected = "Successfully added 100.00 grams of Pedigree."
        self.assertEqual(expected, result)

    def test_add_pet_if_pet_already_exists_raise(self):
        self.pet_shop.add_pet("Tom")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Tom")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet(self):
        result = self.pet_shop.add_pet("Tom")
        self.assertEqual(["Tom"], self.pet_shop.pets)
        self.assertEqual(f"Successfully added Tom.", result)

        result = self.pet_shop.add_pet("Jerry")
        self.assertEqual(["Tom", "Jerry"], self.pet_shop.pets)
        self.assertEqual(f"Successfully added Jerry.", result)

    def test_feed_pet_when_non_existing_pet_raises(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Pedigree", "Tom")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_non_existing_food(self):
        self.pet_shop.add_pet("Tom")
        result = self.pet_shop.feed_pet("Pedigree", "Tom")
        self.assertEqual("You do not have Pedigree", result)

    def test_feed_pet_when_food_is_below_100gr_return_message(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_food("Whiskas", 50)
        result = self.pet_shop.feed_pet("Whiskas", "Tom")
        self.assertEqual("Adding food...", result)

    def test_feed_pet_when_food_is_below_100gr(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_food("Whiskas", 50)
        self.pet_shop.feed_pet("Whiskas", "Tom")
        # food: 50 + 1000 = 1050
        self.assertEqual(1050, self.pet_shop.food["Whiskas"])

    def test_feed_pet_decrement(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_food("Whiskas", 300)
        self.pet_shop.feed_pet("Whiskas", "Tom")
        self.assertEqual(200, self.pet_shop.food["Whiskas"])

        self.pet_shop.feed_pet("Whiskas", "Tom")
        self.assertEqual(100, self.pet_shop.food["Whiskas"])

    def test_feed_pet_return_message(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_food("Whiskas", 300)
        result = self.pet_shop.feed_pet("Whiskas", "Tom")
        self.assertEqual("Tom was successfully fed", result)

    def test_repr(self):
        self.pet_shop.add_pet("Tom")
        self.pet_shop.add_pet("Jerry")
        self.pet_shop.add_pet("Spike")

        expected = f'Shop Test:\n'\
                   f'Pets: Tom, Jerry, Spike'

        self.assertEqual(expected, repr(self.pet_shop))


if __name__ == "__main__":
    main()








