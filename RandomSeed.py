import random
import numpy as np
np.__version__

random.seed(0) #Initialize random number generator, seed does not really matter, but does change the first initialized random number
print(random.randint(0, 1000))
r = random.randint(0, 100)
s = np.random.randint(50, size = 6)
print(r)
print(s)