PATH = "day15/data.txt"
class Ingredient:
    def __init__(self, args, name):
        self.props = args; self.name = name
    def __repr__(self):
        return ("{" + self.name + ": [" + ', '.join([str(x) for x in self.props]) + "]}")
def get_all_distributions(buckets, n):
    if buckets == 1:
        return [[n]]
    res = []
    for i in range(n + 1):
        for x in get_all_distributions(buckets - 1, n - i):
            res.append([i] + x)
    return res
ingreds = [Ingredient(args, name) for args, name in zip([[int(y.split(' ')[-1]) for y in x[:-1].split(',')] for x in open(PATH).readlines()],[x.split(':')[0] for x in open(PATH).readlines()])]
tsps = 100
prods = []
for recipe in get_all_distributions(len(ingreds),tsps):
    props = [0] * 4
    for i, ingred in enumerate(ingreds):
        for j, prop in enumerate(props):
            props[j] += recipe[i] * ingred.props[j]
    prod = 1
    for i in props:
        prod *= i if i > 0 else 0
    prods.append(prod)
print(max(prods))
