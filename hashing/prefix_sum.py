n = int(input()) 
l = int(input()) 
r = int(input()) 
arr = [] 
for i in range(n):
  arr.append(int(input())) 
print(arr) 
def brute_force(arr,l,r):
  sums = 0 
  for i in range(l,r + 1):
    sums += arr[i] 
  return sums 
##optimisation using the prefix sums arrays 
def optimisation(arr,l,r):
  n = len(arr) 
  p = [0]*n 
  p[0] = arr[0] 
  for i in range(1,len(arr)):
    p[i] = p[i - 1] + arr[i] 
  sums = p[r] - p[l - 1] 
  return sums 
  print(brute_force(arr,l,r)) 
  print(optimisation(arr,l,r))
