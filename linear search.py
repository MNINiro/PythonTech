list = [52,15,62,84,68,44]

searchItem = int(input('enter a number:'))
found = 0  # initially it is false

for i in range (len(list)):
    if searchItem == list[i]:
        found=1
        print('item found',searchItem, 'in position:',i+1)

if found==0:
    print('item not found')


# found = 0  # initially it is false
# i = 0
# while i < (len(list)):
#     if searchItem == list[i]:
#         found = 1
#         print("Item found", searchItem, "in position:",i)
#         break;
#     i = i + 1
#
# if found==0:
#     print('item not found')

