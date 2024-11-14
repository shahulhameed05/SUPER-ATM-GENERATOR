from tkinter import *
from PIL import ImageTk, Image

def show_frame(frame):
    frame.tkraise()

Accounts = { 'Username' : ['shahul', 'Priyanshu', 'Dhruv'],
            'Password' : ['1234', '5678', '1111'],
            'AccountNo' : [21002170610021, 21002170610022, 21002170610023],
            'Balance' : [10000, 5000, 7000]
}

index = -1

window = Tk()

window.title('SUPER-ATM-GENERATOR')
window.iconbitmap('./images/moneyIcon.ico')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)
window.geometry('854x480')
window.resizable(0,0)

login = Frame(window)
Menu = Frame(window)
withdraw = Frame(window)
withdraw_next = Frame(window)
Transfer = Frame(window)
Transfer_Amount = Frame(window)
Balance = Frame(window)
Deposit = Frame(window)
changePin = Frame(window)
EnterPin = Frame(window)
ReEnterPin = Frame(window)
PinChanged = Frame(window)

for frame in (login, Menu, withdraw, withdraw_next, Balance, Deposit, Transfer, Transfer_Amount,changePin,EnterPin, ReEnterPin, PinChanged):
    frame.grid(row=0,column=0,sticky='nsew')

# ==========LOGIN PAGE ===========

imgbg =Image.open('./images/backgroundimage.jpg')
loginbg = ImageTk.PhotoImage(imgbg)
bglabel = Label(login, image=loginbg)
bglabel.place(x = 0,y = 0)


img = Image.open('./images/moneylogo.png')
img = img.resize((50,50))
img = ImageTk.PhotoImage(img)
img_label = Label(login, image = img)
img_label.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label.config(bg='#230444')


txt = Label(login, text='Login')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(275), pady=(0, 60))

txt = Label(login, text='Username :')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=3, column=2, pady=(0, 8))

input_name = Entry(login, width=20, font=('Arial', 20))
input_name.grid(row=4, column=2, pady=(0, 20))

txt = Label(login, text='Password :')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=5, column=2, pady=(0, 8))

passw_var = StringVar()
input_password = Entry(login, width=20, textvariable = passw_var, show= '*', font=('Arial', 20))
input_password.grid(row=6, column=2, pady=(0, 20))

def submit():
    name = input_name.get()
    password = input_password.get()
    global index
    j = -1
    for i in Accounts['Username']:
        j = j + 1
        if (name == i and password == Accounts['Password'][j]):
            incorrect['text']=''
            index = j
            print(index)
            show_frame(Menu)
            break
        else:
            incorrect['text']='Incorrect Credential'
    
        
btn = Button(login, text='Login', width=10, height=2, command=submit)
btn.grid(row=7, column=2)

incorrect = Label(login, text='',fg='red',bg='#d2ebe9')
incorrect.grid(row=8, column=2, pady=(0, 20))

show_frame(login)

def checkBal():
    amt = amount_Input.get()

    if amt != '':
        amt = float(amt)
        if(amt < Accounts['Balance'][index]):
            Accounts['Balance'][index] -= amt
            header['text'] = 'Collect Your Cash💸'
        else:
            header['text'] = 'Insufficient Balance⛔'

    bal_val['text'] = Accounts['Balance'][index]
    show_frame(withdraw_next)

def AddBal():
    amt = amount_Input_Deposit.get()

    if amt != '':
        amt = float(amt)
        Accounts['Balance'][index] += amt
        header['text'] = 'Your Amount is Added'

    bal_val['text'] = Accounts['Balance'][index]
    show_frame(withdraw_next)

# ==========Menu PAGE ===========

imgbg2 =Image.open('./images/backgroundimage.jpg')
loginbg2 = ImageTk.PhotoImage(imgbg2)
bglabel2 = Label(Menu, image=loginbg2)
bglabel2.place(x = 0,y = 0)

img2 = Image.open('./images/moneylogo.png')
img2 = img2.resize((50,50))
img2 = ImageTk.PhotoImage(img2)
img_label2 = Label(Menu, image = img2)
img_label2.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label2.config(bg='#230444')
# Menu.config(bg='#230444')

txt = Label(Menu, text='Select Transaction')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(180), pady=(0, 40),columnspan=2)

withdraw_button = Button(Menu, text='Cash Withdrawal', width=25, height=2, command=lambda:show_frame(withdraw))
withdraw_button.grid(row=2, column=2, pady=(8))

Deposit_button = Button(Menu, text='Deposit', width=25, height=2, command=lambda:show_frame(Deposit))
Deposit_button.grid(row=3, column=2, pady=(8))

