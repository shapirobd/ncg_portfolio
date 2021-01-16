import pdb
import os

from flask import Flask, session, request, render_template, redirect, g, flash, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Image, Video
from seed import runSeed

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///nick_griffo_db'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgres:///nick_griffo_db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "bmdcsp77210")

connect_db(app)

# toolbar = DebugToolbarExtension(app)

runSeed()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/<string:folder>')
def show_scanner_1_imgs(folder):

    if "imgs" in folder:
        imgs = Image.query.filter(Image.folder == folder).all()
        serialized_imgs = [Image.serialize(img) for img in imgs]
        resp = jsonify(imgs=serialized_imgs)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    elif "videos" in folder:
        vids = Video.query.filter(Video.folder == folder).all()
        serialized_vids = [Video.serialize(vid) for vid in vids]
        resp = jsonify(vids=serialized_vids)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

@app.route('/img/<string:filename>')
def show_img_from_index(filename):
    img = Image.query.filter(Image.filename == filename).first()
    serialized_img = Image.serialize(img)
    resp = jsonify(img=serialized_img)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/contact')
def show_contact_info():
    contact_info = {
        'email': 'virtuousboy0@gmail.com',
        'instagram': 'https://www.instagram.com/dracaenaamericana/?hl=en',
        'imdb': 'https://www.imdb.com/name/nm11881226/',
        'website': 'http://brett3.net/niconico/'
    }
    resp = jsonify(info=contact_info)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp