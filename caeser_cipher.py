def encrypt(message,shift):
	message=list(message)
	nums=[chr(i) for i in range(ord("a"),ord("z")+1)]
	
	nums1=[chr(j) for j in range(ord("a")+shift,ord("z")+1)]
	
	nums1=nums1+[chr(o) for o in range(ord("a"),ord("a")+shift)]
	for i in range(0,len(message)):
		if message[i] in nums:
			x=nums.index(message[i])
			message[i]=nums1[x]
	return "".join(message)
	
def decrypt(message,shift):
	
	message=list(message)
	nums=[chr(i) for i in range(ord("a"),ord("z")+1)]
	
	nums1=[chr(j) for j in range(ord("a")+shift,ord("z")+1)]
	
	nums1=nums1+[chr(o) for o in range(ord("a"),ord("a")+shift)]
	
	for i in range(0,len(message)):
		if message[i] in nums1:
			x=nums1.index(message[i])
			message[i]=nums[x]
	return "".join(message)
	
def main_start():
	choice=input("What you have to do encrypt or decrypt =")
	if choice=="encrypt":
		
		letter=input("Enter the Message=").lower()
		shifting=int(input("Enter the Shifting="))
		
		e=encrypt(letter,shifting)
		
		print(f"Encrypted Letter ={e}")
		
	elif choice=="decrypt":
		
		letter=input("Enter the Message=")
		shifting=int(input("Enter the Shifting="))
		d=decrypt(letter,shifting)	
		print(f"Decrypted Letter = {d}")	
main_start()