from tkinter import messagebox as mb


class main():
    def __init__(self):
      """az file agar mojod bood vared shavad"""  
      self.bimar_ha = []
      self.pezeshk_ha = []
    def afzodane_pezeshk(self,pezeshk_jadid):
      if self.check_kardane_tekrari_nabodan_pezeshk(pezeshk_jadid) == False:
         self.pezeshk_ha.append(pezeshk(pezeshk_jadid.nam,pezeshk_jadid.name_khanevadegi,pezeshk_jadid.takhasos,pezeshk_jadid.address,pezeshk_jadid.shomare_telephone,pezeshk_jadid.shomare_mobail))
      else:
          msg = mb.showinfo("System_msg", "pezeshk tekrari ast")

    def afzodane_bimar(self,bimar_jadid):
     if self.check_kardane_tekrari_nabodan_bimar(bimar_jadid) == False:
         self.bimar_ha.append(bimar(bimar_jadid.nam,bimar_jadid.name_khanevadegi,bimar_jadid.shomare_mobail))
     else:
         msg = mb.showinfo("System_msg", "bimar tekrari ast")
    def josto_joye_pezeshk(self,p):
        temp = False
        for x in self.pezeshk_ha:
            if x.nam == p.nam and x.name_khanevadegi == p.name_khanevadegi:
                temp = True

        return temp


    def peyda_kardane_pezeshk(self,p):
        for x in self.pezeshk_ha:
            if x.nam == p.nam and x.name_khanevadegi == p.name_khanevadegi:
                return x

    
    def peyda_kardane_bimar(self,b):
        for x in self.bimar_ha:
            if x.nam == b.nam and x.name_khanevadegi == b.name_khanevadegi:
                return x



    def check_kardane_tekrari_nabodan_pezeshk_wt(self,nam,nam_khanevade):
        temp = False
        for x in self.pezeshk_ha:
            if x.nam == nam and x.name_khanevadegi == nam_khanevade:
                temp =  True

        return temp

    def check_kardane_tekrari_nabodan_pezeshk(self, p):
        print("chack kardane tekrari nabodane pezeshk")
        temp = False
        for x in self.pezeshk_ha:
            if x.nam == p.nam and x.name_khanevadegi == p.name_khanevadegi:
                temp = True

        return temp


    def josto_joye_bimar(self,b):
        temp = False
        for x in self.bimar_ha:
            if x.nam == b.nam and x.name_khanevadegi == b.name_khanevadegi:
                temp = True
        if temp == False :
                print("pezeshk morede nazar yaft nashod")
        return temp



    def check_kardane_tekrari_nabodan_bimar_wt(self,nam,nam_khanevade):
        temp = False
        for x in self.bimar_ha:
            if x.nam == nam and x.name_khanevadegi == nam_khanevade:
                temp = True

        return temp

    def check_kardane_tekrari_nabodan_bimar(self,b):
            temp = False
            for x in self.bimar_ha:
                if x.nam == b.nam and x.name_khanevadegi == b.name_khanevadegi:
                    temp = True
            return temp
                  
    def namayesh_nobat_haye_b(self,p,b,t):
       global str2
       str2 = "rooz" + "\t" + "saat" + "\t" + "nam va namkhanevade pezeshk" + "\n"
       for p in self.pezeshk_ha:
        for n in p.nobat_haye_gerefte_shode:
          if n.nam == b.nam and n.name_khanevadegi == b.name_khanevadegi :
                      str2 = str2 + n.rooz + "\t"
                      str2 = str2 + n.saat + "\t"
                      str2 = str2 + p.nam + " " + p.name_khanevadegi + "\n"
                      t = t + 1
       return str2
    
    def namayesh_nobat_haye_bimar(self,bim,t):
        for pez in self.pezeshk_ha:
           mb.showinfo("saat haye kari:", self.namayesh_nobat_haye_b(pez,bim,t))


    def afzodane_saat_kari_pezeshk(self,p,n):
        for pez in self.pezeshk_ha:
            if pez.nam == p.nam and pez.name_khanevadegi == p.name_khanevadegi :
                pez.sabt_saat_kari(n)

        
class saat_():

 def __init__(self,saat):
     self.saat = saat
     self.por = False

class p_nobat():
    
    def __init__(self,rooz,saat):
     self.rooz = rooz
     self.saat = saat_(saat)
     

class b_nobat():
    
    def __init__(self,rooz,saat,nam,name_khanevadegi):
     self.rooz = rooz
     self.saat = saat
     self.nam = nam
     self.name_khanevadegi = name_khanevadegi


