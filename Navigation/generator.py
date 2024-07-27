import string
string.ascii_letters
import random
random.choice(string.ascii_letters)

f = open("C:\\Users\EJMarine2024\Desktop\LBC2\\navigation\\flag.txt", 'w')

i = 0
while i < 1000000:
    f.write(random.choice(string.ascii_letters))
    i = i + 1