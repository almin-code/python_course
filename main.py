# 1. Budzet
# 2. Dodavanje taskova
# 3. brisanje taskova
# 4. logovanje taskova

from methods import get_user_info
from datetime import date

max_budget = 50000

user_info = get_user_info()
for user in user_info:
    if user["id"] == 1:
        budget = user["budget"] + user["credit"]
        if(budget > max_budget):
            quit("Presli ste limit budzeta")
        elif(budget < 0):
            quit("Trenutno nemate dovoljno novca")
        else:
            print(f"Dobar dan, dobrodosli nazad, vas budzet iznosti: {user['budget']}")

        expense = 0

        while expense <= 0 or expense > budget:
            expense = input("Molimo vas unesite iznos vaseg troska: ")
            if expense.isdigit():
                expense = int(expense)
            else:
                expense = 0

        with open("logs/expense_log.txt", "a") as file:
            remaining_budget = budget - expense
            message = f"\nAmmount: {expense}, User: {user['id']}, Budget: {budget}, Preostali budzet: {remaining_budget}, Datetime: {date.today()}"
            file.write(message)

    else:
        quit("Trenutni user ne postoji")