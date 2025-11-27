
def afficher_menu():
    return """
    ------------ M E N U ------------
    1- Ajouter un nouvel enregistrement
    2- Afficher toutes les données
    3- Modifier un enregistrement
    4- Supprimer un enregistrement
    5- Sauvegarder (JSON / CSV / TXT)
    6- Charger (JSON / CSV / TXT)
    0- Quitter
    """

def ajouter_donnee(liste):
    data={
    "id": int,
    "nom": str,
    "age": int
    }
    while True:
        id=input("id: ")
        nom=input("nom: ")
        age=input("age: ")
        if id.isdigit() and age.isdigit():
            if id not in [d["id"] for d in liste]:
                id=int(id)
                age=int(age)
                data["id"] = id
                data["nom"] = nom
                data["age"] = age
                liste.append(data)
                print("enregistrement ajoute")
                break
            else:
                print("id deja existant")
        else:
            print("votre id et age doivent etre des nombres")
    return liste
def afficher_donnees(liste):
    for d in liste:
        print(f"id: {d['id']}, nom: {d['nom']}, age: {d['age']}")
    return
def modifier_donnees(liste):
    while True:
        id=input("id: ")
        if id.isdigit():
            if id not in [d["id"] for d in liste]:
                print("id introuvable")
                break
            for d in liste:
                if d["id"] == int(id):
                    d["nom"] = input("nouveau nom: ")
                    while True:
                        n_age=input("nouveau age: ")
                        if n_age.isdigit():
                            n_age=int(n_age)
                            d["age"] = d["age"]
                            break
                    print("enregistrement modifie")
    return
def supprimer_donnee(liste):
    id=input("id: ")
    if id.isdigit() and id in [d["id"] for d in liste]:
        for d in liste:
            if d["id"] == int(id):
                liste.remove(d)
                print("enregistrement supprime")
                return
    else:
        print("id introuvable")
        return
def save_json(liste, filename):
    import json
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(liste,f,indent=4,ensure_ascii=False)
    return f"Fichier JSON: {filename} sauvgarder avec succees!"
def save_csv(liste, filename):
    import csv
    with open(filename,"w") as f:
        f.write("id-nom-age\n")
        for data in liste:
            f.write(f"{data["id"]}-{data['nom']}-{data['age']}\n")
    return f"Fichier CSV: {filename} sauvgarder avec succees!"
def save_txt(liste,filename):
    with open(filename,"w") as f:
        for data in liste:
            f.write(f"id: {data['id']}, nom: {data['nom']}, age: {data['age']}\n")
    return f"Fichier TXT: {filename} sauvgarder avec succees!"
def load_json(filename):
    import json
    with open(filename,"r",encoding="utf-8") as f:
        content=json.load(f)
    return content
def load_csv(filename):
    import csv
    with open(filename,"r") as f:
        reader=csv.reader(f)
        content=list(reader)
    return content
def load_txt(filename):
    with open(filename,"r") as f:
        content=f.read()
    return content
def main():
    liste=[]
    print(afficher_menu())
    while True:
        choix=input("votre choix: ")
        if choix=="1":
            ajouter_donnee(liste)
        elif choix=="2":
            afficher_donnees(liste)
        elif choix=="3":
            modifier_donnees(liste)
        elif choix=="4":
            supprimer_donnee(liste)
        elif choix=="5":
            filename=input("nom du fichier complet (avec l'extension): ")
            if filename.split(".")[-1].lower()=="json":
                save_json(liste,filename)
            elif filename.split(".")[-1].lower()=="csv":
                save_csv(liste,filename)
            elif filename.split(".")[-1].lower()=="txt":
                save_txt(liste,filename)
            else:
                print("extension non supportee")
        elif choix=="6":
            filename=input("nom du fichier complet (avec l'extension): ")
            if filename.split(".")[-1].lower()=="json":
                load_json(liste,filename)
            elif filename.split(".")[-1].lower()=="csv":
                load_csv(liste,filename)
            elif filename.split(".")[-1].lower()=="txt":
                load_txt(liste,filename)
            else:
                print("extension non supportee")
        elif choix=="0":
            print("programme termine!")
            break