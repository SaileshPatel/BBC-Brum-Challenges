string = "aaaaabcccccccdeee"

for i in range(len(string)-1):
	if string[i] != string[i+1] and string[i] != string[i-1]:
		print(string[i])
