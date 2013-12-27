
var = 0


#global variable
def sum():
	global var
	var += 10
	return var


print sum()
