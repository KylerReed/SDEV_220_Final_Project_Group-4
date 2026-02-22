import pickle #I found this library to be pretty easy to use for saving data

userList = []

class Volunteer:
  #Contains functions needed to handle volunteer objects
  #Load and save functions utilize the pickle library to save data to a .pkl file
  #Rest of the functions modify the data in the userList, which can be saved and loaded
    
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def load():
        global userList
        try:
            path = input("Provide a filename: ")
            with open(path, 'rb') as file:
                userList = pickle.load(file)
            print("Save data found, loading data")
        except:
            print("No save data found")

    def save():
        try:
            path = input("Select a filename: ")
            with open(path, 'wb') as file:
                pickle.dump(userList, file)
            print("Data saved")
        except:
            print("Save failed")


    def createUser():
        user = Volunteer(input("Username:"), 0)
        userList.append(user)

    def deleteUser():
        try:
            user = userList.remove(input("User to remove"))
        except Exception:
            print("User not found")

    def output():
        for i in range(len(userList)):
            print(f"Volunteer #{i}: " + str(userList[i].name) + f", {userList[i].hours} hours")


def clear():
    for i in range(100):
        print("\n")


def main(): #sample command line interface for us to test

    while True:
        option = input("Select Option: ")
        match option.lower():
            case "create":
                Volunteer.createUser()
            case "delete":
                Volunteer.deleteUser()
            case "output":
                Volunteer.output()
            case "exit":
                break
            case "load":
                Volunteer.load()
            case "save":
                Volunteer.save()
            case _:
                print("Invalid option")

main()
