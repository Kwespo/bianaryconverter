BitList = [] #splits it into the 1 and 0

Bianary = [9223372036854775808, 4611686018427387904, 2305843009213693952, 1152921504606846976, 576460752303423488, 288230376151711744, 144115188075855872, 72057594037927936, 36028797018963968, 18014398509481984, 9007199254740992, 4503599627370496, 2251799813685248, 1125899906842624, 562949953421312, 281474976710656, 140737488355328, 70368744177664, 35184372088832, 17592186044416, 8796093022208, 4398046511104, 2199023255552, 1099511627776, 549755813888, 274877906944, 137438953472, 68719476736, 34359738368, 17179869184, 8589934592, 4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1] #bianary

number = int(input("Input your number: ")) #gets the number
numberStart = number

for i in Bianary: #for all 8 bites it will loop

  # If the number fits in the iteration of the list add a 1

  if number < i:
    BitList.append(0)

  
  elif number >= i: 
    BitList.append(1)
    number -= i

  elif number == 0:
    BitList = [0] * 8
    print(BitList)

  else:
    raise Exception("Number is not valid for the 8 bit system")

print(f"You Number : '{numberStart}' in bianary is :{BitList} and it is {len(BitList)} long")