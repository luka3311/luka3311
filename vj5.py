def provjera_broja(broj):
    if 10 <= broj <= 100:
        return f"broj {broj} je unutar raspona."
    else:
        return f"broj{broj} je unutar raspona."
    
if __name__ == "__main__":
    try:
        uneseni_broj = int(input("unesite broj:"))
        print(provjera_broja(uneseni broj))
    except ValueError:
        print("unesena vrijednost nije broj.")