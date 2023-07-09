import time

# get the start time
st = time.time()

nums = [1,2,3,4,5]
print(nums[0], end=" ")
print("\n")
for x in range(2):
    print(nums[1], end=" ")
print("\n")
for x in range(3):
    print(nums[2], end=" ")
print("\n")
for x in range(4):
    print(nums[3], end=" ")
print("\n")    
for x in range(5):
    print(nums[4], end=" ")
print("\n")

# get the end time
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


import time

# get the start time
st = time.time()

nums = [1,2,3,4,5]
print(nums[0], end=" ")
print("\n")
print(*[nums[1] for x in range(2)], end=" ")
print("\n")
print(*[nums[2] for x in range(3)], end=" ")
print("\n")
print(*[nums[3] for x in range(4)], end=" ")
print("\n")
print(*[nums[4] for x in range(5)], end=" ")
print("\n")

# get the end time
et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
