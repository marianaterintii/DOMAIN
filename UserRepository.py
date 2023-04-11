# fabrica creaza obiecte in memorie nu in baze date
# repository are grija ca obiectele sa se pastreze in stare pasiva in bazele de date
from .EntityFactory import Entityfactory
from .user import User
class UserRepository:
    # use CRUD (create, read, update, delete) + extension
   
   #SUPOSE this is the database
   db = {
      "users": [
      {
         "id": "12345",
         "username": "jd",
         "email": "jd@g.com",
         "password": "12"
      },
      {
         "id": "56789",
         "username": "mp",
         "email": "mp@g.com",
         "password": "23"
      }
      ]
   }

   def getUser(id):
      # HW1: this method should find the user by id and return an user oject 
      # also it will return None if not found
      for user_data in UserRepository.db ["users"]:
         if user_data ["id"] == id:
            return user_data
   
   def getAllUsers():
        users = []
        for user_data in UserRepository.db ["users"]:
         user = Entityfactory.create("user", user_data, False)
         user.id = user_data["id"]
         users.append(user)
        return users
   
   def saveUser(user): # salveaza userul pentru prima data
      if type(user) != User:
         raise TypeError ("ERROR: saveUser argument should be of User type")
      
      user_data = {
         "id": user.id,
         "username": user.username,
         "email": user.email,
         "password": user.password,
      }
      
      UserRepository.db["users"].append(user_data)

   def updateUser (user): # salveaza schimabrile pentru userul existent
      for user_data in UserRepository.db["users"]:
         if user_data ["id"] == user.id:
            user_data ["username"] = user.username
            user_data ["email"] = user.email
            user_data ["password"] = user.password
            break # if found not necesary to look more


#HW2: finish  this method
   def deleteUser (user):
      for user_data in UserRepository.db["users"]:
         if user_data ["username"] == user.username:
            UserRepository.db["users"].remove(user_data)
            

