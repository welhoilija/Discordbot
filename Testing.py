Name = "\nWelho#3819"
bosslist = open('bosslist.txt','r')
List = bosslist.read().split(" ")
with open('bosslist.txt','r') as f:
    if Name in List:
         print("You are in the bosslist already")
    else:
    	print(List)