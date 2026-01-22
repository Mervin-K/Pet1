
# mark counter

class FatBurn():
    def __init__(self, mass):
        self.mass = mass

    def check_weight(self):
        weight1 = float(input("Enter your current weight in kilos: "))
        weight2 = float(input("Enter your previous weight in kilos: "))

        if weight1 > weight2:
            print("Your diet doesn't seem to work. I suggest you fix it")
        elif weight1 == weight2:
            print("You either overeat or undermove. Improve one of two")
        elif weight1 < weight2:
            print("Everything is going as planned. Be slow and steady, and you'll lose weight")


class TrainingModality():
    def __init__(self, strength, endurance, muscles, fatloss, mod_question, diet):
        self.strength = strength
        self.endurance = endurance
        self.muscles = muscles
        self.fatloss = fatloss
        self.mod_question = mod_question
        self.diet = diet

    def modality(self):
        self.mod_question = input("What are you training for? What's your purpose?(strength, endurance, muscle, fatloss)")
        # getting to know what kind of training programm will be needed.
        if self.mod_question == "strength":
            onerepmax = float(input("Enter your 1RM in kg: "))
            # getting a metric for strength training
            print(f"{onerepmax}kg is a good weight!")
        elif self.mod_question == "muscle":
            workweight = float(input("Enter your maximum working weight in any basic exercise for 10 reps: "))
            # getting a metric for muscle growth training.
            print(f"We will make your programm based on {workweight}kg!")
        elif self.mod_question == "fatloss":
            workweight = float(input("What's your working weight in bench press for 8 reps? "))
            # getting a metric for muscle growth training, to then modify it for fat loss.
            print("We will use this weight to create you a training cycle")
        elif self.mod_question == "endurance":
            oxygen2 = float(input("Enter your VO2 max:"))
            lt = float(input("Enter your lactate threshold: "))
            rhr = float(input("Enter your resting heart rate: "))
            # getting important metrics for endurance training.
            print(f"{oxygen2}, {lt}, {rhr} are really good metrics. We will use them to create your mesocycle")

        # giving adviced on what training programm to choose
    def experience_reform(self, xp_level: int) -> str:
        xp_level = int(input("What is your experience level?(0-none, 1-newbie, 2-I have been to the gym a couple of times, 3-intermediate, 4-experienced)"))
        pare = (xp_level, self.mod_question)
        match pare:
            case(0, "strength") | (1, "strength"):
                return "I recommend programm CZCLP"
            case(2, "strength"):
                return "I recommend Russian cycle by Denis Cyplenkov"
            case(3, "strength"):
                return "I recommend Bulgarian system"
            case(4, "strength"):
                return "I recommend Ronnie Coleman's 700lbs cycle"
            case(0, "muscle") | (1, "muscle"):
                return "I recommend programm GZCL"
            case(2, "muscle"):
                return "I recommend Bro Split by Hamza"
            case(3, "muscle"):
                return "I recommend RP programm"
            case(4, "muscle"):
                return "I recommend using new training each day, like Arnold Schwarzenegger"
            case(_, _):
                return "No recommendation available for the given experience level and modality"

    def diet(self, diet):
        pare = (self.diet, diet)
        match pare:
            case(0, "no meat"):
                return ("Consult a doctor")
            case(1, "no sweet"):
                return ("It's good, continue the same way")
            case(2, "vegeratian"):
                return ("Consult a dietologist")
            case(3, "vegan"):
                return ("Be ready to buy lots of different proteins")
            case(4, "keto"):
                return ("It's gonna be really hard to do strength or endurance training without carbs")
            case(_, _):
                return ("No dietary restrictions, got it")


class TrainingProgramm(): # not completed yet.
    def __init__(self, reps, reps_in_reserve, meso_length, work_weights, experience):
        self.reps = reps
        self.reps_in_reserve = reps_in_reserve
        self.meso_length = meso_length
        self.work_weights = work_weights
        self.experience = experience

    def reps(self, reps):
        if reps in ["3-6", "6-10", "10-15", "15-20"]:
            if reps == "3-6":
                return "Strength range, not ideal for hypertrophy"
            elif reps == "6-10":
                return "Perfect for hypertrophy. Try to err on the side of higher reps"
                # repetitions = 10
                # I will use repet variable to make a training programm that starts
                # from 3 reps in reserve and then goes up to 1-0 reps in reserve, starting with max amount of reps-3.
            elif reps == "10-15":
                return "Perfect for hypertrophy. Try to err on the side of lower reps"
            elif reps == "15-20":
                return "Not ideal for hypertrophy. Go lower"


class HypertrophyRepsMeso():
    def __init__(self, hypreps: int):
        #hypertrophy repetitions. Amount of reps a person does for hypertrophy.
        hypreps = int(input("Enter maximum number of reps you can do with your working weight in one set: "))
        if hypreps > 10:
            raise ValueError("Max reps should be <=10")
        self.hypreps = hypreps

    def plan(self):
        print(f"week 1: you will do {self.hypreps - 3} reps with choosen weigths")
        print(f"week 2: you will do {self.hypreps - 2} reps with choosen weigths")
        print(f"week 3: you will do {self.hypreps - 1} reps with choosen weigths")
        print(f"week 4: you will do {self.hypreps - 0} reps with choosen weigths")
        print(f"week 5: you will try to do {self.hypreps + 1} reps with choosen weigths. If you could do more - do week 6. Otherwise skip it")
        print(f"week 6: you will try to do {self.hypreps + 2} reps with choosen weights")
        print(f"week 7: you will do super light weigths, like {self.hypreps / 2} with 1/2 of the previous reps. Or you can just skip a week of training")


def main():
    fb = FatBurn(70)
    fb.check_weight()

    tm = TrainingModality(strength=0, endurance=0, muscles=0, fatloss=0, mod_question="strength", diet="vegan")
    tm.modality()
    print(tm.experience_reform(2))

    if tm.mod_question == "muscle":
        hrm = HypertrophyRepsMeso(hypreps=0)
        hrm.plan()


if __name__ == "__main__":
    main()
# dfdfsaf
# I need to add fastAPI here.
