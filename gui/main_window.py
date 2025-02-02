# Fill, vent, ignite, start recording buttons. 
# Settings/Calibration button that opens window to change sample rate, transducer calibration offset + slope, DAC ports. 
# Save button that opens window for options to save certain columns of data, specify file type. ALso options for saving plot like title, axis labels, file type.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title("Crawford Bomb Control Program")
#root.geometry("800x600")

ttk.Label(root, text="High Pressure Combustion Experiment Control | Energetic Materials Combustion Lab").grid(row=0, column=0, sticky="nesw", padx=5)

chamber_frame = ttk.LabelFrame(root, text="Chamber Control", width=800)
chamber_frame.grid(row=1, column=0, sticky="nesw", pady=10, padx=10)

# Components within Chamber Control frame
controls_frame = ttk.Frame(chamber_frame)
controls_frame.grid(row=0, column=0, sticky="nesw")

plot_frame = ttk.Frame(chamber_frame)
plot_frame.grid(row=0, column=1, sticky="nesw")


camera_frame = ttk.LabelFrame(root, text="Camera Control", width=800)
camera_frame.grid(row=2, column=0, sticky="nesw", pady=10, padx=10)


root.mainloop()
