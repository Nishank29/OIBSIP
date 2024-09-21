from tkinter import *
import tkinter.messagebox as tsmg

def calculation():
    try:
        a = float(Height_entry.get())
        b = int(Weight_entry.get())
        result = b / (a * a)

        if result < 18.5:
            category = "Underweight"
        elif 18.5 <= result < 25:
            category = "Normal"
        elif 25 <= result < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        tsmg.showinfo("Your Result", category)
    except ValueError:
        tsmg.showwarning("Input Error", "Please enter valid numbers for height and weight.")

def on_focus(event):
    if Height_entry.get() == "Enter your height":
        Height_entry.delete(0, END)
        Height_entry.config(fg="black")

def on_focus_out(event):
    if Height_entry.get() == "":
        Height_entry.insert(0, "Enter your height")
        Height_entry.config(fg="grey")

def onn_focus(event):
    if Weight_entry.get() == "Enter your weight":
        Weight_entry.delete(0, END)
        Weight_entry.config(fg="black")

def onn_focus_out(event):
    if Weight_entry.get() == "":
        Weight_entry.insert(0, "Enter your weight")
        Weight_entry.config(fg="grey")



root = Tk()
root.title('BMI Calculator')
root.geometry('400x400')

Label(root, text="Body Mass Index Calculator").grid(row=0, column=1)

Label(root, text="Height (m)").grid(row=1, column=0)
Label(root, text="Weight (kg)").grid(row=2, column=0)

Height_entry = Entry(root)
Height_entry.insert(0, 'Enter your height')
Height_entry.bind("<FocusIn>", on_focus)
Height_entry.bind("<FocusOut>", on_focus_out)
Height_entry.grid(row=1, column=1)

Weight_entry = Entry(root)
Weight_entry.insert(0, 'Enter your weight')
Weight_entry.bind("<FocusIn>", onn_focus)
Weight_entry.bind("<FocusOut>", onn_focus_out)
Weight_entry.grid(row=2, column=1)

Submit = Button(root, text="Submit", command=calculation)
Submit.grid(row=3, column=1)

mainloop()
