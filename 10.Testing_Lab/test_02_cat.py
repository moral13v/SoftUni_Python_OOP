class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


from unittest import TestCase, main


class CatTest(TestCase):
    def test_cat_is_initialised_correct(self):
        cat = Cat("Test")
        self.assertEqual("Test", cat.name)
        self.assertEqual(False, cat.fed)
        self.assertEqual(False, cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_cat_is_fed_raises(self):
        cat = Cat("Test")
        cat.fed = True
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_is_fed_after_eating(self):
        cat = Cat("Test")
        self.assertFalse(cat.fed)
        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_is_sleepy_after_eating(self):
        cat = Cat("Test")
        cat.eat()
        self.assertEqual(True, cat.sleepy)

    def test_cat_size_is_increased_after_eating(self):
        cat = Cat("Test")
        self.assertEqual(0, cat.size)
        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_can_not_sleep_if_not_fed_raises(self):
        cat = Cat("Test")
        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_not_sleepy_after_sleep(self):
        cat = Cat("Test")
        cat.eat()
        cat.sleep()
        self.assertEqual(False, cat.sleepy)


if __name__ == '__main__':
    main()






