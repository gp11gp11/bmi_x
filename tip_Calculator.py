print("welcome to tip calculator")
bill=int(input("what was the total bill?"))
tip_perc=int(input("what percentage tip would you like to give? 10,12,or 15\n"))
tip=bill*(tip_perc/100)
total_people=int(input("How many people to split the bill?\n"))
each_to_pay=(tip+bill)/total_people
final_amount = round(each_to_pay,2)
final_amount = "{:.2f}".format(each_to_pay)#to get exact no of decimal places got by searching in stackoveerflow
print(f"Each person need to pay: ${final_amount}")
