# doc-parse-demo

Welcome to the doc parse demo.  This is an attempt to show three LLM-driven image parsing strategies for JPEG images of real estate contracts.  It is a demo only.

This is a framework for future experimentation in image parsing using LLM's.  We have three strategies available in this package:

* "OCR to LLM" - This will run the JPEG through an OCR module, extract the text, then use the OpenAI structured JSON to extract the fields to populate a Contract object.
* "LLM Image Buffer" - GPT-5 and GPT-4o have three input buffers: audio, image, and text.  This means that the LLM can consume the image and extract the fields.
* "Hybrid" - Because these LLM's have buffers for both images and text, we can extract text using an OCR, and feed both it and the image to the LLM to perform the extraction.

This will attempt not only to show how I grappled with the issue of LLM-driven document parsing, but also taught myself the basics of React.js in a very short time.

## Installation

The installation is a bit complex, and is divided into:

* installing tesseract
* installing the Python libraries
* installing the necessary components to run the React.js app

### Requirements

We are assuming you have either a Mac OS or a Linux machine with 8gb or more of RAM.  We will be using Python 3.13.1 and node.js v25.8.0.  You will need an OpenAI key, and be ready to spend a small amount running GPT-5.

### Creating .env

First, do:
```
cp dotenv_example.text .env
```
Then, open .env in a text editor and replace `key` with your OpenAI key.

### Installing tesseract

You will need to install binaries for the tesseract ocr.  If you are running on Linux, you will need to do:
```
sudo apt-get update
sudo apt-get install tesseract-ocr
```
If you are on Mac OS, you will need to do:
```
brew install tesseract
```

### Installing Python requirements

To install Python Libraries, run:
```
pip install -r requirements.txt
```

### React.js installation

We first install node.js and npm.  As this is largely OS-specific, you should look up how to do this on your own.

Then, run:
```
cd doc-parse-demo/parse-app
npm install
```

## Running

### Running python only

If you want to play with different files and approaches, you can investigate the file `llm.py` which contains code for the three approaches described above.  You can run this on a simple example, `data/contract_small.jpeg` as:
```
python llm.py contract_small.py
```
You will notice the output populates a pydantic object defined in `schema.py`, and that this object contains hierarchical objects.  You may want to expand this object on your own to include other fields.

You should be warned that both the "LLM Image Buffer" and "Hybrid" approaches are constrained by token limitations, which tend to be hit up by larger JPEG files (usually around 1mb), which means that the "OCR" approach might be the best in practice.

### Running the servers

First, ensure that ports 5000 and 5173 are free.  In one terminal, start the backend server:
```
cd doc-parse-demo
python server.py
```
In another terminal, start the frontend server:
```
cd doc-parse-demo/parse-app
npm run dev
```
You will be given a link which you can paste into your browser: `http://localhost:5173/`.

### Using the interface

In the interface, you will be asked to upload a file and select your approach.  Once you upload the file, you will need to wait until the document is parsed, and then you can view the extracted fields.

## Future work

Because of time constraints (I prepared this demo for a job interview), I cannot vouch for the stability of the React.js app.  Moreover, if we choose to use the LLM image buffer, we will need an effective strategy to carve the image into processable components.  I can also not vouch for the reliability of these approaches in production.  

Another concernn is latency.  You will notice that the runtime of these approaches is measured in tens of seconds.  For this, I strongly suggest we explore smaller LM's such as Qwen.  In my experience, they are not good at complicated tasks, but simple tasks like document processing are feasible.


