from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(fuel=100, horse_power=200)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_insufficient_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive(self):
        self.vehicle.drive(10)
        # 10 km * 1.25 l/km = 12.5 l
        # 100 l - 12.5 l = 87.5 l
        self.assertEqual(87.5, self.vehicle.fuel)
        self.vehicle.drive(10)
        # 10 km * 1.25 l/km = 12.5 l
        # 87.5 l - 12.5 l = 75 l
        self.assertEqual(75, self.vehicle.fuel)

    def test_refuel_too_much_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(50)
        self.assertEqual(100, self.vehicle.fuel)

    def test_vehicle_to_string(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        result = str(self.vehicle)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()