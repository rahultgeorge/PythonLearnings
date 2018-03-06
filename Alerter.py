def alert():
 prevAverage=0.0
 prevOutliers=[]
 currOutliers=[]
 for i in range(len(inputs)-windowSize+1):
    window=inputs[i:i+windowSize]
    windowAverage=float(sum(window)/windowSize)
    #First Condition
    currOutliers=[]
    for value in window:
        if float(value)>(windowAverage*allowedIncrease):
         currOutliers.append(value)
    for v in prevOutliers:
        if v not in currOutliers and v not in window:
           return True; 
        if i==(len(inputs)-windowSize) and v in currOutliers:
           return True;
    #Second Condition 
    if (windowAverage)>(prevAverage*allowedIncrease) and prevAverage!=0:
      return True;
    prevAverage=windowAverage
    prevOutliers=currOutliers;
 return False;

if __name__ =="__main__":
 global inputs
 global windowSize
 global allowedIncrease
 #Format: 1 3 4
 inputs=[int(x) for x in input().split()]
 windowSize=int(input())
 allowedIncrease=float(input())
 print(alert())

