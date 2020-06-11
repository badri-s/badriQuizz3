from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def main():
    window = Tk()
    window.geometry('530x500')
    window.title("converter")
    unitVar = StringVar()
    window.config(bg="honeydew3")

    units = [
        'Choose',
        'Miligram',
        'Gram',
        'Kilogram',
        'Tonne'
    ]

    converted = {
        'Miligram': 0,
        'Gram': 0,
        'Kilogram': 0,
        'Tonne': 0
    }

    mlg_label = Label(window, text=f"Miligram:{converted['Miligram']}", font=("bahnschrift", 20),bg="honeydew3")
    mlg_label.place(relx=0.04, rely=0.3)

    gr_label = Label(window, text=f"Gram:{converted['Gram']}", font=("bahnschrift", 20),bg="honeydew3")
    gr_label.place(relx=0.04, rely=0.4)

    kg_label = Label(window, text=f"Kilogram:{converted['Kilogram']}", font=("bahnschrift", 20),bg="honeydew3")
    kg_label.place(relx=0.04, rely=0.5)

    tn_label = Label(window, text=f"Tonne:{converted['Tonne']}", font=("bahnschrift", 20),bg="honeydew3")
    tn_label.place(relx=0.04, rely=0.6)


    def update_labels():
        mlg_label['text'] = f"Miligram:{converted['Miligram']}   "
        gr_label['text'] = f"Gram:{converted['Gram']} "
        kg_label['text'] = f"Kilogram:{converted['Kilogram']} "
        tn_label['text'] = f"Tonne:{converted['Tonne']}"

    def calculate():
        try:
            if unitVar.get() == "Choose":
                messagebox.showinfo(title = "Mistake", message = "Choose your unit")
            elif unitVar.get() == "Miligram":
                converted["Miligram"] = f"{user_input_weight.get()} (Chosen unit)"
                converted["Gram"] = float(user_input_weight.get())/1000
                converted["Kilogram"] = float(user_input_weight.get())/1000000
                converted['Tonne'] = float(user_input_weight.get())/1e+9
            elif unitVar.get() == "Gram":
                converted["Miligram"]  = float(user_input_weight.get())*1000
                converted['Gram'] = f"{user_input_weight.get()} (Chosen unit)"
                converted['Kilogram'] = float(user_input_weight.get())/1000
                converted['Tonne'] = float(user_input_weight.get()) /1e+6
            elif unitVar.get() == "Kilogram":
                converted['Miligram'] = float(user_input_weight.get()) * 1e+6
                converted["Gram"] = float(user_input_weight.get()) * 1000
                converted['Kilogram'] = f"{user_input_weight.get()} (Chosen unit)"
                converted['Tonne'] = float(user_input_weight.get())/1000
            elif unitVar.get() == "Tonne":
                converted['Miligram'] = float(user_input_weight.get()) * 1e+9
                converted['Gram'] = float(user_input_weight.get()) *1e+6
                converted['Kilogram'] = float(user_input_weight.get())  * 1000
                converted['Tonne'] = f"{user_input_weight.get()} (Chosen unit)"

            update_labels()
        except:
            messagebox.showinfo(title = "Incorrect value", message = "Please enter a Number")

    user_input_label = ttk.Label(window,text="Choose what you want to convert ",font=("bahnschrift",15),background="honeydew3").grid(row=0,column=0)
    user_input_unit = ttk.OptionMenu(window,unitVar,*units).grid(row=0,column=2)
    user_input_weight = ttk.Entry(window)
    user_input_weight.grid(row=0,column=1)
    conver_button = ttk.Button(window,text="CONVERT",width=30,command=calculate)
    conver_button.grid(row=1,columnspan=4)

    window.mainloop()

main()