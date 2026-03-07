import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import time
import os
import sys
from volunteerTracker import Volunteer

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'applicant_tracker'))
from applicant_tracker.app import app as flask_app

Volunteer.initLoad()

def run_flask():
    """Run Flask in a background thread"""
    flask_app.run(debug=False, use_reloader=False, port=5000, threaded=True)

#Gui Sections:
# Main displays the main window & 4 buttons
# Volunteer hours takes input for hours and a name which then updates the values for each volunteer
# Applicant management links to a database and webpage locally hosted to modify the applicants in the database
# Volunteer Management allows for users to be created, deleted, and have their hours modified
# Modify checks for admin password before then allowing the modifications previously described in the volunteer management screen
def mainGui():
    root = tk.Tk()
    root.title("Volunteer & Applicant Management System")
    
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    time.sleep(2) 

    main_frame = tk.Frame(root, padx=10, pady=10)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    tk.Label(main_frame, text="Volunteer & Applicant Management System", font=("Arial", 16, "bold")).pack(pady=20)
    
    def open_volunteer_hours():
        volunteer_window = tk.Toplevel(root)
        volunteer_window.title("Volunteer Hours")
        
        volunteer_frame = tk.Frame(volunteer_window, padx=10, pady=10)
        volunteer_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(volunteer_frame, text="Volunteer Management", font=("Arial", 14, "bold")).pack()
        
        tk.Label(volunteer_frame, text="Volunteer Name:").pack(anchor=tk.W)
        name_entry = tk.Entry(volunteer_frame, width=30)
        name_entry.pack(pady=5)
        
        tk.Label(volunteer_frame, text="Volunteer Hours:").pack(anchor=tk.W)
        hours_entry = tk.Entry(volunteer_frame, width=30)
        hours_entry.pack(pady=5)
        
        button_frame = tk.Frame(volunteer_frame)
        button_frame.pack(pady=10)
        
        def add_Hours():
            name = name_entry.get()
            hours = hours_entry.get()
            if name and hours:
                messagebox.showinfo("Notice", Volunteer.addHours(name, int(hours)))
                name_entry.delete(0, tk.END)
                hours_entry.delete(0, tk.END)
                Volunteer.save()
                Volunteer.output()
                Volunteer.exportVolunteerData()
            else:
                messagebox.showerror("Error", "Please fill in all fields")
        
        add_btn = tk.Button(button_frame, text="Submit Hours", command=add_Hours, bg="green", fg="white")
        add_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear", command=lambda: [name_entry.delete(0, tk.END), hours_entry.delete(0, tk.END)])
        clear_btn.pack(side=tk.LEFT, padx=5)
    
    volunteer_btn = tk.Button(main_frame, text="Volunteer Hours", command=open_volunteer_hours, width=20, height=3)
    volunteer_btn.pack(pady=10)

    def open_applicant_management():
        """Open Flask applicant tracker in default web browser"""
        webbrowser.open("http://localhost:5000")

    admin_btn = tk.Button(main_frame, text="Applicant Management", command=open_applicant_management, width=20, height=3)
    admin_btn.pack(pady=10)

    def open_directory():
        directory_window = tk.Toplevel(root)
        directory_window.title("Volunteer Directory")

        directory_frame = tk.Frame(directory_window, padx=10, pady=10)
        directory_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(directory_frame, text="Volunteer Directory", font=("Arial", 14, "bold")).pack()

        volunteers = Volunteer.output_list()
        if volunteers:
            for volunteer in volunteers:
                data = volunteer.name + ": " + str(volunteer.hours) + " hours"
                tk.Label(directory_frame, text=data).pack(anchor=tk.W)
        else:
            tk.Label(directory_frame, text="No volunteers found").pack()

    directory = tk.Button(main_frame, text="View Volunteer Directory", command=open_directory, width=20, height=3)
    directory.pack(pady=10)


    
    
    def open_management():

        management_Window = tk.Toplevel(root)
        management_Window.title("Volunteer Management")
        
        management_Frame = tk.Frame(management_Window, padx=10, pady=10)
        management_Frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(management_Frame, text="Volunteer Management", font=("Arial", 14, "bold")).pack()
        
        tk.Label(management_Frame, text="Volunteer Name:").pack(anchor=tk.W)
        name_entry = tk.Entry(management_Frame, width=30)
        name_entry.pack(pady=5)

        tk.Label(management_Frame, text="Administrator Login: (123 for testing purposes)").pack(anchor=tk.W)
        admin_login = tk.Entry(management_Frame, width=30)
        admin_login.pack(pady=5)



        def modify():
            try:
                if(admin_login.get() == "123"):
                    modify_window = tk.Toplevel(root)
                    modify_window.title("Modify Volunteer Hours")
                    modify_frame = tk.Frame(modify_window, padx=10, pady=10)
                    modify_frame.pack(fill=tk.BOTH, expand=True)
        
                    tk.Label(modify_frame, text="Modify Volunteer Hours", font=("Arial", 14, "bold")).pack()

                    text = name_entry.get() + "'s Current Hours: " + str(Volunteer.addHours(name_entry.get(), 0))

                    tk.Label(modify_frame, text="Add/Remove Hours").pack(anchor=tk.W)
                    hours_change = tk.Entry(modify_frame, width=30)
                    hours_change.pack(pady=5)

                    button_frame = tk.Frame(modify_frame)
                    button_frame.pack(pady=10)

                    #Also, all these results should be printed to the terminal as well
                    def addHours():
                        hours = hours_change.get()
                        name = name_entry.get()
                        if name and hours:
                            messagebox.showinfo("Notice", "Hours modified")
                            Volunteer.addHours(name, int(hours))
                            Volunteer.save()
                            Volunteer.output()
                            Volunteer.exportVolunteerData()
                            modify_window.destroy()
                            management_Window.destroy()
                        else:
                            messagebox.showerror("Error", "Invalid Hours")
                    def deleteUser():
                        messagebox.showinfo("Notice", name_entry.get() + " deleted")
                        Volunteer.deleteUser(name_entry.get())
                        Volunteer.save()
                        Volunteer.output()
                        Volunteer.exportVolunteerData()
                        modify_window.destroy()
                        management_Window.destroy()
                    def createUser():
                        messagebox.showinfo("Notice", "User created")
                        Volunteer.createUser(name_entry.get())
                        Volunteer.addHours(name_entry.get(), int(hours_change.get()))
                        Volunteer.save()
                        Volunteer.output()
                        Volunteer.exportVolunteerData()
                        modify_window.destroy()
                        management_Window.destroy()

                    add_btn = tk.Button(button_frame, text="Add/Remove", command=addHours, bg="white", fg="black")
                    add_btn.pack(side=tk.LEFT, padx=5)
                    add_btn = tk.Button(button_frame, text="Create User", command=createUser, bg="white", fg="black")
                    add_btn.pack(side=tk.LEFT, padx=5)
                    add_btn = tk.Button(button_frame, text="Delete User", command=deleteUser, bg="red", fg="white")
                    add_btn.pack(side=tk.LEFT, padx=5)
                else:
                    messagebox.showerror("Error", "Invalid administrator login")
            except:
                messagebox.showerror("Error","Volunteer not found")
        
        button_frame = tk.Frame(management_Frame)
        button_frame.pack(pady=10)

        add_btn = tk.Button(button_frame, text="Find", command=modify, bg="green", fg="white")
        add_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear", command=lambda: [name_entry.delete(0, tk.END), admin_login.delete(0, tk.END)])
        clear_btn.pack(side=tk.LEFT, padx=5)

    directory = tk.Button(main_frame, text="Volunteer Management", command=open_management, width=20, height=3)
    directory.pack(pady=10)



    root.mainloop()

if __name__ == "__main__":
    mainGui()
