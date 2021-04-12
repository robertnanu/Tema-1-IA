import copy
import time

"""
Observatie pentru cei absenti la laborator: trebuie sa dati enter după fiecare afișare a cozii până vă apare o soluție. Afișarea era ca să vedem progresul algoritmului. Puteți să o dezactivați comentând print-ul cu coada și input()
"""


# informatii despre un nod din arborele de parcurgere (nu din graful initial)
class NodParcurgere:
    def __init__(self, info, parinte):
        self.info = info
        self.parinte = parinte  # parintele din arborele de parcurgere

    def obtineDrum(self):
        l = [self]
        nod = self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod = nod.parinte
        return l

    def afisDrum(self):  # returneaza si lungimea drumului
        l = self.obtineDrum()
        for stare in l:
            g.write(str(stare))
        return len(l)

    def contineInDrum(self, infoNodNou):
        nodDrum = self
        while nodDrum is not None:
            if (infoNodNou == nodDrum.info):
                return True
            nodDrum = nodDrum.parinte

        return False
    
    def showSir(self):
        nanu = self.info
        sir = "\n"

        i = 0
        for x in nanu:
            sir += str(i) + ": "
            i += 1
            for i in range(len(x)):
                sir += (x[i] + " ")
            sir += "\n"
        return(sir)

    def __repr__(self):
        return self.showSir()

    def __str__(self):
        return self.showSir()

######################################################################################
#                                   Date intrare                                     #
######################################################################################        

#f = open("D:\IA\Tema1\date_intrare.txt", "r")
f = open('date_intrare.txt', 'r')

def obtineCombinatii(sir):
			combinatii = sir.strip().split("\n")
			listaCombinatii = [aici.strip().split() for aici in combinatii]
			return listaCombinatii

continutFisier = f.read()
siruriStari = continutFisier.split("stare_initiala")
### aici sunt combinatiile
#print(siruriStari[0])
combinatieCulori = obtineCombinatii(siruriStari[0])
start = []
siruriVase = siruriStari[1].split("stare_finala")
### aici sunt cantitatile din vase
#print(siruriVase[0])
start = obtineCombinatii(siruriVase[0])
scop = []
#for scop in siruriVase:
#self.scopuri.append(obtineCombinatii(scop))
scop = obtineCombinatii(siruriVase[1])
#print("Combinatii culori:", self.combinatii)
#print("Cantitati vase: ", self.vase)
#print("Stari finale dorite: ", self.scop)

print(start)
print(combinatieCulori)
print(scop)

f.close()

######################################################################################

class Graph:  # graful problemei
    def __init__(self, start, scop , combinatieCulori):

        self.nrStive = len(start)
        self.start = start
        self.scop = scop
        self.combinatieCulori = combinatieCulori

    # va genera succesorii sub forma de noduri in arborele de parcurgere
    def genereazaSuccesori(self, nodCurent):

        listaSuccesori = []

        for x in range(self.nrStive):
            # verific posibilitatea de a extrage blocul
            if int(nodCurent.info[x][1]) > 0:
                for y in range(self.nrStive):
                    # verific sa nu iau de ex 0 cu 0, deoarece nu ar avea sens
                    if x != y and int(nodCurent.info[y][1]) < int(nodCurent.info[y][0]) and int(nodCurent.info[y][1]) > 0 :
                        ok = False
                        for culoare in combinatieCulori:
                            # verific daca exista combinatia respectiva de culori
                            if (culoare[0] == nodCurent.info[x][2] and culoare[1] == nodCurent.info[y][2]) or (culoare[1] == nodCurent.info[x][2] and culoare[0] == nodCurent.info[y][2]) :
                                ok = True

                                nodNouInfo = copy.deepcopy(nodCurent.info)

                                nextNod = NodParcurgere(nodNouInfo, nodCurent) # ma intereseaza sa afisez si pasii intermediari
                                nextNod.info[y][2] = culoare[2]

                                if (int(nodCurent.info[y][0]) >= int(nodCurent.info[x][1]) + int(nodCurent.info[y][1])):
                                     # actualizez nodul
                                     nextNod.info[x][1] = '0'

                                     del nextNod.info[x][2]
                                    
                                     nextNod.info[y][1] = str(int(nodCurent.info[x][1]) + int(nodCurent.info[y][1]))
                                # adaug nodul urmator in lista de succesori
                                else:
                                     nextNod.info[x][1] = str(int(nextNod.info[x][1]) - (int(nextNod.info[y][0]) - int(nextNod.info[y][1])))
                                     nextNod.info[y][1] = str(int(nodCurent.info[y][0]))

                                listaSuccesori.append(nextNod)

                        if ok != True:
                            nodNouInfo = copy.deepcopy(nodCurent.info)

                            nextNod = NodParcurgere(nodNouInfo, nodCurent)
                            nextNod.info[y][2] = 'nedefinita'

                            if (int(nodCurent.info[y][0]) >= int(nodCurent.info[x][1]) + int(nodCurent.info[y][1])):
                                nextNod.info[x][1] = '0'

                                del nextNod.info[x][2]

                                nextNod.info[y][1] = str(int(nodCurent.info[x][1]) + int(nodCurent.info[y][1]))
                            else:
                                nextNod.info[x][1] =str(int(nextNod.info[x][1]) - (int(nextNod.info[y][0]) - int(nextNod.info[y][1])))
                                nextNod.info[y][1] = str(int(nodCurent.info[y][0]))

                            listaSuccesori.append(nextNod)

        return listaSuccesori

    def __repr__(self):
        sir = ""
        for (k, v) in self.__dict__.items():
            sir += "{} = {}\n".format(k, v)
        return (sir)

