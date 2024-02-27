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
#region Compensation original (not working)
#################
#
#def compensation(Ausgaben_list, Person_list) -> list:
#
#    calculate_debts_all(Person_list, Ausgaben_list)
#
#    comp_list = []
#    #list_object = {'sender': Person, 'receiver': Person, 'Amount': int}
#
#    Person_list_not_excluded = Person_list
#
#    for p in Person_list_not_excluded:
#        print(p)
#        if p.debts == 0:
#            Person_list_not_excluded = Person_list_not_excluded.exclude(pk=p.id)
#
#    return compensation_recursive(Ausgaben_list, Person_list_not_excluded, comp_list)
#            
#
#def compensation_recursive(Ausgaben_list, Person_list_not_excluded, comp_list: list) -> list:
#
#    Person_list_not_excluded.order_by("-debts")
#
#    #Rekursionsbasis
#    if Person_list_not_excluded.count() == 1:
#        print(comp_list)
#        return comp_list
#
#    if Person_list_not_excluded.last().debts < abs(Person_list_not_excluded.first().debts):
#        to_pay = Person_list_not_excluded.last().debts
#        Person_list_not_excluded.last().debts = 0
#        Person_list_not_excluded = Person_list_not_excluded.exclude(pk=Person_list_not_excluded.last().id)
#        Person_list_not_excluded.first().debts += to_pay
#        #print(to_pay)
#        #print(Person_list_not_excluded.last())
#        #print(Person_list_not_excluded.first())
#    else:
#        to_pay = abs(Person_list_not_excluded.first().debts)
#        Person_list_not_excluded.first().debts = 0
#        Person_list_not_excluded = Person_list_not_excluded.exclude(pk=Person_list_not_excluded.first().id)
#        Person_list_not_excluded.last().debts -= to_pay
#        #print(to_pay)
#        #print(Person_list_not_excluded.last())
#        #print(Person_list_not_excluded.first())
#
#    comp_list_object ={
#            'sender': Person_list_not_excluded.last(),
#            'receiver': Person_list_not_excluded.first(),
#            'amount': to_pay
#        }
#    print(comp_list_object)
#    comp_list.append(comp_list_object)
#    compensation_recursive(Ausgaben_list, Person_list_not_excluded, comp_list)
#    return comp_list
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