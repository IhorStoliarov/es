#print(input(format(r'')))
#print(ord('\\'))
#print(ord(':'))
#puth = input()
#print(for i in puth if i == ':' or i == "\\", end='\n')
putch = input().split()
for i in putch:
    if i == chr(92) or i == chr(58):
        print('\n')
    print(putch)

