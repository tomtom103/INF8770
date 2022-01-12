import math
import struct

class LZ77:
    def __init__(self, message, dictSize = 6) -> None:
        self.message = message
        self.dictSize = dictSize
        self.triplets = []

    def encode(self):
        triplets = []  # Pour sauvegarder les triplets

        index = 0  # Position courante dans le message
        while index < len(self.message):
            decalage = 0
            symbDict = self.message[max(0, index - self.dictSize): index]  # Symboles disponibles du dictionnaire
            if len(symbDict) < self.dictSize:
                decalage = self.dictSize - len(symbDict) #Pour l'ajustement des indices de position quand le dictionnaire n'est pas plein.
            
            sousChaine = self.message[index:len(self.message)-1] #Le dernier caractère sera ajouté comme 3e élément du dernier triplet

            # On cherche la sous-chaine la plus longue
            pos, length = 0, 0
            while len(sousChaine) > 0:
                if sousChaine in symbDict:
                    pos, length = symbDict.rfind(sousChaine), len(sousChaine) #dernière occurrence si plusieurs choix
                    break
                sousChaine = sousChaine[:-1] # On a pas trouvé, donc on enlève un élément.
            
            # Regarde ensuite si on peut allonger la sous-chaine trouvée après la position de l'index: AB|ABABABABAB
            increment = 0
            while length > 0 \
                    and index+length+increment < (len(self.message)-1) \
                    and self.message[index-len(symbDict)+pos+length+increment] == self.message[index+length+increment]:
                increment += 1
            length += increment

            # Enregistrement des triplets
            c = self.message[index + length]  #Caractère suivant non encodé.

            if length == 0:
                pos = 0
            else:
                pos = pos + decalage #Pour l'ajustement des indices de position quand le dictionnaire n'est pas plein.

            triplets.append((pos, length, c))

            index += max(length+1, 1)  # Avance la position dans le message
        
        self.triplets = triplets
        return triplets

    def decode(self):
        decoded = ""

        for triplet in self.triplets:
            pos, length, char = triplet[0], triplet[1], triplet[2]
            if (pos, length) == (0, 0):
                decoded += char
            else:
                decalage = 0
                if len(decoded) < self.dictSize:
                    decalage = self.dictSize - len(decoded) #Pour l'ajustement des indices de position quand le dictionnaire n'est pas plein.
                start = max(0, len(decoded) - self.dictSize)
                for i in range(length):
                    decoded += decoded[start+pos-decalage+i]
                decoded += char

        return decoded

    def compression_rate(self) -> float:
        return 1 - (len(self.triplets) * 3) / len(self.message)