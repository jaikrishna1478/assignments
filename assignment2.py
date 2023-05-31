n=[2,3,4,55,56,78,75,69,66,101,100]
even=0
odd=0
for i in n:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("the even numbers count:",even)
print("the odd numbers count:",odd)
