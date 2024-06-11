from flask import *
from database import *
import uuid
from datetime import datetime,date

retailer=Blueprint('retailer',__name__)

@retailer.route('/retailerhome')
def retailerhome():

	if not session.get("lid") is None:
		return render_template("retailerhome.html")
	else:
		return redirect(url_for("public.login"))







@retailer.route('/retailerviewwork',methods=['get','post'])
def retailerviewwork():
	if not session.get("lid") is None:
		data={}
		q="select * from work"
		res=select(q)
		data['view']=res
		
		return render_template("retailerviewwork.html",data=data)
	else:
		return redirect(url_for("public.login"))


@retailer.route('/retailersendproposal',methods=['get','post'])
def retailersendproposal():
	if not session.get("lid") is None:
		from datetime import date
		today = date.today()
		print("Today's date:", today)
		data={}
		work_id=request.args['work_id']
		if 'add' in request.form:
			d=request.form['date']
			a=request.form['a']
			
			q="insert into proposal values(null,'%s','%s','%s','%s','pending')"%(work_id,session['retailer_id'],a,d)
			insert(q)

			flash('proposal send successfully')

			return redirect(url_for('retailer.retailersendproposal',work_id=work_id))
		q="SELECT * FROM `proposal` INNER JOIN `retailer` USING(`retailer_id`) where work_id='%s' and retailer_id='%s' "%(work_id,session['retailer_id'])
		data['view']=select(q)
		# q="SELECT * FROM retailer"
		# data['rview']=select(q)


		return render_template("retailersendproposal.html",data=data,today=today)
	else:
		return redirect(url_for("public.login"))





@retailer.route('/retailerviewproposal',methods=['get','post'])
def retailerviewproposal():
	if not session.get("lid") is None:
		data={}
		work_id=request.args['work_id']
		q="SELECT * FROM `proposal` INNER JOIN `retailer` USING(`retailer_id`) where  retailer_id='%s' and work_id='%s' "%(session['retailer_id'],work_id)
		data['view']=select(q)



		if "action" in request.args:
			action=request.args['action']
			pid=request.args['pid']
		else:
			action=None

		if action=='cancel':
			q="update proposal set status='cancel' where proposal_id='%s'"%(pid)
			update(q)

			flash("Your proposal is cancel")
			return redirect(url_for('retailer.retailerviewproposal',work_id=work_id))


		return render_template("retailerviewproposal.html",data=data)

	else:
		return redirect(url_for("public.login"))



@retailer.route('/editretailer',methods=['get','post'])
def editretailer():
	data={}


	q="select * from retailer where retailer_id='%s'"%(session['retailer_id'])
	res=select(q)
	data['udateretailer']=res
	
	
	if 'manage' in request.form:
		firstname=request.form['fn']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		
		q="update retailer set name='%s',place='%s',phone='%s',email='%s' where retailer_id='%s'"%(firstname,place,phone,email,session['retailer_id'])
		update(q)
		flash("update successfully....!")
		
		return redirect(url_for('retailer.editretailer'))
	return render_template("editretailer.html",data=data)
