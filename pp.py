day_min_calculate = 24* 60
m = "mins"

def day_to_min(num_days):
    return f"{num_days} days are {num_days * day_min_calculate } {m}"



def validate_execute():
    try:
        x = int(elements)

        if x>0:
            my_var = day_to_min(x)
            print(my_var)
        elif x ==0:
            print("cant be 0")
    except:
        print("invalid")     

u_input=""

while u_input != "exit":
    u_input = input("Enter days:")

    print(type(u_input.split(",")))

    for elements in set(u_input.split(",")):
        validate_execute()


    