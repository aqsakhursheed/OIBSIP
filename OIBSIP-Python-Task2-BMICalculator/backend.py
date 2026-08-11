import tkinter as tk
def calculate_BMI():
    try:
        w=float(weight_entry.get())
        h=float(height_entry.get())
        if w<=0 or h<=0:
            result_label.config(text="Please , entre positive numbers only.")
            return
        h2=h*h
        cal=w/h2
        if cal<18.5:
            result_label.config(text=f"BMI:{cal:.2f}, Underweight", fg="Red")
        elif cal >= 18.5 and cal <= 24.9:
            result_label.config(text=f"BMI:{cal:.2f}, Normal", fg="Green")
        elif cal >= 25 and cal <= 29.9:
            result_label.config(text=f"BMI:{cal:.2f}, Overweight", fg="Red")
        else: 
            result_label.config(text=f"BMI:{cal:.2f}, Obese", fg="Red")
    except ValueError:
        result_label.config(text="Please, enter numbers only")


root=tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

tk.Label(root, text="Weight (kg):").pack()
weight_entry=tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack()
height_entry=tk.Entry(root)
height_entry.pack()

calculate_btn=tk.Button(root, text="Calculate" , command=calculate_BMI)
calculate_btn.pack()

result_label=tk.Label(root, text="")
result_label.pack()

root.mainloop()