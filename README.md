# Sprint-2---Microservice-A
Implemented Holds microservice. Takes in JSON data containing a book and user ID, and returns a JSON object that apecifies the book and hold, the date creatred, and a unique hold id. 

Step One: Create a virtual environment in your program folder
python -m venv <environment name> 

Step Two: Activate virtual environment:
<environment name>/Scripts/activate

Step Three: Install requests dependency
pip install requirments.txt

#How to make requests and recieve data:
  Create Hold:
  '''
      request_body = {"user_id": "Book", "book_id": "1234"} 
      post_response = requests.post(url, json=request_body)
      json_data = post_response.json()
      print(json_data)
    json_data = {
         "user_id": "user"
         "book_id": "book"
         "hold_id": "121345-123456-12345"
         "created_at": "YYYY-MM-DD"
    }
'''
  Retrieve Hold:

  '''
      request_body = {"user_id": "Book", "book_id": "1234"} 
      get_response = requests.get(url, json=request_body) 
      json_data = get_response.json() 
      print(json_data) 
    json_data = {
         "user_id": "user"
         "book_id": "book"
         "hold_id": "121345-123456-12345"
         "created_at": "YYYY-MM-DD"
    }  

  '''


  Delete Hold:
  '''
      request_body = {"user_id": "Book", "book_id": "1234"}
      delete_response = requests.delete(url, json=request_body)
     json_data = get_response.json()
      print(json_data)
    json_data = {
         "user_id": "user"
         "book_id": "book"
         "hold_id": "121345-123456-12345"
         "created_at": "YYYY-MM-DD"
    }  
'''
UML Screenshot
<img width="972" height="855" alt="image" src="https://github.com/user-attachments/assets/cf866865-c2ce-4bdb-bd7b-69c2e79de4df" />

