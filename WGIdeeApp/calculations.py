from asyncio.windows_events import NULL
from multiprocessing.managers import BaseManager
from .models import *

def get_sum(ausgaben_list):
    return sum(a.preis for a in ausgaben_list)

def calculate_value_all(person_list, ausgaben_list):
    for p in person_list:
        p.wert = 0
    for a in ausgaben_list:
        a.person.wert += a.preis

def calculate_debts_all(person_list, ausgaben_list):
    for p in person_list:
        p.calculate_debts(ausgaben_list, person_list)

def compensation(ausgaben_list, person_list):

    if len(person_list) == 1:
        return NULL
    
    calculate_debts_all(person_list, ausgaben_list)

    comp_list = []

    pl = []

    for p in person_list:
        if p.debts != 0:
            pl.append(p)

    return compensation_recursive(pl, comp_list)
            

def compensation_recursive(pl: list, comp_list: list) -> list:

    pl.sort(key=lambda x: x.debts)

    #Rekursionsbasis
    if len(pl) == 1:
        return comp_list

    if pl[-1].debts < abs(pl[0].debts):
        to_pay = pl[-1].debts
        pl[-1].debts = 0
        pl[0].debts += to_pay
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
        comp_list_object ={
            'sender': pl[-1],
            'receiver': pl[0],
            'amount': to_pay
        }
        pl.remove(pl[0])

    comp_list.append(comp_list_object)
    compensation_recursive(pl, comp_list)
    return comp_list
