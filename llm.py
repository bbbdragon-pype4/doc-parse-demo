'''
python3 watch_file.py -p1 python3 llm.py data/contract_small.jpeg -d .
'''
import openai
from dotenv import load_dotenv
import os
import sys
from pydantic import BaseModel
from schema import Contract
from typing import List,Dict
from preprocessing import ocr_to_text,encode_image,image_url
from queries import SYSTEM_QUERY,USER_IMAGE_QUERY,USER_HYBRID_QUERY

load_dotenv()

#############
# CONSTANTS #
#############

OPENAI_API_KEY=os.environ['OPENAI_KEY']
OPENAI_MODEL=os.environ['OPENAI_MODEL']
CLIENT=openai.OpenAI(api_key=OPENAI_API_KEY)


###################
# QUERY FUNCTIONS #
###################

def submit_messages(messages: List[Dict],
                    client: openai.OpenAI = CLIENT,
                    model: str = OPENAI_MODEL,
                    schema: BaseModel = Contract,
                   ) -> Contract:

    r=client.chat.completions.parse(model=model,
                                    messages=messages,
                                    response_format=schema,
                                   )

    parsed=r.choices[0].message.parsed
    js=parsed.model_dump()

    return js


def submit_text_query(text: str,
                      systemQuery: str = SYSTEM_QUERY,
                     ) -> Contract:

    messages=[{'role':'system', 
               'content':systemQuery,
              },
              {'role':'user',
               'content':text,
              }]
    r=submit_messages(messages)

    return r


def submit_ocr_query(fileName: str) -> Contract:

    text=ocr_to_text(fileName)
    r=submit_text_query(text)

    return r


def submit_image_buffer_query(fileName: str,
                              systemQuery: str = SYSTEM_QUERY,
                              userImageQuery: str = USER_IMAGE_QUERY,
                             ) -> Contract:

    imageURL=image_url(fileName)
    messages=[{'role':'system', 
               'content':systemQuery,
              },
              {'role':'user',
               'content':[{'type':'text',
                           'text':userImageQuery,
                          },
                          {'type':'image_url',
                           'image_url':{'url':imageURL},
                          }],
              }]
    r=submit_messages(messages)

    return r


def submit_hybrid_query(fileName: str,
                        systemQuery: str = SYSTEM_QUERY,
                        hybridQuery: str = USER_HYBRID_QUERY,
                       ):

    text=ocr_to_text(fileName)
    imageURL=image_url(fileName)
    messages=[{'role':'system', 
               'content':systemQuery,
              },
              {'role':'user',
               'content':[{'type':'text',
                           'text':hybridQuery,
                          },
                          {'type':'text',
                           'text':text,
                          },
                          {'type':'image_url',
                           'image_url':{'url':imageURL},
                          }],
              }]
    r=submit_messages(messages)

    return r
    

if __name__=='__main__':

    print('*'*30)
    print('OCR TO TEXT TO LLM')

    r=submit_ocr_query(sys.argv[1])

    print(r.model_dump_json(indent=2))

    print('*'*30)
    print('IMAGE TO LLM')

    r=submit_image_buffer_query(sys.argv[1])

    print(r.model_dump_json(indent=2))
    
    print('*'*30)
    print('IMAGE AND TEXT (hybrid) TO LLM')

    r=submit_hybrid_query(sys.argv[1])

    print(r.model_dump_json(indent=2))
    
