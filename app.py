from DOMAIN.EntityFactory import Entityfactory
from DOMAIN.UserRepository import UserRepository

u1 = Entityfactory.create("user", {"username": "John", "email": "j@d.com", "password": "123456"})

# p1 = Entityfactory.create("post", {"title": "DDD", "body": "Domain is", "authorId": "123"})
#print(u1, u1.id)
#print(p1, p1.id)

########## SAVE NEW ID #############################
UserRepository.saveUser(u1)
users = UserRepository.getAllUsers()
for u in users:
    print(u.id)
    print (u.username)
print ("#"*20)

#########u  UPDATE NAME  ############################

u1.username = "new name"
UserRepository.updateUser(u1)
users = UserRepository.getAllUsers()
for u in users:
    print(u.id)
    print (u.username) 
print ("#"*20)

############ DELETE USER ###################
UserRepository.deleteUser(u1)
users = UserRepository.getAllUsers()
for u in users:
    print(u.id)
    print (u.username) 
print ("#"*20)

############ GET ID ##########################
user = UserRepository.getUser("12345")
print(user)

##################################

