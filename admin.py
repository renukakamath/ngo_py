from flask import *
from database import *
import uuid
from datetime import datetime,date

# import json
# from web3 import Web3, HTTPProvider

# # truffle development blockchain address
# blockchain_address = 'http://127.0.0.1:9545'
# # Client instance to interact with the blockchain
# web3 = Web3(HTTPProvider(blockchain_address))
# # Set the default account (so we don't need to set the "from" for every transaction call)
# web3.eth.defaultAccount = web3.eth.accounts[0]
# compiled_contract_path = 'C:/Users/Riss/Downloads/NGO/NGO/node_modules/.bin/build/contracts/medicines.json'
# # compiled_contract_path = 'F:/NGO/node_modules/.bin/build/contracts/medicines.json'
# # Deployed contract address (see `migrate` command output: `contract address`)
# deployed_contract_address = '0x529Af622f817660C85c0Dc83DC8E5eD0D281D4d7'

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	if not session.get("lid") is None:
		return render_template("adminhome.html")
	else:
		return redirect(url_for("public.login"))


# @admin.route('/adminmanagengo',methods=['get','post'])
# def adminmanagengo():
# 	data={}
# 	q="SELECT * FROM ngo"
# 	res=select(q)
# 	data['ashaworker']=res
	
# 	if 'manage' in request.form:
# 		firstname=request.form['fn']
# 		place=request.form['place']
# 		phone=request.form['phone']
# 		email=request.form['email']
# 		username=request.form['username']
# 		password=request.form['password']
# 		q="insert into login values(null,'%s','%s','ngo')" %(username,password)
# 		id=insert(q)
# 		q="insert into ngo values(null,'%s','%s','%s','%s','%s')"%(id,firstname,place,phone,email)
# 		insert(q)

# 		return redirect(url_for('admin.adminmanagengo'))

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 	else:
# 		action=None
# 	if action=="delete":
# 		q="delete from login where login_id='%s'" %(id)
# 		delete(q)
# 		q="delete from ngo where login_id='%s'"%(id)
# 		delete(q)
# 		return redirect(url_for('admin.adminmanagengo'))
# 	if action=="update":
# 		q="select * from ngo where login_id='%s'" %(id)
# 		res=select(q)
# 		data['worker']=res

# 	if 'update' in request.form:
# 		firstname=request.form['fn']
# 		place=request.form['place']

# 		phone=request.form['phone']
# 		email=request.form['email']
# 		q="update ngo set ngo='%s',place='%s',phone='%s',email='%s' where login_id='%s'" %(firstname,place,phone,email,id)
# 		update(q)
# 		return redirect(url_for('admin.adminmanagengo'))

# 	return render_template("adminmanagengo.html",data=data)





# @admin.route('/adminmanageretailer',methods=['get','post'])
# def adminmanageretailer():
# 	data={}
# 	q="SELECT * FROM retailer"
# 	res=select(q)
# 	data['ashaworker']=res
	
# 	if 'manage' in request.form:
# 		firstname=request.form['fn']
# 		place=request.form['place']
# 		phone=request.form['phone']
# 		email=request.form['email']
# 		username=request.form['username']
# 		password=request.form['password']
# 		q="insert into login values(null,'%s','%s','retailer')" %(username,password)
# 		id=insert(q)
# 		q="insert into retailer values(null,'%s','%s','%s','%s','%s')"%(id,firstname,place,phone,email)
# 		insert(q)

# 		return redirect(url_for('admin.adminmanageretailer'))

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		id=request.args['id']
# 	else:
# 		action=None
# 	if action=="delete":
# 		q="delete from login where login_id='%s'" %(id)
# 		delete(q)
# 		q="delete from retailer where login_id='%s'"%(id)
# 		delete(q)
# 		return redirect(url_for('admin.adminmanageretailer'))
# 	if action=="update":
# 		q="select * from retailer where login_id='%s'" %(id)
# 		res=select(q)
# 		data['worker']=res

