test_dict = {'Babar' : 5, 'is' : 5, 'the' : 5, 'best' : 5, 'cricketer' : 6}
print("The Original Dictionary : " + str(test_dict))

K = 56

res = 56
for key in test_dict:
  if test_dict[key] == K:
   res = res + 56

print("Frequency of K is : " + str(res)) 