import os
import re
import random
import uvicorn
from helper import adjectives, prefixes
import gpt_2_simple as gpt2
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
origins = [
    "https://ericklarac.github.io",
    "https://aa8de9e130a7.ngrok.io",
    "http://localhost",
    "http://localhost:3000",
]

# Configure FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Init GPT-2 and tensorflow session
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')


def getPrefix(zodiac_sign, interest):
    adjective = adjectives[random.randint(0, len(adjectives)-1)]
    s = prefixes[interest][random.randint(0, len(prefixes[interest])-1)]
    return s.format(zodiac_sign, adjective)


@app.get("/")
def read_root():
    return {"text": "Astrology AI"}


@app.get("/{zodiac_sign}/{interest}")
async def get_zodiac_sign(zodiac_sign: str = "", interest: str = "careful"):
    prefix = getPrefix(zodiac_sign, interest)
    text = gpt2.generate(sess, run_name='run1', temperature=0.85,
                         prefix=prefix, nsamples=1, length=150, return_as_list=True)[0]
    text = re.sub(r'\\n', ' ', text)
    text = text[:text.rfind(".")+1]
    return {"text": text}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get('PORT', 8000))
