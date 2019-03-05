#Subarray with given sum

#code
t=int(input())
sum=[]

for i in range(t):
    a=input().strip().split(" ")
    a=[int(i) for i in a]
    b=[int(i) for i in input().strip().split(" ")]
    # temp=b[32:38]
    # print(temp)
    sum = a[1]
    result =[]
    
        
    
    for i in range(len(b)):
        sum = a[1]
        sum = sum-b[i]
            
                
        for j in range(i+1,len(b)):
            sum=sum-b[j]
            if sum < 0:
                #sum  = 0
                break;
            elif sum==0:
                result.append((i+1 ,j+1))
                # print(result)
                break;
                
            else:
                continue;
        
    #print(result)
    if(len(result)):
        temp_result  = result[0]
        diff = temp_result[1]-temp_result[0]
        for i in range(len(result)):
            temp_diff=result[i][1]-result[i][0]
            if(temp_diff>diff):
                diff = temp_diff
                temp_result = result[i]
        print (str(temp_result[0]) +" "+ str(temp_result[1]))
        
    else:
        
        print("-1")

  
    
    


