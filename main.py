from flask import Flask
from public import public
from admin import admin
from ngo import ngo
from retailer import retailer
from user import user

app=Flask(__name__)
app.secret_key="abc"

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(ngo,url_prefix="/ngo")
app.register_blueprint(retailer,url_prefix="/retailer")
app.register_blueprint(user,url_prefix="/user")

app.run(debug=True,port=5456)