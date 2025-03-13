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
     

a = {'a': 2, 'b': 1}
b = {'a': 3, 'b': 1, "c": 5}

print(is_multisubset(a, b))

a = {'a': 9, 'b': 7}
print(is_multisubset(a, b))
b = {}
print(is_multisubset(a,b))