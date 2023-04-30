from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto

class UserInterface:
    label_font = ImageFont.truetype('Roboto-Medium.ttf', 20)
    value_font = ImageFont.truetype('Roboto-Medium.ttf', 40)

    inky_display = auto()
    inky_display.set_border(inky_display.BLACK)

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    def __init__(self):
        self.inky_display = auto()
        self.inky_display.set_border(self.inky_display.BLACK)

        self.img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        self.draw = ImageDraw.Draw(self.img)

    def show_splash_screen():
        return ''
    
    def write_text(self, text, x, y, font):
        self.draw.text((x, y), text, self.inky_display.BLACK, font)
        self.inky_display.set_image(self.img)
        self.inky_display.show()
    
    def write_label(self, text):
        width, height = self.label_font.getsize(text)

        xPosition = (self.inky_display.WIDTH / 2) - (width / 2)
        yPosition = (self.inky_display.HEIGHT / 4)*3 - (height / 2)

        self.write_text(text, xPosition, yPosition, self.label_font)

    def write_value(self, text):
        width, height = self.value_font.getsize(text)

        xPosition = (self.inky_display.WIDTH / 2) - (width / 2)
        yPosition = (self.inky_display.HEIGHT / 3) - (height / 2)

        self.write_text(text, xPosition, yPosition, self.value_font)