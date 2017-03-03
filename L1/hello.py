import sys

def main():
	print "Hello, World!"
	print "This is {name}".format(name=sys.argv[0])

if __name__ == "__main__":
	main()
