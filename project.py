# importing Flask and other modules
from flask import Flask, request, render_template
import requests
 
# Flask constructor
app = Flask(__name__)  

# as in the mspace api example
def send_text(username,password,sender_id,recipient, message):
   print('sending message')
   result = request.form
   receiver_number = (result['to'])
   receiver_name = (result['message'])
   username=""
   password=""
   sender_id=""
   recipient=receiver_number
   message=receiver_name
   url = "" #url given by the api provider
   url += f"sendtext/username={username}/password={password}/senderid=" \
      f"{sender_id}/recipient={recipient}/message={message}"
   print(message)
   return requests.get(url, None, headers={"accept": "application/json"})
     
 # A decorator used to tell the application
# which URL is associated function
@app.route("/")
def initial_route():
   return render_template('index.html', to='NONE', message='NONE')

@app.route('/receiver_details', methods=["POST", "GET"])
def get_receiver_details():
   result = request.form
   print(request.form)
   receiver_number=(result['to'])
   receiver_name=(result['message'])
   send_text("username", "password", "senderid", receiver_number,receiver_name)
   return render_template('index.html',to=receiver_number,message= receiver_name)

if __name__ == '__main__':
   app.run()
   

   

   

   


   
