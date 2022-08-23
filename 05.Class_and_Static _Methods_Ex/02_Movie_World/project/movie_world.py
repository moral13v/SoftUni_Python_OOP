from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd in customer.rented_dvds:
                            return f"{customer.name} has already rented {dvd.name}"
                        elif dvd.is_rented:
                            return "DVD is already rented"
                        elif dvd.age_restriction > customer.age:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        dvd.is_rented = True
                        customer.rented_dvds.append(dvd)
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd not in customer.rented_dvds:
                            return f"{customer.name} does not have that DVD"
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += str(customer) + '\n'
        for dvd in self.dvds:
            result += str(dvd) + '\n'
        return result



