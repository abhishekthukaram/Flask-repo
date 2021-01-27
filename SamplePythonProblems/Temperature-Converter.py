def temp_converter():
    temp_value= float(raw_input("Please enter the temperature value:"))
    conversion = raw_input("Enter F if converting to fahrenheit and C to celsius: ")
    n= int(raw_input('Enter the value of n:'))
    while(n>0):
        n=n-1
        if(conversion=='F'):
            intermediate = float((1.8*temp_value)+32)
            print ("The value is %d Fahrenheit" %(intermediate))
        elif (conversion=='C'):
            celsius_inter= float((temp_value-32)/1.8)
            print ("The value is %2f degree celsius" %(celsius_inter))
        else:
            print("The selection is invalid")
temp_converter()


