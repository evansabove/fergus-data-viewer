from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto
import time

class UserInterface:
    inky_display = auto()
    inky_display.set_border(inky_display.BLACK)

    img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
    draw = ImageDraw.Draw(img)

    def __init__(self):
        self.inky_display = auto()
        self.inky_display.set_border(self.inky_display.BLACK)

        self.img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        self.draw = ImageDraw.Draw(self.img)

    def show_splash_screen(self):
        text = "FERGUS"
        font = self.get_font(50)
        width, height = font.getsize(text)

        xPosition = (self.inky_display.WIDTH / 2) - (width / 2)
        yPosition = (self.inky_display.HEIGHT / 2) - (height / 2)

        self.draw.text((xPosition, yPosition), text, self.inky_display.BLACK, font)
        self.inky_display.set_image(self.img)
        self.inky_display.show()

        #time.sleep(5)

        # self.draw.rectangle((0, 0, self.inky_display.WIDTH, self.inky_display.HEIGHT), fill=(0, 0, 0, 0))
        # self.inky_display.set_image(self.img)
        # self.inky_display.show()

    
    def write_text(self, text, x, y, font):
        return
        self.draw.text((x, y), text, self.inky_display.BLACK, font)
        self.inky_display.set_image(self.img)
    
    def write_label(self, text):
        font = self.get_font(20)
        width, height = font.getsize(text)

        xPosition = (self.inky_display.WIDTH / 2) - (width / 2)
        yPosition = (self.inky_display.HEIGHT / 4)*3 - (height / 2)

        self.write_text(text, xPosition, yPosition, font)

    def write_value(self, text):
        font = self.get_font(40)
        width, height = font.getsize(text)

        xPosition = (self.inky_display.WIDTH / 2) - (width / 2)
        yPosition = (self.inky_display.HEIGHT / 3) - (height / 2)

        self.write_text(text, xPosition, yPosition, font)

    def get_font(self, size):
        return ImageFont.truetype('Roboto-Medium.ttf', size)