'''
python3 watch_file.py -p1 python3 preprocessing.py data/contract_small.jpeg -d .
'''
import pytesseract
from PIL import Image
import sys
import base64
from typing import Union

def ocr_to_text(fileName: str) -> str:
    '''
    Opens an image file and returns parsed text.
    '''
    img=Image.open(fileName)
    st=pytesseract.image_to_string(img)

    return st


def encode_image(imageFile: Union[str]) -> str:
    '''
    Returns base64 encoding (in utf-8 strings) of either an image file or a werkzeug image
    returned from the react server.
    '''
    try:

        with open(imageFile, "rb") as f:

            content=f.read()

    except Exception as e:

        content=imageFile.read()

    return base64.b64encode(content).decode("utf-8")

        

def image_url(imageFile: Union[str]) -> str:
    '''
    Helper to generate a string for the image that is consumable by the OpenAI API.
    '''
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
