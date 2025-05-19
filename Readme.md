## coffe project code challenge

This is a python project which deals with modelling customer and also order for a coffe shop

## project setup or even structures

_ customer.py which defines the type of customer structure
_coffe.py we also have coffe.py which define the strucure of coffe class
_order.py  order.py it also define the order class

## initializations 
_Required python 3.x

## features

_Truck customer orders and coffe
_Calculate the most aficionado customer for each coffee.



## how to used
1. you are required to create a customer and instance of coffe, customer
2. you should supposed to used-something which is - Customer.create_order(coffe,price) in order to make it simple when creating orders
3. you should also required to create something like Quiry daata at search for example the most aficionado  customer for a coffe 

## example using line 3 of creating aficionado

pyton customer.py

from customer import customer
from coffee import coffee

espresso = Coffee("Espresso")
osman = Customer("Osman")

osman.create_order(espresso, 5.0)
