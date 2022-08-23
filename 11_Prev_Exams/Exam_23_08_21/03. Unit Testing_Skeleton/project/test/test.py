from unittest import TestCase, main
from project.library import Library


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.library = Library("Test")

    def test_constructor(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        self.library.add_book("Vazov", "Pod igoto")
        self.assertEqual({"Vazov": ["Pod igoto"]}, self.library.books_by_authors)
        self.library.add_book("Vazov", "Dyado Yoco gleda")
        self.assertEqual({"Vazov": ["Pod igoto", "Dyado Yoco gleda"]},
                         self.library.books_by_authors)
        self.library.add_book("Terry Pratchett", "Guards, guards")
        self.assertEqual({"Vazov": ["Pod igoto", "Dyado Yoco gleda"], "Terry Pratchett": ["Guards, guards"]},
                         self.library.books_by_authors)

    def test_add_reader(self):
        self.library.add_reader("Pesho")
        self.assertEqual({"Pesho": []}, self.library.readers)
        self.library.add_reader("Gosho")
        self.assertEqual({"Pesho": [], "Gosho": []}, self.library.readers)

    def test_add_existing_reader(self):
        self.library.add_reader("Pesho")
        self.assertEqual("Pesho is already registered in the Test library.",
                         self.library.add_reader("Pesho"))

    def test_rent_book_if_reader_not_found(self):
        result = self.library.rent_book("Gosho", "Terry Pratchett", "Guards, guards")
        expected = f"Gosho is not registered in the {self.library.name} Library."
        self.assertEqual(expected, result)

    def test_rent_book_if_author_not_found(self):
        self.library.add_reader("Gosho")
        result = self.library.rent_book("Gosho", "Terry Pratchett", "Guards, guards")
        expected = f"{self.library.name} Library does not have any Terry Pratchett's books."
        self.assertEqual(expected, result)

    def test_rent_book_if_book_not_found(self):
        self.library.add_reader("Gosho")
        self.library.add_book("Terry Pratchett", "Lords and Ladies")
        result = self.library.rent_book("Gosho", "Terry Pratchett", "Guards, guards")
        expected = f"""{self.library.name} Library does not have Terry Pratchett's "Guards, guards"."""
        self.assertEqual(expected, result)

    def test_rent_book_readers(self):
        self.library.add_reader("Gosho")
        self.library.add_book("Terry Pratchett", "Lords and Ladies")
        self.library.rent_book("Gosho", "Terry Pratchett", "Lords and Ladies")

        result = self.library.readers
        expected = {"Gosho": [{"Terry Pratchett": "Lords and Ladies"}]}
        self.assertEqual(expected, result)

    def test_rent_book_books(self):
        self.library.add_reader("Gosho")
        self.library.add_book("Terry Pratchett", "Lords and Ladies")
        self.library.rent_book("Gosho", "Terry Pratchett", "Lords and Ladies")

        result = self.library.books_by_authors
        expected = {"Terry Pratchett": []}
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
