class saat_():

 def __init__(self,saat):
     self.saat = saat
     self.por = False

class p_nobat():
    
    def __init__(self,rooz,saatha):
     self.rooz = rooz
     self.saatha = saatha
     

class b_nobat():
    
    def __init__(self,rooz,saat,nam):
     self.rooz = rooz
     self.saat = saat
     self.nam = nam



class pezeshk():
    
    def __init__(self,nam,name_khanevadegi,takhasos,address,shomare_telephone,shomare_mobail):
     self.nam = nam
     self.name_khanevadegi = name_khanevadegi
     self.shomare_telephone = shomare_telephone
     self.shomare_mobail = shomare_mobail
     self.address = address
     self.takhasos = takhasos
     self.payam_ha = None
     self.tedad_bimar_ha = 0
     self.nobatha = None
     self.nobat_haye_gerfte_shode = None
    def sabt_saat_kari(self,nobat):
        temp = False
        for x in self.nobatha: 
         if x.rooz == nobat.rooz:
             """rooz vared shode tekrari ast"""
             for y in x.saatha:
                if y == nobat.saat:
                 """saat vared shode tekrari ast"""
                 temp = True
        if temp == False:     
         self.nobatha.append(nobat)
        else:
         print("nobat ghablan gerefte shode ast")
    def namayesh_jadval_nobatha(self,bimarha):
        for bimar in bimarha:
         temp = False
         for x in self.nobatha: 
           if x.rooz == bimar.nobat.rooz:
             """rooz vared shode tekrari ast"""
             for y in x.saatha:
               if  y == bimar.nobat.saat:
                 """saat vared shode tekrari ast"""
                 temp = True
                 self.tedad_bimar_ha = self.tedad_bimar_ha + 1
         if temp == True:     
              print("hi")
              """show in gui"""
    def afzodane_payam(self,payam):    
         self.payam_ha.append(payam)     
    def hazfe_payam(self,shomare):
        self.payam_ha.pop(shomare)    
        
        
    def gereftane_b_nobat(self,nobat):    
       temp = False
       for x in self.nobatha: 
         if x.rooz == nobat.rooz:
             """rooz mojod ast"""
             for y in x.saatha:
                if y.saat == nobat.saat:
                 """saat mojod ast"""
                 if y.por == False:
                    temp = True
       if temp == True: 
         self.nobat_haye_gerefte_shode.append(nobat)
    
    def laghve_nobat(self,nobat):
      temp = False
      for x in self.nobat_haye_gerefte_shode: 
         if x.nam == nobat.nam:
           if x.rooz == nobat.rooz:
                if x.saat == nobat.saat:
                       temp = True
      if temp == True: 
         self.nobat_haye_gerefte_shode.remove(nobat)
    
    """dorost kardane tavabe jostojo""" 
        
    """dorost kardane tavabe nobat giri va laghve nobat"""

    
    
class bimar():
   
    def __init__(self,nam,name_khanevadegi,shomare_mobail):
     self.nam = nam
     self.name_khanevadegi = name_khanevadegi
     self.shomare_mobail = shomare_mobail
     
     
     
     
     
import tkinter as tk
from tkinter import messagebox as mb
Gui = tk.Tk()
Gui.geometry("800x430")
text_to_save = None

def gerftane_vorodi():
 canvas = tk.Canvas(Gui,width = 400 ,height = 300)
 canvas.pack()
 entry = tk.Entry(Gui)
 canvas.create_window(200,140,window = entry)
 def a():
    entry.delete(0,'end')
    
 clear = tk.Button(Gui,text="clear",command = a) 
 """should save and delete instead just delete"""
 clear.pack()

"""dorost kardane tabe pak kardane kole safhe"""

def vared_shodan_pezeshk():
"""pak kardane safhe """
"""gereftane vorodi"""
"""zakhire"""

"""dorost kardane jostojo baraye pezeshk"""
"""dorost kardane namayesh jadval baraye pezeshk ha"""



    

vorod_pezeshk = tk.Button(Gui,"vorod be onvane pezeshk",command = vared_shodan_pezeshk)

vorod_bimar = tk.Button(Gui,"vorod be onvane pezeshk",command = vared_shodan_bimar)    
     









     
     
class main():
    def __init__(self):
      """az file agar mojod bood vared shavad"""  
      self.bimar_ha = None
      self.pezeshk_ha = None
    def afzodane_pezeshk(self,pezeshk_jadid):
       self.pezeshk_ha.append(pezeshk_jadid)
       """zakhire dar file"""
    def afzodane_bimar(self,bimar_jadid):
       self.bimar_ha.append(bimar_jadid)
       """zakhire dar file"""
           
    """jostojoye pezeshk ba nam va ..."""
    
       
        
        
        
        
        
        
        
        
        
        
         
