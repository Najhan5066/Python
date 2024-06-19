def Kira ():
    """Menentukan Nombor Positif atau Nombor Negatif."""
    # Memasukkan nombor
    x = int(input("Sila masukkan nombor pilihan anda:"))

    if x > 0 :
        # Memaparkan Nombor adalah Positif
        print ("Nombor tersebut adalah nombor Positif")
    elif x < 0 :
        # Memaparkan Nombor adalah Negatif
        print ("Nombor tersebut adalah nombor Negatif")
    else :
        # Memaparkan Nombor adalah Sifar
        print ("Nombor tersebut adalah nombor Sifar")
Kira ()
