from pyswip import Prolog
prolog=Prolog()
prolog.consult("khanfamily.pl")
while True:
    num = int(input("Enter 1 for continue\n"))
    print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
    if num==1:
        print("Enter 1 for Beti", "Enter 2 for Beta")
        print("Enter 3 for Dada", "Enter 4 for Nana")
        print("Enter 5 for Dadi", "Enter 6 for Nani")
        print("Enter 7 for Sala", "Enter 8 for Bahu")
        print("Enter 9 for Pota", "Enter 10 for Nawasa")
        print("Enter 11 for BaapDada", "Enter 12 for Khala")
        print("Enter 13 for Pota", "Enter 0 for Exit")
        print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        print("Members of Khan Family-------------------------:")
        print("ChoteKhan, ChotiRani, BarreKhan, BarriRani")
        print("Salim, Kausar, Nadir, Asad, Nahid, Sumra")
        print("Rizwan, Burhan, Rashid, Akram, Salima, Sanam, Rabia")
        print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸:")
        number=int(input(" Enter your Choice for the Relationship that you are interested in:"))
        if(number==1):
            Y=input("Enter name of person whose Beti is required : \n")
            Y=Y.lower()
            for val in prolog.query("beti(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the beti of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 2):
            Y=input("Enter name of person whose Beta is required : ")
            Y=Y.lower()
            for val in prolog.query("beta(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the beta of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 3):
            Y=input("Enter name of person whose Dada is required : ")
            Y=Y.lower()
            for val in prolog.query("dada(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the dada of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 4):
            Y=input("Enter name of person whose Nana is required : ")
            Y=Y.lower()
            for val in prolog.query("nana(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the nana of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 5):
            Y=input("Enter name of person whose Dadi is required : ")
            Y=Y.lower()
            for val in prolog.query("dadi(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the dadi of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 6):
            Y=input("Enter name of person whose Nani is required : ")
            Y=Y.lower()
            for val in prolog.query("nani(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the nani of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 7):
            Y=input("Enter name of person whose Sala is required : ")
            Y=Y.lower()
            for val in prolog.query("sala(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the sala of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 8):
            Y=input("Enter name of person whose Bahu is required : ")
            Y=Y.lower()
            for val in prolog.query("bahu(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the bahu of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 9):
            Y=input("Enter name of person whose Pota is required : ")
            Y=Y.lower()
            for val in prolog.query("pota(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the pota of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 10):
            Y=input("Enter name of person whose Nawasa is required : ")
            Y=Y.lower()
            for val in prolog.query("nawasa(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the nawasa of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number==11):
            Y=input("Enter name of person whose BaapDada is required : ")
            Y=Y.lower()
            for val in prolog.query("baapDada(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the baapDada of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif (number == 12):
            Y=input("Enter name of person whose Khala is required : ")
            Y=Y.lower()
            for val in prolog.query("khala(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the khala of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        elif number == 13:
            Y=input("Enter name of person whose ChachaTaya is required : ")
            Y=Y.lower()
            for val in prolog.query("chachataya(X,"+Y+")"):
                exist = True
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
                print("{0} is the chachataya of {1}.".format(val["X"], Y))
                print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        else:
            print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
            print("Invalid Input.Please Enter valid number if you want")
            print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
    else:
        print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        print("                      You Enter Number For Stop The Process :")
        print("                      If You Want Run It Again :")
        print("⫷s⫸⫷t⫸⫷y⫸⫷l⫸⫷i⫸⫷s⫸⫷h⫸⫷t⫸⫷e⫸⫷x⫸⫷t⫸")
        break



