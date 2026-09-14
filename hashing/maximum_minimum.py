from collections import defaultdict 
n = int(input()) 
q = int(input()) 
arr = [] 
for i in range(n):
  arr.append(int(input()) 
print(arr) 
def brute_force(arr):
  maxelement,maxcount = 0,0 
  minele,mincount = 0,float("inf") 
  for i in range(len(arr)): 
    count = 0 
    for j in range(i,len(arr)):
        if arr[i] == arr[j]:
          count = count + 1 
    return count 
## optimisation using hashmaps O(N*N) to o(N) time and space solution 
def optimisation(arr):
  mp =defaultdict(int) 
  for num in arr:
    mp[num] += 1 
  maxcount = max(mp.keys()) 
  mincount = min(mp.keys()) 
  maxele = [(k,v) for (k,v) in mp.items() v == maxcount] 
  minele = [(k,v) for (k,v) in mp.items() v == mincount] 
  return maxele,minele 
print(brute_force(arr)) 
print(optimisation(arr)) 
