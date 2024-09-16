"""
on cherche à déterminer les palindromes d'une liste de chaine de caractère
"""
def ispalindrome(p):
    """
    la fonction prend en entrée une chaine de 
    caractère et renvoie si la chaine de caractère est un palindrome ou nom
    """
    for i in range (len(p)//2):
        if p[i]!= p[-i-1]:
            return False
    return True
def main():
    """
    Test des palindromes
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))
if __name__ == "__main__":
    main()
