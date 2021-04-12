''' This is a project by Bennett Kahn'''

# this is a function that takes in a list and doubles every element in it
def double_list(l):
	for i in range(len(l)):
		l[i] *= 2
	return l
print(double_list([1,2,3,4,5]))