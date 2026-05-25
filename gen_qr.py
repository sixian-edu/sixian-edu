"""Generate QR code for sixian-edu website."""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw, ImageFont

URL = 'https://sixian-edu.github.io/sixian-edu/'
OUT = r'C:\Users\21342\Desktop\sixian-edu\images\qr-website.png'

qr = qrcode.QRCode(box_size=10, border=2)
qr.add_data(URL)
qr.make(fit=True)

# Generate with rounded modules and brand colors
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask((200,100,100),(26,26,46)),
)
img = img.convert('RGB')

# Add white padding
final = Image.new('RGB', (img.width+40, img.height+80), 'white')
final.paste(img, (20, 20))

# Add text
draw = ImageDraw.Draw(final)
try:
    font = ImageFont.truetype('msyh.ttc', 18)
except:
    font = ImageFont.load_default()
text = '思贤学习站'
tw = draw.textlength(text, font=font)
draw.text(((final.width-tw)/2, final.height-35), text, fill='#1a1a2e', font=font)

final.save(OUT, 'PNG')
print(f'Saved to {OUT}')
