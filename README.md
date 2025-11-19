# OCR Experiments Repository

Here you can work on try to update the ocr feature from our platform. All experiments will be divided on jupyter notebooks and every notebook will be well documented to help your work!

## Table of Contents
1. [Work Environment](#create-your-work-environment)
2. [Repository Tree Structure](#repository-tree-structure)
3. [Table of Experiments](#table-of-experiments)

## Create your Work Environment

Before all instructions, you need the tesseract-ocr package installed on your local machine. Please see this [link](https://tesseract-ocr.github.io/tessdoc/Installation.html).

Please, you will need python to work on this repository, a python environment manager is recommended ([venv](https://docs.python.org/pt-br/3/library/venv.html) or [anaconda/miniconda](https://www.anaconda.com/download/success)).

Python version (used by the repository author): 3.11.

After that, you just need (on repository root dir):

```
bash
pip install -r requirements
```

## Repository Tree Structure 

```
.
├── data // data dir (input and output root dir to any experiment)
│   ├── .keep
├── experiments // experiments dir
│   ├── evaluation.ipynb // text extraction evaluation (TODO)
│   ├── ocr.ipynb // using ocr to extract text from images
│   └── pre-processing.ipynb // pre process images to future ocr usage
├── .env.example // .env.example to configure experimentation
├── README.md // This file
├── requirements.txt // pip requirements.
└── src // source code and logic code
    ├── interfaces.py // Interface to repository usage
    ├── ocr // OCR logic
    │   ├── __init__.py
    │   ├── ...
    ├── preprocess // Pre process logic
    │   ├── __init__.py
    │   ├── ...
    └── settings.py // Environment variables 
```

## Table of Experiments

<center>

<table>
  <tr>
    <th>Experiment</th>
    <th>How use it</th>
  </tr>
  <tr>
    <td>OCR.ipynb</td>
    <td>
        You will test a new ocr algorithm code from source dir.<br> 
        You can change the OCR engine (don't use tesseract)
    </td>
  </tr>
  <tr>
    <td>Pre-processing.ipynb</td>
    <td>
        You will test a new pre process algorithm code from source dir <br>
        You can change the pre process engine (don't use Open Cv)
    </td>
  </tr>
</table>

</center>