class pezeshk():
    
    def __init__(self,nam,name_khanevadegi,shomare_telephone,shomare_mobail,address,takhasos):
     self.nam = nam
     self.name_khanevadegi = name_khanevadegi
     self.shomare_telephone = shomare_telephone
     self.shomare_mobail = shomare_mobail
     self.address = address
     self.takhasos = takhasos
     self.payam_ha = []
     self.tedad_bimar_ha = 0
     self.nobatha = []
     self.nobat_haye_gerefte_shode = []
     
    def sabt_saat_kari(self,nobat):
        temp = False
        for x in self.nobatha: 
         if x.rooz == nobat.rooz and x.saat.saat == nobat.saat.saat:
                 temp = True
        if temp == False:     
         self.nobatha.append(p_nobat(nobat.rooz,nobat.saat.saat))
        else:
         msg = mb.showinfo("System_msg", "in nobat ghablan sabt shode ast")
   

    def afzodane_payam(self,payam):    
         self.payam_ha.append(payam)     
    def hazfe_payam(self,shomare):
        self.payam_ha.pop(shomare)    
        
        
    def gereftane_b_nobat(self,nobat):    
       temp = False
       for x in self.nobatha: 
         if x.rooz == nobat.rooz and x.saat.saat == nobat.saat and x.saat.por == False:
          temp = True
          x.saat.por = True
       if temp == True:
         self.nobat_haye_gerefte_shode.append(b_nobat(nobat.rooz,nobat.saat,nobat.nam,nobat.name_khanevadegi))
    
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

    def namayesh_saat_kari_pezeshk(self):
        global str
        str = "rooz" + "\t" + "saat" + "\t" + "gerefte shode ast:" + "\n"
        for n in self.nobatha:
            str = str + n.rooz + "\t"
            str = str + n.saat.saat + "\t"
            if n.saat.por == True:
             str = str + "bale" + "\n"
            else:
             str = str + "kheyr" + "\n"
        return str

class bimar():
   
    def __init__(self,nam,name_khanevadegi,shomare_mobail):
     self.nam = nam
     self.name_khanevadegi = name_khanevadegi
     self.shomare_mobail = shomare_mobail
     self.shomare_nobat = None
     self.payam = None
     self.laghv = None
     self.tedad_nobat_haye_gerefte_shode = 0
     self.p_n = " "
     self.p_nk = " "
     self.h_payam = None



















import tkinter as tt

root = tt.Tk()
root.geometry("800x430")
#global pezeshk_
pezeshk_ = pezeshk(None,None,None,None,None,None)
#global bimar_
bimar_ = bimar(None,None,None)
#global MAIN_CONTROLLER
MAIN_CONTROLLER = main()

class counter: 
    
    def __init__(self,count):
        self.count = count
        self.b = False
        
    def get_(self):
        return self.count
    
    def up_count(self):
        self.count = self.count + 1
        
    def down_count(self):
        self.count = self.count - 1    
        
    def set_(self,count):
        self.count = count
        
    def can_count(self):
        return self.b    
    
    def set_can(self,b):
        self.b = b

#code haye gereftane vorodi va motaghayer haye pezeshk
text_to_get = tt.StringVar()
canvas = tt.Canvas(root,width = 400 ,height = 300)
entry = tt.Entry(root,textvariable = text_to_get)
entry.focus_set()
canvas.create_window(200,140,window = entry)
counter_ = counter(0)
main_label = tt.Label( root,text = "bimarestan" )    


def a():  
    if not(len(entry.get()) == 0) and counter_.can_count() == False :
     save(text_to_get.get())
     if counter_.get_() == 0 :
        pezeshk_.nam = get()
     if counter_.get_() == 1 :
        pezeshk_.name_khanevadegi = get()
     if counter_.get_() == 2 :
        pezeshk_.takhasos = get()
     if counter_.get_() == 3 :
        pezeshk_.address = get() 
     if counter_.get_() == 4 :
        pezeshk_.shomare_telephone = get() 
     if counter_.get_() == 5 :
        pezeshk_.shomare_mobail = get()
     counter_.set_can(True)
     entry.delete(0,'end')
     print(get())
     
def b():
    
    if not(len(entry.get()) == 0) and counter_.can_count() == True :
     counter_.set_can(False)
     if counter_.get_() < 5 :
      counter_.up_count() 
     else:
      tavaghofe_gereftane_vorodi_pezeshk()     
    
def save(t):
    global s
    s = t
    
def get():
   return s


#code haye gereftane vorodi va motaghayer haye bimar
text_to_get2 = tt.StringVar()
canvas2 = tt.Canvas(root,width = 400 ,height = 300)
entry2 = tt.Entry(root,textvariable = text_to_get2)
entry2.focus_set()
canvas2.create_window(200,140,window = entry2)
counter2_ = counter(0)

def a2():  
    if not(len(entry2.get()) == 0) and counter2_.can_count() == False :
     save2(text_to_get2.get())
     counter2_.set_can(True)
     if counter2_.get_() == 0:
        bimar_.nam = get2()
     if counter2_.get_() == 1:
        bimar_.name_khanevadegi = get2()
     if counter2_.get_() == 1:
        bimar_.shomare_mobail = get2()   
     entry2.delete(0,'end')
     print(get2())

