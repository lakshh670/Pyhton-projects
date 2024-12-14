menu={
    "Pizza":80,
    "Burger":50,
    "Maggi":40,
    "Ice-cream ":60,
    "Patties":30,
    "Coffee":40
}

print("Welcome to our restaurant sir!!\n"
      "Here is the menu:\n"
      "\n"
      "Pizza: Rs80\n"
    "Burger:50\n"
    "Maggi: Rs40\n"
    "Ice-cream : Rs60\n"
    "Patties: Rs30\n"
    "Coffee: Rs40")

item=input("what would you like to order? ")
sum=0
if item in menu:
    sum += menu[item]
    print(item, "has been added.")
else:
    print("Sorry we don't have that item")
    exit()


check=input("Anything else sir? Yes or No: ")
if(check=="No" or check=="no"):
    print("Alright finalizing your order...")
    print("Your total bill is ")
    print(item, " :Rs", menu[item], "\n", "Total: Rs", sum)



else:
    new_item = input("Enter the new item: ")
    if new_item in menu:
        print(new_item, "has been added")
        sum += menu[new_item]
        print("Alright finalizing your order...")
        print("Your total bill is ")
        print(item, " :Rs", menu[item], "\n", new_item, " :Rs", menu[new_item], "\n", "Total: Rs", sum)
    else:
        print("Sorry we don't have that item")
        print("Your total bill for ", item, " is Rs:", sum)
        exit()








