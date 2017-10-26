import re
def main():
	"""
	Takes input text, runs a series of regex on it, and saves output to a file
	"""

	#read data
	textInput = open("./inputTextProcessing.txt", 'r')
	text = textInput.readlines()
	textInput.close()

	#create regex compilers
	interface = re.compile(r"^\w+:")
	inet = re.compile("(inet)\s(\d+)\.(\d+)\.(\d+)\.(\d+)")
	status = re.compile("(status:)\s(\w+)")

	#prep header
	output = ""
	csv = ["interface","inet","status"]

	#iterate through each line and check for match
	for lines in text:
		#check for interface match
		matchInterface = interface.match(lines)
		if matchInterface:
			output = output + ",".join(csv) + "\n"
			csv = ["","",""]
			csv[0] = matchInterface.group(0)[:-1]

		#check inet address match
		matchInet = inet.search(lines)
		if(matchInet):
			csv[1] = matchInet.group(0)[5:]
			
		#check status match
		matchStatus = status.search(lines)
		if(matchStatus):
			csv[2] = matchStatus.group(0)[8:]

	#wrap up end of output
	output = output + ",".join(csv)

	#write output
	textOutput = open("./outputTextProcessing.txt", 'w')
	textOutput.write(output)
	textOutput.close()

if __name__ == '__main__':
	main()
