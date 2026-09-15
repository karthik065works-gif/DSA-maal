n = int(input()) 
arr = [] 
k = int(input()) 
for i in range(n):
  arr.append(int(input()) 
print(arr) 
def brute_force(arr,k):
  cnt = 0 
  for i in range(len(arr)):
    sums = 0
    for j in range(i,len(arr)):
      sums += arr[j] 
      if sums == k:
        cnt += 1 
  return cnt 
from collections import defaultdict 
def optimal_implementation(arr,k):
  mp = defaultdict(int) 
  psum = 0 
  cnt = 0 
  for i in range(len(arr)):
    psum = psum + arr[i] 
    if psum == k:
      cnt = cnt + 1 
    if psum - k in mp:
      cnt += mp[psum - k] 
    mp[psum] += 1 
  return cnt 
print(brute_force(arr,k)) 
print(optimal_solution(arr,k)) 
