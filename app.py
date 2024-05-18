import tkinter as tk
from PIL import Image, ImageTk

def execute_program():
    # Get the values entered by the user
    if start_choice_var.get() == "Ubicació actual":
        inici_location = "Ubicació actual"
    else:
        inici_location = start_entry.get()

    end_location = end_entry.get()
    route = ruta_var.get()

    # Print the values for demonstration
    print("Començament del trajecte:", inici_location)
    print("Final del trajecte:", end_location)
    print("Lot:", route)

# Create the main application window
root = tk.Tk()
root.title("Caixa d'Enginyers: BANCA COOPERATIVA")
root.geometry("450x200")

# Load your custom icon
icon_path = "logo.png"  # Replace "your_icon.png" with the path to your PNG icon file

# Open and convert the PNG image to a format usable by Tkinter
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)

# Set the custom icon
root.iconphoto(True, icon_photo)

# Title label
title_label = tk.Label(root, text="BENVINGUT A BANCA D'ENGINYERS")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Dropdown for Start Location
start_label = tk.Label(root, text="Inici:")
start_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
start_choice_var = tk.StringVar()
start_choice_var.set("Localització actual")  # Default choice
start_choice_dropdown = tk.OptionMenu(root, start_choice_var, "Localització actual", "Tria una localització")
start_choice_dropdown.grid(row=1, column=1, padx=10, pady=5)

start_entry = tk.Entry(root)
start_entry.grid(row=1, column=2, padx=10, pady=5)
start_entry.grid_remove()  # Hide the entry initially

def toggle_start_input(*args):
    if start_choice_var.get() == "Ubicació actual":
        start_entry.grid_remove()
    elif start_choice_var.get() == "Tria una localització":
        start_entry.grid()
    else:
        start_entry.grid_remove()

start_choice_var.trace_add("write", toggle_start_input)
toggle_start_input()

# End Location Entry
end_label = tk.Label(root, text="Final del trajecte:")
end_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
end_entry = tk.Entry(root)
end_entry.grid(row=2, column=1, padx=10, pady=5)

# Ruta Entry
ruta_label = tk.Label(root, text="Lot:")
ruta_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
ruta_var = tk.StringVar()
ruta_dropdown = tk.OptionMenu(root, ruta_var, "2", "4", "5")
ruta_dropdown.grid(row=3, column=1, padx=10, pady=5)

# Button to execute the program
execute_button = tk.Button(root, text="Execute", command=execute_program)
execute_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
