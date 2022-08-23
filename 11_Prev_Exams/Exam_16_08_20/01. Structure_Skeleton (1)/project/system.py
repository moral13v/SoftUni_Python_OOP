from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


def find_item_by_name(item_name, collection):
    for item in collection:
        if item.name == item_name:
            return item


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = find_item_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = find_item_by_name(hardware_name, System._hardware)
        if not hardware:
            return "Hardware does not exist"
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = find_item_by_name(hardware_name, System._hardware)
        software = find_item_by_name(software_name, System._software)
        if hardware and software:
            hardware.uninstall(software)
            System._software.remove(software)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = f'''System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum([software.memory_consumption for software in System._software])} / {sum([hardware.memory for hardware in System._hardware])}
Total Capacity Taken: {sum([software.capacity_consumption for software in System._software])} / {sum([hardware.capacity for hardware in System._hardware])}
'''
        return result.strip()

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:

            light_sw_counter = 0
            express_sw_counter = 0
            for software in hardware.software_components:
                if software.software_type == "Light":
                    light_sw_counter += 1
                elif software.software_type == "Express":
                    express_sw_counter += 1

            result += f'''Hardware Component - {hardware.name}
Express Software Components: {express_sw_counter}
Light Software Components: {light_sw_counter}
Memory Usage: {sum([software.memory_consumption for software in hardware.software_components])} / {hardware.memory}
Capacity Usage: {sum([software.capacity_consumption for software in hardware.software_components])} / {hardware.capacity}
Type: {hardware.hardware_type}
Software Components: {', '.join([software.name for software in hardware.software_components] if hardware.software_components else "None")}
'''

        return result.strip()








