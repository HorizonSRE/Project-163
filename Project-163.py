from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Heart Diagnose Report")
root.geometry("540x540")
root.configure()

q1_rBtn = StringVar(value = "0")
q1 = Label(root, text = "Do you experience shortness of breath during routine activities ?")
q1.pack()
q1_r1 = Radiobutton(root, text = "Yes", variable = q1_rBtn, value = "Yes")
q1_r1.pack()
q1_r2 = Radiobutton(root, text = "No", variable = q1_rBtn, value = "No")
q1_r2.pack()

q2_rBtn = StringVar(value = "0")
q2 = Label(root, text = "Do you have swelling in the feet / ankles / legs (shoes feel tighter) or abdomen ?")
q2.pack()
q2_r1 = Radiobutton(root, text = "Yes", variable = q2_rBtn, value = "Yes")
q2_r1.pack()
q2_r2 = Radiobutton(root, text = "No", variable = q2_rBtn, value = "No")
q2_r2.pack()

q3_rBtn = StringVar(value = "0")
q3 = Label(root, text = "Do you feel any symptoms - confusion, disorientation or loss of memory ?")
q3.pack()
q3_r1 = Radiobutton(root, text = "Yes", variable = q3_rBtn, value = "Yes")
q3_r1.pack()
q3_r2 = Radiobutton(root, text = "No", variable = q3_rBtn, value = "No")
q3_r2.pack()

q4_rBtn = StringVar(value = "0")
q4 = Label(root, text = "Do you experience shortness of breath while at rest / lying down ?")
q4.pack()
q4_r1 = Radiobutton(root, text = "Yes", variable = q4_rBtn, value = "Yes")
q4_r1.pack()
q4_r2 = Radiobutton(root, text = "No", variable = q4_rBtn, value = "No")
q4_r2.pack()

q5_rBtn = StringVar(value = "0")
q5 = Label(root, text = "Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus ?")
q5.pack()
q5_r1 = Radiobutton(root, text = "Yes", variable = q5_rBtn, value = "Yes")
q5_r1.pack()
q5_r2 = Radiobutton(root, text = "No", variable = q5_rBtn, value = "No")
q5_r2.pack()

def hd_score():
    score = 0
    if q1_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q2_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q3_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q4_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if q5_rBtn.get() == "Yes":
        score = score + 10
        print(score)
        
    if score == 10:
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
        
    elif score > 10 and score == 30:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
    
    else:
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor.")

btn = Button(root, text = "Show Report", command = hd_score)
btn.pack()

root.mainloop()