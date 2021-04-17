import random

letter=[chr(97+i) for i in range(26)]+[chr(65+k) for k in range(26)]
random.shuffle(letter)

num=[j for j in range(10)]
random.shuffle(num)

symbol=["$","&","#","@","!","?","_"]
random.shuffle(symbol)

total=int(input("Enter your password length ="))
chars=int(random.random()*total)
symbols=int(random.random()*(total-chars))

pass1=random.choices(letter,k=total-(chars+symbols))
pass2=random.choices(num,k=chars)
pass3=random.choices(symbol,k=symbols)

password=pass1+pass2+pass3
random.shuffle(password)
new_pass=[]
for i in range(0,len(password)):
	new_pass.append(str(password[i]))
print(f"\nYour Password is : {''.join(new_pass)}")