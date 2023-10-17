##My name is Merdan Garlyyev. I am taking CS-230 class. Due date for this assignment is Oct 30, 2022, but I bought an extension for a week. The name of my program is "CurrencyExchanger.py"
## The program recieves original currency, target currency, and amount that user want to exchange to a target currency
## So, program basically exchanges one currency into another taking values from a "plane_currencies.txt" file
import os
##Here I am using a dictionary to store all our values, and use them upon request in the program
exchanger = {"usdollar": 1, "algeriandinar": 118.449952, "angolankwanza": 278.809, "botswananpula": 10.807472, "capeverdeanescudo": 95.4305, "comorianfranc": 426.091764, "egyptianpound": 17.91, "ethiopianbirr": 27.656969, "gambiandalasi": 48.035, "ghanaiancedi": 4.7911, "kenyanshilling": 100.76, "libyandinar": 1.382249, "moroccandirham": 9.4495, "nigeriannaira": 359.68, "ruble": 68.0655, "somalishilling": 578.790042, "zambiankwacha": 10.355021, "zimbabweandollar": 322.355011, "britishpound": 0.777993, "canadiandollar": 1.318179, "euro": 0.863569, "ausdollar": 1.392878}

## Function is defined accordingly, and it's used to check the validity of provided inputs from the "plane_currencies.txt" file.

## If all the inputs are correct, the output will give us "user_name" and "new_amount" of converted currency
def converter (user_name, amount, original_currency, new_currency):
    if ((original_currency.lower() in exchanger) and (new_currency.lower()[:-1] in exchanger)):
        new_amount = (amount*exchanger[new_currency.lower()[:-1]]/exchanger[original_currency.lower()])
## Here i round my result to 2 decimal places using the below line
        rounded = round(new_amount, 2)
        out_file = open('new_currencies.txt', 'a')
        out_file.write(user_name + ", " + str(rounded) + "\n")
## If at least one of the inputs is not correct, the function won't convert currency and say "This is not valid currency" bc provided currency is not valid.
    else:
        print(original_currency, new_currency)
        ori = original_currency.lower()
        new = new_currency.lower()[:-1]
        print(ori, new)
        print(ori in exchanger, new in exchanger)
        out_file = open('new_currencies.txt', 'a')
        out_file.write(user_name + ", This is not a valid currency\n")
    out_file.close()

## This asks the name of our initial file, which is "plane_currencies.txt"
file = input("What's the name of the file? ")

## While the name of the file written down in input value is not correct, it will ask user for a name of a file again until he writes it down correctly.
while not os.path.exists(file):
    file = input("The file doesn't exist. Try one more time: ")

##Below written lines open our initial file, which is "plane_currencies.txt" and presents them in line form
with open(file, 'r') as fileobj:
    Lines = fileobj.readlines()
    for line in Lines:
        splited_line = line.split(", ")
        user_name = splited_line[0]
        amount = splited_line[1]
        old_currency = splited_line[2]
        new_currency = splited_line[3]
        converter(user_name, int(amount), old_currency, new_currency)
