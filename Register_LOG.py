#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def register():
    print('=======REGISTRATION========')
    file=open('file.txt','a')
    file=open('file.txt','r')
    username=input('enter username:')
    password=input('enter password:')
    m,n=[],[]
    for i in file:
        a,b=i.split(',')
        b=b.strip()
        m.append(a)
        n.append(b)
    d=dict(zip(m,n))
    def is_valid(x):
        special_chr=['!','@','#','$','%','&','*']
        if not any([i.isupper() for i in x]):
            return False
        if not any([i.islower() for i in x]):
            return False
        if not any([i.isdigit() for i in x]):
            return False
        if not any([i in special_chr for i in x]):
            return False
        return True
    special_chr=['!','@','#','$','%','&','*']
    if is_valid(password)==False:
        print('password must contain atleast one uppercase,lowercase,special character and a digit')
    elif  username[0] in special_chr or username[0].isdigit():
        print('username doesnt start with number or special characters')
    elif username in m:
        print('user already registered')
    elif username in m:
        print('already a user try to login')
    elif "@" not in username:
        print("Enter valid mail id")
    elif "."not in username:
        print("Enter valid mail id")
    elif "@." in username:
        print("There cannot be any '.' immediate next to '@'")
    elif ".@" in username:
        print("Enter valid mail id")
    elif username.index("@")==0:
        print("Enter valid mail id")
    else:
        file=open('file.txt','a')
        file.write(username+','+password+'\n')
        print('thank you for registering')

def login():
    print('=======LOGIN=======')
    file=open('file.txt','r')
    username=input('enter username:')
    password=input('enter password:')
    m,n=[],[]
    for i in file:
        a,b=i.split(',')
        b=b.strip()
        m.append(a)
        n.append(b)
    d=dict(zip(m,n))
    if '@.' in username:
        print('INVALID'+'\n'+'Enter a proper mail id')
        login()
    try:
        if username in m:
            if d[username]==password:
                print('login successful')
            else:
                print('wrong password')
                x=input('retrieve password? yes or no:').lower()
                if x=='yes':
                    print('your password is:'+d[username])
        else:
            print('username not registered,Please register')
            register()
    except:
        print('login error')
    
def home():
    print('Would you like to register or login?')
    option=input('Enter 1 to register or 2 to login?:').lower()
   
    if option=='2':
        login()
    elif option=='1':
        register()
    else:
        print('invalid Entry')

home()



