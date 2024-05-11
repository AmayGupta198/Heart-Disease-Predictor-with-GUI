import tkinter as tk
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow
import tkinter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
def predictHeartDisease():
    inputValues = []

    age1 = ((int(age.get()) - 29) / (77 - 29))
    print(age1)
    trestbps1 = ((int(rbp.get()) - 94) / (200 - 94))
    chol1 = ((int(serumChol.get()) - 126) / (564 - 126))
    thalach1 = ((int(thalach.get()) - 71) / (202 - 71))
    oldpeak1 = (int(oldpeak.get()) / (6.2))

    inputValues.append(age1)
    inputValues.append(int(sex.get()))
    inputValues.append(int(chestPain.get()))
    inputValues.append(trestbps1)
    inputValues.append(chol1)
    inputValues.append(int(FBS.get()))
    inputValues.append(int(ECG.get()))
    inputValues.append(thalach1)
    inputValues.append(trestbps1)
    inputValues.append(oldpeak1)
    inputValues.append(int(slope.get()))
    inputValues.append(int(ca.get()))
    inputValues.append(int(thal.get()))

    print(inputValues)

    print("\n")
    final_Result = knn_classifier.predict([inputValues])
    print(final_Result)

    substituteWindow = tk.Tk()
    substituteWindow.geometry('640x480-8-200')
    substituteWindow.title("RESULT PREDICTION")

    substituteWindow.columnconfigure(0, weight=2)
    substituteWindow.columnconfigure(1, weight=1)
    substituteWindow.columnconfigure(2, weight=2)
    substituteWindow.columnconfigure(3, weight=2)
    substituteWindow.rowconfigure(0, weight=1)
    substituteWindow.rowconfigure(1, weight=10)
    substituteWindow.rowconfigure(2, weight=10)
    substituteWindow.rowconfigure(3, weight=1)
    substituteWindow.rowconfigure(4, weight=1)
    substituteWindow.rowconfigure(5, weight=1)

    if final_Result[0] == 1:
        label1 = tk.Label(substituteWindow, text="HEART DISEASE DETECTED", font=('Times New Roman', -35, 'bold'), fg='#0080ff')
        label1.grid(row=0, column=1, columnspan=6)
        label2 = tk.Label(substituteWindow, text="PLEASE VISIT NEAREST CARDIOLOGIST AT THE EARLIEST",
                          font=('Times New Roman', -20), fg='red')
    else:
        label1 = tk.Label(substituteWindow, text="NO DETECTION OF HEART DISEASES", font=('Times New Roman', -35, 'bold'))
        label1.grid(row=2, column=1, columnspan=6)
        label2 = tk.Label(substituteWindow, text="Do not forget to exercise daily. ", font=('Times New Roman', -20),
                          fg='green')
        label2.grid(row=3, column=1, columnspan=6)

    substituteWindow.mainloop()

