import sys

def init():
	if len(sys.argv) <= 1:
		ipString = "127.0.0.1"
	else:
		ipString = sys.argv[1]
	print("IP ",ipString)
	
			
def main():
 mc = init()

if __name__ == "__main__":
 main()
