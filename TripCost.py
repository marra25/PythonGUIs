# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 15:03:52 2015

@author: Bryce
"""
# import statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

# Set up GUI

# Welcome the user
tkinter.messagebox.showinfo("Welcome", "User")

# Get destination city
city = tkinter.simpledialog.askstring("City", "Which city will you be traveling to?\n"
            "(Charlotte, Tampa, Pittsburgh, or Los Angeles)")

# Get number of days            
days = tkinter.simpledialog.askinteger("Number of Days", "How many days will you be on vacation?")

# Get amount of spending money
spending_money = tkinter.simpledialog.askinteger("Spending Money", "How much spending money will you take?")

# Process information
def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost = cost - 50
    elif days >= 3:
        cost = cost - 20
    return cost

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

output_cost = trip_cost(city, days, spending_money)    
output = "Your cost with Hotel, Airfare, Rental Car, and Spending Money is: %d" %(output_cost)

# Produce the output
tkinter.messagebox.showinfo("Results", output)
