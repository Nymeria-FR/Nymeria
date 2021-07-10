import discord
from discord import Message, Client, File
from random import randint
from time import time

class Scrabble:
    """
	"""

    def __init__(self, message):
        self.channel = message.channel
        self.author = message.author

    async def launch(self, client):

        def choix_element(tab):
            """choix_element(tab) renvoie une valeur aléatoirement choisie dans le tableau tab"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            assert len(tab) > 0
            n = randint(0,len(tab)-1)
            return tab[n]

        def longueur_max(tab):
            """longueur_max(tab) prend en argument un tableau de chaîne de caractères et renvoie
            la valeur de la plus longue"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            assert len(tab) != 0
            x = tab[0]
            for i in tab:
                if (len(i) > len(x)):
                    x = i
            return len(x)

        def mots_de_long_exact(tab, n):
            """mots_de_long_exact(tab, n) renvoie un tableau des chaînes de tab ayant comme
            longueur exactement n"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            t = []
            for i in tab:
                if (len(i) == n):
                    t.append(i)
            return t

        def mots_de_long_au_plus(tab, n):
            """mots_de_long_au_plus(tab, n) renvoie un tableau des chaînes de tab ayant comme
            longueur n ou moins"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            t = []
            for i in tab:
                if (len(i) <= n):
                    t.append(i)
            return t

        def melange_chaine(mot):
            """Renvoie une copie de la chaîne mot où les caractères ont été aléatoirement permutés"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            t = list(mot)
            for i in range (0,len(t)):
                j = randint(i,len(t)-1)
                t[i],t[j] = t[j],t[i]
            return "".join(t)

        def trie_chaine(mot):
            """Renvoie une chaîne contenant les même caractères que mot, triés en ordre alphabétique"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            t = list(mot)
            t = sorted(t)
            return "".join(t)

        def appartient(c, s):
            """Renvoie True si l'unique caractère de c appartient à la chaîne s et False sinon"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            for i in s:
                if i == c:
                    return True
            return False

        def recherche(m, tab):
            """Recherche la chaîne m dans le tableau de chaînes tab. Renvoie True si la chaîne
            est présente et False sinon"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            i = 0
            j = len(tab) - 1
            while (i <= j):
                mid = (i + j)//2
                if (tab[mid] == m):
                    return True
                else:
                    if (tab[mid] > m ):
                        j = mid-1
                    else:
                        i = mid+1
            return False

        def sous_ensemble(s1, s2):
            """sous_ensemble(s1, s2) vérifie que tous les caractères de s1 apparaissent dans s2"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            for i in s1:
                if not (i in s2):
                    return False
            return True

        def calcule_anagrammes(mots):
            """calcule_anagrammes (mots) renvoie un dictionnaire permettant de retrouver
            efficacement les anagrammes de chaque mot du tableau passé en argument"""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            dic = {}
            for i in mots:
                if trie_chaine(i) in dic:
                    dic[trie_chaine(i)].append(i)
                else:
                    dic[trie_chaine(i)] = [i]
            return dic

        def charge_dico():
            """charge_dico() renvoie le tableau des mots se trouvant dans le fichier
            "dico.txt"."""

            #REMPLACER LE RETURN CI-DESSOUS PAR LE CORP DE LA FONCTION
            f = open("donnees/dico.txt","r")
            dico = f.readlines()
            for i in range(len(dico)):
                dico[i] = dico[i].strip()
            return dico

        def is_correct(m):
            return m.channel == self.channel and m.content.isdigit() and m.author == self.author
        
        def is_correct2(m):
            return m.channel == self.channel and m.author == self.author

        mots = charge_dico ()     # on charge le dictionnaire
        lmax = longueur_max(mots) # on trouve la longueur maximum, lmax
        longueur = 0              # longueur du mot recherché
        while longueur == 0:
            try:
                #on demande à l'utilisateur de saisir une longueur, que l'on
                #convertit en entier
                await self.channel.send("Entrer une longueur de mot entre 1 et " + str(lmax) + ":")
                l = await client.wait_for(event="message", check=is_correct)
                l = int(l.content)
                if l > 0 and l <= lmax: #Si elle est dans l'intervalle, on définit
                    longueur = l        #la variable longueur ce qui fera sortir de la boucle
                else:
                    #Sinon on affiche un message d'erreur, et on re-boucle
                    await self.channel.send("Longueur invalide")
            except:
                #Si la chaîne n'est pas un entier (la fonctio int() renvoie une exception)
                print("Entrée invalide")
        #On filtre les mots de la longueur choisie.
        ml = mots_de_long_exact(mots, longueur)
        #On calcule aussi les mots faisant au plus cette longueur
        minf = mots_de_long_au_plus(mots, longueur)
        #On indexe ces mots par caractères
        minf_idx = calcule_anagrammes(minf)
        #On choisit un mot à deviner aléatoirement
        #parmis les mots de la bonne longueur
        mot = choix_element(ml)
        #On mélange le mot
        mot_melange = melange_chaine(mot)
        #On trie les lettres du mot
        mot_trie = trie_chaine(mot)
        #On demande à l'utilisateur de saisir sa solution
        await self.channel.send("Votre anagramme: " + mot_melange)
        await self.channel.send("Votre solution:")
        sol = await client.wait_for(event="message", check=is_correct2)
        sol = (sol.content).upper()
        #On trie le mot saisi par l'utilisateur
        sol_t = trie_chaine(sol)
        #Si le mot saisi utilise bien les lettres du mot
        #à deviner ET qu'il existe des anagrammes pour ce mot
        #ET si le mot saisi est bien dans la liste des mots correspondant
        # à cette anagramme
        if sous_ensemble(sol, mot) and sol_t in minf_idx and recherche(sol, minf_idx[sol_t]):
            if len(sol) == len(mot):
                #Si la solution proposée et le mot à deviner
                #On la même longueur: champion!
                await self.channel.send("C'est une solution exacte")
            else:
                #Sinon, on a une solution partielle
                #On affiche les meilleures réponses possible
                await self.channel.send("C'est une solution partielle")
                await self.channel.send("Le meilleur anagramme possible était:")
                for m in minf_idx[mot_trie]:
                    await self.channel.send("> " + m)
            return
        #Dans tous les autres cas, c'est une mauvaise réponse
        await self.channel.send(f"Mauvaise réponse, une des réponses était {mot}")