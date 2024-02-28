# L'algorithme qui réalise une calculatrice en notation polonaise inverse (NPI)
from database import NPIResultData

'''
Voici les étapes à suivre pour faire l'algorithme NPI:
1 - Définir une pile vide 
2 - Lire l'expression NPI caractère par caractère
3 - Si le caractère est un opérande (chiffre):
    - Pousser le nombre sur la pile
4 - Sinon si le caractère est un operateur:
    - Dépiler les deux derniers nombresde la pile
    - Effectuer l'opération correspondante sur les deux nombres.
    - Pousser le résultat sur la pile
5. Répéter les étapes 2 à 4 jusqu'à la fin de l'expression
6. Le résultat final est le nombre au sommet de la pile. 

'''


def polonaise_npi(expression):
    """
    Evalue une expression en notation polonaise inverse 

    Args:
      le resultat de l'évaluation de l'expression

    Retourne: 
       
        Le résultat de l'évaluation de l'
    """
    pile = []
    for token in expression.split():
        if token.isdigit():
            pile.append(int(token))
        else:
            if len(pile) < 2:
                raise ValueError("Expression invalide")
            op2 = pile.pop()
            op1 = pile.pop()
            result = 0
            if token == "+":
                result = op1 + op2
            elif token == "-":
                result = op1 - op2
            elif token == "*":
                result = op1 * op2
            elif token == "/":
                if op2 == 0:
                    raise ValueError("Division par zéro n'est pas permi ):")
                result = op1 / op2
            else:
                raise ValueError("Opérateur invalide")
            
            pile.append(result)
           
    return  NPIResultData(expression=expression,result=str(pile.pop()))
