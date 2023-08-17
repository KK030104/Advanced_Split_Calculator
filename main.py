print("Welcome to Samrt Split Calculator!")
print("-----------------------------------")
no_of_persons = int(input("Enter the total number of people to split the bill: "))
print("-----------------------------------------------------")
data = {"Name": [], "Amount": []}

def Total_amount(lst):
    return sum(lst)
    
def calculate_average(lst):
    if not lst:
        return 0  # Handle the case of an empty list to avoid division by zero
    
    total = sum(lst)
    average = total / len(lst)
    return average

for i in range(no_of_persons):
    name = input("Name " + str(i + 1) + ": ")
    amt = float(input("Amount: "))
    print()
    data["Name"].append(name)
    data["Amount"].append(amt)

total_print = Total_amount(data["Amount"])
print("Total amount is: ",total_print,"/-")
print("-----------------------------------")

avg = calculate_average(data["Amount"])

print("The average amount is:", avg,"/-")
print("-----------------------------------")

for i, amount in enumerate(data["Amount"]):
    diff = amount - avg

    if diff == 0:
        print(data["Name"][i], "You have no dues nor any repaid amount.")
        print()
    elif diff < 0:
        print(data["Name"][i], "You have to give:", abs(diff), "/-")
        print()
    else:
        print(data["Name"][i], "You have to receive:", diff, "/-")
        print()
