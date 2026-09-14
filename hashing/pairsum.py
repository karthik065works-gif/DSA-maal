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
        if arr[i] + arr[j] == k:
            cnt = cnt +  1   
  return cnt 
from collections import defaultdict 
def optimal_solutions(arr,k): 
  mp = defaultdict(int) 
  cnt = 0 
  for i in range(len(arr)): 
    cmp = k - arr[i] 
    if cmp in mp:
      cnt += mp[cmp] 
    mp[arr[i]] += 1  
  return cnt 
print(brute_force(arr,k)) 
print(optimal_solution(arr,k)) 