def b2():
    
    if not(len(entry2.get()) == 0) and counter2_.can_count() == True :
     counter2_.set_can(False)
     if counter2_.get_() < 2 :
      counter2_.up_count()
     else:
      tavaghofe_gereftane_vorodi_bimar()
    
def save2(t):
    global s2
    s2 = t
    
def get2():
   return s2



#code haye gereftane vorodi va motaghayer haye pezeshk mojod
text_to_get3 = tt.StringVar()
canvas3 = tt.Canvas(root,width = 400 ,height = 300)
entry3 = tt.Entry(root,textvariable = text_to_get3)
entry3.focus_set()
canvas3.create_window(200,140,window = entry3)
counter3_ = counter(0)

def a3():  
    if not(len(entry3.get()) == 0) and counter3_.can_count() == False :
     save3(text_to_get3.get())
     counter3_.set_can(True)
     if counter3_.get_() == 0:
        pezeshk_.nam = get3()
     if counter3_.get_() == 1:
        pezeshk_.name_khanevadegi = get3()
     entry3.delete(0,'end')
     print(get3())

def b3():
    
    if not(len(entry3.get()) == 0) and counter3_.can_count() == True :
     counter3_.set_can(False)
     if counter3_.get_() < 1 :
      counter3_.up_count()
     else:
      tavaghofe_gereftane_vorodi_pezeshk_mojod()
    
def save3(t):
    global s3
    s3 = t
    
def get3():
   return s3



#code haye gereftane vorodi va motaghayer haye bimar mojod
text_to_get4 = tt.StringVar()
canvas4 = tt.Canvas(root,width = 400 ,height = 300)
entry4 = tt.Entry(root,textvariable = text_to_get4)
entry4.focus_set()
canvas4.create_window(200,140,window = entry4)
counter4_ = counter(0)

def a4():
    if not (len(entry4.get()) == 0) and counter4_.can_count() == False:
        save4(text_to_get4.get())
        counter4_.set_can(True)
        if counter4_.get_() == 0:
            bimar_.nam = get4()
        if counter4_.get_() == 1:
            bimar_.name_khanevadegi = get4()
        entry4.delete(0, 'end')
        print(get4())

def b4():
    
    if not(len(entry4.get()) == 0) and counter4_.can_count() == True :
     counter4_.set_can(False)
     if counter4_.get_() < 1 :
      counter4_.up_count()
     else:
      tavaghofe_gereftane_vorodi_bimar_mojod()
    
def save4(t):
    global s4
    s4 = t
    
def get4():
   return s4



#code haye gereftane vorodi va motaghayer haye bimar mojod
text_to_get5 = tt.StringVar()
canvas5 = tt.Canvas(root,width = 400 ,height = 300)
entry5 = tt.Entry(root,textvariable = text_to_get5)
entry5.focus_set()
canvas5.create_window(200,140,window = entry5)
counter5_ = counter(0)
rooz = tt.Label(root , text = "rooz")
saat = tt.Label(root , text = "saat")


def a5():
    global r
    global s
    global time
    if not (len(entry5.get()) == 0) and counter5_.can_count() == False:
        save5(text_to_get5.get())
        counter5_.set_can(True)
        if counter5_.get_() == 0:
            r = get5()
            saat.pack()
            rooz.forget()
        if counter5_.get_() == 1:
            s = get5()
            time = p_nobat(r,s)
            saat.forget()
            rooz.forget()
        entry5.delete(0, 'end')
        print(get5())


def b5():
    if not (len(entry5.get()) == 0) and counter5_.can_count() == True:
        counter5_.set_can(False)
        if counter5_.get_() < 1:
            counter5_.up_count()
        else:
            tavaghofe_gereftane_vorodi_rooz_va_saat()

def save5(t):
    global s5
    s5 = t
    
def get5():
   return s5

def get5_time():
    return time


#code haye gereftane vorodi jostojo safhe pezeshk
text_to_get6 = tt.StringVar()
canvas6 = tt.Canvas(root,width = 400 ,height = 300)
entry6 = tt.Entry(root,textvariable = text_to_get6)
entry6.focus_set()
canvas6.create_window(200,140,window = entry6)
counter6_ = counter(0)




def a6():
    if not (len(entry6.get()) == 0) and counter6_.can_count() == False:
        save6(text_to_get6.get())
        counter6_.set_can(True)
        if counter6_.get_() == 0:
           pezeshk_.nam = get6()
        if counter6_.get_() == 1:
           pezeshk_.name_khanevadegi = get6()
        entry6.delete(0, 'end')
        print(get6())


def b6():
    if not (len(entry6.get()) == 0) and counter6_.can_count() == True:
        counter6_.set_can(False)
        if counter6_.get_() < 1:
            counter6_.up_count()
        else:
            tavaghofe_gereftane_jostjo_baraye_safhe_pezeshk()


def save6(t):
    global s6
    s6 = t


def get6():
    return s6


