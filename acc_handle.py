import json
from datetime import date
#CHECK BALANCE
def chk_bal():
	print("\n")
	print(("CHECK BALANCE").center(50,'*'))
	acc=input("Enter the account number: ")
	try:
		with open("acc_details.json") as files:
			data=json.load(files)
		result=print("\n\nName: {} | Balance: ₹{}".format(data[acc][0]["Name"],data[acc][0]["Balance"]))
	except(KeyError):
		result=print("\n\nAccount does not exist!! Please enter a valid account number")
		return result

#DISPLAY ALL DETAILS
def details():
	print("\n")
	print(("ACCOUNT DETAILS").center(50,'*'))
	acc=input("Enter the account number:")
	try:
		with open("acc_details.json") as files:
			data=json.load(files)
		result=print("\nAccount #: {}\nName: {}\nAddress: {}\nPhone: {}\nDOB: {}\nBalance: ₹{}"\
                       .format(acc,data[acc][0]["Name"],\
                       data[acc][0]["Address"],data[acc][0]["Phone"],data[acc][0]["DOB"],data[acc][0]["Balance"]))
	except(KeyError):
		result=print("\n\nAccount does not exist!! Please enter a valid account number")
		return result

#LOCATION-WISE LIST OF ACCOUNTS
def loc():
	print("\n")
	print(("LOCATION-WISE ACCOUNTS LIST").center(50,'*'))
	l=input("Enter the location:")
	try:
		with open("acc_details.json") as files:
			data=json.load(files)
		for x,y in data.items():
			if y[1]["Location"]==l:
				print(x)
	except(KeyError):
		print("\n\nAccount does not exist for the location entered!!")
	return
#AGE WISE LIST OF ACCOUNTS
def cal_age(born):
	today = date.today()
	return int(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))

def age():
	print("\n")
	print(("AGE-WISE ACCOUNTS LIST").center(50,'*'))
	try:
		search_age=int(input("Enter the age: "))
		mode=input("Enter the mode: > (or) < (or) =: ")
		with open("acc_details.json") as files:
			data=json.load(files)
		if(mode=='='):
			for x,y in data.items():
				if(cal_age(date(int(y[0]["DOB"][-4:]),int(y[0]["DOB"][3:5]),int(y[0]["DOB"][0:2])))==search_age):
					print(x)
		elif(mode=='>'):
			for x,y in data.items():
				if(cal_age(date(int(y[0]["DOB"][-4:]),int(y[0]["DOB"][3:5]),int(y[0]["DOB"][0:2])))>search_age):
					print(x)
		elif(mode=='<'):
			for x,y in data.items():
				if(cal_age(date(int(y[0]["DOB"][-4:]),int(y[0]["DOB"][3:5]),int(y[0]["DOB"][0:2])))<search_age):
					print(x)
		else:
			pass
	except(KeyError,ValueError):
		print("Enter a valid input")

#UPDATING BALANCE
def update():
	print("\n")
	print(("UPDATE WITHDRAW OR DEPOSIT").center(50,'*'))
	try:
		acc=input("Enter the account number to be updated: ")
		mode=int(input("Enter the mode:1-Deposit, 2-Withdraw: "))
		amt=int(input("Enter the amount: ₹"))
		with open("acc_details.json") as files:
			data=json.load(files)
		bal=data[acc][0]["Balance"]
		print("Previous Balance: ₹",bal)
		if(mode==1):
			data[acc][0]["Balance"]=bal+amt
		if(mode==2):
			data[acc][0]["Balance"]=bal-amt
		with open("acc_details.json","w+") as files:
			json.dump(data,files,indent=4)
			#data1=json.load(files)
		print("New Balance: ₹",data[acc][0]["Balance"])
	except(KeyError,ValueError):
		print("Enter a valid input")
	return
	




#MAIN BLOCK
def main():
	ch=int(input("Enter any of the following choice to perform\n1-Check Balance\n2-Check details of the account number\n3-List accounts: location wise\n4-List accounts: age wise\n5-Update withdrawal or Deposit\n"))
	if(ch==1):
		chk_bal()
	elif(ch==2):
		details()
	elif(ch==3):
		loc()
	elif(ch==4):
		age()
	elif(ch==5):
		update()
	else:
		print("Enter a valid choice")
	if(int(input("Do you wish to continue? [1-Yes 0-No]: "))):
		main()
	return

main()

