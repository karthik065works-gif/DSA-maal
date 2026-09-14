n = int(input()) 
k = int(input()) 
arr = [] 
for i in range(n):
  arr.append(int(input()) 
print(arr)  
def brute_force(arr,k):
  for i in range(len(arr)):
    for j in range(i + 1,len(arr)): 
        if arr[i] == arr[j] and j - i <= k:
            return True 
  return False 
from collections import defaultdict 
def optimal_solution(arr,k): 
  mp = defaultdict(int) 
  for i in range(len(arr): 
    ce = arr[i] 
    if ce in mp:
      d = i - mp[ce]  
      if d <= k:
        return True 
    mp[arr[i]] = i   
    return False 
print(optimal_solution(arr,k)) 
print(brute_force(arr,k)) 

