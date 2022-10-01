exc=[2,3,4]
#total=exc[0]+exc[1]+exc[2]
total=0
for i in range(len(exc)):
    print("month:",(i+1),"expense:",exc[i])
    total=total+exc[i]
print(total)
