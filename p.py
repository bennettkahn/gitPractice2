''' This is a project by Bennett Kahn'''

# this is a function to take in a list and squares all the elements
def square_list(l):
	for i in range(len(l)):
		l[i] *= l[i]
	return l
print(square_list([1, 2, 3, 4, 5]))