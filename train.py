class Train:
    def __init__(self, x, y, type):
        if type == 0:
            self.segments = [["s", x, y], ["o", x, y+1], ["c", x, y+2], ["k", x, y+3], ["s", x, y+4]]
        else:
            self.segments = [["s", x, y], ["o", x+1, y], ["c", x+2, y], ["k", x+3, y], ["s", x+4, y]]
        self.current_pos = (x, y)
        self.head = self.segments[0]
