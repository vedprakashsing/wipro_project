cost=0.51
costPerDay=0.51*24
costPerWeek=costPerDay*7
costPerMonth=costPerWeek*4
checkCost=1
day=0
while(checkCost<918):
    checkCost=checkCost*costPerDay
    day=day+1
print("Cost of server per day:-",costPerDay,"$")
print("Cost of server per week:-",costPerWeek,"$")
print("Cost of server per months:-",costPerMonth,"$")
print("Number of days server can operate in 918$:-",costPerDay)