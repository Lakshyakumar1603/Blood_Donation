#----- BY: BHAVNA AGARWAL --- xII A ---- PCM -----#

import mysql.connector
db= mysql.connector.connect(user='root',password='pankaj',host='localhost', database='blod')
cursor=db.cursor()
x=75

def menu():
    print("1==> SEE THE COLLECTION:")
    print("2==> ENTER NEW RECORD:")
    print("3==> UPDATE:")
    print("4==> DELETE RECORD:")
    print("5==> CREATE OR DELETE OR SEE  LOCAL USER ID:")
    print("6==> ExIT:")
    print("-"*x)

def pas():
    u=input("enter main password to enter in data:")  ### 1221 ####
    a="""select password from pass"""
    cursor.execute(a)
    d=cursor.fetchall()
    if d[0][0]!=u:
        print("Wrong password:")
        print("-"*x)
        return 1
    print("-"*x)

def pas2():
    u=int(input("enter your uid:"))               #### (1000,1001,1002,1003)####
    a="""select pass from localpass where id=%d"""%(u)
    cursor.execute(a)
    d=cursor.fetchall()
    if len(d)==0:
        print("please enter right id :")
        print("-"*x)
        return 1
    a="""select name from user where id=%d"""%(u)
    cursor.execute(a)
    a=cursor.fetchall()
    print("OK",a[0][0])
    p=int(input("enter your id password:"))      ### same as local id(1000,1001,1002,1003)####
    if p!=d[0][0]:
        print(p,d[0][0])
        print("please enter right password:")
        print("-"*x)
        return 1
    print("-"*x)
    
def enter_record():
    nm=str(input("enter donar name :"))
    nm=nm.upper()
    bg=str(input("enter blood group :"))
    bg=bg.upper()
    bd=["A+","B+","A-","B-","AB+","AB-","O+","O-"]
    if bd.count(bg)!=1:
        print("plz enter right blood group:")
        print("-"*x)
        return 1
    am=int(input("enter amount of donate :"))
    if am<100 or am>950 or am%50!=0:
        print("amount of donate is in between 100 to 950 ml and multiple of 50 also")
        print("-"*x)
        return 1
    sql="""insert into data (name,b_grp,amt) values('%s','%s',%d)"""%(nm,bg,am)
    cursor.execute(sql)
    db.commit()
    print("ok new record enter succesfully:")
    print("-"*x)


def see_record():
    sql="""select * from data"""
    cursor.execute(sql)
    d=cursor.fetchall()
    n=0
    print("|---|----------------------------|-------|-----|")
    for j in range(0,len(d)):
        for i in range(0,1):
            print("|",d[n][i],"|",d[n][i+1]," "*(25-len(d[n][i+1])),"|",d[n][i+2]," "*(4-len(d[n][i+2])),"|",d[n][i+3],"|")
        n=n+1
    print("|---|----------------------------|-------|-----|")
    a=""" select sum(amt) from data where b_grp="a+";"""
    cursor.execute(a)
    a=cursor.fetchall()
   # if a[0][0]=="None":  #  how to handle none answer or record 
        #a[0][0]=0
    aa=""" select sum(amt) from data where b_grp="a-";"""
    cursor.execute(aa)
    aa=cursor.fetchall()
   # if aa[0][0]=="":
        #aa[0][0]=0
    b=""" select sum(amt) from data where b_grp="b+";"""
    cursor.execute(b)
    b=cursor.fetchall()
    bb=""" select sum(amt) from data where b_grp="b-";"""
    cursor.execute(bb)
    bb=cursor.fetchall()
    ab=""" select sum(amt) from data where b_grp="ab+";"""
    cursor.execute(ab)
    ab=cursor.fetchall()
    abab=""" select sum(amt) from data where b_grp="ab-";"""
    cursor.execute(abab)
    abab=cursor.fetchall()
    o=""" select sum(amt) from data where b_grp="o+";"""
    cursor.execute(o)
    o=cursor.fetchall()
    oo=""" select sum(amt) from data where b_grp="o-";"""
    cursor.execute(oo)
    oo=cursor.fetchall()
    print("|--------------------------------------------------------------------------------------------------------|")
    print("|                                                TOTAL                                                   |")
    print("|--------------------------------------------------------------------------------------------------------|")
    print("| A+ =>",a[0][0],"| A- =>",aa[0][0],"| B+ =>",b[0][0],"| B- =>",bb[0][0],"| AB+ =>",ab[0][0],"| AB- =>",abab[0][0],"| O+ =>",o[0][0],"| O- =>",oo[0][0],"|")
    print("|--------------------------------------------------------------------------------------------------------|")
    print("-"*x)

