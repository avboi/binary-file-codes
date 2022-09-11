import pickle
print("Welcome to menu driven program for binary files.\n1. Creating Binary\n2. Adding to binary file\n3. Reading from binary\n4. Updating into a binary\n5. Searching into binary")
k = int(input("Choose a number from above: "))

def CreateBinary():
    file = open("somebinary.dat", 'wb')
    print("File has been created")
    file.close()

    #Done! Check your file directory lmao

def Addintobinary():
    #ok so lets add some GPU 
    
    file = open("somebinary.dat", 'ab+')
    while True:
        id = int(input("GPU ID: "))
        name = input("Input name of GPU: ")
        man = input('Manufacturer Name: ')
        reld = int(input("Input year of release in numbers: "))
        cost = int(input("Enter cost: "))
        gpu = [id,name,man,reld,cost]
        pickle.dump(gpu, file)
        choice = input("Do you want to add more records(Y/N)?")
        if choice in 'Nn':
            break

def Readintobinary():
    file = open('somebinary.dat', 'rb')
    try:
        s = pickle.load(file)
        for i in s:
            print(i)
    except EOFError:
        pass
    file.close()

def Updatingbinary():
    #oh damn rtx 3090 outofstock, gotta update that
    stu = {}
    found = False
    try:
        file = open('somebinary.dat', 'rb+')
        rn = int(input("Enter id of GPU to update: " ))
        while True:
            rpos = file.tell()
            stu = pickle.load(file)
            if stu[0] == rn:
                newgpu = input("Enter new gpu name: ")
                stu[1] = newgpu
                file.seek(rpos)
                pickle.dump(stu, file)
                found = True
    except EOFError:
        if found == False:
            print('No such GPU found')
        else:
            print('Record has been updated')
            file.close()

def SearchBinary():
    file = open('somebinary.dat')
    search = int(input("Enter GPU id to search"))
    found = False
    try:
        while True:
            data = pickle.load(file)
            for record in data:
                if record[0] == search:
                    print('GPU name: ', record[1])
                    print('GPU Manufacturer: ', record[2])
                    print('GPU Release Year: ', record[3])
                    print('GPU Price: ', record[4]+'$')
                    found = True
    except Exception:
        file.close()
    if found == True:
        print("Record has been found")

    



if k == 1:
    CreateBinary()
elif k == 2:
    Addintobinary()
elif k == 3:
    Readintobinary()
elif k == 4:
    Updatingbinary()
elif k == 5:
    SearchBinary()
else:
    print("Number invalid.... Exited code")