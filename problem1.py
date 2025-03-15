def is_multisubset(a,b):
     try:
          for key in a:
               if key not in b:
                    return False
               if a[key] > b[key]:
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


print(read_parts_list('collection1.txt'))