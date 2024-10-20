import tkinter as tk
from tkinter import ttk, messagebox
import dataSaver as data
from random import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Restrictive Pairs!")

        # Cadre 1
        self.frame1 = ttk.Frame(root, padding="10")
        self.frame1.grid(row=0, column=0, sticky="ew")
        
        self.labelName = ttk.Label(self.frame1, text="Add a person:")
        self.labelName.grid(row=0, column=0, padx=5, pady=5)

        self.entryFirstName = ttk.Entry(self.frame1)
        self.entryFirstName.grid(row=1, column=0, padx=5, pady=5)

        self.entryLastName = ttk.Entry(self.frame1)
        self.entryLastName.grid(row=1, column=1, padx=5, pady=5)

        self.entryTeam = ttk.Entry(self.frame1)
        self.entryTeam.grid(row=2, column=0, padx=5, pady=5)

        self.buttonAdd = ttk.Button(self.frame1, text="Add", command=self.addName)
        self.buttonAdd.grid(row=2, column=1, padx=5, pady=5)

        # Cadre 2 
        self.frame2 = ttk.Frame(root, padding="10")
        self.frame2.grid(row=1, column=0, sticky="ew")
        
        self.labelList = ttk.Label(self.frame2, text="List:")
        self.labelList.grid(row=0, column=0, pady = 5)

        self.listboxNames = tk.Listbox(self.frame2, width=30)
        self.listboxNames.grid(row=1, column=0, padx=5, pady=5)

        self.buttonDelete = ttk.Button(self.frame2, text="Delete", command=self.deleteSomeone)
        self.buttonDelete.grid(row=2, column=0, pady=5)

        self.scrollbar = ttk.Scrollbar(self.frame2, orient=tk.VERTICAL, command=self.listboxNames.yview)
        self.scrollbar.grid(row=1, column=2, sticky='ns')

        self.listboxNames.config(yscrollcommand=self.scrollbar.set)

        # Cadre à droite
        self.frameInfo = ttk.Frame(root, padding="10", width=300)
        self.frameInfo.grid(row=0, column=1, rowspan=2, sticky="ns")

        self.labelInfo = ttk.Label(self.frameInfo, text="Pairs:")
        self.labelInfo.pack(pady=5)

        self.textInfo = tk.Text(self.frameInfo, width=30, height=10, font=("Arial", 10))
        self.textInfo.pack(pady=5)

        self.buttonShow = ttk.Button(self.frameInfo, text="Make pairs", command=self.takeCoffee)
        self.buttonShow.pack(pady=5)
        
        self.loadNames()

    def takeCoffee(self):
        permanentList=[]
        pairs=[]
        suppressedPerson=[]
        for i in data.loadData():
            permanentList.append(i)
        

        for z in permanentList:
            pplInList = self.nbPeopleInTheTeam(z['team'],permanentList)
            if float(len(z['Coffeed'])+pplInList)>=float((len(permanentList)-1)*data.loadDestroyEverything()):
                z['Coffeed']=[]
        
        numberIterations=0
        
        if len(permanentList)%2==1:
            suppressedPerson=permanentList[0]
            permanentList.pop(0)
        while len(pairs)!=len(permanentList)//2 and numberIterations<data.loadTolerance():
            shuffle(permanentList)
            for i in range(len(permanentList)):
                for otherPerson in range(len(permanentList)):
                    if self.checkSelf(permanentList[i],permanentList[otherPerson])==False:
                        if self.checkAlreadyCoffeed(permanentList[i],permanentList[otherPerson])==False:
                            if self.checkAlreadyPairs(permanentList[i],permanentList[otherPerson],pairs)==False:
                                if self.checkTeam(permanentList[i],permanentList[otherPerson])==False:
                                    pairs.append([permanentList[i],permanentList[otherPerson]])
            if len(pairs)!=len(permanentList)//2:
                pairs=[]
            numberIterations+=1
        if numberIterations>data.loadTolerance()-5:
            messagebox.showwarning("Endless loop", "The code was running for too much time! Please see the readme.md file or options.json")





        print(numberIterations)
        if numberIterations<data.loadTolerance()-5:
            finalText=""
            self.textInfo.delete("1.0",tk.END)
            for twoPeople in pairs:
                for people in twoPeople:
                    for i in permanentList:
                        if i==people:
                            if people == twoPeople[0]:
                                people2=twoPeople[1]
                                finalText+=f"{people['firstName']} {people['lastName']}"+" is in pair with "+f"{people2['firstName']} {people2['lastName']}"
                            else:
                                people2=twoPeople[0]
                            i['Coffeed'].append(f"{people2['firstName']} {people2['lastName']}")
                finalText+="\n"
            if suppressedPerson!=[]:
                finalText+=f"{suppressedPerson['firstName']} {suppressedPerson['lastName']}"+" is alone."
                permanentList.append(suppressedPerson)
            self.textInfo.insert("1.0",finalText)
            data.saveData(permanentList)

    def nbPeopleInTheTeam(self,teamNumber,lst):
        sum=0
        for i in lst:
            if int(i['team'])==int(teamNumber):
                sum+=1
        return sum


    def checkTeam(self,people1,people2):
        if people1['team']==people2['team']:
            return True
        else:
            return False

    def checkSelf(self,people1,people2):
        if people1==people2:
            return True
        else:
            return False

    def checkAlreadyPairs(self,people1,people2,pairList):
        for i in pairList:
            for nb in range(len(i)):
                if i[nb]['firstName']==people1['firstName'] or i[nb]['firstName']==people2['firstName']:
                    return True
        return False
    def checkAlreadyCoffeed(self,people1,people2):
        if people1['Coffeed']!=[]:
            for z in people1['Coffeed']:
                if z == f"{people2['firstName']} {people2['lastName']}":
                    return True
        return False
    def loadNames(self):
        self.listboxNames.delete(0, tk.END)
        for people in data.loadData():
            self.listboxNames.insert(tk.END, f"{people['firstName']} {people['lastName']} | {people['team']}")

    def addName(self):
        firstName = self.entryFirstName.get()
        lastName = self.entryLastName.get()
        team = self.entryTeam.get()
        if firstName and lastName and team:
            if self.isint(team) == False:
                messagebox.showwarning("Error!", "The team (3rd box) has to be an integer.")
            else:
                employe = {
                    "firstName": firstName,
                    "lastName": lastName,
                    "team": team,
                    "Coffeed": []
                }
                data.employes.append(employe)
                self.listboxNames.insert(tk.END, f"{firstName} {lastName} | {team}")
                data.saveData(data.employes)
                self.entryFirstName.delete(0, tk.END)
                self.entryLastName.delete(0, tk.END)
                self.entryTeam.delete(0, tk.END)
        else:
            messagebox.showwarning("Error!", "You need to write in each box. The first is the first name, the second one is the last name, and the third one, is the team.")

    def isint(self,number):
        try:
            int(number)
            return True
        except ValueError:
            return False
    def deleteSomeone(self):
        selected = self.listboxNames.curselection()
        if selected:
            index = selected[0]
            del data.employes[index]
            data.saveData(data.employes)
            self.loadNames()
        else:
            messagebox.showwarning("Error!", "You need to select a person.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
