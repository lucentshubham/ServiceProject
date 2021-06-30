class Qualifications:
    def __init__(self):
        self.data = []
    def addQualification(self,i):
        self.data.append(i)
    def getQualification(self):
        return self.data
class Images:
    def __init__(self) -> None:
        self.images = []
    def addImage(self,i):
        self.images.append(i)
    def getImages(self):
        return self.images
