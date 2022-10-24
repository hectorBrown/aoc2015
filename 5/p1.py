PATH = "5/data.txt"
vowels = ['a', 'e', 'i', 'o', 'u']
banned = ["ab", "cd", "pq", "xy"]
def nice(s):
    if not sum([int(c in vowels) for c in s]) >= 3:
        return False
    double = False
    last = s[0]
    for c in s[1:]:
        if c == last:
            double = True
        last = c
    if not double:
        return False
    if any([b in s for b in banned]):
        return False
    return True
data = [x[:-1] for x in open(PATH).readlines()]
print(sum([int(nice(x)) for x in data]))
