import pickle
import csv

userList = []

class Volunteer:
    
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def initLoad():
        global userList
        try:
            path = "data.pkl" #set this as whatever default path name
            with open(path, 'rb') as file:
                userList = pickle.load(file)
            print("Save data found, loading data")
        except:
            print("No save data found")

    def load(path):
        global userList
        try:
            with open(path, 'rb') as file:
                userList = pickle.load(file)
            print("Save data found, loading data")
        except:
            print("No save data found")

    def save(path):
        try:
            if(path == "" or path == " "):
                path = "data.pkl"
            with open(path, 'wb') as file:
                pickle.dump(userList, file)
            print("Data saved")
        except:
            print("Save failed")


    def createUser(name):
        user = Volunteer(name, 0)
        userList.append(user)

    def deleteUser(user):
        try:
            user = userList.remove(user)
        except Exception:
            print("User not found")

    def output():
        for i in range(len(userList)):
            print(f"Volunteer #{i}: " + str(userList[i].name) + f", {userList[i].hours} hours")
    
    def addHours(user, hours):
        try:
            userList[user].hours += hours
        except:
            print("User not found")

    def lookup(username):
        for user in userList:
            if(user.name == username):
                print(username + "'s Volunteer ID is " + str(userList.index(user)))
                return
            else:
                print("User not found")
    
    def exportVolunteerData():
        exportPath = 'data.csv'
        with open(exportPath, 'w', newline='') as csvFile:
            csvWriter = csv.writer(csvFile)
            csvWriter.writerow(['Name', 'Hours'])
            for user in userList:
                csvWriter.writerow([user.name, user.hours])



        




def clear():
    for i in range(100):
        print("\n")


def main():
    Volunteer.initLoad()
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
            case "log":
                Volunteer.addHours()
            case "lookup":
                Volunteer.lookup()
            case "export":
                Volunteer.exportVolunteerData()
            case _:
                print("Invalid option")

main()