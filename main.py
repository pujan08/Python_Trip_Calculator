print("welcome to the trip calculator.")

total=input("what was the total of your bill? $")
percentage=input("what percentage tip would you you like to give? 10, 12 or 15? ")
person=input("how many people to split the bill? ")

total=float(total)
percentage=int(percentage)/100
person=int(person)
answer=(total+(total*percentage))/person
answer=round(answer,2)
answer="{:.2f}".format(answer)
print(f"each person should pay: ${answer}")
