class Humeur(object):
    #notation americain dans les mois
    def __init__(self):
        self.title = "Humeur du dev de jackpoint"
        self.corpus = "Debut du bousin"
        self.envie = None
    def 02_10_2012(self):
        self.corpus = "Besoin de remotivation et d'arreter de me disperser"
        self.envie = "Etre en couple."
    def 03_16_2012(self):
        self.corpus = "Gros coup de collier beta fin mars"
        self.envie = "Besoin d'une egerie."
        self.state = "hs"



if __name__ == "__main__":
    h = Humeur()
    print dir(h)
    print h.envie()


