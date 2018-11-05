max= input("Inserisci un numero da tastiera: ")
max=int(max)
i=0
while i<9:
	r=input ("Inserisci un numero da tastiera: ")
	r=int(r)
	if max<r:
		max=r
		print (max)
	i+=1