#gereftane vorodi gereftane nobat
text_to_get7 = tt.StringVar()
canvas7 = tt.Canvas(root,width = 400 ,height = 300)
entry7 = tt.Entry(root,textvariable = text_to_get7)
entry7.focus_set()
canvas7.create_window(200,140,window = entry7)
counter7_ = counter(0)




def a7():
    if not (len(entry7.get()) == 0) and counter7_.can_count() == False:
        save7(text_to_get7.get())
        counter7_.set_can(True)
        if counter7_.get_() == 0:
           bimar_.shomare_nobat = get7()
        entry7.delete(0, 'end')
        print(get7())


def b7():
    if not (len(entry7.get()) == 0) and counter7_.can_count() == True:
        counter7_.set_can(False)
        if counter7_.get_() < 0:
            counter7_.up_count()
        else:
            tavaghofe_gereftane_gereftane_nobat()


def save7(t):
    global s7
    s7 = t


def get7():
    return s7


#gereftane vorodi ersal payam
text_to_get8 = tt.StringVar()
canvas8 = tt.Canvas(root,width = 400 ,height = 300)
entry8 = tt.Entry(root,textvariable = text_to_get8)
entry8.focus_set()
canvas8.create_window(200,140,window = entry8)
counter8_ = counter(0)




def a8():
    if not (len(entry8.get()) == 0) and counter8_.can_count() == False:
        save8(text_to_get8.get())
        counter8_.set_can(True)
        if counter8_.get_() == 0:
           bimar_.payam = get8()
        entry8.delete(0, 'end')
        print(get8())


def b8():
    if not (len(entry8.get()) == 0) and counter8_.can_count() == True:
        counter8_.set_can(False)
        if counter8_.get_() < 0:
            counter8_.up_count()
        else:
            tavaghofe_gereftane_ersal_payam()


def save8(t):
    global s8
    s8 = t


def get8():
    return s8



#gereftane laghve nobat
text_to_get9 = tt.StringVar()
canvas9 = tt.Canvas(root,width = 400 ,height = 300)
entry9 = tt.Entry(root,textvariable = text_to_get9)
entry9.focus_set()
canvas9.create_window(200,140,window = entry9)
counter9_ = counter(0)




def a9():
    if not (len(entry9.get()) == 0) and counter9_.can_count() == False:
        save9(text_to_get9.get())
        counter9_.set_can(True)
        if counter9_.get_() == 0:
           bimar_.p_n = get9()
        if counter9_.get_() == 1:
           bimar_.p_nk = get9()
        entry9.delete(0, 'end')
        print(get9())


def b9():
    if not (len(entry9.get()) == 0) and counter9_.can_count() == True:
        counter9_.set_can(False)
        if counter9_.get_() < 0:
            counter9_.up_count()
        else:
            tavaghofe_gereftane_laghve_nobat()


def save9(t):
    global s9
    s9 = t


def get9():
    return s9



#gereftane laghv ersal payam
text_to_get10 = tt.StringVar()
canvas10 = tt.Canvas(root,width = 400 ,height = 300)
entry10 = tt.Entry(root,textvariable = text_to_get10)
entry10.focus_set()
canvas10.create_window(200,140,window = entry10)
counter10_ = counter(0)




def a10():
    if not (len(entry10.get()) == 0) and counter10_.can_count() == False:
        save10(text_to_get10.get())
        counter10_.set_can(True)
        if counter10_.get_() == 0:
           bimar_.h_payam = get10()
        entry10.delete(0, 'end')
        print(get10())


def b10():
    if not (len(entry10.get()) == 0) and counter10_.can_count() == True:
        counter10_.set_can(False)
        if counter10_.get_() < 0:
            counter10_.up_count()
        else:
            tavaghofe_gereftane_hazf_payam()


def save10(t):
    global s10
    s10 = t


def get10():
    return s10



next_pezeshk = tt.Button(text="save",command = a)
save_pezeshk = tt.Button(text="next",command = b)
next_bimar = tt.Button(text="save",command = a2)
save_bimar = tt.Button(text="next",command = b2)

next_pezeshk_mojod = tt.Button(text="save",command = a3)
save_pezeshk_mojod = tt.Button(text="next",command = b3)
next_bimar_mojod = tt.Button(text="save",command = a4)
save_bimar_mojod = tt.Button(text="next",command = b4)

next_rooz_va_saat = tt.Button(text="save",command = a5)
save_rooz_va_saat = tt.Button(text="next",command = b5)


next_search_pezeshk = tt.Button(text="save",command = a6)
save_search_pezeshk = tt.Button(text="next",command = b6)

next_gereftane_nobat = tt.Button(text="save",command = a7)
save_gereftane_nobat = tt.Button(text="next",command = b7)

next_ersal_payam = tt.Button(text="save",command = a8)
save_ersal_payam = tt.Button(text="next",command = b8)

next_laghv_nobat = tt.Button(text="save",command = a9)
save_laghv_nobat = tt.Button(text="next",command = b9)


