# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:34:42 2019

@author: MEHMET OLGUN
"""

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN


class verimadenciligi():
    veriler=[]
    def veriimport(self):
        global veriler
        filepath = filedialog.askopenfilename()
        if filepath!='':
            veriler = pd.read_csv(filepath)
            print(veriler)
    def kMeans(self):
        global veriler
        pencere = Tk()     
        pencere.title(string = "kMeans")
        kmeans = KMeans(n_clusters=int(txtK.get()),random_state=0).fit(veriler)
        Y_kmeans = kmeans.predict(veriler)          
        figure1=plt.figure(figsize=(12, 12))
        veri = veriler.to_numpy()        
        plt.scatter(veri[:,0], veri[:,1], c=Y_kmeans ,s=50, cmap='viridis')
        plt.title("K-Means")
        scatter1 = FigureCanvasTkAgg(figure1, pencere) 
        scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)    
    def Agglomerative(self):
        global veriler
        veri = veriler.to_numpy()    
        pencere = Tk()     
        pencere.title(string = "Agglomerative")
        agglomerative = AgglomerativeClustering(n_clusters=int(txtKume.get()), affinity='euclidean', linkage='ward')
        Y_Agglomerative = agglomerative.fit_predict(veriler)
        figure1=plt.figure(figsize=(12, 12))
        plt.scatter(veri[:,0], veri[:,1], c=Y_Agglomerative ,s=50, cmap='viridis')
        plt.title("Agglomerative")
        scatter1 = FigureCanvasTkAgg(figure1, pencere) 
        scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)  
        
    def DBScan(self):
        global veriler
        veri = veriler.to_numpy()  
        pencere = Tk()    
        pencere.title(string = "DBSCAN")
        Y_DBSCAN = DBSCAN(eps=int(txtEps.get()), min_samples=int(txtMinPts.get())).fit_predict(veriler)
        figure1=plt.figure(figsize=(12, 12))
        plt.scatter(veri[:,0], veri[:,1], c=Y_DBSCAN ,s=50, cmap='viridis')
        plt.title("DBScan")
        scatter1 = FigureCanvasTkAgg(figure1, pencere) 
        scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)  
    
pencere = Tk()
pencere.title(string = "Veri Madenciliği - Mehmet OLGUN")
pencere.geometry("650x350")

vm = verimadenciligi()

btn1 = Button(pencere,text='Veri Seti Ekle',width=10,height=1,command = vm.veriimport)
btn1.grid(row =0,column=0,rowspan=1,pady=2,padx=25)

btn2 = Button(pencere,text='k-Means İle Hesapla',width=20,height=1,command = vm.kMeans)
btn2.grid(row =0,column=1,rowspan=1,pady=2,padx=15)

btn3 = Button(pencere,text='Agglomerative İle Hesapla',width=20,height=1,command = vm.Agglomerative)
btn3.grid(row =0,column=2,rowspan=1,pady=2,padx=15)

btn4 = Button(pencere,text='DBScan İle Hesapla',width=15,height=1,command = vm.DBScan)
btn4.grid(row =0,column=3,rowspan=1,pady=2,padx=15)

label1 = Label(pencere,text="K Değeri :")
label1.grid(row=1,column=0)
txtK = Entry(pencere,bd=1)
txtK.grid(row=1,column=1,columnspan=2,padx=2,pady=25)
label2 = Label(pencere,text="Küme Sayısı :")
label2.grid(row=2,column=0)
txtKume = Entry(pencere,bd=1)
txtKume.grid(row=2,column=1,columnspan=2,padx=2,pady=25)
label3 = Label(pencere,text="EPS :")
label3.grid(row=3,column=0)
txtEps = Entry(pencere,bd=1)
txtEps.grid(row=3,column=1,columnspan=2,padx=2,pady=25)
label4 = Label(pencere,text="MinPts :")
label4.grid(row=4,column=0)
txtMinPts = Entry(pencere,bd=1)
txtMinPts.grid(row=4,column=1,columnspan=2,padx=2,pady=25)
labelMy = Label(pencere,text="Mehmet Olgun")
labelMy.grid(row=5,column=3)



pencere.mainloop()

