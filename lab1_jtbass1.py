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

# Problem 3
def get_missing_parts(goal, inventory):
    """
    Compares `goal` (desired parts list) with `inventory` and returns a dictionary of 
    missing parts and their required quantities.
    """
    if is_multisubset(goal, inventory):
        return {}  # No missing parts if goal is already met
    
    # Compute missing quantities
    return {part: goal[part] - inventory.get(part, 0) for part in goal if inventory.get(part, 0) < goal[part]}

# Problem 4

# Read parts lists from files
parts1 = read_parts_list('collection1.txt')
parts2 = read_parts_list('collection2.txt')
parts3 = read_parts_list('collection3.txt')
parts4 = read_parts_list('collection4.txt')
parts5 = read_parts_list('collection5.txt')
parts6 = read_parts_list('collection6.txt')


print(is_multisubset(parts1, parts2))
print(is_multisubset(parts1, parts3))
print(is_multisubset(parts2, parts3))
print(is_multisubset(parts3, parts3))
print(is_multisubset(parts3, parts1))
print(is_multisubset(parts3, parts2))
print(is_multisubset(parts6, parts4))
print(is_multisubset(parts6, parts5))

print(get_missing_parts(parts3, parts3))
print(get_missing_parts(parts6, parts4))
print(get_missing_parts(parts6, parts5))
