import tkinter as tk

root = tk.Tk()
root.wm_attributes("-transparentcolor", "white")	# 흰색을 투명하도록 지정
root.wm_attributes("-topmost", 1)
root.attributes("-fullscreen",not root.attributes("-fullscreen"))
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
canvas = tk.Canvas(root, width=monitor_width, height=monitor_height, bg='white')	# 배경을 흰색으로 지정
canvas.grid(columnspan=3, rowspan=3)
instructions = tk.Label(root,wraplength=1000, text="HelloSDAFSDFASFASDASDFASDFADFASDFDSASDFSDSAFADSFASDFASDFASDFADSFASDFADSFASDFADFASDFASDFASDFASDFASDFASDFSDFASDFASDFADWSFSDSDFDSFASDASDFASDFASDFSDFASDFDFASDFASDFASDASDFD World", font="Raleway")
instructions.grid(columnspan=3, column=0, row=0)

root.mainloop()