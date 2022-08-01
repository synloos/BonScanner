# import the necessary packages
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

text_from_image = pytesseract.image_to_string(Image.open('Examples/Zettel2.jpg'))

print(text_from_image)
