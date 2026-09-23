import mysql.connector as msql
#ESTABISHING CONNECTION
con=msql.connect(host="localhost",user="root",passwd="0143",database="SDIBANK",use_pure=True)
cur=con.cursor()
#defing functions
def withdraw():
    ID = int(input("ENTER ID : "))
    PASS = int(input("ENTER PASSWORD : "))
    wd = int(input("ENTER AMOUNT TO WITHDRAW : "))

# 1. Get current balance
    q = "SELECT balance FROM users WHERE id={} AND pass={}".format(ID, PASS)
    cur.execute(q)
    res = cur.fetchall()

    if res == []:
        print("ACCOUNT NOT FOUND OR PASSWORD INCORRECT")
        main()
    else:
        current_balance = res[0][0]

        # 2. Check if balance is enough
        if wd > current_balance:
            print("INSUFFICIENT BALANCE")
            main()
        else:
            try:
                # 3. Withdraw money
                q2 = "UPDATE users SET balance = balance - {} WHERE id={} AND pass={}".format(wd, ID, PASS)
                cur.execute(q2)
                con.commit()
                print("SUCCESSFULLY WITHDRAWN:", wd)
                print("NEW BALANCE:", current_balance - wd)
                s=int(input("ENTER 1 TO RESTART ANY-OTHER TO EXIT "))
                if s==1:
                    main()
                else:
                    exit()
            except:
                print("ERROR OCCURRED, TRY AGAIN")

def changepass():
    ID=int(input("ENTER ID : "))
    PASS=int(input("ENTER OLD PASSWORD : "))
    newpass=int(input("ENTER NEW PASSWORD : "))
    q="update users set pass={} where id={} AND PASS={}".format(newpass,ID,PASS)
    cur.execute(q)
    con.commit()
    print("PASSWORD HAS BEEN CHANGED")
    s=int(input("PRESS 1 TO RESTART ANYOTHER TO EXIT "))
    if s==1:
            main()
    else:
            exit()

def addbal():
        AMT = int(input("ENTER AMOUNT TO DEPOSIT : ")) 
        ID  = int(input("ENTER ID : "))
        PAS = int(input("ENTER PASSWORD : "))
        q = "UPDATE users SET balance = balance + {} WHERE pass = {} AND id = {}".format(AMT, PAS, ID)
        cur.execute(q)
        con.commit()
        print("AMOUNT DEPOSITED : ",AMT)
        s=int(input("PRESS 1 TO RESTART ANYOTHER TO EXIT "))
        if s==1:
            main()
        else:
            exit()
def login():
    ids=int(input("ENTER BANK-ID : "))
    pas=int(input("ENTER PASSWORD : "))
    q = "SELECT * FROM users WHERE id = {} and pass={}".format(ids,pas)
    cur.execute(q)
    r=cur.fetchall()
    if r==[]:
        print("\t\t\tSORRY YOU'R ACCOUNT DOESN'T EXIST \n\t\t\t\tPLEASE CREATE ONE ")
        main()
    if r!=[]:
        print("1.CHECK BALANCE \t\t\t \t\t2.ADD BALANCE TO YOUR ACCOUNT")
        print("3.CHANGE PASSWORD\t\t\t\t4.WITHDRAW MONNEY")
        print("\n\t\t\t5.EXIT ")
        y=int(input("ENTER CHOICE : "))
        if y==2:
            addbal()
        elif y==1:
            for k in r:
                print("BALANCE : ",k[2])
                s=int(input("PRESS 1 TO RESTART ANYOTHER TO EXIT "))
                if s==1:
                    main()
                else:
                    exit()
        elif y==3:
             changepass()
        elif y==4:
                withdraw()
        elif y==5:
            exit()
def register():
    try:
        ids=int(input("ENTER ID : "))
        name=input("ENTER NAME : ")
        
        print("\t\t\tPLEASE ONLY CHOOSE FROM MENU ")
        print("\t 1.SAVINGS \t\t\t\t\t 2.CURRENT ACCOUNT ")
        acc=int(input("ENTER ACCOUNT-TYPE : "))
        if acc==1:
            at="SAVINGS"
        elif acc==2:
            at="CURRENT ACCOUNT"
        else:
            print("PLEASE CHOOSE FROM MENU ONLY ")
            register()
        age=int(input("ENTER AGE : "))
        if age<18:
            print("\t\t\tSORRY YOU ARE UNDERAGE ")
            main()
        pa=int(input("ENTER PASS : "))
        qe="insert into users values({},'{}',0,'{}',{},{})".format(ids, name,at, age, pa)
        cur.execute(qe)
        con.commit()
        print("\t\t\tACCOUNT  CREATED SUCCESSFULLY ")
        main()
    except:
        print("\t\t\t PLEASE ENTER VALID INPUT ")
        register()
#MainScreen-layout
def main():
    try:
        print("\t\t\t--------SDI BANK---------")
        print("\t 1.LOGIN \t\t\t\t\t 2.REGISTER ")
        x=int(input("ENTER CHOICE : "))
        if x==1:
            login()
        elif x==2:
            register()
        else:
            print("ONLY  CHOOSE FROM MENU ")
            main()
    except:
        print("\t\t^-^-----------PLEASE ENTER CAREFULLY-----------^-^")
        main()
main()

    
    