next_hazf_payam = tt.Button(text="save",command = a10)
save_hazf_payam = tt.Button(text="next",command = b10)


def vared_shodan_pezeshk():
     main_label.forget()
     vorod_bimar.forget()
     vorod_pezeshk.forget()
     vorod_pezeshk_mojod.pack() 
     sabt_nam_pezeshk.pack()
     
def vared_shodan_bimar():
     main_label.forget()
     vorod_bimar.forget()
     vorod_pezeshk.forget()
     vorod_bimar_mojod.pack() 
     sabt_nam_bimar.pack()
      
def sabt_nam_pezeshk():
     gereftane_vorodi_pezeshk()
     vorod_pezeshk_mojod.forget() 
     sabt_nam_pezeshk.forget()

def sabt_nam_bimar():
     gereftane_vorodi_bimar()
     vorod_bimar_mojod.forget() 
     sabt_nam_bimar.forget()
    
def vared_shodan_pezeshk_mojod():
     gereftane_vorodi_pezeshk_mojod()
     vorod_pezeshk_mojod.forget() 
     sabt_nam_pezeshk.forget()


     #gereftane nam va nam khane vadegi bararye vorod va vorod be kar ha ee ke pezeshk mitavanad anjam dahad

def vared_shodan_bimar_mojod():
     gereftane_vorodi_bimar_mojod()
     vorod_bimar_mojod.forget() 
     sabt_nam_bimar.forget()
     #gereftane nam va nam khane vadegi bararye vorod va vorod be kar ha ee ke pezeshk mitavanad anjam dahad
     
def vared_kardane_saat_va_rooze_kari():
   vared_kardane_saat_va_rooze_kari.forget()
   namayesh_saat_kari_pezeshk.forget()
   namayesh_list_payamha.forget()
   rooz.pack()
   gereftane_vorodi_rooz_va_saat()
       
       
vorod_pezeshk = tt.Button(text = "vorod be onvane pezeshk",command = vared_shodan_pezeshk)
vorod_bimar = tt.Button(text = "vorod be onvane bimar",command = vared_shodan_bimar)  

sabt_nam_pezeshk = tt.Button(text = "sabt nam pezeshk",command = sabt_nam_pezeshk)
sabt_nam_bimar = tt.Button(text = "sabt nam bimar",command = sabt_nam_bimar)  

vorod_pezeshk_mojod = tt.Button(text = "vorode pezeshk",command = vared_shodan_pezeshk_mojod)
vorod_bimar_mojod = tt.Button(text = "vorode bimar",command = vared_shodan_bimar_mojod)  


    
#bimar menu

def j_v_j_p():
    gereftane_jostjo_baraye_safhe_pezeshk()

def l_n():
    pak_bimar_menu()
    list_menu()

jost_va_jo_baraye_pezeshk = tt.Button(text = "jost_va_jo_baraye_pezeshk" , command = j_v_j_p) #nobat giri dar safhe pezeshk yaft shode
list_nobat_haye_gerefte_shode = tt.Button(text = "list_nobat_haye_gerefte_shode",command = l_n)#laghve nobat morede nazar

#jost va jo baraye pezeshk dar sorate mojod bodane pezeshk:
#mb -> show name of pezeshk


######################


def namayesh_nobat_haye_pezeshk_peyda_shode():
    if MAIN_CONTROLLER.josto_joye_pezeshk(pezeshk_):
       mb.showinfo("saat haye kari:",MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_).namayesh_saat_kari_pezeshk())

def gereftane_nobat_az_pezeshk_safhe():
    gereftane_gereftane_nobat()

def ersal_payam_be_pezeshk_safhe():
    gereftane_ersal_payam()

def baz2():
    pak_jostjo_menu()
    bimar_menu()

namayesh_saat_kari_pezeshk_peyda_shode = tt.Button(text = "namayesh_nobat_ha" , command = namayesh_nobat_haye_pezeshk_peyda_shode)
gereftane_nobat_az_pezeshk = tt.Button(text = "gereftane_nobat" , command = gereftane_nobat_az_pezeshk_safhe)
ersal_payam_be_pezeshk = tt.Button(text = "ersal payam" , command = ersal_payam_be_pezeshk_safhe)
dokme_bazgasht_be_menu_list2 = tt.Button(text = "-> menu_bimar" , command = baz2)
#jostojo baraye pezeshk -> gereftane nobat
#namayesh saat kari
#ersal payam


def namayesh_nobat_haye_bimar_list():
    if MAIN_CONTROLLER.josto_joye_bimar(bimar_):
       temp_bimar =  MAIN_CONTROLLER.peyda_kardane_bimar(bimar_)
       MAIN_CONTROLLER.namayesh_nobat_haye_bimar(temp_bimar,temp_bimar.tedad_nobat_haye_gerefte_shode)

def laghve_nobat_bimar():
     gereftane_laghve_nobat()

