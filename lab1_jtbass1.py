# Problem 1 
def is_multisubset(a, b):
    """
    Checks if dictionary `a` is a multisubset of dictionary `b`. 
    A multisubset means all keys in `a` exist in `b` with at least the same count.
    """
    for key in a:
        if key not in b or a[key] > b[key]:
            return False
    return True  

# Problem 2 
def read_parts_list(filename):
    """
    Reads a parts list from a file and returns a dictionary mapping part names to their quantities.
    If a part appears multiple times, its quantity is summed.
    """
    data = {}
    try:
        with open(filename) as file:
            for line in file:
                key, val = line.split()
                data[key] = data.get(key, 0) + int(val)  # Aggregate quantities
    except FileNotFoundError:
        print(f"File {filename} not found")  # Handle missing file error
    except ValueError:
        print(f"Invalid data format in {line}")  # Handle incorrect formatting
    return data  

def get_missing_parts(goal, inventory):
    """
    Compares `goal` (desired parts list) with `inventory` and returns a dictionary of 
    missing parts and their required quantities.
    """
    if is_multisubset(goal, inventory):
        return {}  # No missing parts if goal is already met
    
    # Compute missing quantities
    return {part: goal[part] - inventory.get(part, 0) for part in goal if inventory.get(part, 0) < goal[part]}

