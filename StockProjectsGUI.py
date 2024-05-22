import tkinter as tk 
import joblib
import ktrain

window = tk.Tk()
window.geometry("1200x500")
window.title("Stock Analysis")
window.configure(bg= "#AEB6BF" )


def prediction1():  
    sn = str(entry.get())
    label3 = tk.Label(window, text="The results BERT model is : ", bg = "white",font=(30), width=50, height=3)
    label3.grid(column=1, row=8)
    
    clf =  ktrain.load_predictor("tf_model")
    data = clf.predict([sn])
    #print(clf())
    #print(clf)
    print(data)
    labeln = tk.Label(text=data, bg = "white",font=(15), width=30, height=1)
    labeln.grid(column=1, row=9)    
    
def prediction2(): #Naive Bayes
    sn = str(entry.get())
    label3 = tk.Label(window, text="The results model is : ", bg = "white",font=(30), width=50, height=3)
    label3.grid(column=1, row=8)
    clf = joblib.load("Naive Bayes_model")
    data = clf.predict([sn])
    print(data)
    for i in range(1):
        if(data[i]==0):
            labeln = tk.Label(text="The stock will go down", bg = "white",font=(15))
            labeln.grid(column=1, row=9)
        elif(data[i]==1):
            labeln = tk.Label(text="The stock will go up", bg = "white",font=(15))
            labeln.grid(column=1, row=9)


def prediction3():
    sn = str(entry.get())
    label3 = tk.Label(window, text="The results RandomForestClassifier model is : ", bg = "white",font=(30), width=50, height=3)
    label3.grid(column=1, row=8)
    
    clf = joblib.load("1model2_predictor")
    data = clf.predict([sn])
   # print(clf())
    print(data)
    
def reset():
    label3 = tk.Label(window, text="", bg = "#AEB6BF",font=(30), width=50, height=3)
    label3.grid(column=1, row=8)
    label3.config(text=" ")
    labeln = tk.Label(window, text="", bg = "#AEB6BF",font=(30), width=50, height=3)
    labeln.grid(column=1, row=9)
    labeln.config(text=" ")
    


label1 = tk.Label(text="Welcom to Stock Analysis", bg = "#AEB6BF",font=('Times 25'), width=0, height=1)
label1.place(x=35, y=35, anchor="center")
label1.grid(column=1, row=0)


label2 = tk.Label(text="Enter any sentance:", bg = "#AEB6BF",font=(50), width=50, height=3)
label2.grid(column=1, row=1)

label2 = tk.Label(text="", bg = "#AEB6BF" ,width=0, height=1)
label2.grid(column=0, row=2)
entry =tk.Entry(window, width=100, justify='center', font=('Arial 14'))
entry.grid(column=1,row=2)


label00 = tk.Label(text=" ", bg = "#AEB6BF", width=0, height=5)
label00.grid(column=0, row=4)


button1 = tk.Button(text="Bert model", command= prediction1, height=2) #name of the model 
button1.place(x=400, y= 170)


button2 = tk.Button(text=" model2", command= prediction2, height=2) #name of the model 
button2.place(x=500, y= 170)

button3 = tk.Button(text="RandomForestClassifier model", command= prediction3, height=2) #name of the model 
#button3.place(x=650, y= 170)

button4 = tk.Button(text="Reset", command= reset, height=2) #name of the model 
button4.place(x=850, y= 170)

window.mainloop()

