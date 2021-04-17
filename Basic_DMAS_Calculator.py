"""DMAS Calculator (DMAS = Div, Mul ,Add ,Sub)"""

def calc(first,ops,second):
	if ops=="+":
		return first+second
	if ops=="*":
		return first * second
	if ops=="/":
		return first/second
	if ops=="-":
		return first-second
	if ops=="%":
		return first%second
		
equation=list(input("Equation = "))
list1=[]
opertors=['+','-','*','/',"%"]
equation1=[]
for i in equation:
	for j in opertors:
		if i == j:
			equation1.append(''.join(list1))
			equation1.append(j)
			list1.clear()
			break
	else:
			list1.append(i)
else:
	equation1.append(''.join(list1))
	equation=equation1


num=len(equation1)
prev=0

while len(equation1)>1:
    if "/" in equation1:
        i=prev
        while i<num or "/" in equation1:
            if equation1[i]=="/":
                equation1[i-1]=float(equation1[i-1])/float(equation1[i+1])
                del equation1[i+1],equation1[i]
                num=num-2
                prev=i
            else:
                prev+=1
            i=prev
        else:
            num=len(equation1)
            prev=0
            
    if "*" in equation1:
        i=prev
        while i<num or "*" in equation1:
            if equation1[i]=="*":
                equation1[i-1]=float(equation1[i-1])*float(equation1[i+1])
                del equation1[i+1],equation1[i]
                num=num-2
                prev=i
            else:
                prev+=1
            i=prev
        else:
            num=len(equation1)
            prev=0
    
    if "+" in equation1:
        i=prev
        while i<num or "+" in equation1:
            if equation1[i]=="+":
                equation1[i-1]=float(equation1[i-1])+float(equation1[i+1])
                del equation1[i+1],equation1[i]
                num=num-2
                prev=i
            else:
                prev+=1
            i=prev
        else:
            num=len(equation1)
            prev=0
    
    if "-" in equation1:
        i=prev
        while i<num or "-" in equation1:
            if equation1[i]=="-":
                equation1[i-1]=float(equation1[i-1])-float(equation1[i+1])
                del equation1[i+1],equation1[i]
                num=num-2
                prev=i
            else:
                prev+=1
            i=prev
        else:
            num=len(equation1)
            prev=0
            
if int(equation1[0]) == equation1[0]:
	print("Solved Equation=",int(equation1[0]))
else:
    print("Solved Equation=",equation1[0])