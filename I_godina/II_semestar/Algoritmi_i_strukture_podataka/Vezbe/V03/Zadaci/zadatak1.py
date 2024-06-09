class Rectangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height
    
    @property.setter
    def height(self, height):
        self._height = height

    @property
    def obim(self):
        return 2 * (self.width + self.height)
    
    @property
    def povrsina(self):
        return self.width * self.height
    


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(side, side)
    
    @property
    def side(self):
        return self.width
    
    @property.setter
    def side(self, side):
        self.width = side
        self.height = side
    
    @property.setter
    def width(self, side):
        self.width = side
        self.height = side
    
    @property.setter
    def height(self, side):
        self.width = side
        self.height = side
    
    

def main():
    rec = Rectangle(4, 5)
    print(rec.width, rec.height)
    print(rec.obim, rec.povrsina)
    sq = Square(5)
    print(sq.side, sq.width, sq.height)
    print(sq.obim, sq.povrsina)

if __name__ == "__main__":
    main()
    