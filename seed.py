from app import db
from models import Image, Video

import os

def runSeed():
    db.drop_all()
    db.create_all()
    contact_files = os.listdir('static/images/contact_imgs')
    # print(contact_files)
    designs_logos_files = os.listdir('static/images/designs_logos_imgs')
    # print(designs_logos_files)
    scanner_1_files = os.listdir('static/images/scanner_1_imgs')
    # print(scanner_1_files)
    p_2020_files = os.listdir('static/images/photography_2020_imgs')
    # print(p_2020_files)
    p_2019_files = os.listdir('static/images/photography_2019_imgs')
    # print(p_2019_files)
    p_2018_files = os.listdir('static/images/photography_2018_imgs')
    # print(p_2018_files)
    p_2017_files = os.listdir('static/images/photography_2017_imgs')
    # print(p_2017_files)
    p_2016_files = os.listdir('static/images/photography_2016_imgs')
    # print(p_2016_files)
    music_video_files = os.listdir('static/videos/music_videos')
    # print(music_video_files)
    water_video_files = os.listdir('static/videos/water_videos')
    # print(water_video_files)
    beauty_virtue_video_files = os.listdir('static/videos/beauty_and_virtue_videos')
    # print(beauty_virtue_video_files)
    

    contact_files_descriptions = {}
    designs_logos_files_descriptions = {"Beauty Mag Cover Zero Avenue2.png": "For Feature Film 'Zero Avenue' - Magazine",
    "Unlocking the Sidepocket Full-Recovered222.png": "In Collaboration with Jeremy Kleiman"}
    scanner_1_files_descriptions = {}
    p_2020_files_descriptions = {"UTLDNG-1.jpg": "For Nate G's 'Rain Kids' Cover"}
    p_2019_files_descriptions = {}
    p_2018_files_descriptions = {"bwminolta-14.jpg": "For Nate G's 'Seedlings' single"}
    p_2017_files_descriptions = {}
    p_2016_files_descriptions = {}

    music_video_headers = {}
    music_video_footers = {}
    water_video_headers = {}
    water_video_footers = {}
    beauty_virtue_video_headers = {}
    beauty_virtue_video_footers = {}

    for file in contact_files:
        contact_files_descriptions[file] = ""
    for file in designs_logos_files:
        if file not in designs_logos_files_descriptions:
             designs_logos_files_descriptions[file] = ""
    for file in scanner_1_files:
        scanner_1_files_descriptions[file] = "In collaboration with Brett Reuben"
    for file in p_2020_files:
        if file not in p_2020_files_descriptions:
             p_2020_files_descriptions[file] = ""
    for file in p_2019_files:
        p_2019_files_descriptions[file] = ""
    for file in p_2018_files:
        if file not in p_2018_files_descriptions:
             p_2018_files_descriptions[file] = ""
    for file in p_2017_files:
        p_2017_files_descriptions[file] = ""
    for file in p_2016_files:
        p_2016_files_descriptions[file] = ""

    music_video_headers['angel_pose_embed.txt'] = "Angel Pose MV"
    music_video_footers['angel_pose_embed.txt'] = "Video, Editing and Design by Nicholas Griffo"
    music_video_headers['pink_sunset.mp4'] = "Pink Sunset MV"
    music_video_footers['pink_sunset.mp4'] = "Video by Josh Thomas & Nicholas Griffo, Editing and Design by Nicholas Griffo"
    music_video_headers['stereo.mp4'] = "Stereo MV"
    music_video_footers['stereo.mp4'] = "Video, Editing and Design by Nicholas Griffo"
    
    for video in water_video_files:
        water_video_headers[video] = None
        water_video_footers[video] = None
    
    for video in beauty_virtue_video_files:
        beauty_virtue_video_headers[video] = "Beauty & Virtue Public Access Channel 8 - NYC 8Ball TV"
        beauty_virtue_video_footers[video] = "http://8balltv.club/"
    
    Image.add_all_imgs(contact_files, 'images/contact_imgs', contact_files_descriptions)
    Image.add_all_imgs(designs_logos_files, 'images/designs_logos_imgs', designs_logos_files_descriptions)
    Image.add_all_imgs(scanner_1_files, 'images/scanner_1_imgs', scanner_1_files_descriptions)
    Image.add_all_imgs(p_2020_files, 'images/photography_2020_imgs', p_2020_files_descriptions)
    Image.add_all_imgs(p_2019_files, 'images/photography_2019_imgs', p_2019_files_descriptions)
    Image.add_all_imgs(p_2018_files, 'images/photography_2018_imgs', p_2018_files_descriptions)
    Image.add_all_imgs(p_2017_files, 'images/photography_2017_imgs', p_2017_files_descriptions)
    Image.add_all_imgs(p_2016_files, 'images/photography_2016_imgs', p_2016_files_descriptions)
    Video.add_all_vids(music_video_files, 'images/music_videos', music_video_headers, music_video_footers)
    Video.add_all_vids(water_video_files, 'images/water_videos', water_video_headers, water_video_footers)
    Video.add_all_vids(beauty_virtue_video_files, 'images/beauty_and_virtue_videos', beauty_virtue_video_headers, beauty_virtue_video_footers)
    
    db.session.commit()