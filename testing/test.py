import itertools

#corners = [(1,1), (1, 12), (32, 12), (32, 1)]
corners = [(1,1), (1, 12)]
ll = [x for x in itertools.permutations(corners)]
for l in ll:
    print(list(l))