#USD->VND: 
def usdvnd(usdvalue): 
  usd = float(usdvalue)
  vnd = usd*23500 
  return print("₫",vnd) 

#VND->USD: 
def vndusd(value): 
  usd = float(value)/23500.00 
  return print("$",usd) 

#USD->JOD: 
def usdjod(usdvalue): 
    jod = float(usdvalue)*0.71
    return print("د.ا",jod) 
  
#JOD->USD: 
def jodusd(value):

    usd = float(value)*1.41
    return print("$",usd) 

#USD->LEK
def usdlek(usdvalue):
    lek = float(usdvalue)*115.32
    return print("L",lek) 
    
#LEK->USD 
def lekusd(value):
    usd = float(value)/115.32
    return print("$",usd) 

#USD->DZD: 
def usddzd(usdvalue): 
    dzd = float(usdvalue)*146 
    return print("$",dzd)
 
#DZD->USD: 
def dzdusd (value): 
    usd = (float(value))/146
    return print("دج",usd)


#print("Please choose one of the following currencies: [ JOD, VND, LEK, DZD] to convert to and from USD")
 
money=input("Which country do you want to convert from into USD?\n JOD \n VND \n LEK\n DZD\n")
 
if money=="JOD"or money=="jod":
    value=float(input("How much JOD money? Please provide the amount you wish to convert\n د.ا"))
    #JODvalue = float(value) 
    jodusd(value)
    usconversion=input("Do you want to convert USD to VND? Please respond with yes(Y) or no(N)\n")

    
    if usconversion=="Y"or usconversion=="y":
        usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Jordanian Dinar(JOD)\n$")
        usdjod(usdvalue)
        print("Thank you for converting with us!")

    elif usconversion=="N" or usconversion=="n":
        print("Thank you for converting with us!")
    else:
        usconversion=input("Please respond with a Y or N")
        if usconversion=="Y" or usconversion=="y":
            usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Jordanian Dinar(JOD)\n$")
            usdjod(usdvalue)
            print("Thank you for converting with us!")
        else:
            print("Thank you for converting with us!")
 
 
if money=="VND" or money=="vnd":
    value=input("How much VND money? Please provide the amount you wish to convert\n₫")
    value = float(value) 
    vndusd(value)

    usconversion=input("Do you want to convert USD to VND? Please respond with yes(Y) or no(N)\n")

    if usconversion=="Y"or usconversion=="y":
        usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Vietnamese Dong(VND)\n$")
        usdvnd(usdvalue)
        print("Thank you for converting with us!")

    elif usconversion=="N" or usconversion=="n":
        print("Thank you for converting with us!")
    else:
        usconversion=input("Please respond with a Y or N")
        if usconversion=="Y" or usconversion=="y":
            usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Vietnamese Dong(VND)\n$")
            usdvnd(usdvalue)
            print("Thank you for converting with us!")
        else:
            print("Thank you for converting with us!")
   
if money=="LEK" or money=="lek":
    value=input("How much LEK money? Please provide the amount you wish to convert\nL")
    value = float(value) 
    lekusd(value)
    usconversion=input("Do you want to convert USD to LEK? Please respond with yes(Y) or no(N)")


    if usconversion=="Y"or usconversion=="y":
        usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Albanian Lek(LEK)\n$")
        usdlek(usdvalue)
        print("Thank you for converting with us!")

    elif usconversion=="N" or usconversion=="n":
        print("Thank you for converting with us!")
    else:
        usconversion=input("Please respond with a Y or N")
        if usconversion=="Y" or usconversion=="y":
            usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Albanian Lek(LEK)\n$")
            usdlek(usdvalue)
            print("Thank you for converting with us!")
        else:
            print("Thank you for converting with us!")
 
if money=="DZD" or money=="dzd":
    value=input("How much DZD money? Please provide the amount you wish to convert\nدج")
    value = float(value)
    dzdusd(value)
    usconversion=input("Do you want to convert USD to DZD? Please respond with yes(Y) or no(N)\n")

    if usconversion=="Y"or usconversion=="y":
        usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Algerian Dinar(DZD)\n$")
        usddzd(usdvalue)
        print("Thank you for converting with us!")

    elif usconversion=="N" or usconversion=="n":
        print("Thank you for converting with us!")
    else:
        usconversion=input("Please respond with a Y or N")
        if usconversion=="Y" or usconversion=="y":
            usdvalue=input("Please provide the amount of US Dollars(USD) you wish to convert to Algerian Dinar(DZD)\n$")
            usddzd(usdvalue)
            print("Thank you for converting with us!")
        else:
            print("Thank you for converting with us!")


