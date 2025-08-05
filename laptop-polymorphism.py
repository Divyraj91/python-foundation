# Base class
class Laptop:
    def features(self):
        return "Basic Laptop features"

# Single Inheritance
class Dell(Laptop):
    def features(self):
        return "Dell Laptop with Windows 11"

# Multilevel Inheritance
class DellGaming(Dell):
    def features(self):
        return "Dell Gaming Laptop with NVIDIA GPU"

# Hierarchical Inheritance
class HP(Laptop):
    def features(self):
        return "HP Laptop with Long Battery Life"

class Lenovo(Laptop):
    def features(self):
        return "Lenovo Laptop with Lightweight Design"

# Multiple Inheritance
class TouchScreen:
    def features(self):
        return "Touch screen enabled"

class HPConvertible(HP, TouchScreen):  # Multiple inheritance
    def features(self):
        return "HP Convertible Laptop with Touch Screen"

# Hybrid Inheritance
class SmartLaptop(Dell, TouchScreen):
    def features(self):
        return "Smart Laptop with Dell performance and Touch support"

# Function using polymorphism
def show_features(obj):
    print(f"{obj.__class__.__name__} features: {obj.features()}")

# Function to detect inheritance type
def get_inheritance_type(obj):
    bases = [cls.__name__ for cls in obj.__class__.__bases__]
    name = obj.__class__.__name__

    if name == "Dell" and "Laptop" in bases:
        return "Single Inheritance"
    elif name == "DellGaming" and "Dell" in bases:
        return "Multilevel Inheritance"
    elif name in ["HP", "Lenovo"] and "Laptop" in bases:
        return "Hierarchical Inheritance"
    elif name == "HPConvertible" and "HP" in bases and "TouchScreen" in bases:
        return "Multiple Inheritance"
    elif name == "SmartLaptop" and "Dell" in bases and "TouchScreen" in bases:
        return "Hybrid Inheritance"
    elif name == "Laptop":
        return "Base Class (No Inheritance)"
    else:
        return "Unknown Inheritance"

# List of objects from different inheritance types
objects = [Laptop(), Dell(), DellGaming(), HP(), Lenovo(), HPConvertible(), SmartLaptop()]

# Final output with inheritance type
for obj in objects:
    show_features(obj)
    print(f"Type of Inheritance: {get_inheritance_type(obj)}\n")
