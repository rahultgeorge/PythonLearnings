if __name__ == '__main__':
    N = int(input())
l=[]
for i in range(N):
    line=input()
    if (line.count("insert")>0):
        line=line.replace("insert","").lstrip().rstrip().split();
        line=[ int(x) for x in line]
        l.insert(line[0],line[1])
    elif (line.count("remove")>0):
        line=line.replace("remove","").lstrip().rstrip().replace(" ","");
        line=int(line)
        l.remove(line)
    elif (line.count("append")>0):
        line=line.replace("append","").lstrip().rstrip().replace(" ","");
        line=int(line)
        l.append(line)
    elif (line.count("sort")>0):
        l.sort()
    elif (line.count("pop")>0):
        l.pop()
    elif (line.count("reverse")>0):
        l.reverse()
    else:
        print(l)
        
     
    
    