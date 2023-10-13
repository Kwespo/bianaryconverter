bInp = input("Input your binary list (Separated by spaces): ") # input the binary


bList = bInp.split()

for num in bList:

  if num == "0":
    num += "1"
  
  elif num == "1":
    num += "0"

  else:
    print("Invalid number")

print(bList)