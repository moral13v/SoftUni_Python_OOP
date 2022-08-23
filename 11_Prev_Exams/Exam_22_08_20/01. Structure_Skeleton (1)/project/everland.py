from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses
            total_consumption += room.room_cost
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        output = ""
        for room in self.rooms:
            total_consumption = room.expenses + room.room_cost
            new_budget = room.budget - (room.expenses + room.room_cost)
            if new_budget >= 0:
                room.budget = new_budget
                output += f"{room.family_name} paid {total_consumption:.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                output += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return output.strip()

    def status(self):
        output = f"Total population: {sum([room.members_count for room in self.rooms])}\n"
        for room in self.rooms:
            output += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                child_counter = 0
                for child in room.children:
                    child_counter += 1
                    output += f"--- Child {child_counter} monthly cost: {child.get_monthly_expense():.2f}$\n"
            output += f"--- Appliances monthly cost: {sum([ap.get_monthly_expense() for ap in room.appliances]):.2f}$\n"
        return output.strip()
