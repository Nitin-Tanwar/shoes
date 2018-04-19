from tkinter import *
win = Tk()
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
count=0
def add():
    f=open("out.txt",'a')
    shoe_company=s1.get()
    shoe_no=s2.get()
    shoe_color=s3.get()
    shoe_model=s4.get()
    shoe_price=s5.get()
    f.writelines(shoe_company.ljust(20)+shoe_no.ljust(20)+shoe_color.ljust(20)+shoe_model.ljust(20)+shoe_price.ljust(20)+"\n")
    f.close()
def next():
    f=open("out.txt",'r')
    i=0
    global count
    try:
        while(i<=count):
            l=f.readline()
            i=i+1
            l1=l.split()
        s1.set(l1[0])
        s2.set(l1[1])
        s3.set(l1[2])
        s4.set(l1[3])
        s5.set(l1[4])
        print(l1)
    except:
            m="" 
            s1.set(m) 
            s2.set(m) 
            s3.set(m) 
            s4.set(m) 
            s5.set(m)
            print("no more record found")
    count=count+1
    f.close()    
def prev():
    f=open("out.txt",'r')
    i=0
    global count
    try:
        while(i<=count-1):
            l=f.readline()
            i=i+1
            l1=l.split()
        s1.set(l1[0])
        s2.set(l1[1])
        s3.set(l1[2])
        s4.set(l1[3])
        s5.set(l1[4])
        print(l1)
    except:
            m="" 
            s1.set(m) 
            s2.set(m) 
            s3.set(m) 
            s4.set(m) 
            s5.set(m)
            print("no more record found")
    count=count-1
    f.close()
        
def delete():
    m=s1.get()
    f=open("out.txt","r")
    global count
    for line in f:
        count=count+1
    print("No. of lines in file:")
    print(count)
    f.seek(0)
    l=f.readlines() 
    print(l) 
    f.close() 
    f=open("out.txt","w") 
    for i in l: 
        l1=i.split() 
        print(l1) 
        if(l1[0]!=m): 
             f.writelines(l1[0].ljust(20)+l1[1].ljust(20)+l1[2].ljust(20)+l1[3].ljust(20)+l1[4].ljust(20)+"\n") 
    f.close()
    
def update():
    m1=s1.get() 
    m2=s2.get() 
    m3=s3.get() 
    m4=s4.get() 
    m5=s5.get() 
    f=open("out.txt","r") 
    l=f.readlines() 
    f.close() 
    f=open("out.txt","w") 
    for i in l: 
        l1=i.split() 
        if(l1[0]!=m1): 
            f.writelines(l1[0].ljust(20)+l1[1].ljust(20)+l1[2].ljust(20)+l1[3].ljust(20)+l1[4].ljust(20)+"\n") 
        else: 
            f.writelines(l1[0].ljust(20)+m2.ljust(20)+m3.ljust(20)+m4.ljust(20)+m5.ljust(20)+"\n")
    print("record updated")
    f.close()
            
        
def search(): 
    m=s1.get()
    global count
    flag=0
    f=open("out.txt","r")
    for line in f:
        count=count+1
    print("No. of lines in file:")
    print(count)
    f.seek(0)
    l=f.readlines()
    print(l)
    for i in l: 
        l1=i.split() 
        if(l1[0]==m): 
            print(l1) 
            s1.set(l1[0]) 
            s2.set(l1[1]) 
            s3.set(l1[2]) 
            s4.set(l1[3]) 
            s5.set(l1[4])
            flag=1
            break
    if(flag==0):
        print("record not found")
    else:
        print("record found")
    f.close()
def first_record():
    f=open('out.txt','r')
    global count
    flag=0
    for line in f:
        count=count+1
    print("No. of lines in file:")
    print(count)
    f.seek(0)
    l=f.readlines()
    l1=list(l)
    print("\n")
    print(l1)
    l2=l1[0].split()
    s1.set(l2[0])
    s2.set(l2[1]) 
    s3.set(l2[2]) 
    s4.set(l2[3]) 
    s5.set(l2[4])
    print("\n First Record of file is as:")
    print(l1[0])
    f.close()
    
 
def last_record():
    f=open('out.txt','r')
    count=0
    flag=0
    for line in f:
        count=count+1
    print("No. of lines in file:")    
    print(count)
    f.seek(0)
    l=f.readlines()
    l1=list(l)
    print(l1)
    l2=l1[count-1].split()
    s1.set(l2[0])
    s2.set(l2[1]) 
    s3.set(l2[2]) 
    s4.set(l2[3]) 
    s5.set(l2[4])
    print("\n Last Record of file is as:")
    print(l1[count-1])
    f.close()
  
win.configure(background='pink')
l1=Label(win,text='shoe details',bg="pink",font=('Ariel',20,'bold'))        
l2=Label(win,text='shoe company',bg="pink",font=('Ariel',10,'bold'))    
l3=Label(win,text='shoe no',bg="pink",font=('Ariel',10,'bold'))
l4=Label(win,text='shoe color',bg="pink",font=('Ariel',10,'bold'))
l5=Label(win,text='shoe model',bg="pink",font=('Ariel',10,'bold'))
l6=Label(win,text='shoe price',bg="pink",font=('Ariel',10,'bold'))
t1=Entry(win,textvariable=s1)
t2=Entry(win,textvariable=s2)
t3=Entry(win,textvariable=s3)
t4=Entry(win,textvariable=s4)
t5=Entry(win,textvariable=s5) 
b1=Button(win,text='add',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=add)
b5=Button(win,text='>',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=next)
b2=Button(win,text='update',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=update)
b3=Button(win,text='delete',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=delete)
b4=Button(win,text='search',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=search)
b6=Button(win,text='<',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=prev)
b7=Button(win,text='>|',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=last_record)
b8=Button(win,text='|<',fg="red",width=10,bg="lightyellow",font=('Ariel',10,'bold'),command=first_record)
l1.grid(row=1,column=2)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=6,column=1)
t1.grid(row=2,column=2)
t2.grid(row=3,column=2)
t3.grid(row=4,column=2)
t4.grid(row=5,column=2)
t5.grid(row=6,column=2)
b1.grid(row=8,column=1)
b2.grid(row=8,column=2)
b3.grid(row=8,column=3)
b4.grid(row=8,column=4)
b5.grid(row=11,column=1)
b6.grid(row=11,column=2)
b7.grid(row=11,column=3)
b8.grid(row=11,column=4,columnspan=2)

win.mainloop()


