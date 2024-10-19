import json
import os
from tkinter import messagebox

def loadData():
    try:
        with open('data.json', 'r') as fichier:
            return json.load(fichier)
    except json.JSONDecodeError as e:
        messagebox.showwarning("JSON Error", f"data.json encounters an error: {e}")
        return []
    

def saveData(toAdd):
    with open('data.json', "w") as fichier:
        json.dump(toAdd, fichier, indent=4)


def loadOptions():
    try:
        with open('options.json', 'r') as fichier:
            return json.load(fichier)
    except json.JSONDecodeError as e:
        messagebox.showwarning("JSON Error", f"options.json encounters an error: {e}")

def loadTolerance():
    for options in loadOptions():
        return options['tolerance']
    
def loadDestroyEverything():
    for options in loadOptions():
        return options['destroyEverything']


employes = loadData()