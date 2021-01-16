from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

import os

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    filename = db.Column(db.Text, nullable=False)
    folder = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)

    @classmethod
    def add_all_imgs(cls, imgs, folder, descriptions):
        for img in imgs:
            if (img != '.DS_Store'):
                if not img.endswith('.tif'):
                    description = descriptions[img]
                    new_img = Image(filename=img, folder=folder, description=description)
                    db.session.add(new_img)

    @classmethod
    def serialize(cls, img):
        return {
            'filename': img.filename,
            'folder': img.folder,
            'description': img.description
        }

class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    filename = db.Column(db.Text, nullable=False)
    folder = db.Column(db.Text, nullable=False)
    embed = db.Column(db.Text)
    extension = db.Column(db.Text)
    header = db.Column(db.Text)
    footer = db.Column(db.Text)

    @classmethod
    def getEmbedText(cls, filename):
        f = open(filename, "r")
        return f.read()
    

    @classmethod
    def add_all_vids(cls, vids, folder, headers, footers):
        for vid in vids:
            if (vid != '.DS_Store'):
                if "embed" in vid:
                    embed = cls.getEmbedText(f'./static/videos/{folder}/{vid}')
                    header = headers[vid]
                    footer = footers[vid]
                    new_vid= Video(filename=vid, folder=folder, embed=f'{embed}', header=header, footer=footer)
                    db.session.add(new_vid)
                else:
                    extension = os.path.splitext(vid)[1][1:].lower()
                    header = headers[vid]
                    footer = footers[vid]
                    new_vid= Video(filename=vid, folder=folder, extension=extension, header=header, footer=footer)
                    db.session.add(new_vid)

    @classmethod
    def serialize(cls, vid):
        return {
            'filename': vid.filename,
            "folder": vid.folder,
            'embed': vid.embed,
            'extension': vid.extension,
            'header': vid.header,
            'footer': vid.footer
        }