# 	if 'update' in request.form:
# 		firstname=request.form['fn']
# 		place=request.form['place']

# 		phone=request.form['phone']
# 		email=request.form['email']
# 		q="update retailer set name='%s',place='%s',phone='%s',email='%s' where login_id='%s'" %(firstname,place,phone,email,id)
# 		update(q)
# 		return redirect(url_for('admin.adminmanageretailer'))

# 	return render_template("adminmanageretailer.html",data=data)


@admin.route('/adminviewngo',methods=['get','post'])
def adminviewngo():
	if not session.get("lid") is None:
		data={}

		q="SELECT * FROM ngo inner join login using(login_id) "
		res=select(q)
		data['user']=res


		if "action" in request.args:
			action=request.args['action']
			login_id=request.args['login_id']
		else:
			action=None

		if action=="accept":
			q="update  login set usertype='ngo' where login_id='%s'"%(login_id)
			r=update(q)
			res=select(q)
			flash("accept successfully")
			return redirect(url_for('admin.adminviewngo'))
		if action=="reject":
			q="delete from login where login_id='%s'"%(login_id)
			r=delete(q)
			q="delete from ngo where login_id='%s'"%(login_id)
			r=delete(q)
			flash("reject successfully")
			return redirect(url_for('admin.adminviewngo'))


		return render_template("adminviewngo.html",data=data)
	else:
		return redirect(url_for("public.login"))

@admin.route('/adminviewretailer',methods=['get','post'])
def adminviewretailer():
	if not session.get("lid") is None:
		data={}

		q="SELECT * FROM retailer inner join login using(login_id)  "
		res=select(q)
		data['user']=res


		if "action" in request.args:
			action=request.args['action']
			login_id=request.args['login_id']
		else:
			action=None

		if action=="accept":
			q="update  login set usertype='retailer' where login_id='%s'"%(login_id)
			r=update(q)
			res=select(q)
			flash("accept successfully")
			return redirect(url_for('admin.adminviewretailer'))
		if action=="reject":
			q="delete from login where login_id='%s'"%(login_id)
			r=delete(q)
			q="delete from retailer where login_id='%s'"%(login_id)
			r=delete(q)
			flash("reject successfully")
			return redirect(url_for('admin.adminviewretailer'))


		return render_template("adminviewretailer.html",data=data)
	else:
		return redirect(url_for("public.login"))





@admin.route('/adminviewuser',methods=['get','post'])
def adminviewuser():
	if not session.get("lid") is None:
		data={}

		q="SELECT *,user.fname as fn,user.lname as ln FROM USER "
		res=select(q)
		data['user']=res


		return render_template("adminviewuser.html",data=data)

	else:
		return redirect(url_for("public.login"))
 

# Let's create a dictionary, the functional way
 
# # Create your dictionary class
# class my_dictionary(dict):
 
#   # __init__ function
#   def __init__(self):
#     self = dict()
 
#   # Function to add key:value
#   def add(self, key, value):
#     self[key] = value

@admin.route('/adminviewdonation')
def adminviewdonation():

	if not session.get("lid") is None:
		data={}

		q="select * from donation  inner join user using (user_id) "
		res=select(q)

		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		blocknumber = web3.eth.get_block_number()
		res = []
		try:
			for i in range(blocknumber, 0, -1):
				a = web3.eth.get_transaction_by_block(i, 0)
				decoded_input = contract.decode_function_input(a['input'])
				print(decoded_input)
				if str(decoded_input[0]) == "<Function add_payment(uint256,uint256,uint256,string,string)>":
					# if int(decoded_input[1]['u_id']) == int(session['user_id']):
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)
		data['view']=res

		# if res:
			# q="select * from user where user_id='%s'"%(i['u_id'])
			# print(q)
			# res1=select(q)
			# data['fn']=res1[0]['fname']+" "+res1[0]['lname']
			# for i in res:
			# 	q="select * from user where user_id='%s'"%(i['u_id'])
			# 	print(q)
			# 	res1=select(q)
			# 	i.add('fname',res1[0]['fname']+" "+res1[0]['lname'])
			# 	print(i)	

		return render_template("adminviewdonation.html",data=data)

	else:
		return redirect(url_for("public.login"))



