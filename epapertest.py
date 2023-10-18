import sys
sys.path.insert(1, "./lib")

import epd2in13b_V4 as EPaper
#import epdconfig

from PIL import Image, ImageDraw, ImageFont

epd = EPaper.EPD() # get the display
epd.init()           # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear()      # was (0xFF) clear the display
print("print text")
def BlkprintToDisplay(string, col, row):
    HBlackImage = Image.new('1', (epd.height, epd.width), 255)
    HRedImage = Image.new('1', (epd.height, epd.width), 255)
    
    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 30) # Create our font, passing in the font file and font size
    
    draw.text((col, row), string, font = font, fill = 0)
    
    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))
    

def RedprintToDisplay(string, col, row):
    HBlackImage = Image.new('1', (epd.height, epd.width), 255)
    HRedImage = Image.new('1', (epd.height, epd.width), 255)
    
    draw = ImageDraw.Draw(HRedImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 30) # Create our font, passing in the font file and font size
    
    draw.text((col ,row), string, font = font, fill = 0)
    
    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))

BlkprintToDisplay("Hello, World!", 25,65)    
epd.Clear()
RedprintToDisplay("Ciaran Doidge",10,10)
epd.sleep()
