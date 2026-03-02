import tkinter as tk
from tkinter import messagebox
from volunteerTracker import Volunteer

Volunteer.initLoad()

def mainGui():
    root = tk.Tk()
    root.title("Volunteer & Applicant Management System")

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
        applicant_window = tk.Toplevel(root)
        applicant_window.title("Applicant Management")
        
        applicant_frame = tk.Frame(applicant_window, padx=10, pady=10)
        applicant_frame.pack(fill=tk.BOTH, expand=True)
        
        tk.Label(applicant_frame, text="Applicant Management", font=("Arial", 14, "bold")).pack()
        
        tk.Label(applicant_frame, text="placeholder").pack(pady=20)

    admin_btn = tk.Button(main_frame, text="Admin Login", command=open_applicant_management, width=20, height=3)
    admin_btn.pack(pady=10)

    root.mainloop()

mainGui()