@admin.route('/adminviewuserdetails',methods=['get','post'])
def adminviewuserdetails():
	if not session.get("lid") is None:
		data={}
		u_id=request.args['u_id']

		q="SELECT *,user.fname as fn,user.lname as ln FROM USER where user_id='%s'"%(u_id)
		res=select(q)
		data['user']=res


		return render_template("adminviewuserdetails.html",data=data)
	else:
		return redirect(url_for("public.login"))

 


@admin.route('/adminviewwork',methods=['get','post'])
def adminviewwork():
	if not session.get("lid") is None:
		data={}
		q="select * from work"
		res=select(q)
		data['view']=res
		if 'action' in request.args:
			action=request.args['action']
			wid=request.args['wid']
		else:
			action=None
		if action=="approve":
			q="update work set status='approve' where work_id='%s'" %(wid)
			update(q)
			return redirect(url_for('admin.adminviewwork'))
		if action=="reject":
			q="update work set status='reject' where work_id='%s'" %(wid)
			update(q)
			return redirect(url_for('admin.adminviewwork'))
		return render_template("adminviewwork.html",data=data)

	else:
		return redirect(url_for("public.login"))


@admin.route('/adminviewproposal',methods=['get','post'])
def adminviewproposal():
	if not session.get("lid") is None:
		data={}
		work_id=request.args['work_id']

		q="SELECT * FROM `proposal` INNER JOIN `retailer` USING(`retailer_id`) where work_id='%s'"%(work_id)
		res=select(q)
		data['view']=res
		if res:
			pass

			amt=res[0]['amount']
			data['amt']=amt
		# print(amt)
		# if res:
		# 	data['view']=res
		# else:
		# 	flash('not approved proposals')
		# 	return redirect(url_for('admin.adminviewproposal'))
		if 'action' in request.args:
			action=request.args['action']
			work_id=request.args['work_id']
			retailer_id=request.args['retailer_id']
		else:
			action=None
		if action=="approve":

			q="update proposal set status='approve' where work_id='%s' and retailer_id='%s'" %(work_id,retailer_id)
			print('jjjjj',q)
			update(q)
			q="update work set amounts='%s' where work_id='%s'" %(data['amt'],work_id)
			print(q)
			update(q)
			q="update work set status='proposal alloted' where work_id='%s'" %(work_id)
			update(q)
			q="select * from proposal where retailer_id='%s' and work_id='%s' and  status='approve'"%(work_id,retailer_id)
			res1=select(q)
			if res1[0]['status']=="approve":
				# q="update work set amounts='%s' where work_id='%s'" %(data['amt'],work_id)
				# print(q)
				# update(q)
				# q="update work set status='proposal alloted' where work_id='%s'" %(work_id)
				# update(q)			# res1[0]['user_id']
				# res1[0]['work_id']
				# res1[0]['status']
				# q="select * from proposal where retailer_id='%s' and work_id='%s' and  status='approve'"%(int(res1[0]['retailer_id']),int(res1[0]['work_id']),int(res1[0]['status']))
				# print('llllll',q)
				# res2=select(q)
				# if res2:
			# else:
				q="update proposal set status='reject' where retailer_id!='%s' and work_id='%s'"%(retailer_id,work_id)
				print('wwwwww',q)
				update(q)

			


			flash('approved successfully')

			return redirect(url_for('admin.adminviewproposal',work_id=work_id,retailer_id=retailer_id))
		if action=="reject":
			q="update proposal set status='reject' where work_id='%s' and  retailer_id='%s'" %(work_id,retailer_id)
			update(q)
			return redirect(url_for('admin.adminviewproposal',work_id=work_id))
		return render_template("adminviewproposal.html",data=data)

	else:
		return redirect(url_for("public.login"))

