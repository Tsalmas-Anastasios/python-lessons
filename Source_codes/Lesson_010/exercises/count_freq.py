beginner_string = input('Give a string to count: ')

freq_dict = {}
for char in beginner_string:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

sorted_dict = {k:v for k,v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)}

for key, value in sorted_dict.items():
    print(f" {key} {value}", end="")