
bInp = input("Input your binary list (Separated by spaces): ") # input the binary

revInp = ["1", ]


#validation:
"""
256 128 64 32 16 8 4 2 1
"""
if len(bInp.strip()) > 8: 
  print("Number is too large. This is using 8 bit bianary")



# Flipping the bits
def flip():
  """
  Flipping the bits
  """
  global bInp, revInp

  for num in bInp:

    if num == "1":
        revInp += "0"

    elif num == "0":
      revInp += "1"

    elif num == " " or num == ",":
      pass

    else:
      print("Invalid number")
    
  addbit()

#adding the bits

def addbit():
  """
  Adding the 1 bit to the end of the list
  """
  if revInp[-1] == "0":
    revInp[-1] = "1"
  
  else:
    n = -1

    """
    Loop though the list in reverse till you find the first 0 and the change all 1s from there to a 0.
    """  



if __name__ == '__main__':
  flip()