def baz1():
    pak_list_menu()
    bimar_menu()

namayesh_nobat_haye_bimar = tt.Button(text = "namayesh nobat haye bimar" , command = namayesh_nobat_haye_bimar_list)
laghve_nobat_b = tt.Button(text = "laghve_nobat_be_shomare" , command = laghve_nobat_bimar)
dokme_bazgasht_be_menu_list = tt.Button(text = "-> menu_bimar" , command = baz1)
#namayesh nobat haye bimar
#emkan laghv nobat








##########

def namayesh_saat_kari():
    if MAIN_CONTROLLER.josto_joye_pezeshk(pezeshk_):
       mb.showinfo("saat haye kari:",MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_).namayesh_saat_kari_pezeshk())


def namayesh_payam_ha_va_emkan_hazf_va_bazgasht():
    strtr = "payam ha:"+"\n"
    #pak kardan dar tavaghof
    for pm in MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_).payam_ha:
        strtr = strtr + pm
    gereftane_hazf_payam()
    mb.showinfo("payam_haye_bimaran:", strtr)
    dokme_bazgasht_be_menu_payam_ha.pack()


def bazzz():
 pak_payam_ha_menu()
 pezeshk_menu()

vared_kardane_saat_va_rooze_kari = tt.Button(text = "vared_kardan_saat_va_rooze_kari", command = vared_kardane_saat_va_rooze_kari) 
namayesh_saat_kari_pezeshk = tt.Button(text = "namayesh saat haye kari", command = namayesh_saat_kari)
namayesh_list_payamha = tt.Button(text = "list payam ha va entegha dat",command = namayesh_payam_ha_va_emkan_hazf_va_bazgasht)#hazf niz dar haminja etefagh mi oftad
dokme_bazgasht_be_menu_payam_ha = tt.Button(text="menu pezeshk",command = bazzz)
#saat kari sabt shode!




def bazgasht_pezeshk_menu_asli():
    vared_kardane_saat_va_rooze_kari.forget()
    namayesh_saat_kari_pezeshk.forget()
    namayesh_list_payamha.forget()
    menu_pezeshk_asli()

def bazgasht_bimar_menu_asli():
    jost_va_jo_baraye_pezeshk.forget()  # ,command = j_v_j_p) nobat giri dar safhe pezeshk yaft shode
    list_nobat_haye_gerefte_shode.forget()  # ,command = l_n)#laghve nobat morede nazar
    menu_bimar_asli()

def bazgaht_be_menu_pezeshk1():
    pezeshk_menu()


def bazgaht_be_menu_pezeshk2():
    pezeshk_menu()
    #text_for_namayesh_list_payam_ha

dokme_bazgasht_menu_asli1 = tt.Button(text = "->menu_asli",command  = bazgasht_pezeshk_menu_asli)
dokme_bazgasht_menu_asli2 = tt.Button(text = "->menu_asli" , command = bazgasht_bimar_menu_asli)
dokme_az_saat_kari_bazgasht_menu_pezeshk = tt.Button(text = "->menu_asli" , command = bazgaht_be_menu_pezeshk1)
dokme_az_list_payamha_bazgasht_menu_pezeshk = tt.Button(text = "->menu_asli" , command = bazgaht_be_menu_pezeshk2)


def menu_pezeshk_asli():
    dokme_bazgasht_menu_asli1.forget()
    main_menu()

def menu_bimar_asli():
    dokme_bazgasht_menu_asli2.forget()
    main_menu()


def gereftane_vorodi_pezeshk():
    next_pezeshk.pack()
    save_pezeshk.pack()
    canvas.pack()
    entry.pack()

def tavaghofe_gereftane_vorodi_pezeshk():
    next_pezeshk.forget()
    save_pezeshk.forget()
    canvas.forget()
    entry.forget()
    counter_.set_(0)
    entry.delete(0,'end')
    print(pezeshk_.nam)
    print(pezeshk_.name_khanevadegi)
    MAIN_CONTROLLER.afzodane_pezeshk(pezeshk_)
    print(MAIN_CONTROLLER.pezeshk_ha[0].nam)
    print(MAIN_CONTROLLER.pezeshk_ha[0].name_khanevadegi)
    main_menu()
    
def gereftane_vorodi_bimar():
    next_bimar.pack()
    save_bimar.pack()
    canvas2.pack()
    entry2.pack()
    

def tavaghofe_gereftane_vorodi_bimar():
    next_bimar.forget()
    save_bimar.forget()
    canvas2.forget()
    entry2.forget()
    counter2_.set_(0)
    entry2.delete(0,'end')
    MAIN_CONTROLLER.afzodane_bimar(bimar_)
    main_menu()
   



def gereftane_vorodi_pezeshk_mojod():
    next_pezeshk_mojod.pack()
    save_pezeshk_mojod.pack()
    canvas3.pack()
    entry3.pack()

