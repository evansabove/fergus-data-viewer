from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto

class UserInterface:
    inky_display = auto()

    def __init__(self):
        self.inky_display = auto()

    def show_splash_screen(self):
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        fergus_font = self.get_font(50)
        fergus_text = "FERGUS"
        fergus_width, fergus_height = fergus_font.getsize(fergus_text)

        fergus_x = (self.inky_display.WIDTH / 2) - (fergus_width / 2)
        fergus_y = (self.inky_display.HEIGHT / 2) - (fergus_height / 2)

        draw.text((fergus_x, fergus_y), fergus_text, self.inky_display.BLACK, fergus_font)

        connection_font = self.get_font(20)
        connection_text = "Connecting to..."
        connection_width, connection_height = connection_font.getsize(connection_text)

        connection_x = (self.inky_display.WIDTH / 2) - (connection_width / 2)
        connection_y = (self.inky_display.HEIGHT / 4) - (connection_height / 2)

        draw.text((connection_x, connection_y), connection_text, self.inky_display.BLACK, connection_font)
        

        self.inky_display.set_image(img)
        self.inky_display.show()
    
    def write(self, label, value):
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        label_font = self.get_font(20)
        label_width, label_height = label_font.getsize(label)

        label_x = (self.inky_display.WIDTH / 2) - (label_width / 2)
        label_y = (self.inky_display.HEIGHT / 4)*3 - (label_height / 2)

        value_font = self.get_font(40)
        value_width, value_height = value_font.getsize(value)

        value_x = (self.inky_display.WIDTH / 2) - (value_width / 2)
        value_y = (self.inky_display.HEIGHT / 3) - (value_height / 2)
        
        draw.text((label_x, label_y), label, self.inky_display.BLACK, label_font)
        draw.text((value_x, value_y), value, self.inky_display.BLACK, value_font)

        self.inky_display.set_image(img)
        self.inky_display.show()
    
    def get_font(self, size):
        return ImageFont.truetype('/home/andy/fergus-data-viewer/Roboto-Medium.ttf', size) #change this