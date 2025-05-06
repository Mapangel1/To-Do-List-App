import tkinter as tk
import os
import json
file_name = "TDLA_CONFIGS.json"
#----------------------------------TITLE FOR THE APP----------------------------------------
root = tk.Tk()
root.title("TDLA") # Sets the title (Set to TDLA as default)
root.geometry("800x500") #Sets the regular Box size (Set to 800x500 as default)
#------------------------------NAMES FOR TEXTBOXES-------------------------------------------------------
label = tk.Label(root, text="Enter the thing you need to do and/or time.")# Labels your textboxes
label.pack()
label_errors = tk.Label(root, text="Errors/Confirmations", font=("Arial", 10))
label_errors.place(x=350,y=300)

#--------------------------------TEXTBOXES-------------------------------
entry = tk.Entry(root, width=30)#Size of text Box (Set to 30 Width as default)
entry.pack()
text_box = tk.Text(root,width=50,height=10) #Size of a multi-line Text Box (Set to 50 width and 10 height as default)
text_box.place(x=205,y=125)#sets a position for the text bosses (Placed at x=205,y=125 as default)
text_box.tag_configure("big", font=("Arial", 13)) # TEXT SIZE (Set to 13 and Arial Font)
text_box.tag_configure("small", font=("Arial", 10)) # (Set to 10 and Arial Font)
text_box_errors = tk.Text(root, width=50,height=10)
text_box_errors.place(x=205,y=325)
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
    all_text = text_box.get("1.0", tk.END)  # Get all text from the box
    with open(file_name, "w") as file:
        json.dump({"tasks": all_text.strip().split("\n")}, file)  # Save each line as a list item
    text_box_errors.insert(tk.END, "Tasks saved." + "\n")

#----------------------BUTTON CONFIG------------------------------------------
button_submit = tk.Button(root, text="Submit(Small Text)", command=show_text) # Buttons
button_big_text = tk.Button(root, text="Bigger Text", command=show_text_big)
button_submit.pack()
button_big_text.place(x=363,y=90) # Button Location on the app (Set to x=363,y=90 as default)
button_save = tk.Button(root, text="Save TDL", command=save)
button_save.place(x=50,y=50)
root.mainloop()