def tavaghofe_gereftane_vorodi_pezeshk_mojod():
    next_pezeshk_mojod.forget()
    save_pezeshk_mojod.forget()
    canvas3.forget()
    entry3.forget()
    counter3_.set_(0)
    entry3.delete(0,'end')
    #if mojod bod
    #pezeshk_menu()
    #else
    #pezeshk mojod menu
    print(pezeshk_.nam)
    print(pezeshk_.name_khanevadegi)
    if MAIN_CONTROLLER.josto_joye_pezeshk(pezeshk_) == False:
        main_menu()
        msg = mb.showinfo("System_msg","pezeshk morede nazar mojod nist")
    else:
        pezeshk_menu()
    
def gereftane_vorodi_bimar_mojod():
    next_bimar_mojod.pack()
    save_bimar_mojod.pack()
    canvas4.pack()
    entry4.pack()
    

def tavaghofe_gereftane_vorodi_bimar_mojod():
    next_bimar_mojod.forget()
    save_bimar_mojod.forget()
    canvas4.forget()
    entry4.forget()
    counter4_.set_(0)
    entry4.delete(0,'end')
    #if mojod bod
    #bimar_menu()
    #else 
    #bimar mojod menu
    print(bimar_.nam)
    print(bimar_.name_khanevadegi)
    if MAIN_CONTROLLER.josto_joye_bimar(bimar_) == False:
        main_menu()
        msg = mb.showinfo("System_msg", "bimar morede nazar mojod nist")
    else:
        bimar_menu()

def gereftane_vorodi_rooz_va_saat():
    dokme_bazgasht_menu_asli1.forget()
    next_rooz_va_saat.pack()
    save_rooz_va_saat.pack()
    canvas5.pack()
    entry5.pack()
    

def tavaghofe_gereftane_vorodi_rooz_va_saat():
    rooz.forget()
    saat.forget()
    next_rooz_va_saat.forget()
    save_rooz_va_saat.forget()
    canvas5.forget()
    entry5.forget()
    counter5_.set_(0)
    entry5.delete(0,'end')
    MAIN_CONTROLLER.afzodane_saat_kari_pezeshk(pezeshk_, time)
    print(MAIN_CONTROLLER.pezeshk_ha[0].nobatha[0].rooz + "!!!")
    print(MAIN_CONTROLLER.pezeshk_ha[0].nobatha[0].saat.saat + "!!!")
    pezeshk_menu()
    

def pezeshk_menu():
    
   vared_kardane_saat_va_rooze_kari.pack()
   namayesh_saat_kari_pezeshk.pack()
   namayesh_list_payamha.pack()
   dokme_bazgasht_menu_asli1.pack()


def pak_pezeshk_menu():
    vared_kardane_saat_va_rooze_kari.forget()
    namayesh_saat_kari_pezeshk.forget()
    namayesh_list_payamha.forget()
    dokme_bazgasht_menu_asli1.forget()


def bimar_menu():
    jost_va_jo_baraye_pezeshk.pack()#,command = j_v_j_p) nobat giri dar safhe pezeshk yaft shode    
    list_nobat_haye_gerefte_shode.pack()#,command = l_n)#laghve nobat morede nazar
    dokme_bazgasht_menu_asli2.pack()
    dokme_bazgasht_be_menu_list2.forget()
    dokme_bazgasht_be_menu_list.forget()


def pak_bimar_menu():
    jost_va_jo_baraye_pezeshk.forget()  # ,command = j_v_j_p) nobat giri dar safhe pezeshk yaft shode
    list_nobat_haye_gerefte_shode.forget()  # ,command = l_n)#laghve nobat morede nazar
    dokme_bazgasht_menu_asli2.forget()



def gereftane_jostjo_baraye_safhe_pezeshk():
     entry6.pack()
     canvas6.pack()
     save_search_pezeshk.pack()
     next_search_pezeshk.pack()
     pak_bimar_menu()

def tavaghofe_gereftane_jostjo_baraye_safhe_pezeshk():
    save_search_pezeshk.forget()
    next_search_pezeshk.forget()
    canvas6.forget()
    entry6.forget()
    counter6_.set_(0)
    entry6.delete(0, 'end')
    print(pezeshk_.nam)
    print(pezeshk_.name_khanevadegi)
    if MAIN_CONTROLLER.josto_joye_pezeshk(pezeshk_) == False:
        bimar_menu()
        msg = mb.showinfo("System_msg", "pezeshk morede nazar mojod nist")
    else:
        pak_bimar_menu()
        jostjo_menu()


def gereftane_gereftane_nobat():
    entry7.pack()
    canvas7.pack()
    save_gereftane_nobat.pack()
    next_gereftane_nobat.pack()
    dokme_bazgasht_be_menu_list2.forget()
    pak_jostjo_menu()


