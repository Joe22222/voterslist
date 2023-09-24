ppl = []
vot = []

while True:
    name = input("Type the name of the voter: ")
    if name == "0":
        break
    ppl.append(name)
print()
for i in ppl:
    x = input("Is " + i + " 18 years or older? ")
    if x.lower() in ["yes", "y"]:
        y = input("Has " + i + " been involved in any crime? ")
        if y.lower() in ["yes", "y"]:
            print(i + " is not allowed to vote.")
        else:
            print(i + " is eligible to vote.")
            vot.append(i)
    else:
        print("Sorry,",i,"is not old enough to vote.")

print("Eligible voters:", vot)

while True:
    action = input("Do you want to delete a voter? (yes/no): ").lower()
    if action == "no":
        break
    elif action == "yes":
        voter_to_remove = input("Enter the name of the voter you want to remove: ")
        if voter_to_remove in vot:
            vot.remove(voter_to_remove)
            print(voter_to_remove + " has been removed from the list of eligible voters.")
        else:
            print(voter_to_remove + " is not in the list of eligible voters.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print("Final voters list:", vot)
