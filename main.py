import tkinter as tk
from tkinter import messagebox
import webbrowser
import threading
import time
import os
import sys
from volunteerTracker import Volunteer

# Add applicant_tracker to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'applicant_tracker'))
from applicant_tracker.app import app as flask_app

Volunteer.initLoad()

def run_flask():
    """Run Flask in a background thread"""
    flask_app.run(debug=False, use_reloader=False, port=5000, threaded=True)

def mainGui():
    root = tk.Tk()
    root.title("Volunteer & Applicant Management System")
    
    # Start Flask in background thread when app launches
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    time.sleep(2)  # Wait for Flask to start

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

    admin_btn = tk.Button(main_frame, text="Admin Login", command=open_applicant_management, width=20, height=3)
    admin_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    mainGui()