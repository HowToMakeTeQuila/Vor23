n = int(input('Write a 4 digit number: ')) 


n_swapped = 100*(n % 100) + (n // 100) 

print('The swapped number is:',n_swapped)
