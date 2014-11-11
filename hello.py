#!/usr/bin/env python
# -*- coding: utf-8 -*-

#GoCardless costs
def transaction_value():
	averagevalue = raw_input("What is your average bill size? ")
	averagevalue = float(averagevalue)
	return averagevalue

def number_of_transactions():
	totaltransactions = raw_input("How many transactions do you take a month? ")
	totaltransactions = int(totaltransactions)
	return totaltransactions

def gocardless_cost(transaction_value):
	if transaction_value >= 200:
		return 2 
	else:
		return transaction_value * 0.01

transaction_value = transaction_value()
number_of_transactions = number_of_transactions()
transaction_cost = gocardless_cost(transaction_value)
#gocardless cost printed
print "GoCardless will cost you £ %.2f" % (transaction_cost * number_of_transactions)

#Credit Card costs

def percentagefee():
	percentagefee = raw_input("What is the perctange fee? ")
	percentagefee = float(percentagefee)
	return percentagefee
	
def one_off_cost():
	oneoffcost = raw_input("What is the one off cost? ")
	oneoffcost = float(oneoffcost)
	return oneoffcost

def credit_card_cost():
	return (((percentagefee() / 100) * transaction_value) * number_of_transactions) + (one_off_cost() * number_of_transactions)

credit_cost = credit_card_cost()

print "Credit Cards will cost you £ %.2f " % credit_cost

print "Gocardless will be £ %.2f cheaper than cards " % (credit_cost - (transaction_cost * number_of_transactions))


