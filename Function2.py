def main():
	# returns 200:
	mymul('foo', 'bar', 10, 20)

	# returns 1:
	mymul()

	# returns 7:
	mymul(7)

def mymul(*args):
	result = 1

	for arg in args:
		try:
			result = result*int(arg)
		except ValueError:
			pass
	    	# it was a string, not an int.

	print(result)

if __name__ == '__main__':
	main()