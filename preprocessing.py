'''
python3 watch_file.py -p1 python3 preprocessing.py data/contract_small.jpeg -d .
'''
import pytesseract
from PIL import Image
import sys
import base64

def ocr_to_text(fileName: str) -> str:

    img=Image.open(fileName)
    st=pytesseract.image_to_string(img)

    return st


def encode_image(imageFile):

    with open(imageFile, "rb") as f:

        return base64.b64encode(f.read()).decode("utf-8")


def image_url(imageFile):

    encoding=encode_image(imageFile)
    imageString=f'data:image/jpeg;base64,{encoding}'
    
    return imageString


if __name__=='__main__':

    r=ocr_to_text(sys.argv[1])

    print(r)

    r=encode_image(sys.argv[1])

    print(r[:100])

    r=image_url(sys.argv[1])

    print(r[:100])
