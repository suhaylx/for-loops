for item in {1,2,3,4,6}:
  for values in {'a', 'b','c'}:
    print(item, values)
user = {
'name' : 'Suhaylx',
'age' : 18,
'can_swim' : False
 }
for dictionary_items in user.values():
  print(dictionary_items)
for dict_items in user.items():
  print(dict_items)


for keys, item_s in user.items():
  print(keys,item_s)

#There is still other ways to iterate
for example_value in user.items():
  dict_keys, dict_values = example_value
#as example_value value is typle we assign values to another two value
  print(dict_keys, dict_values)