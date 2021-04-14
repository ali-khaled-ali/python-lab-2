import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="lmessi10",
    database='pydatabase'
)
cur = mydb.cursor()

# mycursor.execute("CREATE DATABASE pydatabase")
# cur.execute(''' DROP TABLE employees''')
# cur.execute('''create table  employees(
#             id int primary key not null,
#             full_name text not null,
#             email char(50) not null,
#             salary int not null,
#             isManager BOOL,
#             isHired BOOL
#             );''')


class Person:
    def __init__(self, full_name, money, sleepmood='tired', healthRate='75'):
        self.full_name = full_name
        self.money = money
        self.sleepmood = sleepmood
        self.healthRate = healthRate

    def sleep(self, hours):
        print('sleep')
        if (hours == 7):
            self.sleepmood = 'happy'
        elif (hours < 7):
            self.sleepmood = 'tired'
        else:
            self.sleepmood = 'lazy'

    def eat(self, meals):
        print('eat')
        if (meals == 3):
            self.healthRate = 100
        if (meals == 2):
            self.healthRate = 75
        if (meals == 1):
            self.healthRate = 50

    def buy(self, items):
        print('buy')
        self.money -= 10 * items


class Employee(Person):
    def __init__(self, id, full_name, email, salary, is_manager, workmood='tired', money=1000):
        Person.__init__(self, full_name, money, sleepmood='tired', healthRate='75')
        self.id = id
        self.email = email
        self.workmood = workmood
        self.salary = salary
        self.is_manager = is_manager

        sql = ('''Insert into employees
                    values(%s, %s, %s, %s, %s,%s)
                    ''')
        values = (self.id, self.full_name, self.email, self.salary, self.is_manager, 0)
        cur.execute(sql, values)
        mydb.commit()

    def work(self, hours):
        print('work')
        if (hours == 8):
            self.workmood = 'happy'
        if (hours > 8):
            self.workmood = 'tired'
        else:
            self.workmood = 'lazy'

    def sendEmail(self):
        print('send Email')


class Office:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
    @staticmethod
    def get_all_employees():
        print('all emp')
        cur.execute('select * from employees')
        rows = cur.fetchall()
        return rows

    @staticmethod
    def get_employee(empid):
        print('emp')
        sql = 'select * from employees where id = %s'
        cur.execute(sql, empid)
        rows = cur.fetchall()
        return rows

    @staticmethod
    def fire(empid):
        print('fire')
        sql = 'Update employees set isHired = %s where id = %s'
        value = ('0', empid)
        cur.execute(sql, value)
        cur.execute(sql, empid)

    @staticmethod
    def hire(empid):
        print('hire')
        sql = 'update employees set isHired = %s where id = %s'
        value=('1',empid)
        cur.execute(sql,value)
        mydb.commit()


# emp = Employee('alikhaled',1000,1,'lolo','good',1000,0)
# # #
# emp.buy(10)
# # #
# print(emp.money)

def input_menu():
    inp = input('enter your option\n'
                'add employee: add\n'
                'hire employee: hire\n'
                'fire employee: fire\n'
                'get all employees: getall\n'
                'get one employee: getemp\n'
                'quit menu: q \n')
    return inp


def add_emp_menu():
    value = []
    inp = input("enter id of employee: ")
    value.append(int(inp))
    inp = input("enter name of employee: ")
    value.append(inp)
    inp = input("enter email of employee: ")
    value.append(inp)
    inp = input("enter salary of employee: ")
    value.append(int(inp))
    inp = input("enter status of employee:\n"
                "if manager enter mngr:\n"
                "if not enter nrml: \n")
    if (inp == 'mngr'):
        value.append(1)
    else:
        value.append(0)

    return value


inp = input_menu()

while inp != 'q':
    if inp == 'add':
        emp = add_emp_menu()
        Employee(emp[0], emp[1], emp[2], emp[3], emp[4])
    elif inp == 'hire':

        Office.hire(1)
    elif inp == 'fire':
        Office.fire(int(input('enter the id of the employee ')))
    elif inp == 'get all':
        all_emp = Office.get_all_employees()
        for x in all_emp:
            print(x)
    elif inp == 'get emp':
        print(Office.get_employee(int(input('enter the id of the employee'))))
    inp = input_menu()
