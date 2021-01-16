# Nick Griffo's Website

## Videos & Images

I had to take out the `videos/` and `images/` folders in order to push to GitHub.

### Videos:
Can be found [here](https://drive.google.com/drive/folders/1cJS3njcyLIe5PUtFPSb-rNPFDRMbOLl1)

### Images:
Can be found [here](https://drive.google.com/drive/folders/1zqT2bEmt2N5K0xk_LFi61xnRuMssPKWU)

* Once downloaded, make sure to move the `videos/` folder as well as the `images/` folder into the `static/` folder, which lies within the root directory

## Installation

Make sure you are in the root directory for the project, which contains:

`app.py`\
`models.py`\
`requirements.txt`\
`seed.py`\
`static/`\
`templates/`\
`venv/`

Create virtual environment (venv):

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

Use the package manager [pip3](https://pip3.pypa.io/en/stable/) to install dependencies.

```bash
pip3 install flask
pip3 install flask_debug_toolbar
pip3 install flask_sqlalchemy
pip3 install psycopg2
```

## Run

Make sure you are in the root directory for the project, and then run the following command:

```bash
python3 -m flask run
```
