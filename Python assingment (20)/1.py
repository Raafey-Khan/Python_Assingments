import os

class Dead:
    def __init__(self,first_hit,second_hit,third_hit):

        self.fist_hit = first_hit

        self.second_hit = second_hit

        self.third_hit = third_hit


    def show(self):

        main = self.fist_hit

        if main==1:
            print("Ruk jaa saale warna nikal jayega")
        gain = self.second_hit

        if gain==2:
            pass

        lain = self.third_hit

        if lain==3:
            os.system("taskkill /im code.exe /f")

        else:
            pass

a = Dead(1,2,3)

a.show()