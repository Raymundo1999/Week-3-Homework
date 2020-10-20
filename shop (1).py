#shop.py

#this will let the total cost and customer money work.
def check_money(total_cost, customer_money):
    #Your code here
#this will just tell you if you have enough money or not enough.
    if total_cost > customer_money :
        print ("Not enought Money!")
        return False
    elif total_cost <= customer_money:
        print ("Proccessed Money")
        return True
#this is what it will be checking if you have enough for.
#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
