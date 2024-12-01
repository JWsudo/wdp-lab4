def powitanie(imie, jezyk ="polski"):
    if jezyk == "polski":
        print(f"Witaj {imie}")
    if jezyk == "angielski":
        print(f"Hello {imie}")
    if jezyk == "niemiecki":
        print(f"guten morgen {imie}")

powitanie("Jan")
powitanie("Jan", "polski")
powitanie("Jan", "angielski")
powitanie("Jan", "niemiecki")