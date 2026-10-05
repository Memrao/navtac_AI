# Bank classes

# class Bank:
#     def __init__(self, name,number, balance, account_type, branch):
#         self.name=name
#         self.number=number
#         self.balance=balance
#         self.account_type=account_type
#         self.branch=branch
# bank1=Bank("Memona","03303967609", "200000", "Saving", "Malir Cantt")
# print(f"Name: {bank1.name} \nNumber: {bank1.number} \nBalance:{bank1.balance} \nAccount Type: {bank1.account_type} \nBranch: {bank1.branch}")


    
class student:
    def __init__(self, name, age, roll_no, semester, course, year):
        self.name=name
        self.age=age
        self.roll_no=roll_no
        self.semester=semester
        self.course=course
        self.year=year
std=student("Memona",21, 14393, "4th", "BESE","2025")       
print(f"Name: {std.name} \nAge: {std.age} \nRoll_no: {std.roll_no} \nSemester: {std.semester} \nCourse: {std.course} \nYear: {std.year}")
