PATH = "4/data.txt"
import hashlib
def valid(s):
    return s[:5] == ''.join(['0'] * 5)
key = open(PATH).readline()
num = 1
while True:
    if valid(hashlib.md5((key + str(num)).encode()).hexdigest()):
        break
    num += 1
print(num)
