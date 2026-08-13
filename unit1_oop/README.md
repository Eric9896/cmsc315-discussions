# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This program modeled a small smart home system built around a central hub called "Lair." A parent class represented a generic connected device, and a child class extended it to model smart lights with brightness control and a schedule. The program demonstrated inheritance, class and instance namespaces, and the difference between shallow and deep copying.

## Implementation

### 1. Parent Class: SmartDevice

The `SmartDevice` class was created with a class variable, `hub_name`, shared across all devices on the hub. The constructor initialized three instance variables: `name`, `room`, and `is_on`. A `status()` method returned a readable one-line summary of the device, and a `turn_on()` method changed the device state. A `__str__` special method was added that delegated to `status()`, so any device printed cleanly with `print()`.

### 2. Child Class and Inheritance: SmartLights

The `SmartLights` class inherited from `SmartDevice`. It added its own class variable, `category`, and two new instance variables: `brightness` and `schedule`. The constructor called `super().__init__()` to initialize the inherited attributes instead of repeating that logic. The `schedule` parameter defaulted to `None` and was assigned inside the constructor to avoid Python's mutable default argument problem. A student-created method, `adjust_brightness()`, clamped the brightness between 0 and 100. The `status()` method was overridden to call the parent version through `super()` and append the brightness and schedule information.

### 3. Class and Instance Namespaces

The `demonstrate_namespaces()` function created two `SmartLights` objects. The `category` class variable was accessed through the class itself and through an object, showing both lookups reached the same value. A new attribute, `motion_override`, was added to only the first object after creation. Printing each object's `__dict__` showed that the new attribute existed only on the first object, and that the class variables appeared in neither instance namespace because they live on the class. The class namespace was also displayed to show where `category` and the methods are actually stored.

### 4. Shallow and Deep Copying

The `demonstrate_copying()` function created a `SmartLights` object whose `schedule` attribute was a mutable list. A shallow copy was created with `copy()` and a deep copy with `deepcopy()`. After a new time was added to the original object's schedule, the shallow copy reflected the change as well, because both objects were still referencing the same underlying list. The deep copy kept its original schedule because `deepcopy()` duplicated the nested data instead of sharing references to it.

### 5. Main Function

The `main()` function created one parent object and one child object. It called an inherited method, the new child method, and the overridden `status()` method to demonstrate inheritance in action, then ran the namespace and copying demonstration functions.

## Reflection

This assignment helped reinforce how Python actually interprets and organizes data into one small program. My biggest takeaway was seeing where the attributes live: class variables sat in the class namespace and never appeared in an object's `__dict__`, while instance variables belonged to each object individually. My main challenges were small (but painful) syntax mistakes. I structured a conditional expression wrong and capitalized `Return`, and both broke the program until I slowed down and read what Python was telling me. Seeing the copy demonstration at work was probably the most helpful part. After appending a time to the original light's schedule, the shallow copy ended up reflecting the change too, since both objects shared the same list, while the deep copy kept its own independent version.

This is a great concept. Compared to procedural programming, where a script is mostly a sequence of functions run in order, OOP bundles data and behavior together. It's tedious to plan and write it out at the same time but it pays off in maintainability and reusability: a change to `SmartDevice` automatically applies to every device that inherits from it, and adding a new device type means writing a small subclass instead of copying code. Life is always easier when you can build off of what's already in place, so I plan on using this method going forward.

## AI Attribution

I used Claude (Anthropic) in this unit for concept explanations, a separate reference example, help setting up my GitHub repository, and copy-editing my written documentation. All TODO implementations in `unit1_discussion.py` are my own work.
