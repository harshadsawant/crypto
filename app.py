#using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
  
from Crypto.PublicKey import RSA
# creating a Flask app 
app = Flask(__name__) 
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
		
  	key = RSA.generate(1024)
	pub_key = key.publickey()	

        data = "hello world"
        return jsonify({'Private Key': key})
	return jsonify({'Public Key': pub_key})
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 
