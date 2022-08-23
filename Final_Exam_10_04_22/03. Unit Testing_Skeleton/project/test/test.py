from project.movie import Movie
from unittest import TestCase, main

class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Test", 2020, 5.5)
        self.movie2 = Movie("Test2", 2022, 4.5)

    def test_constructor(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(2020, self.movie.year)
        self.assertEqual(5.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_validator_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_validator_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1801
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_if_actor_exists(self):
        self.movie.add_actor("Pesho")
        expected = "Pesho is already added in the list of actors!"
        result = self.movie.add_actor("Pesho")
        self.assertEqual(expected, result)

    def test_add_actor_happy_case(self):
        self.movie.add_actor("Pesho")
        self.movie.add_actor("Gosho")
        self.movie.add_actor("Misho")
        self.assertEqual(["Pesho", "Gosho", "Misho"], self.movie.actors)

    def test_GT_magic_method(self):
        result = self.movie > self.movie2
        expected = '"Test" is better than "Test2"'
        self.assertEqual(expected, result)

    def test_GT_magic_method_reversed(self):
        result = self.movie < self.movie2
        expected = '"Test" is better than "Test2"'
        self.assertEqual(expected, result)

    def test_repr(self):
        self.movie.add_actor("Pesho")
        self.movie.add_actor("Gosho")
        self.movie.add_actor("Misho")

        expected = f"Name: Test\n" \
                   f"Year of Release: 2020\n" \
                   f"Rating: 5.50\n" \
                   f"Cast: Pesho, Gosho, Misho"

        self.assertEqual(expected, repr(self.movie))


if __name__ == "__main__":
    main()












