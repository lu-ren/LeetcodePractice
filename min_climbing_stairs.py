def min_climbing_stairs(costs):
    r = []

    for i in range(len(costs)):
        v = min(r[i - 1], r[i - 2]) + costs[i] if i > 1 else costs[i]
        r.append(v)
    if len(r) > 1:
        return min(r[-1], r[-2])
    return r[-1]

print (min_climbing_stairs([10, 15, 20]))
print (min_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
