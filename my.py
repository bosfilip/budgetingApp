import mysql.connector

def spent(name, sAmount, eDate):

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="aJopek1608",
        database="budgetdb"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES LIKE 'spent'")
    result = mycursor.fetchone()
    if result:
        q = "INSERT INTO spent(name, amount, date) VALUES(%s, %s, %s)"
        v = (name, sAmount, eDate)
        mycursor.execute(q,v)
        mydb.commit()
    else:
        mycursor.execute("CREATE TABLE spent(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(500) NOT NULL, amount DECIMAL(10,2) NOT NULL, date DATE NOT NULL);")
        q = "INSERT INTO spent(name,amount,date) VALUES(%s, %s, %s)"
        v = (name, sAmount, eDate)
        mycursor.execute(q,v)
        mydb.commit()
def deposit(name, dAmount, dDate):

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="aJopek1608",
        database="budgetdb"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW TABLES LIKE 'deposit'")
    result = mycursor.fetchone()
    if result:
        q = "INSERT INTO deposit(name, amount, date) VALUES(%s, %s, %s)"
        v = (name, dAmount, dDate)
        mycursor.execute(q, v)
        mydb.commit()
    else:
        mycursor.execute(
            "CREATE TABLE deposit(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(500) NOT NULL, amount DECIMAL(10,2) NOT NULL, date DATE NOT NULL);")
        q = "INSERT INTO deposit(name,amount,date) VALUES(%s, %s, %s)"
        v = (name, dAmount, dDate)
        mycursor.execute(q, v)
        mydb.commit()

def expenseList(date1, date2):

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="aJopek1608",
        database="budgetdb"
    )

    mycursor = mydb.cursor()

    q = "SELECT * FROM spent WHERE date BETWEEN %s AND %s;"
    v = (date1, date2)
    mycursor.execute(q,v)
    mydb.commit()
def depositList():
    pass

def BackEngine():
    pass

def user():
    print("Wellcome to budgeting app")
    w1 = input("What would you like to do?\n"
               "To add new expense type 'e'\n"
               "To add new deposit type 'd'\n"
               "To check expenses/deposits within a specific period, type 'h'\n"
               "To check expenses/deposits for this month type 'm'\n"
               "Input: ")
    if w1 == "e":
        eName = input("Enter name of expense: ")
        sAmount = input("Enter amount spent: ")
        eDate = input("Enter date for this expense: ")
        spent(eName, sAmount, eDate)
    elif w1 == "d":
        dName = input("Enter name of deposit: ")
        dAmount = input("Enter amount of deposit: ")
        dDate = input("Enter date for this deposit: ")
        deposit(dName, dAmount, dDate)
    elif w1 == "h":
        wh1 = input("Do you want to see expenses or deposits for a specific period?\n"
                    "For expense history type 'e'\n"
                    "For deposit history type 'd'\n"
                    "Input: ")
        if wh1 == "e":
            periodD = input("Input the desired date range for viewing your expense history\n"
                            "ex. YYYY-MM-DD to YYYY-MM-DD\n"
                            "Input: ")
            periodD = periodD.split(" to ")
            date1 = periodD[0].strip()
            date2 = periodD[1].strip()
            expenseList(date1, date2)
        elif wh1 == "d":
            depositList()

        dbEngine()
    elif w1 == "m":
        dbEngine()

user()



