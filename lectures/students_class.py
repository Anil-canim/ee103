class students:
    def __init__(self,isim,puan):
        self.ad=isim
        self.notu=puan
    def show_the_situation(self):
        print(f"öğrencinin adı {self.ad} and notu {self.notu}")

öğrenci1=students("anıl",80)
öğrenci1.show_the_situation()