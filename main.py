from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = [
    {"id":1, "name":"Abi","email":"abi@example.com"}
]

#Request Model
class User(BaseModel):
    name:str
    email: str

#root path
@app.get("/")
def root():
    return {
        "status":True,
        "message": "FastAPI is Runing!"
    }

#post method
@app.post("/posts")
def store_user(user: User):
    new_user = {
        "id":len(users)+1,
        "name":"Ravana",
        "email":"ravana@example.com"
    }
    users.append(new_user)
    
    return {
        "status":True,
        "message": "User Stored Sucessfully!"
    }
    
#get method
@app.get("/users")
def list_users():
    return {
        "status":200,
        "message":"Users List Retrived Sucessfully!",
        "count": len(users),
        "data":users
    }
    

#get_specific_user
@app.get("/users/{user_id}")
def get_users(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return {
                "status": True,
                "data":user
            }
            
    return{
        "status": False,
        "message": "User Not Found!"
    }
    
#update_the_user
@app.put("/users/{user_id}")
def update_user(user_id:int,user:User):
    for index,existing_user in enumerate(users):
        if existing_user["id"] == user_id:
            users[index]["name"] = user.name
            users[index]["email"] = user.email
            return {
                "status": True,
                "message": "User updated successfully",
                "data": users[index]
            }
            return{
                "status" : False,
                "message" : "User Not Found"
            }
            
    
#delete user
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)
            return {
                "status": True,
                "message": "User Deleted Sucessfully!",
                "data": deleted_user
            }
            
        return {
            "status": False,
            "Message" : "User Not Found!"
        }