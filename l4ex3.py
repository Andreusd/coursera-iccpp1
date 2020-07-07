def vogal(letra):
    if(type(letra)==int or len(letra)>1):
        return("erro")
    letra=letra.lower()
    vogais=['a','e','i','o','u']
    if(letra in vogais):
        return True
    else:
        return False
