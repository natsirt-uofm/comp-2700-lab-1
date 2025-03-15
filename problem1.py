def is_multisubset(a,b):
     try:
          for key in a:
               if key not in b or a[key] > b[key]:
                    return False
          return True
     except KeyError:
          return False   
     

def read_parts_list(filename):
     data = {}
     try:
          with open(filename) as file:
               for line in file:
                    (key, val) = line.split()
                    val = int(val)

                    data[key] = data.get(key, 0) + val
     except FileNotFoundError:
          print(f"File {file} not found")
     except ValueError:
          print(f"Invalid data format in {line}")
     return data

def get_missing_parts(goal, inventory):
     parts_needed = {}
     if is_multisubset(goal, inventory) is True:
          return parts_needed
     for part in goal:
          required_qty = goal[part]
          available_qty = inventory.get(part, 0)
          if available_qty < required_qty:
               parts_needed[part] = required_qty - available_qty
     return parts_needed


          


print(read_parts_list('collection1.txt'))