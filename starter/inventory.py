"""
Command-line inventory tracker -- you choose the scenario.

See ../PROJECT_OVERVIEW.md to pick your stakeholder and data file. Design your own
class for one inventory item, based on what *your* stakeholder needs.
There's no single right set of attributes, and that's on purpose.

Run it from your repo's top folder (not from inside this folder):
    python3 starter/inventory.py
Before your final push you'll rename this folder to analysis/.
"""
import json

CATEGORY_THRESHOLDS = {
    "PPE": 20,
    "Wound Care": 15,
    "Medication": 15,
    "Equipment": 10,
}

class HealthcareSupply :

    """Represents a medical supply item, its current stock, and its category."""
    
    #TODO: rename this class to something that fits your scenario, and
    #write a real docstring. What does one of these represent? At minimum
    #you'll need a name and a quantity. Add what your stakeholder asked
    #for, not more and not less.


    def __init__(self, name, quantity, category):
        """Store name, quantity, and category for a supply item."""
        # TODO: add your own parameters (self, plus each attribute you're
        # tracking) and store each one as self.whatever = whatever.

        self.name = name
        self.quantity = quantity
        self.category = category

# TODO: return True or False. Your stakeholder didn't say what
        # "low" means, so decide, and write down the assumption in
        # REFLECTION.md's "Assumptions" section.
        
    def is_low_stock(self):
       """Return True when item quantity is below its category threshold."""    
       limit = CATEGORY_THRESHOLDS.get(self.category, 10)
       return self.quantity < limit

    def stock_status_message(self):
        """Return a readable stock alert or availability message for this item."""
        limit = CATEGORY_THRESHOLDS.get(self.category, 10)
        if self.is_low_stock():
            return (
                f"Low stock: only {self.quantity} {self.name} available "
                f"(threshold: {limit})"
            )
        return f"{self.quantity} {self.name} available"
        
# Testing print delete when finished
          
a = HealthcareSupply("Face Shields", 5, "PPE")
b = HealthcareSupply("Pulse Oximeters", 30, "Equipment")
print(a.is_low_stock())
print(b.is_low_stock())

test_low = HealthcareSupply("Gloves", 5, "PPE")
test_ok = HealthcareSupply("Stethoscope", 20, "Equipment")
print(test_low.stock_status_message())
print(test_ok.stock_status_message())


def read_batch_file(filepath):
    """Read the batch file and return its lines unchanged"""
    lines = []
    with open(filepath, "r", encoding="utf-8") as f:
       for line in f.read().splitlines():
               lines.append(line) 
    return lines

    #Read the batch file at `filepath` and return a list of its lines
    #(strings), unchanged. Deciding whether a line is usable happens in
    #validate_line(), not here. Use this docstring as the model for the
    #ones you write below: 
    # TODO: implement
    


def validate_line(line):
    """TODO: write your own docstring. What makes an ADD, REMOVE, or
    SEARCH line valid? What do you return for a valid line, and what for
    an invalid one?"""

    """Return a parsed tuple for valid ADD, REMOVE, or SEARCH lines, or print a skip reason and return None."""
    # TODO: implement. One choice worth making on purpose: a quantity can
    # be present but not a number ("five"). Wrap int(quantity) in a
    # try/except ValueError. That asks Python "did this work?" instead
    # of trying to predict every way it could fail.
    

    if not line or not line.strip():
        print("SKIPPED - blank line")
        return None

    parts = line.split(",")
    command = parts[0].strip().upper()

    # ADD command

    if command == "ADD":
        if len(parts) != 4:
            print(f"SKIPPED - ADD requires 4 fields: {line}")
            return None
        name = parts[1].strip()
        category = parts[3].strip()
        if not name or not category:
            print(f"SKIPPED - missing supply name or category: {line}")
            return None
        try:
            quantity = int(parts[2].strip())
        except ValueError:
            print(f"SKIPPED - quantity is not whole number: {line}")
            return None
        if quantity <= 0:
            print(f"SKIPPED - ADD quantity must be positive: {line}")
            return None
        return ("ADD", name, quantity, category)

    # REMOVE commad
    if command == "REMOVE":
        if len(parts) != 3:
            print(f"SKIPPED - REMOVE requires 3 fields: {line}")
            return None
        name = parts[1].strip()
        if not name:
            print(f"SKIPPED - missing supply name: {line}")
            return None
        try:
            quantity = int(parts[2].strip())
        except ValueError:
            print(f"SKIPPED - quantity is not a whole number: {line}")
            return None
        return ("REMOVE", name, quantity)
    
     # SEARCH command
    if command == "SEARCH":
        if len(parts) != 2 or not parts[1].strip():
            print(f"SKIPPED - SEARCH requires a supply name: {line}")
            return None
        return("SEARCH", parts[1].strip())

    print(f"SKIPPED - unknown or misspelled command: {line}")
    return None
    

def process_transactions(lines):
    """Apply valid transaction lines to an inventory dictionary and return it."""
    # TODO: implement. Loop over the lines, apply each valid one to your
    # collection of items, and print a specific message for each line
    # you skip. Return the collection at the end. The full inventory
    # printout is print_summary's job, not this function's.
    

    items = {}
    for line in lines:
        parsed =



def find_item(items, name):
    """TODO: write your own docstring."""
    # TODO: implement
    pass


def export_to_json(items, filepath="inventory.json"):
    """TODO: write your own docstring. json.dump can't write your objects
    directly, so turn each one into a dict first."""
    # TODO: implement
    pass


def print_summary(items):
    """TODO: write your own docstring."""
    # TODO: implement. This one only prints, so it doesn't need to return
    # anything.
    pass


# TODO: point this at the data file for the scenario you chose.
lines = read_batch_file("data/healthcare_transactions.txt")
items = process_transactions(lines)
print_summary(items)
export_to_json(items)