Transfer_button = Button(Menu, text='Transfer', width=25, height=2, command=lambda: show_frame(Transfer))
Transfer_button.grid(row=2, column=3, pady=(8))

Balance_button = Button(Menu, text='Balance Inquiry', width=25, height=2, command=checkBal)
Balance_button.grid(row=3, column=3, pady=(8))

ChangePin_button = Button(Menu, text='Change Pin', width=25, height=2, command=lambda: show_frame(changePin))
ChangePin_button.grid(row=4, column=2, pady=(8))

# ==========Withdrawal PAGE ===========

imgbg3 =Image.open('./images/backgroundimage.jpg')
loginbg3 = ImageTk.PhotoImage(imgbg3)
bglabel3 = Label(withdraw, image=loginbg3)
bglabel3.place(x = 0,y = 0)

img3 = Image.open('./images/moneylogo.png')
img3 = img3.resize((50,50))
img3 = ImageTk.PhotoImage(img3)
img_label3 = Label(withdraw, image = img3)
img_label3.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label3.config(bg='#230444')

txt = Label(withdraw, text='Enter Amount')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(18), pady=(5, 40), columnspan=3)

amount_Input = Entry(withdraw, width=20, font=('Arial', 20))
amount_Input.grid(row=2, column=2, padx=(200,10))

txt = Label(withdraw, text='Continue')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=3, column=3, pady=(60,12))

yes = Button(withdraw, text='YES', width=25, height=2, command=checkBal)
yes.grid(row=4, column=3, pady=(8))

no = Button(withdraw, text='NO',  width=25, height=2)
no.grid(row=5, column=3)

# ==========Withdrawal->YES PAGE ===========

imgbg4 =Image.open('./images/backgroundimage.jpg')
loginbg4 = ImageTk.PhotoImage(imgbg4)
bglabel4 = Label(withdraw_next, image=loginbg4)
bglabel4.place(x = 0,y = 0)

img4 = Image.open('./images/moneylogo.png')
img4 = img4.resize((50,50))
img4 = ImageTk.PhotoImage(img4)
img_label4 = Label(withdraw_next, image = img4)
img_label4.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label4.config(bg='#230444')

txt = Label(withdraw_next, text='Current Balace : ')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=2, column=2, padx=(210,0), pady=(20,10))

header = Label(withdraw_next, text='')
header.config(font=('verdana bold',24),bg='#230444',foreground='white')
header.grid(row=1, column=2, padx=(175), pady=(5, 40), columnspan=3)

bal_val = Label(withdraw_next, text=Accounts['Balance'][index])
bal_val.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
bal_val.grid(row=3, column=2, padx=(210,0), pady=(10))

def clear_input():
    input_name.delete(0, END)
    input_password.delete(0, END)
    amount_Input.delete(0, END)
    account_no.delete(0, END)
    account_no2.delete(0, END)
    amount_Input2.delete(0, END)
    amount_Input_Deposit.delete(0, END)
    header['text']=''
    incorrect2['text']=''
    incorrect3['text']=''
    newpin.delete(0, END)
    newpin2.delete(0, END)


txt = Label(withdraw_next, text='Return to Login')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=4, column=3, padx=(0),pady=(0,12))

yes = Button(withdraw_next, text='YES', width=25, height=2, command=lambda: [clear_input(), show_frame(login)])
yes.grid(row=5, column=3, pady=(8))

Quit = Button(withdraw_next, text='QUIT', width=25, height=2, command= window.destroy)
Quit.grid(row=6, column=3)



# ==========Deposit PAGE ===========

imgbg5 =Image.open('./images/backgroundimage.jpg')
loginbg5 = ImageTk.PhotoImage(imgbg5)
bglabel5 = Label(Deposit, image=loginbg5)
bglabel5.place(x = 0,y = 0)

img5 = Image.open('./images/moneylogo.png')
img5 = img5.resize((50,50))
img5 = ImageTk.PhotoImage(img5)
img_label5 = Label(Deposit, image = img5)
img_label5.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label5.config(bg='#230444')

txt = Label(Deposit, text='Enter Amount')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(18), pady=(5, 40), columnspan=3)

amount_Input_Deposit = Entry(Deposit, width=20, font=('Arial', 20))
amount_Input_Deposit.grid(row=2, column=2, padx=(200,10))

txt = Label(Deposit, text='Continue')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=3, column=3, pady=(60,12))


yes = Button(Deposit, text='YES', width=25, height=2, command=AddBal)
yes.grid(row=4, column=3, pady=(8))

no = Button(Deposit, text='NO',  width=25, height=2)
no.grid(row=5, column=3)

# ==========Transfer PAGE ===========

