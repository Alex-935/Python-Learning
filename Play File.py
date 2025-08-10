class Pokemon5:
    def __init__(self, name, type1, type2=None):#short for initialse method
        if not name:
            raise ValueError("There is no name given")
        if type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']:
            raise ValueError("Invalid Type")
        if type1 not in ['Normal', "Fire", 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground', 'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy']: 
            raise ValueError("Invalid Type")
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.weakness = weakness

    def __str__(self):
        return 'This object is of type Pokemon'

    def weakness(self):
        match self.type1:
            case 'Normal':
                return ['Fighting']
            case 'Fire':
                return ['Water', 'Ground', 'Rock']
            case 'Water':
                return ['Electric', 'Grass']
            case _:
                return "Couldn't be bothered to code"
    

    
def mainObject5():
    poke1 = pokeDetails5()
    
    if poke1.type2 == None:
        print(f"{poke1.name} is a {poke1.type1} type")
    else:
        print(f"{poke1.name} is a {poke1.type1}/{poke1.type2} type")

    print("The pokemon's weakness' are:", poke1.weakness())


def pokeDetails5():
    
    name = (input("Please enter the Pokemon's name: ")).capitalize()
    type1 = (input("Please enter the Pokemon's first type: ")).capitalize()
    type2 = (input("Please enter the Pokemon's second type: ")).capitalize()
    #name, type1 and type2 are attributes of the object poke1
    try:
        return Pokemon5(name, type1, type2)
    except:
        ...

if __name__ == "__mainObject5__":
    mainObject5()

mainObject5()
