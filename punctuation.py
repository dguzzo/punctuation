import string
import sys
from PIL import Image, ImageFont, ImageDraw

## VARIABLES
# size of output canvas in pixels
canvasHeight = 8000;
canvasWidth = 8000;

# pixel border width
trim = 100;

font1size = 48;
font2size = 72;

# number of symbols to be output on each line
symbolsPerLine = 70;
# and the number of lines
linesOfText = 70;

# symbolsPerLine = int(math.floor(math.sqrt(len(punct))));
# linesOfText = int(math.floor(len(punct)/symbolsPerLine));


if (len(sys.argv) > 1):
   bookname = sys.argv[1]
else:
   bookname = 'ulysses'

with open(bookname + '.txt','r') as file:
    txt = file.read()

include = set(string.punctuation)

def getPunctuation(text):
   return ''.join(ch for ch in text if ch in include)

punct = getPunctuation(txt);

# file = open('blood-punct.txt','w')
with open(bookname + '-punct.txt','w') as file:
    file.write(punct)

deltaW = (canvasWidth - trim*2)/symbolsPerLine
deltaH = (canvasHeight - trim*2)/linesOfText

bkgColor = (238,212,187)
bkgColor = (255,255,255)

img = Image.new("RGB", [canvasWidth,canvasHeight], bkgColor)
draw = ImageDraw.Draw(img)
# font from (SEE LICENSE!): http://www.fontsquirrel.com/fonts/glacial-indifference
font1 = ImageFont.truetype("GlacialIndifference-Bold.otf", font1size)
font2 = ImageFont.truetype("GlacialIndifference-Bold.otf", font2size)

# transitionFill = (0,0,0);
# endSentenceFill = (125,0,0);
# parentheticalFill = (235,235,235);

# in case you want to change by transition
transitionFill = (0,0,0);
endSentenceFill = (0,0,0);
parentheticalFill = (0,0,0);

# getTextSize
for ii in range(linesOfText):
   for jj in range(symbolsPerLine):
      symb = punct[jj + ii*symbolsPerLine]
      if (symb == '.'):
         draw.text((trim + jj*deltaW,trim + ii*deltaH - round(font2size/4)), symb,fill=endSentenceFill,font=font2)
      elif (symb == ','):
         draw.text((trim + jj*deltaW,trim + ii*deltaH - round(font2size/4)), symb,fill=transitionFill,font=font2)
      elif (symb == '!') or (symb == '?'):
         draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill=endSentenceFill,font=font2)
      elif (symb == '"') or (symb == '\'') or (symb == '(') or (symb == ')') or (symb == '[') or (symb == ']'):
         draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill=parentheticalFill,font=font2)
      elif (symb == ';') or (symb == '-') or (symb == ':'):
         draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill=transitionFill,font=font2)
      else:
         draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill="green",font=font2)

img.save(bookname + '.png')

print(len(punct))