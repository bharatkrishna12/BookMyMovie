class project1():
    list_for_test1=[]
    list_for_test2=[]
    Booked_Ticekt_Count=0
    Booked_Ticekt_Count_up_even=0
    Booked_Ticekt_Count_down_even=0
    Booked_Ticekt_Count_up_odd=0
    Booked_Ticekt_Count_down_odd=0
    @classmethod
    def detail(cls):
        name=input("Enter a name :")
        gen=input("Enter a gender :")
        while gen.lower() not in ["male","female","tansgender"]:
            print("Plz Enter valid gender")
            gen=input("Enter a gender :")
        age=(input('Enter age'))
        while age.isnumeric()==False or len(age)!=2:
            print('Plz Enter valid age')
            age=(input("Enter age :"))
        phone_num=(input("Enter Your number :"))
        while phone_num.isnumeric()==False or len(phone_num)>10 or len(phone_num)<10:
            print("Plz Enter valid phone number")
            phone_num=input("Enter your number :")
        return name , gen ,age,phone_num
    @classmethod
    def Buy_a_Ticket(cls):
        detail_of_customer={}
        try:
            rows=int(input("Enter a row number between 1 to {} \n".format(cls.row)))
            while rows not in range(1,cls.row+1):
                print("Plz enter valid row number")
                rows=int(input("Enter a row number between 1 to {} \n".format(cls.row)))
            columns=int(input('Enter a seat number between 1 to {}\n'.format(cls.column)))
            while columns not in range(1,cls.column+1):
                print("Plz enter valid seat number")
                columns=int(input('Enter a seat number between 1 to {}\n'.format(cls.column)))
            rows=rows-1
            columns=columns-1
            if cls.total_seats<=60:
                if cls.seats[rows][columns]=="b":
                    print('This is seat is booked')
                    print('Try other')
                else:
                    print("The  price of ticket: $10")
                    print("Type Yes or No to confirmm or cancel ")
                    i=input("Type here \n")
                    while i.upper() not in ["YES","NO"]:
                        print("Plz Enter  Yes Or No ")
                        i=input("Type here \n")
                    if i.upper()=="YES":
                        name,gen,age,phone_num=project1.detail()
                        cls.seats[rows][columns]="b"
                        cls.detail_of_customer[cls.seats[rows][columns]]={"Name":name,"Gender":gen,"Age":age,"Phone_number":phone_num,"Ticket_Price":"10"}
                        cls.Booked_Ticekt_Count+=1# this for increase the purchase ticket count
                        print("Booked Successfully")
                    else:
                        print('Thank you for visiting')
                        
            if cls.total_seats>60:
                if cls.row%2==0:
                    cls.list_for_test1=[i for i in range(0,cls.row//2)]
                    if rows in cls.list_for_test1:
                        if cls.seats[rows][columns]=='b':
                            print("This seat is booked")
                            print("Try other")
                        else:
                            print("The price of ticekt : $10")
                            print("Type Yes or No to confirm or cancel ")
                            i=input("Type here  \n")
                            while i.upper() not in ["YES","NO"]:
                                print("Plz Enter  Yes Or No ")
                                i=input("Type here \n")

                            if i.upper()=="YES":
                                name,gen,age,phone_num=project1.detail()
                                cls.seats[rows][columns]="b"
                                cls.detail_of_customer[cls.seats[rows][columns]]={"Name":name,"Gender":gen,"Age":age,"Phone_number":phone_num,"Ticket_Price":"10"}
                                cls.Booked_Ticekt_Count_up_even+=1# this for increase the purchase ticket count

                                print('Thank you for booking')

                            else:
                                print('Thank you for visiting')
                    else:
                        cls.list_for_test2=[i for i in range(cls.row//2,cls.row)]
                        if rows in cls.list_for_test2:
                            if cls.seats[rows][columns]=='b':
                                print("This seat is booked")
                                print("Try other")
                            else:
                                print("The price of ticekt : $8")
                                print("Type Yes or No to confirm or cacel ")
                                i=input("type here \n")
                                while i.upper() not in ["YES","NO"]:
                                    print("Plz Enter  Yes Or No ")
                                    i=input("Type here \n")

                                if i.upper()=="YES":
                                    name,gen,age,phone_num=project1.detail()
                                    cls.seats[rows][columns]="b"
                                    cls.detail_of_customer[cls.seats[rows][columns]]={"Name":name,"Gender":gen,"Age":age,"Phone_number":phone_num,"Ticket_Price":"10"}  

                                    cls.Booked_Ticekt_Count_down_even+=1# this for increase the purchase ticket count

                                    print("Thank you for booking")
                                else:
                                    print('Thank your for visiting')

                else:
                    cls.list_for_test1=[i for i in range(0,cls.row)]

                    if rows in cls.list_for_test1:
                        if rows<(cls.row-1)//2:
                            if cls.seats[rows][columns]=='b':
                                print("This seat is booked")
                                print("Try other")
                            else:
                                print("The price of ticekt : $10")
                                print("Type Yes or No to confirm or cancel ")
                                i=input("type here \n")
                                while i.upper() not in ["YES","NO"]:
                                    print("Plz Enter  Yes Or No ")
                                    i=input("Type here \n")

                                if i.upper()=="YES":
                                    name,gen,age,phone_num=project1.detail()
                                    cls.seats[rows][columns]="b"
                                    cls.detail_of_customer[cls.seats[rows][columns]]={"Name":name,"Gender":gen,"Age":age,"Phone_number":phone_num,"Ticket_Price":"10"}  

                                    cls.Booked_Ticekt_Count_up_odd+=1# this for increase the purchase ticket count


                                    print("Thank you for booking")

                                else:
                                    print('Thank you for visiting')

                        elif rows<cls.row:
                            if cls.seats[rows][columns]=='b':
                                print("This seat is booked")
                                print("Try other")
                            else:
                                print("The price of ticekt : $8")
                                print("Type Yes or No to confirm or cancel ")
                                i=input("\n type here ")
                                while i.upper() not in ["YES","NO"]:
                                    print("Plz Enter  Yes Or No ")
                                    i=input("Type here \n")

                                if i.upper()=="YES":
                                    name,gen,age,phone_num=project1.detail()
                                    cls.seats[rows][columns]="b"
                                    cls.detail_of_customer[cls.seats[rows][columns]]={"Name":name,"Gender":gen,"Age":age,"Phone_number":phone_num,"Ticket_Price":"10"}  

                                    cls.Booked_Ticekt_Count_down_odd+=1# this for increase the purchase ticket co
                                    print("Thank you for booking")
                                else:
                                    print("Thank you for visiting")
        except ValueError:
            print("Thank you for visiting")
        except UnboundLocalError :
            print('Thank you for visiting')

class project(project1):
    print('Creat The Auditorium')
    row=input("Enter the number of rows:")
    column=input("Enter the number of seats in each row:")
    while row.isnumeric()==False or column.isnumeric()==False:
        print("plz enter valid charchters")
        row=input("Enter the number of rows:")
        column=input("Enter the number of seats in each row:")
    row=int(row)
    column=int(column)
    total_seats=row*column
    seats=[]
    detail_of_customer={}
    
    for i in range(row):
                seats.append(["s"]*column)
            
    def showseats(self):
        flag=True
        for i in range(1,self.column+1):
            if i==1:
                print(' ',i,end='')
            elif i<=self.column-1:
                print('',i,end='')
            if i==self.column:
                    print('',i,end='\n')
        for num in range(0,self.row):
            print(num+1,'',end='')
            print(' '.join(self.seats[num]))
        for i in range(0,self.row):
            for k in range(0,self.column):
                if self.seats[i][k]=='b':
                    print('{}th ROW,{}th COL\n BOOKED \n'.format(i+1,k+1))
                    flag=False
        if flag==True:
            print("ALL SEATS ARE VACANT")
            
    def menu(self):
        print('1.Show the seats')
        print('2.Buy a Ticket')
        print('3.Statistics')
        print('4.Show booked Tickets User Info')
        print('0.Exit')

    def Ticket_user_info(self):
        try:
            r=int(input('Enter a row number :'))
            r=r-1
            c=int(input('Enter a seat number :'))
            c=c-1
            if r>self.row or c>self.column:
                print('No such  row and column number')
            else:
                k=self.seats[r][c]
                if k!='b':
                    print('You are not able to access it')
                else:
                    print(self.detail_of_customer[k])
        except ValueError :
            print("You are not able to access it")
        
    def Statistics(self):
        percentage_of_Tickets_booked=self.Booked_Ticekt_Count/self.total_seats*100 # here we calculate percentage of ticket booked
        Total_Income=0
        current_Income=0
        if self.total_seats<=60:
            Total_Income=self.total_seats*10
            percentage_of_Tickets_booked=self.Booked_Ticekt_Count/self.total_seats*100
            current_Income=self.Booked_Ticekt_Count*10
        else:
            # here all total income,percentage_of_Tickets_booked
            Total_Income=self.total_seats*10
            percentage_of_Tickets_booked=(self.Booked_Ticekt_Count_up_even+self.Booked_Ticekt_Count_down_even+self.Booked_Ticekt_Count_down_odd+self.Booked_Ticekt_Count_up_odd)/self.total_seats*100
            if self.row%2==0:
                a=self.Booked_Ticekt_Count_up_even * 10
                b=self.Booked_Ticekt_Count_down_even * 8
                current_Income=a+b
            
            else:
                current_Income=(self.Booked_Ticekt_Count_up_odd*10)+(self.Booked_Ticekt_Count_down_odd*8)
        print('Number of Purchased Tickets :',self.Booked_Ticekt_Count+self.Booked_Ticekt_Count_up_even+self.Booked_Ticekt_Count_down_even+self.Booked_Ticekt_Count_down_odd+self.Booked_Ticekt_Count_up_odd)
        print('Percentage of Tickets booked :',round(percentage_of_Tickets_booked,2))
        print('Total income :',Total_Income)
        print('Current income :',current_Income)

        
pk=project() 
pk.menu()
a=input()
while a.isnumeric()==False or int(a) not in range(0,4+1):
    print('Enter right key')
    a=input()
a=int(a)
while a!=0:
    if a==1:
        pk.showseats()
    elif a==2:
        pk.Buy_a_Ticket()
    elif a==3:
        pk.Statistics()
    elif a==4:
        pk.Ticket_user_info()
    pk.detail_of_customer
    pk.menu()
    a=input()
    while a.isnumeric()==False or int(a) not in range(0,4+1):
        print('Enter right key')
        a=input()
    a=int(a)