def tavaghofe_gereftane_gereftane_nobat():
        entry7.forget()
        canvas7.forget()
        save_gereftane_nobat.forget()
        next_gereftane_nobat.forget()
        counter7_.set_(0)
        entry7.delete(0, 'end')
        p = MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_)
        if len(p.nobatha) > 0 :
         if int(bimar_.shomare_nobat) >= 1 and int(bimar_.shomare_nobat) <= len(p.nobatha):
            rrr = p.nobatha[int(bimar_.shomare_nobat)-1].rooz
            sss = p.nobatha[int(bimar_.shomare_nobat)-1].saat.saat
            bn = b_nobat(rrr,sss,bimar_.nam,bimar_.name_khanevadegi)
            MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_).gereftane_b_nobat(bn)
            msg = mb.showinfo("System_msg", "nobat gerefte shod")
         else:
            msg = mb.showinfo("System_msg", "in nobat vojod nadarad")
        else:
            msg = mb.showinfo("System_msg", "pezeshk nobat ra ekhtiar nemikonad")
        
        jostjo_menu()


def gereftane_ersal_payam():
    entry8.pack()
    canvas8.pack()
    save_ersal_payam.pack()
    next_ersal_payam.pack()
    pak_jostjo_menu()


def tavaghofe_gereftane_ersal_payam():
    entry8.forget()
    canvas8.forget()
    save_ersal_payam.forget()
    next_ersal_payam.forget()
    dokme_bazgasht_be_menu_list2.forget()
    counter8_.set_(0)
    entry8.delete(0, 'end')
    MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_).afzodane_payam(bimar_.payam)
    msg = mb.showinfo("System_msg", "payam ersal shod")
    jostjo_menu()


def gereftane_laghve_nobat():
    entry9.pack()
    canvas9.pack()
    save_laghv_nobat.pack()
    next_laghv_nobat.pack()
    pak_list_menu()
    dokme_bazgasht_be_menu_list2.forget()
    dokme_bazgasht_be_menu_list.forget()



def tavaghofe_gereftane_laghve_nobat():
        entry9.forget()
        canvas9.forget()
        save_laghv_nobat.forget()
        next_laghv_nobat.forget()
        counter9_.set_(0)
        entry9.delete(0, 'end')
        rooooz = None
        saaaat = None
        sas = False
        for pez in MAIN_CONTROLLER.pezeshk_ha:
          if pez.nam == bimar_.p_n and pez.name_khanevadegi == bimar_.p_nk:
             for n in pez.nobat_haye_gerefte_shode:
                if n.nam == bimar_.nam and n.name_khanevadegi == bimar_.name_khanevadegi:
                  rooooz = n.rooz
                  saaaat = n.saat
                  pez.nobat_haye_gerefte_shode.remove(n)
                for m in pez.nobatha :
                 if m.rooz == rooooz and m.saat.saat == saaaat:
                  pez.nobatha.remove(m)
                  sas = True

        if sas == True:
            msg = mb.showinfo("System_msg", "nobat laghv shod")
        else:
            msg = mb.showinfo("System_msg", "nobat vojod nadarad")

        list_menu()




def gereftane_hazf_payam():
    entry10.pack()
    canvas10.pack()
    save_hazf_payam.pack()
    next_hazf_payam.pack()
    pak_pezeshk_menu()
    #dokme bazgsht

def tavaghofe_gereftane_hazf_payam():
    entry10.forget()
    canvas10.forget()
    save_hazf_payam.forget()
    next_hazf_payam.forget()
    if int(bimar_.h_payam) >=1 and int(bimar_.h_payam) <= len(MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_).payam_ha):
      MAIN_CONTROLLER.peyda_kardane_pezeshk(pezeshk_).hazfe_payam(int(bimar_.h_payam)-1)
      mb.showinfo("sys.msg:", "payam hazaf shod")
    else:
      mb.showinfo("sys.msg:","in payam vojod nadarad")

    counter10_.set_(0)
    entry10.delete(0, 'end')
    pezeshk_menu()



def pak_payam_ha_menu():
    entry10.forget()
    canvas10.forget()
    save_hazf_payam.forget()
    next_hazf_payam.forget()
    dokme_bazgasht_be_menu_payam_ha.forget()



def jostjo_menu():
    namayesh_saat_kari_pezeshk_peyda_shode.pack()
    gereftane_nobat_az_pezeshk.pack()
    ersal_payam_be_pezeshk.pack()
    dokme_bazgasht_be_menu_list2.pack()

def pak_jostjo_menu():
    namayesh_saat_kari_pezeshk_peyda_shode.forget()
    gereftane_nobat_az_pezeshk.forget()
    ersal_payam_be_pezeshk.forget()




def list_menu():
    namayesh_nobat_haye_bimar.pack()
    laghve_nobat_b.pack()
    dokme_bazgasht_be_menu_list.pack()


def pak_list_menu():
    namayesh_nobat_haye_bimar.forget()
    laghve_nobat_b.forget()




def main_menu():
    vorod_pezeshk.pack()
    vorod_bimar.pack()
    main_label.pack()



    
    
main_menu()

root.mainloop()









