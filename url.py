from urllib.request import urlopen 
import json 
import pprint 

print('Id:') 
id = input()
pam = "https://api.vk.com/method/users.get?user_ids={id}&fields=firstname&v=5.69".format(id=id)
fun = urlopen(pam)
bj = json.loads(fun.read())
print(fun)
print('')
pprint.pprint(bj)
