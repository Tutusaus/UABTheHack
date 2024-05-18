import tkinter as tk

def execute_program():
    # Get the values entered by the user
    if start_choice_var.get() == "Current Location":
        start_location = "Current Location"
    else:
        start_location = start_var.get() if start_choice_var.get() == "Dropdown" else start_entry.get()

    end_location = end_entry.get()
    route = ruta_var.get()

    # Print the values for demonstration
    print("Començament del trajecte:", start_location)
    print("Final del trajecte:", end_location)
    print("Ruta:", route)

    print("Hola planeta")


# Create the main application window
root = tk.Tk()
root.title("Caixa d'Enginyers: BANCA COOPERATIVA")
root.geometry("400x200")

# Title label
title_label = tk.Label(root, text="BENVINGUT A BANCA D'ENGINYERS")
title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Dropdown for Start Location
start_label = tk.Label(root, text="Start Location:")
start_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
start_choice_var = tk.StringVar()
start_choice_var.set("Choose Location")  # Default choice
start_choice_dropdown = tk.OptionMenu(root, start_choice_var, "Current Location", "Choose Location")
start_choice_dropdown.grid(row=1, column=1, padx=10, pady=5)

start_var = tk.StringVar()
start_dropdown = tk.OptionMenu(root, start_var, "Location A", "Location B", "Location C")
start_dropdown.grid(row=1, column=2, padx=10, pady=5)

start_entry = tk.Entry(root)
start_entry.grid(row=1, column=2, padx=10, pady=5)
start_entry.grid_remove()  # Hide the entry initially

def toggle_start_input(*args):
    if start_choice_var.get() == "Current Location":
        start_dropdown.grid_remove()
        start_entry.grid_remove()
    elif start_choice_var.get() == "Choose Location":
        start_dropdown.grid_remove()
        start_entry.grid()
    else:
        start_entry.grid_remove()
        start_dropdown.grid()

start_choice_var.trace_add("write", toggle_start_input)
toggle_start_input()

# End Location Entry
end_label = tk.Label(root, text="Final del trajecte:")
end_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
end_entry = tk.Entry(root)
end_entry.grid(row=2, column=1, padx=10, pady=5)

# Ruta Entry
ruta_label = tk.Label(root, text="Destination:")
ruta_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
ruta_var = tk.StringVar()
ruta_dropdown = tk.OptionMenu(root, ruta_var, "Destination 1", "Destination 2", "Destination 3")
ruta_dropdown.grid(row=3, column=1, padx=10, pady=5)

# Button to execute the program
execute_button = tk.Button(root, text="Execute", command=execute_program)
execute_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
