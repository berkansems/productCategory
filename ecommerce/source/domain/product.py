from source.domain.base import Base


class Product(Base):
    def __init__(self, id=None, name=None, description=None, price=None, category_Id=None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.price = price
        self.category_Id = category_Id

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setPrice(self, price):
        self.price = price

    def setCategory_Id(self, category_Id):
        self.category_Id = category_Id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def getCategory_Id(self):
        return self.category_Id
