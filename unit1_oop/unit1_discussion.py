"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
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
#
# Replace the pass statement with your implementation.

class SmartDevice:
    hub_name = "Lair" # The class variable that will be shared across all devices
    
    def __init__(self, name, room):
        self.name = name    # Instance variables
        self.room = room
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def status(self):
        """Return a legible line about this device."""
        state = "ON" if self.is_on else "OFF"
        return f"[{self.hub_name}] {self.name} ({self.room}) is {state}"

    def __str__(self):
        return self.status()


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SmartLights(SmartDevice):
    category = "Security" # New class variable

    def __init__(self, name, room, brightness=100, schedule=None):
        super().__init__(name, room)
        self.brightness = brightness  # New Instance Variable 
        self.schedule = schedule if schedule is not None else ["07:00", "22:00"] # Instance Variable 2

    def adjust_brightness(self, level):
        """New method to set the brightness level between 0 and 100."""
        self.brightness = max(0, min(100, level))
        print(f"{self.name} brightness set to {self.brightness}%")

    def status(self):
        """Overrides the parent method to include brightness and active schedule."""
        base_status = super().status()
        return f"{base_status} | Brightness: {self.brightness}% | Schedule: {self.schedule}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    light1 = SmartLights("Recessed Lights", "Trophy Room") # Obj. 1 
    light2 = SmartLights("Pathway Accent", "Driveway") # Obj. 2

    print(f"Class (SmartLights.category): {SmartLights.category}") # Access class variable
    print(f"Object (light1.category): {light1.category}")

    light1.motion_override = True
    print(f"\nAdd 'motion_override' to light1: {light1.motion_override}") # Adding a new attribute

    print("\nlight1 Instance Namespace (__dict__):")
    print(light1.__dict__)

    print("\nlight2 Instance Namespace (__dict__):") # Display each object's namespace using __dict__
    print(light2.__dict__)

    print("\nSmartLights Class Namespace (__dict__ attributes):") # Display information about the class namespace
    print([attr for attr in SmartLights.__dict__.keys() if not attr.startswith("__")])


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    
    original_light = SmartLights("Vault Warning Light", "Vault", brightness=90, schedule=["06:00", "18:00"]) # Create an object containing nested mutable data
    shallow_light = copy(original_light) # Create a shallow copy
    deep_light = deepcopy(original_light) # Create a deep copy

    print("Before modifying original schedule:")
    print(f"  Original: {original_light}")
    print(f"  Shallow:  {shallow_light}")
    print(f"  Deep:     {deep_light}")

    # SHALLOW COPY: Duplicates the outer object container, but shares memory references for nested mutable objects (schedule list). Modifying original affects shallow.
    # DEEP COPY: Recursively duplicates the outer object AND all nested mutable objects independently. Modifying original leaves deep copy untouched.
    original_light.schedule.append("23:59")

    print("\nAfter modifying original schedule:")
    print(f"  Original: {original_light}") # Modify the originals nested data
    print(f"  Shallow:  {shallow_light}")
    print(f"  Deep:     {deep_light}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    suits = SmartDevice("Suit Displays", "Armory Vault") # Parent object: Basic device in the Armory
    print(f"Initial State: {suits}")
    suits.turn_on()
    print(f"Maintenance Prep: {suits}")

    display_light = SmartLights("Equipment Spotlights", "Armory Vault", brightness=30)
    print(f"Initial State: {display_light}") # Child object & inheritance: Lighting for gear inspection
    
    display_light.turn_on()              # Inherited method from SmartDevice
    display_light.adjust_brightness(95) # Child method
    print(f"Inspection Mode: {display_light}")

    # 3. Required demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()