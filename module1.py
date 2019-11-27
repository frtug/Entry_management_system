import smtplib
import sqlite3

from datetime import datetime
import Login

# for accessing and sending the mail to the Host
def send_email(sub,msg,hostEmail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(Login.EMAIL_ADDRESS,Login.PASSWORD)
        message = 'Subject: {}\n{}'.format(sub,msg)
        server.sendmail(Login.EMAIL_ADDRESS,hostEmail,message)
        server.quit()
        print("Successful send\n")
    except:
        print("Email failed to send\n")

con = sqlite3.connect('test.db')

con.execute('''CREATE TABLE IF NOT EXISTS COMPANY
         (USER_NAME      TEXT     NOT NULL,
           USER_PHONE    INTEGER  NOT NULL,
           CHECK_IN       TEXT    NOT NULL,
           CHECK_OUT      TEXT     NOT NULL,
           HOST_NAME     TEXT     NOT NULL,
           ADDRESS_VISITED    TEXT     NOT NULL          
           );''')
con.commit()

print ("Opened database successfully")

user_name = input("Enter user Name")
user_email = input("enter the Email")
user_phone = input("enter the phone number")

now = datetime.now()
check_in = now.strftime("%H:%M:%S")

print("Current Time =", check_in)

host_name = input("Enter Your Name")
host_email = input("enter the Email")
host_phone = input("enter the phone number")

sub = "Checking In User"
msg = "Mr "+host_name +", "+ user_name +" is coming"
send_email(sub,msg,host_email)

address_visted = "BH5 Room No 820,LPU  "
out = input("Press Q or q to checkout\n")
if out == 'Q' or out =='q' :
    nowout = datetime.now()
    check_out = nowout.strftime("%H:%M:%S")
    print(check_out)
    sub = "Checking Out User"
    msg = user_name + " is leaving \n" + user_phone + " \n" + user_email +"\n check in "+check_in+"\n   check out "+check_out;
    send_email(sub, msg,host_email)

con.execute("INSERT INTO COMPANY VALUES(?,?,?,?,?,?)",(user_name,user_phone,check_in,
                                                   check_out,host_name,
                                                       address_visted))
con.commit()
print("VAlues are inserted")

d = input("Hit Y or y to access the stored data or press any key to exit")
if d == "y" or d == "Y":
    d = con.execute("SELECT * FROM COMPANY")
    print(d.fetchall())
    con.commit()
else:
    quit()

con.close()