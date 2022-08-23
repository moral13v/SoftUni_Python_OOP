from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("name", "mammal type", "sound")

    def test_init(self):
        self.assertEqual("name", self.mammal.name)
        self.assertEqual("mammal type", self.mammal.type)
        self.assertEqual("sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        result = self.mammal.make_sound()
        self.assertEqual(expected, result)

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), self.mammal._Mammal__kingdom)

    def test_info(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        result = self.mammal.info()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
