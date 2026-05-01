import tkinter as tk  # İnterfeys üçün kitabxana
import functions as f  # Hesablama funksiyalarımızı gətiririk

pencere = tk.Tk()  # Proqramın əsas pəncərəsini yaradırıq
pencere.title("Zaur & Mehemmed Kalkulyatoru")  # Pəncərənin başlığını qoyuruq
pencere.geometry("300x400")  # Ölçülərini təyin edirik
pencere.resizable(False, False)  # Ölçüsünün dəyişdirilməsini qadağan edirik

ekran_yazisi = tk.StringVar()  # Ekrandakı yazını idarə edən dəyişən
ifade_metni = ""  # Yazılan rəqəmləri sətir kimi saxlayırıq
ifade_listi = []  # Hesablamaq üçün rəqəm və işarələri siyahı edirik

def duymeye_basanda(acar):  # Rəqəm və işarə düymələri üçün funksiya
    global ifade_metni  # Global dəyişəni istifadə edirik
    if acar.isdigit():  # Əgər basılan simvol rəqəmdirsə
        ifade_metni = ifade_metni + acar  # Yazıya rəqəmi artırırıq
        ekran_yazisi.set(ifade_metni)  # Ekranda göstəririk
        if ifade_listi and str(ifade_listi[-1]).replace(".", "", 1).isdigit():  # Əvvəlki də rəqəmdirsə
            ifade_listi[-1] = ifade_listi[-1] + acar  # Onları birləşdiririk (məsələn 1 və 2 olur 12)
        else:  # Yeni bir ədəddirsə
            ifade_listi.append(acar)  # Siyahıya təzə element kimi əlavə edirik
    elif acar == ".":  # Nöqtə düyməsi basılıbsa
        if not ifade_listi or not str(ifade_listi[-1]).replace(".", "", 1).isdigit():  # Boşdursa
            ifade_metni = ifade_metni + "0."  # "0." yazırıq
            ifade_listi.append("0.")  # Siyahıya əlavə edirik
        elif "." not in ifade_listi[-1]:  # Əgər ədəddə hələ nöqtə yoxdursa
            ifade_metni = ifade_metni + "."  # Nöqtəni artırırıq
            ifade_listi[-1] = ifade_listi[-1] + "."  # Siyahıda da qeyd edirik
        ekran_yazisi.set(ifade_metni)  # Ekranı yeniləyirik
    elif acar in ["+", "*", "/"]:  # Əməliyyat düymələri
        if len(ifade_listi) > 0:  # Əgər ekranda nəsə varsa
            if ifade_listi[-1] in ["+", "-", "*", "/"]:  # Axırıncı simvol artıq işarədirsə
                ifade_listi[-1] = acar  # Köhnə işarəni silib təzəsini qoyuruq
                ifade_metni = ifade_metni[:-1] + acar  # Mətndə də dəyişirik
            else:  # Normal halda
                ifade_listi.append(acar)  # İşarəni siyahıya atırıq
                ifade_metni = ifade_metni + acar  # Mətnə artırırıq
        ekran_yazisi.set(ifade_metni)  # Ekranda göstəririk
    elif acar == "-":  # Çıxma və ya mənfi işarəsi
        if not ifade_listi:  # Siyahı boşdursa
            ifade_metni = ifade_metni + "-"  # Mənfi kimi başlayırıq
            ifade_listi.append("-")  # Siyahıya mənfi atırıq
        elif ifade_listi[-1] in ["+", "-", "*", "/"]:  # İşarədən sonra gəlirsə
            ifade_metni = ifade_metni + "-"  # Yenə mənfi rəqəm üçün
            ifade_listi.append("-")  # Siyahıya əlavə
        else:  # Normal çıxma əməliyyatı
            ifade_listi.append("-")  # Siyahıya çıxma işarəsi
            ifade_metni = ifade_metni + "-"  # Mətnə çıxma
        ekran_yazisi.set(ifade_metni)  # Ekranı yeniləyirik

def hamisini_sil():  # C düyməsinin funksiyası
    global ifade_metni  # Mətni sıfırlamaq üçün
    ifade_metni = ""  # Boş sətir edirik
    ifade_listi.clear()  # Siyahını təmizləyirik
    ekran_yazisi.set("")  # Ekranı boşaldırıq

def sonuncunu_sil():  # CE düyməsinin funksiyası
    global ifade_metni  # Mətni dəyişmək üçün
    if len(ifade_listi) > 0:  # Siyahı boş deyilsə
        silinen = ifade_listi.pop()  # Sonuncu elementi siyahıdan çıxarırıq
        uzunluq = len(str(silinen))  # Həmin elementin neçə hərfdən ibarət olduğunu tapırıq
        ifade_metni = ifade_metni[:-uzunluq]  # Mətndən o qədər simvol silirik
        ekran_yazisi.set(ifade_metni)  # Ekranı yeniləyirik

