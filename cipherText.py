def caesar(givenstr, shift): 
  encodedTxt = ""
  for i in givenstr:
    if i.isalpha():
      InAlphaOrder = ord(i) + shift 
      if InAlphaOrder > ord('z'):
        InAlphaOrder -= 26
      lastLetter = chr(InAlphaOrder)
      encodedTxt += lastLetter
  print ("Your encoded ciphertext is: ", encodedTxt)
  return encodedTxt