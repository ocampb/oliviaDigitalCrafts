bill = int(input ("what was your bill?"))
tipPercent = int(input ("what tip would you like to give? Put it in a percentage"))/100 

def tipCalc(moola):
    print("this is your tip")
    amount = (bill * tipPercent) 
    print ("%.2f" % amount)

tipCalc(bill)