heart = pd.read_csv("heart.csv")
min_max = MinMaxScaler()
columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
heart[columns_to_scale] = min_max.fit_transform(heart[columns_to_scale])
y = heart['target']
X = heart.drop(['target'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)

knn_classifier = KNeighborsClassifier(n_neighbors=4)
knn_classifier.fit(X_train, y_train)

mainWindow = tk.Tk()
mainWindow.geometry('640x480')
mainWindow.title("HEART DISEASE PREDICTION")

mainWindow.configure(bg='#F9E79F')  # Changing background color

# Calculate center position
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
x = (screen_width / 2) - (640 / 2)
y = (screen_height / 2) - (480 / 2)
mainWindow.geometry(f'640x480+{int(x)}+{int(y)}')

label1 = tk.Label(mainWindow, text="HEART DISEASE PREDICTION MODEL", font=('Times New Roman', -35, 'bold'), bg='#FF5733', fg='white')
label1.grid(row=0, column=0, columnspan=6, pady=10)

label2 = tk.Label(mainWindow, text="Enter the details carefully", font=('Times New Roman', -20), fg='white', bg='#FFC300')
label2.grid(row=1, column=0, columnspan=6, pady=10)

entry_styles = {"font": ("Times New Roman", -15, 'bold')}

ageFrame = tk.LabelFrame(mainWindow, text="Age(yrs)", bg='#ABEBC6')  # Changing style and color
ageFrame.grid(row=2, column=0, padx=10, pady=5)
ageFrame.config(font=("Times New Roman", -15))
age = tk.Entry(ageFrame, **entry_styles)
age.grid(row=2, column=2, sticky='nw')

sexFrame = tk.LabelFrame(mainWindow, text="Sex", bg='#ABEBC6')
sexFrame.grid(row=2, column=1, padx=10, pady=5)
sexFrame.config(font=("Times New Roman", -15))
sex = tk.Entry(sexFrame, **entry_styles)
sex.grid(row=2, column=2, sticky='nw')

chestPainFrame = tk.LabelFrame(mainWindow, text="CP (0-4)", bg='#ABEBC6')
chestPainFrame.grid(row=2, column=2, padx=10, pady=5)
chestPainFrame.config(font=("Times New Roman", -15))
chestPain = tk.Entry(chestPainFrame, **entry_styles)
chestPain.grid(row=2, column=2, sticky='nw')

rbpFrame = tk.LabelFrame(mainWindow, text="RBP (94-200)", bg='#ABEBC6')
rbpFrame.grid(row=3, column=0, padx=10, pady=5)
rbpFrame.config(font=("Times New Roman", -15))
rbp = tk.Entry(rbpFrame, **entry_styles)
rbp.grid(row=2, column=2, sticky='nw')

serumCholFrame = tk.LabelFrame(mainWindow, text="Serum Chol", bg='#ABEBC6')
serumCholFrame.grid(row=3, column=1, padx=10, pady=5)
serumCholFrame.config(font=("Times New Roman", -15))
serumChol = tk.Entry(serumCholFrame, **entry_styles)
serumChol.grid(row=2, column=2, sticky='nw')

FBSFrame = tk.LabelFrame(mainWindow, text="Fasting BP(0-4)", bg='#ABEBC6')
FBSFrame.grid(row=3, column=2, padx=10, pady=5)
FBSFrame.config(font=("Times New Roman", -15))
FBS = tk.Entry(FBSFrame, **entry_styles)
FBS.grid(row=2, column=2, sticky='nw')

ECGFrame = tk.LabelFrame(mainWindow, text="ECG (0,1,2)", bg='#ABEBC6')
ECGFrame.grid(row=4, column=0, padx=10, pady=5)
ECGFrame.config(font=("Times New Roman", -15))
ECG = tk.Entry(ECGFrame, **entry_styles)
ECG.grid(row=2, column=2, sticky='nw')

thalachFrame = tk.LabelFrame(mainWindow, text="thalach(71-202)", bg='#ABEBC6')
thalachFrame.grid(row=4, column=1, padx=10, pady=5)
thalachFrame.config(font=("Times New Roman", -15))
thalach = tk.Entry(thalachFrame, **entry_styles)
thalach.grid(row=2, column=2, sticky='nw')

exangFrame = tk.LabelFrame(mainWindow, text="exAngina(0/1)", bg='#ABEBC6')
exangFrame.grid(row=4, column=2, padx=10, pady=5)
exangFrame.config(font=("Times New Roman", -15))
exang = tk.Entry(exangFrame, **entry_styles)
exang.grid(row=2, column=2, sticky='nw')

oldpeakFrame = tk.LabelFrame(mainWindow, text="Old Peak(0-6.2)", bg='#ABEBC6')
oldpeakFrame.grid(row=5, column=0, padx=10, pady=5)
oldpeakFrame.config(font=("Times New Roman", -15))
oldpeak = tk.Entry(oldpeakFrame, **entry_styles)
oldpeak.grid(row=2, column=2, sticky='nw')

slopeFrame = tk.LabelFrame(mainWindow, text="Slope(0,1,2)", bg='#ABEBC6')
slopeFrame.grid(row=5, column=1, padx=10, pady=5)
slopeFrame.config(font=("Times New Roman", -15))
slope = tk.Entry(slopeFrame, **entry_styles)
slope.grid(row=2, column=2, sticky='nw')

caFrame = tk.LabelFrame(mainWindow, text=" C. A (0-3)", bg='#ABEBC6')
caFrame.grid(row=5, column=2, padx=10, pady=5)
caFrame.config(font=("Times New Roman", -15))
ca = tk.Entry(caFrame, **entry_styles)
ca.grid(row=2, column=2, sticky='nw')

thalFrame = tk.LabelFrame(mainWindow, text=" THAL(0,1,2,3)", bg='#ABEBC6')
thalFrame.grid(row=6, column=1, padx=10, pady=5)
thalFrame.config(font=("Times New Roman", -15))
thal = tk.Entry(thalFrame, **entry_styles)
thal.grid(row=2, column=2, sticky='nw')

analyseButton = tk.Button(mainWindow, text="..................PREDICT NOW!.....................",
                          font=('Times New Roman', -15, 'bold'), bg='#FF5733', fg='white', command=predictHeartDisease)
analyseButton.grid(row=8, column=0, columnspan=3, pady=20)

mainWindow.mainloop()
