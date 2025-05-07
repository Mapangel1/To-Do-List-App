import tkinter as tk
import os
import json
file_name = os.path.join(os.path.dirname(__file__), "TDLA_CONFIGS.json")
print(f"File path: {file_name}")
if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        json.dump({"": []}, file)
#----------------------------------CONFIGS FOR THE APP----------------------------------------
root = tk.Tk()
root.title("TDLA") # Sets the title (Set to TDLA as default)
root.geometry("800x500") #Sets the regular Box size (Set to 800x500 as default)
root.configure(bg="lightblue")  # choose any color or hex code if you would like
#------------------------------NAMES FOR TEXTBOXES-------------------------------------------------------
label = tk.Label(root, text="Enter the thing you need to do and/or time.")# Labels your textboxes
label_errors = tk.Label(root, text="Errors/Confirmations", font=("Arial", 10)) #Font "Arial" size 10
label_functions = tk.Label(root, text="Functions", font=("Arial", 10)) #Font "Arial" size 10
label.pack()
label_errors.place(x=350,y=300) #Size of text box x=350,y300 set as default
label_functions.place(x=50,y=25) #Size of text x=50,y25 set as default
#--------------------------------TEXTBOXES-------------------------------
entry = tk.Entry(root, width=30)#Size of text Box (Set to 30 Width as default)
entry.pack()
text_box = tk.Text(root,width=50,height=10) #Size of a multi-line Text Box (Set to 50 width and 10 height as default)
text_box.place(x=205,y=125)#sets a position for the text bosses (Placed at x=205,y=125 as default)
text_box.tag_configure("big", font=("Arial", 13)) # TEXT SIZE (Set to 13 and Arial Font)
text_box.tag_configure("small", font=("Arial", 10)) # (Set to 10 and Arial Font)
text_box_errors = tk.Text(root, width=50,height=10)
text_box_errors.place(x=205,y=320)
#-------------------------COMMANDS FOR BUTTONS--------------------------------
#Small Text
def show_text():
    user_input = entry.get()
    text_box.insert(tk.END, user_input + "\n", "small")
#Big text
def show_text_big():
    user_input = entry.get()
    text_box.insert(tk.END, user_input + "\n", "big")
#Save To do list things
def save():
    with open(file_name, "r") as file:
        try:
            save_data = json.load(file)
        except json.JSONDecodeError:
            text_box_errors.insert(tk.END, "Save is corrupted or empty (Ignore sometimes)" + "\n")
    all_text = text_box.get("1.0", tk.END) #1.0 means 1 which is line one from character zero
    with open(file_name, "w") as file:
        json.dump({"": all_text.strip().split("\n")}, file) #Split, splits the tasks into new lines. 
    text_box_errors.insert(tk.END, "Tasks saved." + "\n")
#Deletes Save data
def delete():
    with open(file_name, "w") as file:
        json.dump({"": []}, file)
    text_box_errors.insert(tk.END, "Save has been successfully deleted.\n")
#Loads save
def load():
    with open(file_name, "r") as file:
        load_data = json.load(file)
    text_box.insert(tk.END, load_data)
    text_box_errors.insert(tk.END, "Save has been successfuly loaded.\n")

#----------------------BUTTON CONFIG------------------------------------------
button_submit = tk.Button(root, text="Submit(Small Text)", command=show_text) # Buttons
button_big_text = tk.Button(root, text="Submit(Bigger Text)", command=show_text_big)
button_save = tk.Button(root, text="Save TDL", command=save)
button_delete = tk.Button(root,text="Delete Save", command=delete)
button_load = tk.Button(root, text="Load Save", command=load)
button_submit.pack()
button_big_text.place(x=343,y=70) # Button Location on the app (Set to x=363,y=90 as default)
button_save.place(x=50,y=50)
button_delete.place(x=50,y=80)
button_load.place(x=50,y=110)
#-------------------------------------------------------------------------------
root.mainloop()
input("\n[APP CLOSED] Press Enter to exit...")
