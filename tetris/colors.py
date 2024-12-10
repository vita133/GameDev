class Colors:
    dark_grey = (26, 31, 40)
    bright_yellow = (255, 223, 0)
    turquoise = (0, 204, 204)
    bright_red = (255, 51, 51)
    lime_green = (102, 255, 102)
    orange = (255, 153, 51)
    light_blue = (102, 204, 255)
    pink = (255, 102, 178)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.bright_yellow, cls.turquoise, cls.bright_red, 
                cls.lime_green, cls.orange, cls.light_blue, cls.pink]
    