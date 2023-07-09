# μπορούμε να ανοίξουμε ένα αρχείο και να προσθέσουμε καινούριο
# περιεχόμενο σε αυτό. Χρησιμοποιούμε το mode 'a' κατά το άνοιγμα
# του αρχείου για να μπορέσουμε να προσθέσουμε περιεχόμενο.

f = open('myfile.txt', 'a')             # open file 'myfile.txt'

f.write('Τελευταία γραμμή')         # add the text in the end of the file
f.close()               # close the file

f = open('myfile.txt', 'r')             # open the file to read its content
text = f.read()             # read the first line
print(text)                 # print the readed line
f.close()                   # close the opened file