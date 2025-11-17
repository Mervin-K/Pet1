
username = input("Enter your name: ")


laycount = int(input("How many chicks have you fucked: "))
if laycount == 0:
    print(f"What's up my boy {username}! {laycount} chicks is what everyone starts from. Let's elaborate on something")
elif laycount <=5:
    print(f"What's up my boy {username}! {laycount} chicks is not a lot, but it's better than nothing. Let's elaborate on something")
elif laycount <=15:
    print(f"What's up my boy {username}! {laycount} chicks is an amateur level, so you're a pretty respectable player. Let's elaborate on something")
elif laycount <=50:
    print(f"What's up my boy {username}! {laycount} chicks is a pretty advanced level. You can as well get a longtime girlfriend and I could not consider that a mistake. Let's elaborate on something")
elif laycount <=150:
    print(f"What's up my boy {username}! {laycount} chicks is a pro level. Let's elaborate on something")
elif laycount >150:
    print(f"What's up my boy {username}! {laycount} chicks is a happy man level. Let's elaborate on something")
else:
    print("Enter a real number")


weight = float(input("Enter your weight(kilos): "))
if weight < 75:
    print("Are you made of feather?")
elif weight >= 75 and weight <= 100:
    print("If you're not 5'5 you have to bulk up")
elif weight >= 100 and weight <= 125:
    print("I hope you're above 6'0 otherwise you're fat")
elif weight >= 125:
    print("If you're not a pro bodybuilder you're probably closer to diabetes than you think")
else:
    print("Enter a real number")


bodyfat = float(input("Enter your bodyfat: "))
if bodyfat <=0:
    print("You're probably dead")
if bodyfat <=15:
    print("You're good to go")
elif bodyfat >=16:
    print("You probably will get some benefits from losing extra fat")
elif bodyfat >=25:
    print("Jesus! You have to lose fat immediately")
else:
    print("Enter a real number")


income = float(input("How much money do you make a year after taxes(in dollars): "))
if income <= 0:
    print("Get a job broooo")
elif income <= 25000:
    print("You will gain a lot of benefits from improving your finances")
elif income <= 60000:
    print("That's good, but more will definitely be more beneficial")
elif income <= 100000:
    print("Income is probably not your problem")
elif income <= 250000:
    print("You're pretty well off")
elif income <= 500000:
    print("You're rich")


capital = float(input("How much money do you have overall(in dollars): "))
if capital <= 0:
    print("Start saving and investing money")
elif capital <= 250000:
    print("That's a good start")
elif capital <= 500000:
    print("You're pretty well off. Don't spend it on a mortgage!")
elif capital <= 1000000:
    print("Capital is probably not your problem")
elif capital <= 3000000:
    print("That's more than enough")
elif capital <= 10000000:
    print("You're a truly rich man")
elif capital >= 10000000:
    print("You can have zero work hours for the rest of your life. Money is definitely not your problem")


    def calculate_smv(laycount, weight, bodyfat, income, capital):

        if laycount <= 0:
            lay_coef = 0.2
        elif laycount <= 5:
            lay_coef = 0.6
        elif laycount <= 15:
            lay_coef = 1.0
        elif laycount <= 50:
            lay_coef = 1.4
        elif laycount <= 150:
            lay_coef = 1.8
        else:
            lay_coef = 2.0

        if weight < 60:
            weight_coef = 0.6
        elif weight < 75:
            weight_coef = 1.4
        elif weight <= 90:
            weight_coef = 2.0
        elif weight <= 100:
            weight_coef = 1.6
        elif weight <= 110:
            weight_coef = 1.2
        else:
            weight_coef = 0.8

        if bodyfat < 4:
            bodyfat_coef = 0.4
        elif bodyfat <= 8:
            bodyfat_coef = 1.8
        elif bodyfat <= 15:
            bodyfat_coef = 2.0
        elif bodyfat <= 20:
            bodyfat_coef = 1.6
        elif bodyfat <= 25:
            bodyfat_coef = 1.0
        else:
            bodyfat_coef = 0.6

        if income <= 0:
            income_coef = 0.0
        elif income <= 25000:
            income_coef = 0.4
        elif income <= 60000:
            income_coef = 0.7
        elif income <= 100000:
            income_coef = 1.0
        elif income <= 250000:
            income_coef = 1.5
        elif income <= 500000:
            income_coef = 1.8
        else:
            income_coef = 2.0

        if capital <= 0:
            capital_coef = 0.0
        elif capital <= 25000:
            capital_coef = 0.4
        elif capital <= 100000:
            capital_coef = 0.8
        elif capital <= 250000:
            capital_coef = 1.0
        elif capital <= 1000000:
            capital_coef = 1.2
        elif capital <= 2500000:
            capital_coef = 1.5
        elif capital <= 5000000:
            capital_coef = 1.7
        else:
            capital_coef = 2.0

        smv = lay_coef * weight_coef * bodyfat_coef * income_coef * capital_coef

        return smv, [lay_coef, weight_coef, bodyfat_coef, income_coef, capital_coef]


    def get_smv_ratin(smv_score):
        if smv_score >= 1.8:
            return "ELITE, top 1%"
        elif smv_score >= 1.4:
            return "HIGH, above average, 10%"
        elif smv_score >= 1.0:
            return "Average, 25%"
        elif smv_score >= 0.6:
            return "Below average, 51%"
        else:
            return "Low, lower than 51th percentile"



