#superclass
class Account():
    
    itself = 'Nothing'
    
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        self.balance -= amount
        return 'The amount in your {} is now ${}.'.format(self.itself, self.balance)
    
    def deposit(self, amount):
        self.balance += amount
        return 'The amount in your {} is now ${}.'.format(self.itself, self.balance)


class Checking_Account(Account):
    
    itself = 'checking account'
    
    def __init__(self, balance):
        Account.__init__(self, balance)
        self.balance = balance

class Savings_Account(Account):
    
    itself = 'savings account'
    
    def __init__(self, balance):
        Account.__init__(self, balance)
        self.balance = balance

class Business_Account(Account):
    
    itself = 'business account'
    
    def __init__(self, balance):
        Account.__init__(self, balance)
        self.balance = balance
        
chk = Checking_Account(1263.96)

sav = Savings_Account(523.64)

bus = Business_Account(12605.03)

def make_number(strg):
    
    j = 0
    
    while j == 0:
        
        try:
            numb = int(strg)
            j = 1
            continue
        
        except:
            strg = input('You must enter a number:    ')
    
    return numb

def withdraw_check(wthd, acct):
    
    remain = acct.balance - wthd
    while True:
        if remain >= 0:
            return wthd
        else:
            wthd = make_number(input('You do not have enough funds in your account. Please choose a correct amount:    '))
            remain = acct.balance - wthd
            
def rounding(intg):
    return round(intg * 100)/100

def positive(intg):
    while True:
        if intg > 0:
            return intg
        else:
            intg = make_number(input('Please enter a positive number:    '))
            
def acct_options(acct):
    
    choice = input('You have accessed the {}. Your balance here is ${}.\n What would you like to do?\n1. Deposit cash\n2. Withdraw cash\n3. Back\n'.format(acct.itself, acct.balance))
    
    i = 0
    
    while i == 0:
        if choice == '1':
            depot = input('Please enter the amount you would like to deposit:    ')
            acct.deposit(positive(make_number(depot)))
        elif choice == '2':
            withd = input('Please enter the amount you would like to withdraw:    ')
            acct.withdraw(withdraw_check(positive(make_number(withd)),acct))            
        elif choice == '3':
            i = 1
            break
        else:
            choice = input('Please choice a valid response:\n1. Deposit cash\n2. Withdraw cash\n3. Back\n')
            continue
        choice = input('The amount in your {} is now ${}. What would you like to do now?\n1. Deposit cash\n2. Withdraw cash\n3. Back\n'.format(acct.itself, rounding(acct.balance)))
        
    return None

pin = input('Welcome to the ATM machine.\nPlease input your pin (5962):    ')

k = 0

while k == 0:
    if pin == '5962':
        acct_choice = input('Which account would you like to access?\n1. Checking Account\n2. Savings Account\n3. Business Account\n4. Log out\n')
        while True:
            if acct_choice == '1':
                acct_options(chk)
                break
            elif acct_choice == '2':
                acct_options(sav)
                break
            elif acct_choice == '3':
                acct_options(bus)
                break
            elif acct_choice == '4':
                k = 1
                print('Goodbye.')
                break
            else:
                acct_choice = input('Please choose a valid input:\n1. Checking Account\n2. Savings Account\n3. Business Account\n')
    else:
        pin = input('Please enter a valid pin (5962):    ')