imgbg6 =Image.open('./images/backgroundimage.jpg')
loginbg6 = ImageTk.PhotoImage(imgbg6)
bglabel6 = Label(Transfer, image=loginbg6)
bglabel6.place(x = 0,y = 0)

img6 = Image.open('./images/moneylogo.png')
img6 = img6.resize((50,50))
img6 = ImageTk.PhotoImage(img6)
img_label6 = Label(Transfer, image = img6)
img_label6.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label6.config(bg='#230444')

txt = Label(Transfer, text='Enter Account No.')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(18), pady=(5, 40), columnspan=3)

account_no = Entry(Transfer, width=20, font=('Arial', 20))
account_no.grid(row=2, column=2, padx=(200,10))

txt = Label(Transfer, text='Continue')
txt.config(font=('verdana',12),bg='#d2ebe9',foreground='black')
txt.grid(row=4, column=3, pady=(60,12))

def check_ac_no():
    ac = int(account_no.get())

    for i in Accounts['AccountNo']:
        if i == ac:
            show_frame(Transfer_Amount)
        else:
            incorrect2['text']='Incorrect Account No.'

incorrect2 = Label(Transfer, text='',fg='red',bg='#d2ebe9')
incorrect2.config(font=('verdana',10))
incorrect2.grid(row=3, column=2, padx=(200,10),pady=(8))

yes = Button(Transfer, text='YES', width=25, height=2, command=check_ac_no)
yes.grid(row=5, column=3,pady=(8))

no = Button(Transfer, text='NO',  width=25, height=2)
no.grid(row=6, column=3)

# ==========Transfer->amount ===========

def AccTransfer():
    amt = amount_Input2.get()
    amt = float(amt)
    ac_no = account_no.get()
    ac_no = int(ac_no)
    global index
    if (amt < Accounts['Balance'][index]):
        Accounts['Balance'][index] -= amt
        bal_val['text'] = Accounts['Balance'][index]


        for i in range(len(Accounts['AccountNo'])):
            if(ac_no == Accounts['AccountNo'][i]):
                index = i
                break
        Accounts['Balance'][index] += amt
        header['text'] = 'Transfered successfully'
    else:
        header['text'] = 'Insufficient Balance⛔'

    show_frame(withdraw_next)

imgbg7 =Image.open('./images/backgroundimage.jpg')
loginbg7 = ImageTk.PhotoImage(imgbg7)
bglabel7 = Label(Transfer_Amount, image=loginbg7)
bglabel7.place(x = 0,y = 0)

img7 = Image.open('./images/moneylogo.png')
img7 = img7.resize((50,50))
img7 = ImageTk.PhotoImage(img7)
img_label7 = Label(Transfer_Amount, image = img7)
img_label7.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label7.config(bg='#230444')

txt = Label(Transfer_Amount, text='Enter Amount')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(200), pady=(5, 40), columnspan=2)

amount_Input2 = Entry(Transfer_Amount, width=20, font=('Arial', 20))
amount_Input2.grid(row=2, column=2, padx=(180,10))

txt = Label(Transfer_Amount, text='Continue')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=3, column=3, pady=(60,12))

yes = Button(Transfer_Amount, text='YES', width=25, height=2, command=AccTransfer)
yes.grid(row=4, column=3, pady=(8))

no = Button(Transfer_Amount, text='NO',  width=25, height=2)
no.grid(row=5, column=3)

# ==========Change Pin ===========

imgbg8 =Image.open('./images/backgroundimage.jpg')
loginbg8 = ImageTk.PhotoImage(imgbg8)
bglabel8 = Label(changePin, image=loginbg8)
bglabel8.place(x = 0,y = 0)

img8 = Image.open('./images/moneylogo.png')
img8 = img8.resize((50,50))
img8 = ImageTk.PhotoImage(img8)
img_label8 = Label(changePin, image = img8)
img_label8.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label8.config(bg='#230444')

txt = Label(changePin, text='Enter Account No.')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(18), pady=(5, 40), columnspan=3)

account_no2 = Entry(changePin, width=20, font=('Arial', 20))
account_no2.grid(row=2, column=2, padx=(200,10))

txt = Label(changePin, text='Continue')
txt.config(font=('verdana',12),bg='#d2ebe9',foreground='black')
txt.grid(row=4, column=3, pady=(60,12))

incorrect3 = Label(changePin, text='',fg='red',bg='#d2ebe9')
incorrect3.config(font=('verdana',10))
incorrect3.grid(row=3, column=2, padx=(200,10),pady=(8))

def check_ac_no2():
    ac = int(account_no2.get())
    print(ac)
    print(Accounts['AccountNo'][index])
    if Accounts['AccountNo'][index] == ac:
        show_frame(EnterPin)
    else:
        incorrect3['text']='Incorrect Account No.'

