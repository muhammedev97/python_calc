# Bu funksiyalar riyazi hesablamaları yerinə yetirmək üçündür.
def topla(a, b):  # Toplama funksiyası
    netice = a + b  # İki ədədi toplayıb dəyişənə yazırıq
    return netice  # Cavabı geri qaytarırıq

def cix(a, b):  # Çıxma funksiyası
    netice = a - b  # Birinci ədəddən ikincini çıxırıq
    return netice  # Nəticəni qaytarırıq

def vur(a, b):  # Vurma funksiyası
    netice = a * b  # Ədədləri bir-birinə vururuq
    return netice  # Cavabı geri veririk

def bol(a, b):  # Bölmə funksiyası
    if b == 0:  # Əgər bölən sıfırdırsa
        raise ZeroDivisionError  # Xəta mesajı fırladırıq (sıfıra bölmək olmaz)
    netice = a / b  # Bölməni icra edirik
    return netice  # Nəticəni qaytarırıq

def hesabla_siyahini(siyahi):  # Siyahıdakı ifadəni hesablayan əsas hissə
    is_siyahisi = siyahi.copy()  # Orijinal siyahı korlanmasın deyə kopya çıxarırıq

    i = 0  # Dövr üçün indeks təyin edirik
    while i < len(is_siyahisi):  # Siyahının sonuna qədər gedirik
        element = is_siyahisi[i]  # Cari elementi götürürük
        if element == "-" and (i == 0 or is_siyahisi[i-1] in ["+", "-", "*", "/"]):  # Mənfi işarəsini yoxlayırıq
            if i + 1 < len(is_siyahisi):  # İşarədən sonra nəsə varmı?
                menfi_eded = float(is_siyahisi[i+1]) * -1  # Ədədi mənfiyə vurub mənfi edirik
                is_siyahisi[i : i+2] = [menfi_eded]  # İşarə və rəqəmi tək mənfi ədədlə əvəzləyirik
                i = 0  # Siyahı dəyişdi, yenidən başdan başlayırıq
                continue  # Növbəti dövrə keçirik
        i = i + 1  # İndeksi bir vahid artırırıq

    i = 0  # İndeksi yenidən sıfırlayırıq
    while i < len(is_siyahisi):  # Vurma və bölmələri axtarırıq
        if is_siyahisi[i] == "*" or is_siyahisi[i] == "/":  # Əgər vurma və ya bölmədirsə
            sol_teref = float(is_siyahisi[i-1])  # Sol tərəfdəki rəqəm
            sag_teref = float(is_siyahisi[i+1])  # Sağ tərəfdəki rəqəm
            isare = is_siyahisi[i]  # İşarənin özü

            if isare == "*":  # Əgər vurmadırsa
                cavab = vur(sol_teref, sag_teref)  # Vurma funksiyasını çağırırıq
            else:  # Əgər bölmədirsə
                cavab = bol(sol_teref, sag_teref)  # Bölmə funksiyasını çağırırıq
            
            is_siyahisi[i-1 : i+2] = [cavab]  # Hesabladığımız 3 elementi tək cavabla əvəz edirik
            i = 0  # Başdan yenidən yoxlayırıq
        else:  # Əgər vurma/bölmə deyilsə
            i = i + 1  # Növbəti elementə keçirik

    i = 0  # İndeksi axırıncı dəfə sıfırlayırıq
    while i < len(is_siyahisi):  # İndi isə toplama və çıxmaları tapırıq
        if is_siyahisi[i] == "+" or is_siyahisi[i] == "-":  # Əgər toplama və ya çıxmadırsa
            sol_teref = float(is_siyahisi[i-1])  # Sol arqument
            sag_teref = float(is_siyahisi[i+1])  # Sağ arqument
            isare = is_siyahisi[i]  # Hansı işarədir?

            if isare == "+":  # Toplamadırsa
                cavab = topla(sol_teref, sag_teref)  # Toplayırıq
            else:  # Çıxmadırsa
                cavab = cix(sol_teref, sag_teref)  # Çıxırıq
            
            is_siyahisi[i-1 : i+2] = [cavab]  # Nəticəni siyahıya yazırıq
            i = 0  # Yenidən başa qayıdırıq
        else:  # Başqa bir şeydirsə
            i = i + 1  # İrəli gedirik

    return is_siyahisi  # Hesablanmış siyahını geri qaytarırıq

def calculate(args):  # Main tərəfindən çağırılan funksiya
    netice_listi = hesabla_siyahini(args)  # Hesablamanı başladırıq
    return netice_listi  # Nəticəni main-ə veririk
