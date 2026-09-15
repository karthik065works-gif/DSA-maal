n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(len(arr)):
  arr.append(int(input())) 
print(arr) 
def brute_force(arr,k):
  cnt = 0 
  for i in range(len(arr)):
    for j in range(i + 1,len(arr)):
      if abs(arr[i] - arr[j]) == k:
        cnt += 1 
  return cnt 
## optimisation 
from collections import defaultdict 
def optimisation(arr,k):
  cnt = 0 
  mp = defaultdict(int) 
  for i in range(len(arr)):
    c1 = arr[i] + k 
    c2 = arr[i] - k 
    if c1 in mp:
      cnt += mp[c1] 
    if c2 in mp:
      cnt += mp[c2] 
    mp[arr[i]] += 1 
    return cnt 
  print(optimisation(arr,k)) 
  print(brute_force(arr,k))
