import os
login = 0
benar = 0
while login < 3:
    os.system("cls")
    username = ["user","user2","user3"]
    pw = ["123","1234","12345"]
    user_inp = input("Masukkan username anda : ")
    pw_inp = input("Masukkan password anda : ")

    if user_inp in username and pw_inp in pw:
        login += 4
    else : print("Login GAGAL\n")

if login > 3:
    if username.index(user_inp) == pw.index(pw_inp):
        print("\nLogin BERHASIL\n")
        
        # GAME TEBAK ANGKA
        import random
        kom = random.randint(1,10)
        kesempatan = 3
        while kesempatan > 0:
            print("----"*5,"GAME TEBAK ANGKA","----"*5)
            print(f"Kom akan memilih dari angka 1 - 10\nTebaklah angka yang dipilih oleh kom\nKesempatan {kesempatan}x")
            player = int(input("Masukkan angka dari 1 - 10 : "))
            if player == kom : 
                print("\nSELAMAT TEBAKAN ANDA BENAR")
                benar = 1
            elif player > kom : 
                print(f"\nAngka yang anda masukkan lebih BESAR daripada {player}\n")
                kesempatan -= 1
            elif player < kom : 
                print(f"\nAngka yang anda masukkan lebih KECIL daripada {player}\n")
                kesempatan -= 1
                
            if kesempatan == 0 :
                print("Kesempatan anda habis")
                print(f"Angka yang dipilih kom adalah {kom}\n")
                benar = 1
        
            if benar == 1:
                main_lagi = input("Mau main lagi (y/n) : ")
                if main_lagi == "y" or main_lagi == "Y": 
                    kesempatan = 3
                    benar = 0   
                    kom = random.randint(1,10)  
                    print("\nAngka DIACAK LAGI\n")
                else: 
                    print("\nAkhir dari pemograman")
                    break
else: print("\nLogin GAGAL")