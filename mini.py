import mysql.connector
import datetime




def book():
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
)
    cur=con.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    con.close()
    return rows


def member():
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
)
    cur=con.cursor()
    cur.execute("SELECT * FROM member")
    rows=cur.fetchall()
    con.close()
    return rows

def issue():
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM issue")
    rows=cur.fetchall()
    con.close()
    return rows

def returns():
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM return_")
    rows=cur.fetchall()
    con.close()
    return rows

def payment():
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("SELECT * FROM payment")
    rows=cur.fetchall()
    con.close()
    return rows

def ins_mem(mem_date,mem_name,phone_no,passwords):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("INSERT INTO  member(mem_date,mem_name,phone_no,passwords) VALUES(%s,%s,%s,%s)",(mem_date,mem_name,phone_no,passwords))
    con.commit()
    con.close()

def ins_book(book_name,amount,author):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("INSERT INTO book(book_name,amount,author) VALUES(%s,%s,%s)",(book_name,amount,author))
    con.commit()
    con.close()
    
    
def ins_issue(member_id,book_id,issue_date):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("INSERT INTO issue VALUES (%s,%s,%s)",(member_id,book_id,issue_date))
    con.commit()
    con.close()

def ins_return(book_id,member_id,return_date,ret_status):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("INSERT INTO return_ VALUES (%s,%s,%s,%s,%s)",(book_id,member_id,return_date,ret_status,None))
    con.commit()
    con.close()

def upd_pay(payment_id,fine):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("UPDATE payment SET fine=%s WHERE payment_id=%s",(fine,payment_id))
    con.commit()
    con.close()

def payd(payment_id):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.callproc('pay_done',[payment_id])
    con.commit()
    con.close()


def upd_payid():
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.callproc('upd_pay_id')
    con.commit()
    con.close()

def fine():
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.callproc('fine')
    con.commit()
    con.close()

def ret_date(issue_date,ret):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    result=cur.callproc('return_date',[issue_date,ret])
    con.close()
    return result

def login(mem_id,passw,res):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    result=cur.callproc('login',[mem_id,passw,res])
    con.close()
    return result
    
# res=ret_date("2020-03-09"," ")
# print(res[1])

#for row in member():
    #print(row)

# res=login(1,"ddv"," ")
# print(res[2])

def ret_bk(mem_id,bk_id):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("Update return_ set ret_status=0 where member_id=%s and book_id=%s",(mem_id,bk_id))
    con.commit()
    con.close()

def search(name):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("select * from book where book_name='%s'"%(name))
    rows=cur.fetchall()
    con.close()
    return rows

def avail(bk_id,ret):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    result=cur.callproc('avail',[bk_id,ret])
    con.close()
    return result

def search_pay(mem_id):
    con = mysql.connector.connect(
    user="root", 
    password = "tiger", 
    host="localhost", 
    database = "mini"
    
    )
    cur=con.cursor()
    cur.execute("select * from payment where member_id='%s'"%(mem_id))
    rows=cur.fetchall()
    con.close()
    return rows


