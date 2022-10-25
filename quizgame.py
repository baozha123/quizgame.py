print("Welcome to Baozha's quiz game")

playing = input("Do you want to play? ")
if playing.lower() != "yes" :
        print("滚吧傻逼")
        quit()

print("Okay! let's play!")
score = 0

answer = input("What is my favorite game? ")
if answer.lower() == "poe":
        print("Correct!")
        score += 1
else:
        print("Incorrect. ")

answer = input("What is my pets name? ")
if answer.lower() == "royce":
        print("Correct!")
        score += 1
else:
        print("Incorrect. ")

answer = input("What is my favorite food? ")
if answer.lower() == "noodle":
        print("Correct!")
        score += 1
else:
        print("Incorrect. ")

answer = input("What am I known for? ")
if answer.lower() == "table tennis olympian":
        print("Correct!")
        score += 1
else:
        print("Incorrect. ")

answer = input("Where did I attend collage? ")
if answer.upper() == "NYU":
        print("Correct!")
        score += 1
else:
        print("Incorrect. ")

print("You got " + str(score/6 * 100) + "% correct!")
