# While loop

email="memona@gmail.com"
password="123"
status="Studied"


while True:
    user_email=input("Enter your email   ")
    user_password=input("Enter your password   ")
    user_status=input("Enter your status   ")

    if(email==user_email and password==user_password and status==user_status):
        break
    print("Try again")

print("Login Successful")    


