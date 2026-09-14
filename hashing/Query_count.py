n = int(input()) 
arr = [] 
q = int(input()) 
for i in range(len(arr)): 
  arr.append(int(input()) 
print(arr) 
from collections import defaultdict 
def brute_force(arr,q):
  for i in range(q):
    query = int(input()) 
    count = 0 
    for j in range(len(arr)):
        if arr[j] == query:
          count = count + 1 
        print(count)  
### optimisation using hash_arrays techniques 
def optimisation(arr,q):
  hash = [0]*51 
  for i in range(len(arr)): 
    hash[arr[i]] += 1 
  for i in range(q):
    query = int(input()) 
    print(hash[query]) 
## final optimisation use of hashmap data structures 
def space_optimisation(arr,q):
  mp = defaultdict(int) 
  for num in arr:
    mp[num] += 1 
  for i in range(q):
    query = int(input()) 
    print(mp[query]) 
print(space_optimisation(arr,q)) 
print(brute_force(qrr,q)) 
print(optimisation(arr,q)) 

