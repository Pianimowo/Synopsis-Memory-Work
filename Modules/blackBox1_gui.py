from universalFunctions import decoder

class blackBox:
    def __init__(self, input_voltage, ground, control):
        self.input_voltage = input_voltage
        self.ground = ground
        self.control = control




        self.newcontrol = decoder(self.control)

        size_of_gap = (self.input_voltage-self.ground)/float(2**len(self.control))


        self.output = self.ground + (size_of_gap*self.newcontrol)

    def get_output(self):
        print(self.output)




def test():
    print("Hello")





if __name__ == "__main__":
    blackBoxTest = blackBox(4, 0, [0, 1, 1, 1])
    blackBoxTest.get_output()

# GUI Integration
import tkinter as tk
from tkinter import messagebox

def run_blackbox():
    try:
        input_voltage = float(entry_voltage.get())
        ground = float(entry_ground.get())
        control = list(map(int, entry_control.get().split()))
        bb = blackBox(input_voltage, ground, control)
        output = bb.output
        output_label.config(text=f"Output: {output:.4f}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

if __name__ == "__main__":
    # Original test call removed in favor of GUI
    root = tk.Tk()
    root.title("blackBox Controller")

    tk.Label(root, text="Input Voltage:").grid(row=0, column=0)
    entry_voltage = tk.Entry(root)
    entry_voltage.insert(0, "4")
    entry_voltage.grid(row=0, column=1)

    tk.Label(root, text="Ground:").grid(row=1, column=0)
    entry_ground = tk.Entry(root)
    entry_ground.insert(0, "0")
    entry_ground.grid(row=1, column=1)

    tk.Label(root, text="Control (space-separated bits):").grid(row=2, column=0)
    entry_control = tk.Entry(root)
    entry_control.insert(0, "0 1 1 1")
    entry_control.grid(row=2, column=1)

    tk.Button(root, text="Compute Output", command=run_blackbox).grid(row=3, column=0, columnspan=2)

    output_label = tk.Label(root, text="Output: ")
    output_label.grid(row=4, column=0, columnspan=2)

    root.mainloop()
