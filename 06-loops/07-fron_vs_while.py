# For: para iterables, cuando sabemos cuando terminara
# While: cuando no sabemos cuando no terminara

my_list=[1,2,3,4,5,6,7,8,9]

for number in my_list:
    print(number)

item = 1
while item <= len(my_list):
    print(item)
    item = item + 1