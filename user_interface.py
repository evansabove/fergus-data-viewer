from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto

class UserInterface:
    inky_display = auto()

    def __init__(self):
        self.inky_display = auto()

    def show_splash_screen(self):
        text = "FERGUS"
        font = self.get_font(50)
        width, height = font.getsize(text)

        x = (self.inky_display.WIDTH / 2) - (width / 2)
        y = (self.inky_display.HEIGHT / 2) - (height / 2)

        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        draw.text((x, y), text, self.inky_display.BLACK, font)
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
        return ImageFont.truetype('Roboto-Medium.ttf', size)