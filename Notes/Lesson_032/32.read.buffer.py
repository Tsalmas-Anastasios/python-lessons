'''
Άνοιγμα του αρχείου source.txt (βρίσκεται στον φάκελο της Python,
αν όχι, φτιάξτε και τοποθετήστε το εκεί)
και εκτύπωσή του ανά 10 χαρακτήρες (1 byte = i χαρακτήρας)
'''

def read_file_with_buffer(file_path, buffer_size):
    with open(file_path, 'r') as file:
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            print(data)

file_path = 'source.txt'
buffer_size = 10
read_file_with_buffer(file_path, buffer_size)
