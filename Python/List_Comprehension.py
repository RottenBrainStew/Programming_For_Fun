squares = []
for x in range(11):
    squares.append(x**2)
print(squares)

sq = [x**2 for x in range(11)] #simplified expression for the above statement without having to overwrite x
print(sq)
