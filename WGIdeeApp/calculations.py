from multiprocessing.managers import BaseManager
from .models import *

def get_sum(Ausgaben_list):
    return sum(a.Preis for a in Ausgaben_list)

def calculate_value_all(Person_list, Ausgaben_list):
    for p in Person_list:
        p.calculate_value(Ausgaben_list)

def calculate_debts_all(Person_list, Ausgaben_list):
    for p in Person_list:
        p.calculate_debts(Ausgaben_list, Person_list)

#################
#region ehemalige Person Funktionen, jetzt unabhängig von Objekt
#################


# def calculate_value(user, Ausgabe_list):
#     user.wert = 0
#     for a in Ausgabe_list:
#         if user == a.Person:
#             user.wert += a.Preis

# def calculate_debts(user, Ausgaben_list, Person_list):
#     user.calculate_value(Ausgaben_list)
#     sum = get_sum(Ausgaben_list)
#     Person_count = Person_list.count()
#     average = sum / Person_count
#     user.debts = average - user.wert


#endregion

#################
#region Compensation testing
#################

def compensation(Ausgaben_list, Person_list) -> list:

    calculate_debts_all(Person_list, Ausgaben_list)

    comp_list = []
    #list_object = {'sender': Person, 'receiver': Person, 'Amount': int}

    pl = []

    for p in Person_list:
        #print(p)
        if p.debts != 0:
            pl.append(p)

    return compensation_recursive(pl, comp_list)
            

def compensation_recursive(pl: list, comp_list: list) -> list:

    pl.sort(key=lambda x: x.debts)
    #print(pl)

    #Rekursionsbasis
    if len(pl) == 1:
        #print(comp_list)
        return comp_list

    if pl[-1].debts < abs(pl[0].debts):
        to_pay = pl[-1].debts
        pl[-1].debts = 0
        pl[0].debts += to_pay
        #print(to_pay)
        #print(pl[-1])
        #print(pl[0])
        comp_list_object ={
            'sender': pl[-1],
            'receiver': pl[0],
            'amount': to_pay
        }
        pl.remove(pl[-1])
    else:
        to_pay = abs(pl[0].debts)
        pl[0].debts = 0
        pl[-1].debts -= to_pay
        #print(to_pay)
        #print(pl[-1])
        #print(pl[0])
        comp_list_object ={
            'sender': pl[-1],
            'receiver': pl[0],
            'amount': to_pay
        }
        pl.remove(pl[0])

    #print(comp_list_object)
    comp_list.append(comp_list_object)
    #print(comp_list)
    compensation_recursive(pl, comp_list)
    return comp_list
#endregion