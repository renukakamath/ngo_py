import datetime
from flask import *
from database import *
import uuid
# import json
# from web3 import Web3, HTTPProvider

# # truffle development blockchain address
# blockchain_address = 'http://127.0.0.1:9545'
# # Client instance to interact with the blockchain
# web3 = Web3(HTTPProvider(blockchain_address))
# # Set the default account (so we don't need to set the "from" for every transaction call)
# web3.eth.defaultAccount = web3.eth.accounts[0]
# # compiled_contract_path = 'F:/NGO/node_modules/.bin/build/contracts/medicines.json'

# compiled_contract_path = 'C:/Users/Riss/Downloads/NGO/NGO/node_modules/.bin/build/contracts/medicines.json'

# # Deployed contract address (see `migrate` command output: `contract address`)
# deployed_contract_address = '0x529Af622f817660C85c0Dc83DC8E5eD0D281D4d7'
# # syspath=r"C:\Users\Riss\Downloads\MedicineRecommendation\MedicineRecommendation\static\\"
public=Blueprint('public',__name__)


@public.route('/')
def home():

	session.clear()
	
	return render_template("home.html")

@public.route('/login',methods=['get','post'])
def login():
	session.clear()



	
	if 'login' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'" %(username,password)
		res=select(q)
		if res:


			session['lid']=res[0]['login_id']
			lid=session['lid']

			
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.adminhome'))
			elif res[0]['usertype']=='retailer':
				q="select * from retailer where login_id='%s'"%(session['lid'])
				res=select(q)
				session['retailer_id']=res[0]['retailer_id']
				flash("login successfully....!")
				return redirect(url_for('retailer.retailerhome'))
			elif res[0]['usertype']=='ngo':
				q="select * from ngo where login_id='%s'"%(session['lid'])
				res=select(q)
				session['ngo_id']=res[0]['ngo_id']
				flash("login successfully....!")
				return redirect(url_for('ngo.ngohome'))
			elif res[0]['usertype']=='user':
				q="select * from user where login_id='%s'"%(session['lid'])
				res=select(q)
				session['user_id']=res[0]['user_id']
				flash("login successfully....!")
				return redirect(url_for('user.userhome'))
			elif res[0]['usertype']=='pending':
				
				flash("your account is proccessing  please wait  ....!")
				# return redirect(url_for('user.userhome'))
		else:
			flash("invalid username and password")
	return render_template("login.html")



@public.route('/userregister',methods=['get','post'])
def userregister():
	data={}
	
	if 'login' in request.form:
		firstname=request.form['fn']
		lname=request.form['ln']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		q="insert into login values(null,'%s','%s','user')" %(username,password)
		id=insert(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,firstname,lname,place,phone,email)
		insert(q)
		flash("registered successfully....!")
		return redirect(url_for('public.login'))

	return render_template("userregister.html",data=data)





@public.route('/adminmanagengo',methods=['get','post'])
def adminmanagengo():
	data={}
	
	
	if 'manage' in request.form:
		firstname=request.form['fn']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		i=request.files['i']
		path="static/ngo_id_proof"+str(uuid.uuid4())+i.filename
		i.save(path)
		q="insert into login values(null,'%s','%s','pending')" %(username,password)
		id=insert(q)
		q="insert into ngo values(null,'%s','%s','%s','%s','%s','%s')"%(id,firstname,place,phone,email,path)
		insert(q)
		print(q)
		flash('registered successfully')
		return redirect(url_for('public.adminmanagengo'))
	return render_template("adminmanagengo.html",data=data)





@public.route('/adminmanageretailer',methods=['get','post'])
def adminmanageretailer():
	data={}
	
	
	if 'manage' in request.form:
		firstname=request.form['fn']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		username=request.form['username']
		password=request.form['password']
		i=request.files['i']
		path="static/retailer_id_proof"+str(uuid.uuid4())+i.filename
		i.save(path)		
		q="insert into login values(null,'%s','%s','pending')" %(username,password)
		id=insert(q)
		q="insert into retailer values(null,'%s','%s','%s','%s','%s','%s')"%(id,firstname,place,phone,email,path)
		insert(q)
		flash('registered successfully')

		return redirect(url_for('public.adminmanageretailer'))

	

	return render_template("adminmanageretailer.html",data=data)
