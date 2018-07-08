#function to yield even numbers
def even(n):
 result=[]
 for i in range(n):
  if(i%2==0):
   result.append(i)
 return result

print(even(int(input()))) 
    