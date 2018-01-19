def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2)

convertToBinary(5)
