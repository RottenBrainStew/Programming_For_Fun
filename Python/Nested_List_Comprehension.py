#List comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original layout of multi-dimensional matrix: {}".format(matrix))
newL = []
nextL = []
for i in range(len(matrix)):
    newL.append([row[i] for row in matrix])

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for element in mat:
    for index in element:
        x = index + 1
        #element.append(x) Creates an infinite loop
    element.append(x)
print(list(zip(*matrix)))
print(mat)
print("This is a way to copy a multi-dimensional list to an empty list called {} with the rows and columns being inverted.".format(newL))
