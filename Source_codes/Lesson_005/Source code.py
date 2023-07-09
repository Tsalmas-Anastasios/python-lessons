print('------------------------------------LESSON No 5------------------------------------')

print("Example 1")
a = 200
b = 30
if b > a:
    print('To b einai megalitero tou a')
elif b == a:
    print('b == a')
else:
    print('To a einai megalitero tou b')


# se mia grammh
if b > a:
    print('To b einai megalitero tou a')
elif b == a:
    print('a==b')
else:
    print('To a einai megalitero toy b')

# τριαδικός τελεστής
# mporei na exei apeiro plithos if....else.....
print('A') if a > b else print('B')


# for loop
for i in range(10):
    print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i = i + 1


# continue
for i in range(10):
   if i % 2 == 0:
        continue

# break
for i in range(10):
   if i % 2 == 0:
       break
   

# example
counter = 0
for i in range(1, 200):
    if i % 3 == 0 and i % 4 == 0:
        print(i)
        counter += 1
        if counter > 0:
            break