"""
##############################################################################################	
#                                 Initializare problema                                      #
##############################################################################################		

#pozitia i din vectorul de noduri da si numarul liniei/coloanei corespunzatoare din matricea de adiacenta		
noduri=["a","b","c","d","e","f","g","i","j","k"]

m=[
	[0,1,1,1,0,0,0,0,0,0],
	[0,0,0,0,1,1,0,0,0,0],
	[0,0,0,0,1,0,1,0,0,0],
	[0,0,0,0,0,0,0,1,0,0],
	[0,0,1,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,1,1,0,0,1,0,0],
	[0,0,0,0,0,0,0,0,1,1],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0]
]
mp=[
	[0,3,9,7,0,0,0,0,0,0],
	[0,0,0,0,4,100,0,0,0,0],
	[0,0,0,0,10,0,5,0,0,0],
	[0,0,0,0,0,0,0,4,0,0],
	[0,0,1,0,0,10,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,1,7,0,0,1,0,0],
	[0,0,0,0,0,0,0,0,2,1],
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0]
]
start="a"
scopuri=["f"]
gr=Graph(noduri, m, mp, start, scopuri)
"""

gr = Graph(start, scop , combinatieCulori)

nrSolutiiCautate = 4
continua = True

# este asemanator BF, deoarece avem cost 1 pe fiecare mutare (BFS este UCS cu costuri de 1)
def uniform_cost(gr):

    global nrSolutiiCautate, lungimeasemanare, lungimesolutie, continua
    # in coada vom avea doar noduri de tip NodParcurgere (nodurile din arborele de parcurgere)
    c = [NodParcurgere(start, None)]
      # variabila pe care o setez la false cand consider ca s-au afisat suficiente solutii
    lungimesolutie = 0

    # face len(scop)
    for i in scop:
        lungimesolutie += 1

    # cauta fiecare element din scop pentru a verifica daca exista in starea mea actuala
    while (len(c) > 0 and continua):
        lungimeasemanare = 0
        nodCurent = c.pop(0)
        # cautam in toate elementele introduse j scopuri
        for i in  nodCurent.info:
            for j in  scop:
                if i[1] != 0:
                    if i[1] == j[0] and i[2] == j[1]:
                        lungimeasemanare += 1

        if lungimeasemanare == lungimesolutie:
            g.write("Solutia numarul " + str(4 - nrSolutiiCautate + 1))
            nodCurent.afisDrum()
            nrSolutiiCautate -= 1
            g.write(" \n################# \n\n\n")

        if nrSolutiiCautate == 0:
            continua = False

        lSuccesori = gr.genereazaSuccesori(nodCurent)

        # adauga in coada ce a descoperit nou
        c.extend(lSuccesori)

g = open("D:\IA\Tema1\date_iesire.txt", "w")

time1 = time.time()

uniform_cost(gr)

time2 = time.time()

durata = round(1000 * (time2 - time1))

g.write("Executia programului a durat: " + str(durata) + " ms\n")
#g.write(str(psutil.virtual_memory()))

g.close()
