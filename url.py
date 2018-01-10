from urllib.request import urlopen 
import json 
import pprint 

def i_d(id): 
 req = "https://api.vk.com/method/users.get?user_ids={id}&v=5.8&fields=online".format(id=id) 
 try: 
  req_q = urlopen(req) 
  q = json.loads(req_q.read()) #чтение Json-данных 
 except: 
  print('ERROR') 
return q 

if __name__ == "__main__": 
id = input('id:') #вводим id нужного пользователя 
print('PLease:') 
pprint.pprint(i_d(id))
тут была ошибка я поправил
