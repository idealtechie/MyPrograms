def prime(num):

	for i in range(2, num):		if num % i  == 0:

			return(False)

			break

		else:

			return(True)

n=34

for i in range(2,n//2):

	if(prime(i)==True):

		if(prime(n-i)==True):

			print(i,n-i)
