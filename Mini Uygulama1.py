while True:
    komut = input(":")
    
    if komut == "merhaba":
        print("Merhaba! Nasılsın?")
    elif komut == "help":
        print("Kullanılabilir komutlar: merhaba, help, exit")
    elif komut == "exit":
        print("Güle güle!")
        break
    else:
        print(f"'{komut}' komutu tanınmadı")