n_people=int(input("Enter for the number of the people to calculate:"))
i=0

while i<n_people:
    principle_investment=float(input("Enter the investment of yours:"))

    rate_frequency=input("Enter the rate calculated:(monthly/yearly)")
    if rate_frequency=="yearly":
        n_times=1
    elif rate_frequency=="monthly":
        n_times=int(input("Enter the number of times rate calculated in a year:"))
    else:
        print("Invalid.Please try again!")

    rate=float(input("ENter the rate of interest:"))

    time_yearly=int(input("ENter the number of years you gonna be payin the ecompund interest for in years:"))

    compund_amount=principle_investment*((1+((rate/100)/n_times))**(time_yearly*n_times))
    compound_interest=compund_amount-principle_investment

    print(f"User name: {i+1}|Compound amount accumulated:{compund_amount:,.3f}|Compound interest:{compound_interest:,.3f}")

    i+=1








