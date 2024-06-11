from public import *


user=Blueprint('user',__name__)


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
# # deployed_contract_address = '0x3534a9a1Eff73497f1822f963AAcA4F36ef5ffe9'



@user.route('/userhome')
def userhome():
	if not session.get("lid") is None:
		return render_template("userhome.html")
	else:
		return redirect(url_for("public.login"))

@user.route('/usersenddonation',methods=['get','post'])
def usersenddonation():
	if not session.get("lid") is None:
		data={}


		q="select * from donation  inner join user using (user_id) where user_id='%s'"%(session['user_id'])
		res=select(q)
		data['ona']=res
		# if 'add' in request.form:
		# 	a=request.form['a']
		# 	import  datetime
		# 	d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			

				# q="INSERT INTO `medicine` VALUES(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(a,b,c,d,e,f,g,h,i)
				# insert(q)
			# with open(compiled_contract_path) as file:
			# 	contract_json = json.load(file)  # load contract info as JSON
			# 	contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			# contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			# id=web3.eth.get_block_number()
			# message = contract.functions.add_payment(id,session['lid'], a,d).transact()
			# flash("payment successfully")
			# return redirect(url_for('user.usersenddonation'))

		# with open(compiled_contract_path) as file:
		# 	contract_json = json.load(file)  # load contract info as JSON
		# 	contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		# contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		# blocknumber = web3.eth.get_block_number()
		# res = []
		# try:
		# 	for i in range(blocknumber, 0, -1):
		# 		a = web3.eth.get_transaction_by_block(i, 0)
		# 		decoded_input = contract.decode_function_input(a['input'])
		# 		print(decoded_input)
		# 		if str(decoded_input[0]) == "<Function add_payment(uint256,uint256,uint256,string,string)>":
		# 			if int(decoded_input[1]['u_id']) == int(session['user_id']):
		# 				res.append(decoded_input[1])
		# except Exception as e:
		# 	print("", e)
		# data['view']=res

		# if res:
		# 	q="select * from user where user_id='%s'"%(session['user_id'])
		# 	res1=select(q)
		# 	uname=res1[0]['fname']
		# 	data['names']=uname



		# 	q="insert into donation values(null,'%s','%s',curdate())"%(user_id,a)
		# 	insert(q)
		# 	flash(' send successfully')
		# 	return redirect(url_for('user.usersendproposal'))
		# q="SELECT * FROM `donation` INNER JOIN `user` USING(`user_id`) where user_id='%s'"%(user_id)
		# data['view']=select(q)
		
		return render_template("usersenddonation.html",data=data)
	else:
		return redirect(url_for("public.login"))

@user.route('/userviewwork',methods=['get','post'])
def userviewwork():
	if not session.get("lid") is None:
		data={}
		q="select * from work where status='proposal alloted'"
		res=select(q)
		data['view']=res

		return render_template("userviewwork.html",data=data)
	else:
		return redirect(url_for("public.login"))


@user.route('/usserwork',methods=['get','post'])
def usserwork():
	if not session.get("lid") is None:
		data={}
		q="select * from work"
		res=select(q)
		data['view']=res

		return render_template("usserwork.html",data=data)
	else:
		return redirect(url_for("public.login"))


@user.route('/usermakepayment',methods=['get','post'])
def usermakepayment():
	if not session.get("lid") is None:
		data={}
		work_id=request.args['work_id']
		data['amounts']=request.args['amounts']
		print(data['amounts'])
		data['bal_amt']=request.args['bal_amt']
		print(data['bal_amt'])

		tot=int(data['amounts'])-int(data['bal_amt'])
		data['tot']=tot
		flash("WANTED DONATION IS"+" "+ str(data['tot']))

		import  datetime
		d=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
		if 'add' in request.form:
			a=request.form['a']
			aamt=request.form['aamt']
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			id=web3.eth.get_block_number()
			message = contract.functions.add_payment(id,int(session['user_id']),int(work_id),a,d).transact()



			
			q="update work set bal_amt=bal_amt+'%s' where work_id='%s'"%(a,work_id)
			print(q)
			q="insert into donation values(null ,'%s','%s',curdate())"%(session['user_id'],a)
			insert(q)
			update(q)
			flash("payment successfully")
			return redirect(url_for('user.usersenddonation'))

	#///////////////////////////////////////////////////////////////////////////
		#///////////////////////////////////////////////////////////////////////////




			# with open(compiled_contract_path) as file:
			# 	contract_json = json.load(file)  # load contract info as JSON
			# 	contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			# contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			# blocknumber = web3.eth.get_block_number()
			# res = []
			# try:
			# 	for i in range(blocknumber, 0, -1):
			# 		a = web3.eth.get_transaction_by_block(i, 0)
			# 		decoded_input = contract.decode_function_input(a['input'])
			# 		print(decoded_input)
			# 		if str(decoded_input[0]) == "<Function add_payment(uint256,uint256,uint256,string,string)>":
			# 			if int(decoded_input[1]['u_id']) == int(session['user_id']):
			# 				res.append(decoded_input[1])
			# except Exception as e:
			# 	print("", e)
			# data['view']=res
			
			# if res:
			# 	q="select * from work where work_id='%s'"%(res[0]['w_id'])
			# 	print('nbbbbbbbbbbbbb',q)
			# 	res1=select(q)
			# 	if res1:
			# 		data['b_amount']=res1[0]['amount']
					# if res1[0]['amounts']=res[0]['amount']:
					# 	flash('donation reached')
				
					# else:
					# 	cur_amt=res[0]['amount']
					# 	print('cccc',cur_amt)
					# 	tot_amt=res1[0]['amounts']
					# 	print('aaaa',tot_amt)
					# 	session['add_amt']=int(tot_amt)-int(cur_amt)
					# 	print('vvvvvv',session['add_amt'])
					# 	with open(compiled_contract_path) as file:
					# 		contract_json = json.load(file)  # load contract info as JSON
					# 		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
					# 	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
					# 	id=web3.eth.get_block_number()
					# 	message = contract.functions.add_payment(id,int(session['user_id']),int(work_id),session['add_amt'],d).transact()
					# 	flash("payment successfully")
					# 	return redirect(url_for('user.usersenddonation'))	
		#///////////////////////////////////////////////////////////////////////////




				
		return render_template("usermakepayment.html",data=data)
	else:
		return redirect(url_for("public.login"))


@user.route('/edituser',methods=['get','post'])
def edituser():
	data={}


	q="select * from user where user_id='%s'"%(session['user_id'])
	res=select(q)
	data['udateuser']=res
	
	
	if 'login' in request.form:
		firstname=request.form['fn']
		lname=request.form['ln']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		
		q="update user set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where user_id='%s'"%(firstname,lname,place,phone,email,session['user_id'])
		update(q)
		flash("update successfully....!")
		
		return redirect(url_for('user.edituser'))
	return render_template("edituser.html",data=data)