def bir_simvol_sil():  # Backspace funksiyası
    global ifade_metni  # Global mətni götürürük
    if ifade_metni == "":  # Əgər onsuz da boşdursa
        return  # Heç nə etmirik
    ifade_metni = ifade_metni[:-1]  # Axırıncı bir hərfi silirik
    ekran_yazisi.set(ifade_metni)  # Ekranda göstəririk
    if not ifade_listi:  # Siyahı boşdursa çıxırıq
        return
    axirinci = ifade_listi[-1]  # Sonuncu elementə baxırıq
    if axirinci in ["+", "-", "*", "/"]:  # İşarədirsə
        ifade_listi.pop()  # Tamamilə silirik
    else:  # Rəqəmdirsə
        if len(axirinci) > 1:  # Birdən çox rəqəmdən ibarətdirsə
            ifade_listi[-1] = axirinci[:-1]  # Birini silirik
        else:  # Tək rəqəmdirsə
            ifade_listi.pop()  # Siyahıdan çıxarırıq

def faiz_hesabla():  # % düyməsinin funksiyası
    global ifade_metni  # Mətni yeniləmək üçün
    if ifade_listi:  # Siyahı boş deyilsə
        if ifade_listi[-1] not in ["+", "-", "*", "/"]:  # Axırıncı rəqəmdirsə
            reqem = float(ifade_listi[-1]) / 100  # 100-ə bölüb faiz edirik
            ifade_listi[-1] = str(reqem)  # Siyahıda yeniləyirik
            ifade_metni = str(reqem)  # Ekranda göstərmək üçün metni dəyişirik
            ekran_yazisi.set(ifade_metni)  # Ekranı yeniləyirik

def hesabla_duymesi():  # = düyməsi üçün funksiya
    global ifade_metni  # Nəticəni ekrana yazmaq üçün
    try:
        if not ifade_listi:  # Boşdursa hesablamırıq
            return
        if ifade_listi[-1] in ["+", "-", "*", "/"]:  # Axırı işarə ilə bitibsə olmaz
            return
        sonuc_listi = f.calculate(ifade_listi.copy())  # Hesablama funksiyasını çağırırıq
        cavab = sonuc_listi[0]  # Gələn cavabı götürürük
        if cavab == int(cavab):  # Əgər tam ədəddirsə (.0 yoxdursa)
            cavab = int(cavab)  # Tam ədədə çeviririk
        ifade_metni = str(cavab)  # Nəticəni mətnə çeviririk
        ifade_listi.clear()  # Siyahını təmizləyirik
        ifade_listi.append(str(cavab))  # Cavabı siyahıya təzə başlanğıc kimi qoyuruq
        ekran_yazisi.set(ifade_metni)  # Ekranda cavabı göstəririk
    except ZeroDivisionError:  # Sıfıra böləndə
        ekran_yazisi.set("Sıfıra bölmək olmaz!")  # Xəbərdarlıq yazırıq
        hamisini_sil()  # Ekranı təmizləyirik
    except:  # Başqa bir xəta olsa
        ekran_yazisi.set("Xəta baş verdi")  # Xəta mesajı
        hamisini_sil()  # Təmizləyirik

ekran = tk.Entry(pencere, textvariable=ekran_yazisi, justify="right", font=("Arial", 20))  # Yazı sahəsi
ekran.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)  # Ekrana yerləşdiririk

duymeler = [  # Düymələrin siyahısı
    ("%", 1, 0), ("CE", 1, 1), ("C", 1, 2), ("⌫", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
]

for (yazi, setir, sutun) in duymeler:  # Hər bir düymə üçün dövr
    if yazi == "=":  # Əgər bərabərdirsə
        komanda = hesabla_duymesi  # Hesabla funksiyasını bağlayırıq
    elif yazi == "C":  # Əgər C düyməsidirsə
        komanda = hamisini_sil  # Həmişini sil funksiyası
    elif yazi == "CE":  # Əgər CE-dirsə
        komanda = sonuncunu_sil  # Sonuncunu sil funksiyası
    elif yazi == "⌫":  # Əgər silmə işarəsidirsə
        komanda = bir_simvol_sil  # Bir simvol sil funksiyası
    elif yazi == "%":  # Əgər faizdirsə
        komanda = faiz_hesabla  # Faiz funksiyası
    else:  # Rəqəm və ya digər işarələrdirsə
        komanda = lambda t=yazi: duymeye_basanda(t)  # Düyməyə basma funksiyası

    # Düyməni yaradırıq
    tk.Button(pencere, text=yazi, command=komanda, font=("Arial", 14)).grid(row=setir, column=sutun, sticky="nsew", padx=2, pady=2)

for i in range(4):  # Sütunları nizamlamaq üçün dövr
    pencere.grid_columnconfigure(i, weight=1)  # Hər sütuna eyni weight veririk

for i in range(6):  # Sətirləri nizamlamaq üçün dövr
    pencere.grid_rowconfigure(i, weight=1)  # Hər sətirə eyni weight veririk

pencere.mainloop()  # Proqramı işlək vəziyyətdə saxlayırıq
