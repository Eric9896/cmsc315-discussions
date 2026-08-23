```python
"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

This program demonstrates object-oriented programming concepts
including inheritance, namespaces, shallow copying, and deep copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.

class ParentClass:
    # Class variable shared by all ParentClass objects.
    category = "Smart Home Device"

    def __init__(self, name, location):
        # Instance variables are unique to each object.
        self.name = name
        self.location = location

    def describe(self):
        """Return basic information about the smart-home device."""
        return f"{self.name} is located in the {self.location}."


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.

class ChildClass(ParentClass):
    # Class variable specific to the child class.
    device_type = "Security Device"

    def __init__(self, name, location, status, security_level):
        # Call the parent constructor to initialize inherited attributes.
        super().__init__(name, location)

        # Additional instance variables for the child class.
        self.status = status
        self.security_level = security_level

        # Nested mutable data used later to demonstrate copying.
        self.settings = {
            "alerts": ["motion", "door"],
            "authorized_users": ["Lewis"]
        }

    def describe(self):
        """Override the parent method with more detailed information."""
        return (
            f"{self.name} is a {self.device_type} located in the "
            f"{self.location}. Status: {self.status}, "
            f"Security Level: {self.security_level}."
        )

    def arm_device(self):
        """Change the device status to armed."""
        self.status = "Armed"
        return f"{self.name} has been armed."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    device1 = ChildClass(
        "Front Door Lock",
        "front entrance",
        "Locked",
        "High"
    )

    device2 = ChildClass(
        "Garage Camera",
        "garage",
        "Active",
        "Medium"
    )

    # Access the class variable through the class itself.
    print("Class variable through class:", ChildClass.device_type)

    # Access the same class variable through an object.
    print("Class variable through object:", device1.device_type)

    # Add a new attribute to only one object after creation.
    device1.battery_level = 95

    # Display each object's namespace.
    print("\nDevice 1 namespace:")
    print(device1.__dict__)

    print("\nDevice 2 namespace:")
    print(device2.__dict__)

    # Display information about the class namespace.
    print("\nChildClass namespace:")
    print(ChildClass.__dict__.keys())


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Security Camera",
        "backyard",
        "Active",
        "High"
    )

    # A shallow copy creates a new outer object, but nested mutable
    # objects such as the settings dictionary are still shared.
    shallow = copy(original)

    # A deep copy creates a new outer object and recursively copies
    # nested mutable objects as well.
    deep = deepcopy(original)

    print("Original settings before modification:")
    print(original.settings)

    print("\nShallow copy before modification:")
    print(shallow.settings)

    print("\nDeep copy before modification:")
    print(deep.settings)

    # Modify nested data in the original object.
    original.settings["alerts"].append("window")

    print("\nOriginal settings after modification:")
    print(original.settings)

    # The shallow copy shares the nested list, so it also reflects
    # the modification made to the original object.
    print("\nShallow copy after modification:")
    print(shallow.settings)

    # The deep copy has its own nested objects, so it remains unchanged.
    print("\nDeep copy after modification:")
    print(deep.settings)


# TODO 5:
# Complete the main function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test an object from the parent class.
    parent = ParentClass("Thermostat", "living room")
    print("\nParent object:")
    print(parent.describe())

    # Create and test an object from the child class.
    child = ChildClass(
        "Smart Lock",
        "front door",
        "Locked",
        "High"
    )

    print("\nChild object:")
    print(child.describe())

    # Demonstrate inheritance by calling the child-specific method.
    print(child.arm_device())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
```
