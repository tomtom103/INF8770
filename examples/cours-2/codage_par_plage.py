# Run-length encoding, RLE
import numpy as np

Message = "AAAABAAAAAABBBAABAAAACABBABCDAADACAAAAAAAAAAAAAAAAAAAAAABABABBBA"
compteur = 2 #La meilleure taille pour ce message est 2 bits. Plusieurs courtes répétitions

dictsymb =[Message[0]]
dictbin = ["{:b}".format(0)]
nbsymboles = 1
for i in range(1,len(Message)):
    if Message[i] not in dictsymb:
        dictsymb += [Message[i]]
        dictbin += ["{:b}".format(nbsymboles)] 
        nbsymboles +=1
        
longueurOriginale = np.ceil(np.log2(nbsymboles))*len(Message) #Longueur du message avec codage binaire

for i in range(nbsymboles):
    dictbin[i] = "{:b}".format(i).zfill(int(np.ceil(np.log2(nbsymboles))))
        
dictsymb.sort()
dictionnaire = np.transpose([dictsymb,dictbin])
print(dictionnaire) 

i=0
MessageCode = []
longueur = 0
while i < len(Message):
    carac = Message[i] #caractere qui sera codé
    repetition = 1
    #Calcul le nombre de répétitions.
    i += 1
    #tient compte de la limite du compteur
    while i < len(Message) and repetition < 2**compteur and Message[i] == carac: 
        i += 1
        repetition += 1
    #Codage à l'aide du dictionnaire  
    coderepetition = "{:b}".format(repetition-1).zfill(compteur)
    codebinaire = dictbin[dictsymb.index(carac)]
    MessageCode += [coderepetition, codebinaire]
    longueur += len(codebinaire) + len(coderepetition)

print(MessageCode)

print("Longueur = {0}".format(longueur))
print("Longueur originale = {0}".format(longueurOriginale))
