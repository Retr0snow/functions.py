"""
This program helps you to calculate the amount you can save based on a percentage from your income.

User sets the different saving account names (Function: add_saving_accounts)

program calculates the saving amount and sets it to the saving accounts(Function: calculate_saving). 
Calculation is based on the income and the percentage you want to save from it
the percent is set default to 10% can be changed writing the parameter in the function

Finally you can print the status of the account after calculation (function: print_account_status)

"""

def add_saving_accounts(): 
    """Function add saving accounts, user chose how many saving accounts wants to create and name them.
        Uses Total saving account value to save haw many accounts user needs and use it in the for buckle
        to set the names in a dictionary. The names ar saved as keys with no values. 
        accounts names cannot be empty.
        
        Retruns:
        return: dict of saving accounts names with empty values in it.
    """
    while True:#Save the amount of accounts in a int:
        try:
            total_saving_accounts = int(input("How many saving accounts do you whant to create: "))
            break
        except:
            print("Wrong input please enter the total amount to be created in numbers.")
    my_saving_accounts = dict()
    
    for i in range(total_saving_accounts):#Insert by user: names of accounts
        my_saving_accounts[input("Please enter the name of the saving account number {}: ".format(i+1))] = 0
        while True:
            if "" in my_saving_accounts:
                my_saving_accounts[input("Saving account can't be empty, please enter valid name:")] = my_saving_accounts.pop("")
            else:
                break
    
    return my_saving_accounts
        
def calculate_saving(income:float, accounts:dict, percent:float = 0.10) ->dict:
    """Function takes calculates how much we can save in the saving accounts. The default 
    saving percent is 10. We can change the saving amount percent if we want to save 
    more in theese accounts. Program returns the dictionary with the amount saved

    Args:
        income (float): Total income amount. 
        accounts (dict): Names and values of the saving accounts
        percent (float, optional): Percent in decimals to calculate the saving amount. 
            Defaults to 10%->0.10.

    Returns:
        dict: dictionary with the amount saved
    """
    accounts_with_savings = dict()
    amount_discounted = 0
    for i in accounts:#i gives dict keys
        accounts_with_savings[i] = income * percent
    return accounts_with_savings
    
def print_account_status(income:float, my_saving_accounts:dict):
    """This function print in console the account status. If the user 
    receive a negative saldo after substracting saving amount get a warning message

    Args:
        income (float): Total income.
        my_saving_accounts (dict): Saving accounts in a dictionary with the amounts calculated.
    """
    total_saved = 0
         
    print(f"{''.center(20,'-')}\nTotal income = {income}€\n{''.center(20,'-')}\nSaving accounts:\n")
    for key, value in my_saving_accounts.items():
        print(f"{key} : {value}€")
        total_saved += value
    print(f"\nSaldo remaining in the account: {income - total_saved}€")
    
    if income - total_saved < 0:
        print(f"{''.center(65,'-')}\n!!!The remaining saldo is negative, try a lower saving percent!!!\n{''.center(65,'-')}")
        
#-----------------------------------------------------------------------------
#-------------------------------Main code-------------------------------------
#-----------------------------------------------------------------------------        

income = float(input("Please enter the total income per month: "))
my_saving_accounts = add_saving_accounts()
my_saving_accounts = calculate_saving(income, my_saving_accounts,0.60)
print_account_status(income, my_saving_accounts)

my_saving_accounts = calculate_saving(income, my_saving_accounts,)
print_account_status(income, my_saving_accounts)











#-------------test---------------------
'''a = {"key":"value"}
a[input("the key: ")] = 0
print(a)'''
#---------------palautetta----------------------
'''Erittäin kattavasti kirjoitettu docstringit ja käytetty runsaasti kommentteja selittämään 
kukin vaihe. Koodi toimii hyvin.

Koodi on selkeää ja monipuolista. Docstring on luotu hyvin, selkeästi kirjoitettu.

Funktiossa add_saving_accounts: Jos syöttää useamman kuin yhden tyhjän nimen saving accounteille, 
tämä johtaa bugiin: Ohjelma pyytää vain yhden uuden nimen. Käyttäjältä pitäisi kysyä uutta 
nimeä heti väärän syötteen jälkeen. Pääfunktion voisi määritellä käyttäen: if __name__ == "__main__":

Hyvin tehty ja selitetty, mutta minusta oikein on amounT (ilman H lopussa)

Hyvät ohjeet ja kommentit. Koodissa turha muuttuja "amount_discounted". Virhesyötteen 
tarkistuksessa ongelma: jos savings accountin nimi on tyhjä, se tarkistetaan vain viimeisestä nimestä.

Koodiin oli jäänyt testaus 60% säästöprosentilla, mutta muuten todella selkeä koodi 
ja documentaatiot. Helposti pystyi lukemaan mistä on kyse. 

Palautteena sanoisin että try: Exceptissä voisi käyttää "Except: ValueError" 
koska tässä näytetään testaavan vain yhden että käyttävä syöttää numeron. 

Tässä kohdassa oli myös hienosti testattu väärän syötön varalle, mutta "income" syöttäessä voi vielä antaa huonon syötteen.
mielenkiintoista, olen kirjanpitäjä :)'''