def update():
    u=int(input("update record of which number:"))
    l=["name","blood group","amount of donate"]
    s="""select * from data where sno = '%s' """%(u)
    cursor.execute(s)
    d=cursor.fetchall()
    if len(d)==0:
        print("not found in data")
        return 1
    for i in range(3):
        print(i+1,"==",l[i])
    uu=int(input("update what:"))
    if uu <0 or uu>3:
        return 1
    elif uu==1:
        n=str(input("enter new name:"))
        n=n.upper()
        s="""update data set name='%s' where sno='%s'"""%(n,u)
        cursor.execute(s)
        db.commit()
    elif uu==2:
        n=str(input("enter blood group:"))
        n=n.upper()
        bd=["A+","B+","A-","B-","AB+","AB-","O+","O-"]
        if bd.count(n)!=1:
            print("plz enter right blood group:")
            return 1
        s="""update data set b_grp='%s' where sno='%s'"""%(n,u)
        cursor.execute(s)
        db.commit()
    elif uu==3:
        n=int(input("enter amount of donate:"))
        if n<500 or n>950 or (n%50)!=0:
            print("amount of donate is in between 100 to 950 ml and multiple of 50 also")
            print("-"*x)
            return 1
        s="""update data set amt='%d' where sno='%s'"""%(n,u)
        cursor.execute(s)
        db.commit()
    print("ok record is update succesfully:")
    print("-"*x)
    

        
def delete():
    n=int(input("enter number to delete from data:"))
    s="""delete from data where sno='%s'"""%(n)
    cursor.execute(s)
    db.commit()
    print("ok 1 record delet from data:")
    up2()
    print("-"*x)
    
def up2():
    s="""select sno from data"""
    cursor.execute(s)
    d=cursor.fetchall()
    L,l=[],[]
    for i in range(1,len(d)+1):
        L.append(d[i-1][0])
        l.append(d[i-1][0])
    a=len(L)
    for i in range(1,a+1):
        L[i-1]=i
    c=0
    while a>0:
        b="""update data set sno=%d where sno=%d"""%(L[c],l[c])
        cursor.execute(b)
        db.commit()
        c=c+1
        a=a-1

def codu():
    print("1==> TO CREATE USER:")
    print("2==> TO DELETE USER:")
    print("3==> TO SEE USERS:")
    u=int(input("enter your choice:"))
    if u<1 or u>3:
        print("please enter right choice:")
        return 1
    pas()
    if u==1:
        id=int(input("enter new user id:"))
        a="""select * from user where id=%d"""%(id)
        cursor.execute(a)
        a=cursor.fetchall()
        print(len(a))
        if len(a)>0:
            print("user id already are in data please enter new id:")
            return 1
        n=str(input("enter new user name:"))
        n=n.upper()
        p=int(input("enter new user password:"))
        a="""insert into user values (%d,%s)"""%(id,n)
        cursor.execute(a)
        db.commit()
        a="""insert into localpass values (%d,%d)"""%(id,p)
        cursor.execute(a)
        db.commit()
    if u==2:
        id=int(input("enter user id to delete it :"))
        a=""" select * from user where id=%d"""%(id)
        cursor.execute(a)
        a=cursor.fetchall()
        if len(a)<1:
            print("user id not found:")
            return 1
        a="""delete from user where id=%d"""%(id)
        cursor.execute(a)
        db.commit()
        a="""delete from localpass where id=%d"""%(id)
        cursor.execute(a)
        db.commit()
    if u==3:
        suser()
    print("-"*x)
        
    
def suser():
    a="""select * from user"""
    cursor.execute(a)
    a=cursor.fetchall()
    print("|-----------------------------|")
    print("| ID         |    NAME        |")
    for i in range(len(a)):
        print("| ",a[i][0],"    | ",a[i][1],"       |")
    print("|-----------------------------|")
        
        
        
        
        

x=75
xx=pas()
print("-"*x)
b=True
while True:
    if xx==1:
        break
    menu()
    d=int(input("enter your choice ==> "))
    print("-"*x)
    if d==6:
        print("thankyou dear user:")
        break
    if d<1 or d>6:
        print("plz enter right choice:")
        print("-"*x)
        continue
    else:
        if d==1:
            up2()
            a=see_record()
            if a==1:
                print("-"*x)
                continue

        elif d==2:
            a=enter_record()
            if a==1:
                print("-"*x)
                continue
        elif d==3:
            p=pas2()
            if p==1:
                print("-"*x)
                continue
            
            a=update()
            if a==1:
                print("-"*x)
                continue
        elif d==4:
            p=pas2()
            if p==1:
                print("-"*x)
                continue
            delete()
            print("-"*x)
        elif d==5:
            a=codu()
            if a==1:
                print("-"*x)
                continue
            
