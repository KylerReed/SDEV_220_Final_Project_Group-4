import pickle
import csv

userList = []

class Volunteer:

    # The class volunteer makes an object with can store the name and hours of a volunteer
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours

    def initLoad(): #First load just uses the default path, its data.pkl right now
        global userList
        try:
            path = "data.pkl" #set this as whatever default path name
            with open(path, 'rb') as file:
                userList = pickle.load(file)
            print("Save data found, loading data")
        except:
            print("No save data found")

    def load(path): #Names should be (mostly) self explanatory
        global userList
        try:
            with open(path, 'rb') as file:
                userList = pickle.load(file)
            print("Save data found, loading data")
        except:
            print("No save data found")

    def save(path="data.pkl"):
        try:
            if(path == "" or path == " "):
                path = "data.pkl"
            with open(path, 'wb') as file:
                pickle.dump(userList, file)
            print("Data saved")
        except:
            print("Save failed")


    def createUser(name):
        try:
            user = Volunteer(name, 0)
            userList.append(user)
        except Exception:
            print("Error creating user")

    def deleteUser(username):
        try:
            for user in userList:
                if user.name == username:
                    userList.remove(user)
                    print(f"User {username} deleted")
                    return
            print("User not found")
        except Exception:
            print("Error deleting user")

    def output():
        for i in range(len(userList)):
            print(f"Volunteer #{i}: " + str(userList[i].name) + f", {userList[i].hours} hours")

    def output_list():
        return(userList)
    
    def addHours(username, hours):
        try:
            if(hours < 0):
                return("Error updating hours")
            for user in userList:
                if user.name == username:
                    user.hours += hours
                    return("Hours added")
            return("User not found")
        except:
            return("Error updating hours")

    #Not actually used
    def lookup(username):
        for user in userList:
            if(user.name == username):
                print(username + "'s Volunteer ID is " + str(userList.index(user)))
                return
            else:
                print("User not found")

    # Saves to a csv file which can be found in the explorer and moved anywhere else for future use
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

#Also not actually used, for testing only
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
