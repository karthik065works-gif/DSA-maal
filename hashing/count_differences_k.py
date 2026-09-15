n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
  arr.append(int(input()) 
print(arr) 
def brute_force(arr,k): 
  cnt = 0 
  for i in range(len(arr)):
    for j in range(i + 1,len(arr)):
      if arr[i] - arr[j] == k:
        cnt += 1 
    return cnt 
from collections import defaultdict 
def optimisation(arr,k):
  mp = defaultdict(int) 
  cnt =  0 
  for i in range(len(arr)):
    ce = k + arr[i] 
    if ce in mp:
      cnt += mp[ce] 
    mp[arr[i]] += 1 
  return cnt 
  print(optimisation(arr,k)) 
  print(brute_force(arr,k))
    
  
      i