yes = Button(changePin, text='YES', width=25, height=2, command=check_ac_no2)
yes.grid(row=5, column=3,pady=(8))

no = Button(changePin, text='NO',  width=25, height=2)
no.grid(row=6, column=3)

# ==========Enter Pin ===========

imgbg9 =Image.open('./images/backgroundimage.jpg')
loginbg9 = ImageTk.PhotoImage(imgbg9)
bglabel9 = Label(EnterPin, image=loginbg9)
bglabel9.place(x = 0,y = 0)

img9 = Image.open('./images/moneylogo.png')
img9 = img9.resize((50,50))
img9 = ImageTk.PhotoImage(img9)
img_label9 = Label(EnterPin, image = img9)
img_label9.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label9.config(bg='#230444')

txt = Label(EnterPin, text='Enter New Pin')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(18), pady=(5, 40), columnspan=3)

newpin_var = StringVar()
newpin = Entry(EnterPin, width=20, textvariable = newpin_var, show= '*', font=('Arial', 20))
newpin.grid(row=2, column=2, padx=(200,10))

txt = Label(EnterPin, text='Continue')
txt.config(font=('verdana',12),bg='#d2ebe9',foreground='black')
txt.grid(row=3, column=3, pady=(60,12))

yes = Button(EnterPin, text='YES', width=25, height=2, command=lambda: show_frame(ReEnterPin))
yes.grid(row=4, column=3,pady=(8))

no = Button(EnterPin, text='NO',  width=25, height=2)
no.grid(row=5, column=3)

# ==========ReEnter Pin ===========

imgbg10 =Image.open('./images/backgroundimage.jpg')
loginbg10 = ImageTk.PhotoImage(imgbg10)
bglabel10 = Label(ReEnterPin, image=loginbg10)
bglabel10.place(x = 0,y = 0)

img10 = Image.open('./images/moneylogo.png')
img10 = img10.resize((50,50))
img10 = ImageTk.PhotoImage(img10)
img_label10 = Label(ReEnterPin, image = img10)
img_label10.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label10.config(bg='#230444')

txt = Label(ReEnterPin, text='ReEnter New Pin')
txt.config(font=('verdana bold',24),bg='#230444',foreground='white')
txt.grid(row=1, column=2, padx=(18), pady=(5, 40), columnspan=3)

newpin2_var = StringVar()
newpin2 = Entry(ReEnterPin, width=20, textvariable = newpin2_var, show= '*', font=('Arial', 20))
newpin2.grid(row=2, column=2, padx=(200,10))

txt = Label(ReEnterPin, text='Continue')
txt.config(font=('verdana',12),bg='#d2ebe9',foreground='black')
txt.grid(row=3, column=3, pady=(60,12))

def checkPin():
    p1 = newpin.get()
    p2 = newpin2.get()
    print(p1)
    print(p2)

    if(p1 == p2):
        header2['text'] = 'Pin Changed Successfully'
        Accounts['Password'][index] = p1
    else:
        header2['text'] = 'Different Pin'
    show_frame(PinChanged)

yes = Button(ReEnterPin, text='YES', width=25, height=2, command=checkPin)
yes.grid(row=4, column=3,pady=(8))

no = Button(ReEnterPin, text='NO',  width=25, height=2)
no.grid(row=5, column=3)

# ==========PinChanged PAGE ===========

imgbg11 =Image.open('./images/backgroundimage.jpg')
loginbg11 = ImageTk.PhotoImage(imgbg11)
bglabel11 = Label(PinChanged, image=loginbg11)
bglabel11.place(x = 0,y = 0)

img11 = Image.open('./images/moneylogo.png')
img11 = img11.resize((50,50))
img11 = ImageTk.PhotoImage(img11)
img_label11 = Label(PinChanged, image = img11)
img_label11.grid(row=0, column=0, padx=(20), pady=(10,0))
img_label11.config(bg='#230444')

header2 = Label(PinChanged, text='')
header2.config(font=('verdana bold',24),bg='#230444',foreground='white')
header2.grid(row=1, column=2, padx=(175), pady=(5, 40))

txt = Label(PinChanged, text='Return to Login')
txt.config(font=('verdana',18),bg='#d2ebe9',foreground='black')
txt.grid(row=2, column=2, padx=(0),pady=(0,12))

yes = Button(PinChanged, text='YES', width=25, height=2, command=lambda: [clear_input(), show_frame(login)])
yes.grid(row=3, column=2, pady=(8))

Quit = Button(PinChanged, text='QUIT', width=25, height=2, command= window.destroy)
Quit.grid(row=4, column=2)

window.mainloop()