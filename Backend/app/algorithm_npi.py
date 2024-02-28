# L'algorithme qui réalise une calculatrice en notation polonaise inverse (NPI)
from .database import NPIResultData



def polonaise_npi(expression):
    """
    Evalue une expression en notation polonaise inverse 

    Args:
      le resultat de l'évaluation de l'expression

    Retourne: 
       
        Le résultat de l'évaluation
    """
    pile = []
    tokens = " ".join(expression).split() if len(expression)==5 else expression.split()
    for token in tokens:
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
