##This program calculates the retirement benefit

CONTRIB_RATE=0.05
def main():
    grossPay=float(input("Please Enter the Gross pay:"))
    bonus=float(input("Pealse the amount of bonuses:"))
    showPayContrib(grossPay)
    showBonusContrib(bonus)
    
    
def showPayContrib(gross):
    contrib=gross*CONTRIB_RATE
    print("Contribution for the gross pay: $", format(contrib, ',.2f'), sep="")
    
def showBonusContrib(bonus):
    contrib=bonus*CONTRIB_RATE
    print("Contribution for bonuses: $", format(contrib, ',.2f'), sep="")
    
main()
    
