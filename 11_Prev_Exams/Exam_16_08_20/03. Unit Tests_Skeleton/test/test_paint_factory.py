from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory("Test", 3)

    def test_constructor(self):
        self.assertEqual("Test", self.paint_factory.name)
        self.assertEqual(3, self.paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_can_add(self):
        self.assertTrue(self.paint_factory.can_add(3))
        self.assertFalse(self.paint_factory.can_add(4))

    def test_add_ingredient_not_enough_space_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient("white", 4)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredients_wrong_ingredient_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("black", 1)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredients_adds(self):
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("yellow", 1)
        self.assertEqual({"white": 2, "yellow": 1}, self.paint_factory.ingredients)

    def test_remove_ingredient_with_negative_value_raises(self):
        self.paint_factory.add_ingredient("white", 1)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 2)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredients_wrong_ingredient_raises(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient("white", 2)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_removes(self):
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("yellow", 1)
        self.paint_factory.remove_ingredient("white", 1)
        self.paint_factory.remove_ingredient("yellow", 1)
        self.assertEqual({"white": 1, "yellow": 0}, self.paint_factory.ingredients)

    def test_products_property(self):
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("yellow", 1)
        self.assertEqual(self.paint_factory.ingredients, self.paint_factory.products)


    def test_repr(self):
        self.paint_factory.add_ingredient("white", 1)
        self.paint_factory.add_ingredient("yellow", 1)
        expected = f"Factory name: Test with capacity 3.\n" \
                   f"white: 1\n" \
                   f"yellow: 1\n"
        actual = str(self.paint_factory)
        self.assertEqual(expected, actual)




if __name__ == "__main__":
    main()