class Train:
    def __init__(self, x, y):
        self.segments = [["s", x, y], ["o", x, y+1], ["c", x, y+2], ["k", x, y+3], ["s", x, y+4]]
        self.current_pos = (x, y)
        self.create()
        self.head = self.segments[0]

    def create(self):
        # later
        print("hi")

    def add_segment(self, pos):
        new_segment = "#"
        self.segments.append(new_segment)