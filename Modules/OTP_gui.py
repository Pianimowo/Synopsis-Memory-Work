import tkinter as tk
from OTP import OTP

class MemoryVisualizer:
    def __init__(self, master, otp):
        self.master = master
        self.otp = otp
        self.labels = []

        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack()

        for r in range(otp.memory.shape[0]):
            row = []
            for c in range(otp.memory.shape[1]):
                label = tk.Label(self.grid_frame, text="0.00", width=6, height=2, relief="ridge", borderwidth=1)
                label.grid(row=r, column=c)
                row.append(label)
            self.labels.append(row)

        refresh_btn = tk.Button(master, text="Refresh", command=self.update_grid)
        refresh_btn.pack(pady=10)

        self.update_grid()

    def update_grid(self):
        for r in range(self.otp.memory.shape[0]):
            for c in range(self.otp.memory.shape[1]):
                v = self.otp.memory[r, c]
                self.labels[r][c].config(text=f"{v:.2f}")
                self.labels[r][c].config(bg=self.voltage_color(v))
    
    def voltage_color(self, v):
        # Normalize to 0–255 red (VDD = red)
        VDD = self.otp.VDD
        intensity = int(255 * min(max(v / VDD, 0), 1))
        return f"#ff{255-intensity:02x}{255-intensity:02x}"  # shades of red

if __name__ == "__main__":
    root = tk.Tk()
    root.title("OTP Memory Grid")

    otp = OTP(5, 8, 0.4)
    otp.createGrid(8, 8)

    app = MemoryVisualizer(root, otp)
    root.mainloop()


# import tkinter as tk
# from tkinter import *
# from OTP import OTP

# class OTP_gui:
#     def __init__(self, master, otp):
#         self.master = master
#         self.otp = otp
#         self.labels = []
#         self.vdd = None
#         self.vpp = None
#         self.vrr = None
#         self.a = []
#         self.sel = None
#         self.d = None
#         self.we = None

#         self.grid_frame = tk.Frame(master)
#         self.grid_frame.pack()

#     def generateTable(self):
#         if self.getInputs() == 1:
#             instance = OTP(vdd, vpp, vrr)
#         else:
#             return


#     def getInputs():
#         try:
#             vdd = entry_VDD.get()
#             vpp = entry_VPP.get()
#             vrr = entry_VRR.get()
#             concatA = entry_A.get()
#             a = [int(item) for item in concatA.split()]
#             sel = entry_SEL.get()
#             d = entry_D.get()
#             we = entry_WE.get()
#             return 1
#         except Exception as e:
#             return 0


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("NVM OTP")

#     tk.Label(root, text="Length").grid(row=0, column=0)
#     entry_Length = tk.Entry(root).grid(row=0, column=1)

#     tk.Label(root, text="Width").grid(row=1, column=0)
#     entry_Width = tk.Entry(root).grid(row=1, column=1)

#     tk.Button(root, text="Generate Table", command=generateTable).grid(row=2, column=0, columnspan=2)


#     tk.Label(root, text="VDD").grid(row=3, column=0)
#     entry_VDD = tk.Entry(root).grid(row=3, column=1)

#     tk.Label(root, text="VPP").grid(row=4, column=0)
#     entry_VPP = tk.Entry(root).grid(row=4, column=1)

#     tk.Label(root, text="VRR").grid(row=5, column=0)
#     entry_VRR = tk.Entry(root).grid(row=5, column=1)

#     tk.Button(root, text="Initialize Table", command=generateTable).grid(row=6, column=0, columnspan=2)


#     tk.Label(root, text="A").grid(row=0, column=2)
#     entry_A = tk.Entry(root).grid(row=0, column=3)

#     tk.Label(root, text="SEL").grid(row=1, column=2)
#     entry_SEL = tk.Entry(root).grid(row=1, column=3)

#     tk.Label(root, text="D").grid(row=2, column=2)
#     entry_D = tk.Entry(root).grid(row=2, column=3)

#     tk.Label(root, text="WE").grid(row=3, column=2)
#     entry_WE = tk.Entry(root).grid(row=3, column=3)

#     tk.Button(root, text="Update Inputs", command=generateTable).grid(row=4, column=2, columnspan=2)


#     root.mainloop()