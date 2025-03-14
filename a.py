from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Otopark")
global kapasite,araclar,aracindex
kapasite = 5
araclar = {}
aracindex = 0
def ode():
    win2 = Tk()
    win2.title("Ödeme Ekranı")
    lbl = Label(win2,text="Araç Seçin")
    lbl.pack()
    buttons = {}
    def aracodeme(i):
        global kapasite,araclar,aracindex
        saatbasi = 0
        saat = int(saat_entry.get())
        toplam = 0
        indirimli = 0
        if "Otomobil" in buttons[i].cget("text"):
            saatbasi = 50
        elif "Ticari" in buttons[i].cget("text"):
            saatbasi = 60
        elif "Motorsiklet" in buttons[i].cget("text"):
            saatbasi = 30
        toplam = saat*saatbasi
        if saat < 3:
            indirimli = toplam
        elif saat < 5:
            indirimli = toplam - toplam*0.2
        else:
            indirimli = toplam - toplam*0.3
        kapasite += 1
        aracindex -= 1
        araclar.pop(i)
        messagebox.showinfo(title="Ödeme Tamamlandı", message=f"Tutar: {indirimli}")
        messagebox.showinfo(title= "Ödeme Tamamlandı", message=f"Toplam Kapasite {kapasite}")
        kapasite_lbl.config(text=f"Toplam Kapasite: {kapasite}")
        win2.destroy()

    for i in range(0,aracindex):
        buttons[i] = Button(win2,text=f"{araclar[i]} {i+1}",width=30,command=lambda: aracodeme(i))
        buttons[i].pack()
    saat_lbl =  Label(win2,text="Kaç Saat Kalacak:")
    saat_entry = Entry(win2,width=30)
    saat_lbl.pack()
    saat_entry.pack()
    win2.mainloop() 

def oto():
    global aracindex,araclar,kapasite
    if kapasite != 0:
        araclar[aracindex] = "Otomobil"
        aracindex+=1
        kapasite -=1
        messagebox.showinfo(title="Araç Eklendi!",message=f"Araç Başarıyla Eklendi! Kapasite: {kapasite}")
        kapasite_lbl.config(text=f"Toplam Kapasite: {kapasite}")
    else:
        messagebox.showinfo(title="Kapasite Dolu!",message="Araç Kapasitesi Dolu")

def ticari():
    global aracindex,araclar,kapasite
    if kapasite != 0:
        araclar[aracindex] = "Ticari"
        aracindex+=1
        kapasite -=1
        messagebox.showinfo(title="Araç Eklendi!",message=f"Araç Başarıyla Eklendi! Kapasite: {kapasite}")
        kapasite_lbl.config(text=f"Toplam Kapasite: {kapasite}")
    else:
        messagebox.showinfo(title="Kapasite Dolu!",message="Araç Kapasitesi Dolu")

def moto():
    global aracindex,araclar,kapasite
    if kapasite != 0:
        araclar[aracindex] = "Motorsiklet"
        aracindex+=1
        kapasite -=1
        messagebox.showinfo(title="Araç Eklendi!",message=f"Araç Başarıyla Eklendi! Kapasite: {kapasite}")
        kapasite_lbl.config(text=f"Toplam Kapasite: {kapasite}")
    else:
        messagebox.showinfo(title="Kapasite Dolu!",message="Araç Kapasitesi Dolu")


title = Label(win,text="Hoşgeldiniz!")
lbl = Label(win,text="Araç Tipi Seçin:")
oto_lbl = Button(win,text="Otomobil",width=30,command=oto)
ticari_lbl = Button(win,text="Ticari",width=30,command=ticari)
motorsiklet_lbl = Button(win,text="Motorsiklet",width=30,command=moto)
kapasite_lbl = Label(win,text="Toplam Kapasite: 5")
odeme_lbl = Button(win,text="Ödeme Yap",command=ode)

title.pack()
lbl.pack()
oto_lbl.pack()
ticari_lbl.pack()
motorsiklet_lbl.pack()
kapasite_lbl.pack()
odeme_lbl.pack()
win.mainloop()