fastapi ->Framework to run your python application
uvicorn -> helps you to run your application at desired port and also pops up swagger to test your apis
pip install -r requirements.txt is useful to install all the libraries

Inorder to setup Mongodb database 
steps to follow
1. Install docker(chatgpt ) -> use cli to install docker 
2. docker pull mongo
3. docker run -d \
--name mongodb \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
mongo
4. docker ps  
to vaildate is your docker contianer of mongo up and running

#you will create a database -> collections(tables) both are same functionality but different nam

By default mongo db creates or works with the data in the format of dictornary

insert_one is an inbuilt function from mongodb which will help u to ingest the data into the db

Inorder to run your application
uvicorn app:app --reload


Whenever you create a record in db, by default mongodb will create a object id for u .