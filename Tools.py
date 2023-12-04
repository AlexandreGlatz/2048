#permet de rejouer
def Retry():

    while True:

        answer = AskInputs("Veux-tu rejouer (oui ou non) ?", ["oui","non"])
    
        if answer == "oui":
            return True  
        elif answer == "non":
            print("D'accord, à la prochaine")
            return False  
        else:
            print("Réponse non reconnue. Veuillez répondre par 'oui' ou 'non'.")

#Demander un int
def AskInt(Message: str) -> int:
    while True:
        Input: str = input(Message)
        if Input.isdigit():
            return int(Input)
        else:
            print("Il faut entrer un numéro")

#Demander un int dans range défini par borne Min Max
def AskIntInRange(Message: str, Min: int, Max: int) -> int:
    while True:

        Input: str = input(Message)
        
        if Input.isdigit() and Min <= int(Input) <= Max:
                 return int(Input)
        else:
            print(f"Il faut entrer un numéro entre {Min} et {Max}")


#Demander un input présent dans la liste
def AskInputs(Message : str, AuthorizedInputs: list[str]) -> str:
    while True:

        Input : str = input(Message).lower()
        
        if Input in AuthorizedInputs:
            return str(Input)
        else:
            print("Ce n'est pas une réponse valable.")

#deamnde un Input avec une longuer précise
def AskInputsLength(Message : str, Comparaison: str, AuthorizedInputs: list[str]) -> str:
    while True:

        Input : str = input(Message).lower()
        
        if len(Input) == len(Comparaison) and Input in AuthorizedInputs:
            return str(Input)
        else:
            print("Nombre de lettres ne correspond pas/ Le mot n'est pas dans la liste des mots valables !")
            print("------------------------------------")