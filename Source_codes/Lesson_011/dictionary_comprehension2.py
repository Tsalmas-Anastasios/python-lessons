import time

# get the start time
st = time.time()


input_list = [1, 2, 3, 4, 5, 6, 7]
output_dict = {} 
# Χρήση βρόχου for για δημιουργία του λεξικού εξόδου
for var in input_list:
    if var % 2 != 0:
        output_dict[var] = var**3
print(output_dict)

# get the end time
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

# get the start time
st = time.time()

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0} 
print(dict_using_comp)

# get the end time
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
