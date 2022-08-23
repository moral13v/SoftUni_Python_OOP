from unittest import TestCase, main

from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train("Test", 10)

    def test_constructor(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_if_full_raises(self):
        self.train.capacity = 1
        self.train.add("Pesho")
        with self.assertRaises(ValueError) as ex:
            self.train.add("Gosho")
        self.assertEqual("Train is full", str(ex.exception))
        self.assertEqual(self.train.TRAIN_FULL, str(ex.exception))

    def test_add_if_passenger_exists_raises(self):
        self.train.add("Pesho")
        with self.assertRaises(ValueError) as ex:
            self.train.add("Pesho")
        self.assertEqual("Passenger Pesho Exists", str(ex.exception))
        self.assertEqual(self.train.PASSENGER_EXISTS.format("Pesho"), str(ex.exception))

    def test_add_happy_case(self):
        result = self.train.add("Pesho")
        self.assertEqual("Added passenger Pesho", result)
        self.assertEqual(self.train.PASSENGER_ADD.format("Pesho"), result)
        self.assertEqual(["Pesho"], self.train.passengers)

        result = self.train.add("Gosho")
        self.assertEqual("Added passenger Gosho", result)
        self.assertEqual(self.train.PASSENGER_ADD.format("Gosho"), result)
        self.assertEqual(["Pesho", "Gosho"], self.train.passengers)

    def test_remove_passenger_not_found_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.train.remove("Misho")
        self.assertEqual("Passenger Not Found", str(ex.exception))
        self.assertEqual(self.train.PASSENGER_NOT_FOUND, str(ex.exception))

    def test_remove_happy_case(self):
        self.train.add("Pesho")
        self.train.add("Gosho")
        self.train.add("Misho")
        self.assertEqual(["Pesho", "Gosho", "Misho"], self.train.passengers)

        result = self.train.remove("Pesho")
        self.assertEqual("Removed Pesho", result)
        self.assertEqual(self.train.PASSENGER_REMOVED.format("Pesho"), result)

        self.assertEqual(["Gosho", "Misho"], self.train.passengers)


if __name__ == "__main__":
    main()