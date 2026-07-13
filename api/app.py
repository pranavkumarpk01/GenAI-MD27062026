from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI(
      title="Student CRUD operation",
      description="Simple CRUD API using FastAPI and Mongo",
      version="1.0"
)

#Establish connection with your db
client = MongoClient("mongodb://admin:password@localhost:27017/")
db =client["training_db"]
collection = db["students"]

@app.get("/students")
def get_students():
    
    students=[]
    for student in collection.find():
      student["_id"] = str(student["_id"])
      students.append(student)

    return students  

@app.post("/students")
def create_student(student: dict):
   result = collection.insert_one(student)

   return{
      "message":"student created",
      "id": str(result.inserted_id)
   }

@app.put("/students/{student_id}")
def update_student(student_id:str , student:dict):
   result = collection.update_one(
      {"_id":ObjectId(student_id)},
      {"$set":student}
   )

   if result.modified_count == 0:
      raise HTTPException(status_code=404 , detail="Student not found")
   
   return{
      "message":"Student updated"
   }

@app.delete("/students/{student_id}")
def delete_student(student_id:str):
   result = collection.delete_one(
      {"_id": ObjectId(student_id)}
   )

   if result.deleted_count == 0:
      raise HTTPException(status_code=404 , detail="Student not found")
   
   return{
      "message":"Student deleted"
   }