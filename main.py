import pickle
import os

def addentry():
    service=input('enter the service: ')
    username=input('enter username: ')
    password=input('enter password: ')
    entry=[service,username,password] 
    with open('data.bat','ab') as file:
        pickle.dump(entry,file)
        print('data entered')
    wait=input('press any key to continue: ')
    print('\n'*50)


def search():
    search=input('enter service: ')
    with open('data.bat','rb') as file:
        while True:
            try:
                data=pickle.load(file)
                if data[0]==search:
                    print(data)
            except:
                print('data not found')
                break
    wait=input('press any key to continue: ')
    print('\n'*50)

def remove():
    search=input('enter service: ')
    file1=open('data.bat','rb')
    file2=open('temp.bat','wb')
    while True:
        try:
            data=pickle.load(file1)
            if data[0]!=search:
                pickle.dump(data)
        except:
            break
    file1.close()
    file2.close()
    os.remove('data.bat')
    os.rename('temp.bat','data.bat')
    print('data removed successfully')
    wait=input('press any key to continue: ')
    print('\n'*50)

def show():
    with open('data.bat','rb') as file1:    
        while True:
            try:
                data=pickle.load(file1)
                print(data)
            except:
                break   
    print('\n'*1)
    wait=input('press any key to continue: ')
    print('\n'*50)


masterpass=input('enter master password')
if masterpass=='pass':
    print('welcome....')
    while True:
        print('chose your function....')
        print('1. add a new entry')
        print('2. search an existing entry')
        print('3. remove an existing entry')
        print('4. show full database')
        print('5. exit')

        choice=int(input('enter function number:'))
        if choice==1:
            addentry()
        if choice==2:
            search()
        if choice==3:
            remove()
        if choice==4:
            show()
        if choice==5:
            end = input('are you sure that you want to exit[y/n]: ')
            if end.lower() == 'y':
                break
            if end.lower() == 'n':
                continue

else:
    print('master password was incorrect')
