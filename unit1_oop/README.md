# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

I implemented a smart-home device system that demonstrated object-oriented programming, inheritance, namespaces, shallow copying, deep copying, special methods, and error handling. The program was contained in `unit1_discussion.py`.

## Design and Implementation

I created `SmartDevice` as the parent class. It stored a device's name, room, and connection status. Its `platform` class variable represented information shared by all smart devices. Its methods connected a device and returned information about it.

I created `SmartThermostat` as a child of `SmartDevice`. It inherited the parent's attributes and `connect()` method while adding a temperature, a nested schedule, validation, and thermostat-specific behavior. I overrode `device_info()` and implemented `__str__()` and `__repr__()` as special methods. These additions encapsulated thermostat behavior inside the class instead of exposing implementation details throughout the program.

## Namespaces

I demonstrated namespaces by creating two thermostat objects. I accessed `platform` through both the class and an object. I then added `firmware_version` to only one object and printed both instance dictionaries with `__dict__`. The output showed that the new attribute existed in only that object's namespace. I also printed selected class-level values to distinguish shared class data from instance-specific data.

## Shallow and Deep Copying

I created a thermostat containing a nested schedule represented by a list of dictionaries. I made a shallow copy with `copy()` and a deep copy with `deepcopy()`. After I changed a nested temperature in the original schedule, the shallow copy showed the same change because both objects referenced the same nested list. The deep copy did not change because its nested data had been copied independently.

## Error Handling and Edge Case

As my student-created extension, I added temperature validation, schedule management, and readable `__str__()` and `__repr__()` methods. The thermostat accepted only numeric temperatures between 50 and 90 degrees. I tested a boundary-related edge case by attempting to set the temperature to 120 degrees. The program raised and caught a `ValueError`, displayed a helpful message, and continued running instead of failing.

## Real-World Application

This design could support a larger smart-home application. Additional devices, such as smart locks, lights, or security cameras, could inherit common connection behavior from `SmartDevice` while implementing their own attributes and methods. Validation could prevent unsafe or invalid settings from affecting the rest of the system.

## Reflection

While completing this assignment, I learned how inheritance, namespaces, and object copying influence program organization and behavior. The most challenging concept was understanding why changes to nested data appeared in a shallow copy but not in a deep copy. Comparing the schedules and object identities helped me see that a shallow copy creates a new outer object while preserving references to nested objects. A deep copy recursively creates independent nested data.

Compared with procedural programming, object-oriented programming requires additional planning and may create memory and design overhead because developers must define classes and manage objects. However, OOP improves maintainability and reusability by combining related data and behaviors into modular components. For practical application development, this structure makes it easier to test, update, and extend one component without rewriting the entire program. I could apply these concepts in future networking, cloud, or cybersecurity software by creating reusable classes for devices, users, alerts, and connections. Encapsulation and validation would also help prevent one invalid operation from causing a larger system failure.

## Running the Program

Use Python 3 from the `unit1_oop` directory:

```bash
python unit1_discussion.py
```

The program prints the parent and child demonstrations, the safely handled invalid-temperature test, the class and instance namespaces, and the shallow/deep-copy comparison.
