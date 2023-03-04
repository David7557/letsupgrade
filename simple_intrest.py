def simple_interest(P,T,R):
	print('The principal is', P)
	print('The time period is', T)
	print('The rate of interest is',R)
	
	si = (P * T * R)/100
	
	print('The Simple Interest is', si)
	return si
	
simple_interest(8, 6, 8)
