Initialize with Parent[i] = i

function find(x):
  if Parent[x] != x:
    return find(Parent[x])
  else:
    return x

function Union(x, y):
  Parent[find(y)] = find(x)


# Leetcode 684 Redundant Connection

  
