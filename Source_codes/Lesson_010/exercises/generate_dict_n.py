number = int(input("Enter an integer number as input: "))

output_dict = {}
for i in range(1, number + 1):
    for j in range(1, i + 1):
        output_dict[j] = j ** 2
    
    print(output_dict)


print('\nThe following dicts generated with dict comprehension')
for i in range(1, number + 1):
    output_dict = {var:var ** 2 for var in range(1, i + 1)}
    print(output_dict)