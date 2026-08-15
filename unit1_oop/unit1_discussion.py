"""
Unit 1 Discussion: Python OOP, Namespaces, and Copying

This program models smart-home devices while demonstrating inheritance,
class and instance namespaces, shallow copying, deep copying, and validation.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
# Requirements: include a class variable, at least two instance variables,
# a constructor, and a method that returns or displays object information.
class SmartDevice:
    """Represent a general device connected to a smart-home system."""

    platform = "HomeLink"

    def __init__(self, name, room):
        if not str(name).strip():
            raise ValueError("Device name cannot be empty.")
        if not str(room).strip():
            raise ValueError("Room name cannot be empty.")
        self.name = str(name).strip()
        self.room = str(room).strip()
        self.is_online = False

    def connect(self):
        """Connect the device to the smart-home platform."""
        self.is_online = True
        return f"{self.name} connected to {self.platform}."

    def device_info(self):
        """Return a readable description of the device."""
        status = "online" if self.is_online else "offline"
        return f"{self.name} is in the {self.room} and is {status}."


# TODO 2:
# Create a child class that inherits from the parent class.
# Requirements: use inheritance; add a class variable, at least two instance
# variables, and a new method; and override a parent method.
class SmartThermostat(SmartDevice):
    """Represent a thermostat with temperature controls and schedules."""

    device_type = "Thermostat"
    MIN_TEMPERATURE = 50
    MAX_TEMPERATURE = 90

    def __init__(self, name, room, temperature, schedule=None):
        super().__init__(name, room)
        self.temperature = self._validate_temperature(temperature)
        self.schedule = deepcopy(schedule) if schedule is not None else []

    @classmethod
    def _validate_temperature(cls, temperature):
        """Return a valid numeric temperature or raise a clear error."""
        if isinstance(temperature, bool) or not isinstance(temperature, (int, float)):
            raise TypeError("Temperature must be a number.")
        if not cls.MIN_TEMPERATURE <= temperature <= cls.MAX_TEMPERATURE:
            raise ValueError(
                f"Temperature must be between {cls.MIN_TEMPERATURE} and "
                f"{cls.MAX_TEMPERATURE} degrees."
            )
        return temperature

    def set_temperature(self, temperature):
        """Change the target temperature after validating the input."""
        self.temperature = self._validate_temperature(temperature)
        return f"{self.name} was set to {self.temperature} degrees."

    def add_schedule(self, time, temperature):
        """Add a validated schedule entry to the thermostat."""
        if not str(time).strip():
            raise ValueError("Schedule time cannot be empty.")
        self.schedule.append(
            {
                "time": str(time).strip(),
                "temperature": self._validate_temperature(temperature),
            }
        )

    def device_info(self):
        """Override the parent description with thermostat information."""
        status = "online" if self.is_online else "offline"
        return (
            f"{self.name} is a {self.device_type.lower()} in the {self.room}, "
            f"is {status}, and is set to {self.temperature} degrees."
        )

    def __str__(self):
        return self.device_info()

    def __repr__(self):
        return (
            f"SmartThermostat(name={self.name!r}, room={self.room!r}, "
            f"temperature={self.temperature!r}, schedule={self.schedule!r})"
        )


# TODO 3:
# Demonstrate class and instance namespaces by creating two child objects,
# accessing a class variable through the class and an object, adding an
# attribute to only one object, and displaying class and instance namespaces.
def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    upstairs = SmartThermostat("Upstairs Thermostat", "Hallway", 70)
    downstairs = SmartThermostat("Downstairs Thermostat", "Living Room", 72)

    print("Class variable through class:", SmartThermostat.platform)
    print("Class variable through object:", upstairs.platform)

    # This dynamically created attribute belongs only to upstairs.
    upstairs.firmware_version = "2.1.0"
    print("Upstairs instance namespace:", upstairs.__dict__)
    print("Downstairs instance namespace:", downstairs.__dict__)
    print(
        "Downstairs has firmware_version:",
        hasattr(downstairs, "firmware_version"),
    )
    print(
        "Selected class namespace values:",
        {
            "platform": SmartThermostat.platform,
            "device_type": SmartThermostat.device_type,
            "minimum": SmartThermostat.MIN_TEMPERATURE,
            "maximum": SmartThermostat.MAX_TEMPERATURE,
        },
    )


# TODO 4:
# Demonstrate shallow and deep copying with nested mutable data by modifying
# the original and displaying the original, shallow copy, and deep copy.
def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = SmartThermostat(
        "Main Thermostat",
        "Living Room",
        70,
        [{"time": "06:30", "temperature": 68}],
    )
    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy shares the nested schedule. A deep copy duplicates it.
    original.schedule[0]["temperature"] = 72
    print("Original schedule:", original.schedule)
    print("Shallow-copy schedule:", shallow_copy.schedule)
    print("Deep-copy schedule:", deep_copy.schedule)
    print(
        "Original and shallow copy share schedule:",
        original.schedule is shallow_copy.schedule,
    )
    print(
        "Original and deep copy share schedule:",
        original.schedule is deep_copy.schedule,
    )


# TODO 5:
# Create parent and child objects, demonstrate inheritance, and call the
# namespace and copying demonstrations.
def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    security_camera = SmartDevice("Front Door Camera", "Entryway")
    print(security_camera.device_info())
    print(security_camera.connect())
    print(security_camera.device_info())

    print("\n=== Child Object and Inheritance ===")
    thermostat = SmartThermostat("Primary Thermostat", "Living Room", 70)
    print(thermostat.connect())  # Inherited from SmartDevice.
    print(thermostat.device_info())  # Overridden in SmartThermostat.
    print(thermostat.set_temperature(72))
    thermostat.add_schedule("22:00", 66)
    print("Updated schedule:", thermostat.schedule)
    print("Object representation:", repr(thermostat))

    print("\n=== Student Extension and Edge-Case Test ===")
    try:
        thermostat.set_temperature(120)
    except ValueError as error:
        print("Invalid setting handled safely:", error)

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
