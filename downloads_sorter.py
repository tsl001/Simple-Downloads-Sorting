import shutil
import subprocess
import os
import argparse
from time import sleep

def move_images(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.jpg') or item.endswith('.jpeg') or item.endswith('.png') or item.endswith('.gif'):
            if not os.path.exists(HOME_DIR + '/Image Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Image Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Image Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('Images done moving')

def move_documents(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.docx') or item.endswith('.doc'):
            if not os.path.exists(HOME_DIR + '/Document Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Document Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Document Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('Documents done moving')

def move_music(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.mp3') or item.endswith('.wav'):
            if not os.path.exists(HOME_DIR + '/Music Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Music Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Music Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('Music done moving')

def move_compressed(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.zip') or item.endswith('.7z'):
            if not os.path.exists(HOME_DIR + '/Compressed Files Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Compressed Files Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Compressed Files Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('Compressed files done moving')

def move_powerpoint(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.pptx') or item.endswith('.ppt'):
            if not os.path.exists(HOME_DIR + '/Powerpoint Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Powerpoint Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Powerpoint Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('Powerpoint files done moving')

def move_apps(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.app'):
            if not os.path.exists(HOME_DIR + '/App Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/App Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/App Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('App files done moving')

def move_videos(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.mp4') or item.endswith('.mkv') or item.endswith('.mlv') or item.endswith('.MOV'):
            if not os.path.exists(HOME_DIR + '/Video Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Video Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Video Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('Video files done moving')

def move_texts(sourcefiles,sourcepath):
    for item in sourcefiles:
        if item.endswith('.txt'):
            if not os.path.exists(HOME_DIR + '/Text Downloads/' + item):
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Text Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,item),HOME_DIR + '/Text Downloads/copy ' + item)

    if args.DEBUG == 1:
        print('Text files done moving')


parser = argparse.ArgumentParser()
parser.add_argument('--DEBUG',type=int,default=0,help='Will print when files are done moving if set to 1')
args = parser.parse_args()

HOME_DIR = subprocess.getoutput('cd ~ ; pwd')
KNOWN_TYPES = ['png','jpg','mp4','mp3','gif','mlv','app','zip','7z','pptx','wav','docx','doc']

if not os.path.exists(HOME_DIR + '/PDF Downloads/'):
    subprocess.Popen('mkdir ~/PDF\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Text Downloads/'):
    subprocess.Popen('mkdir ~/Text\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Image Downloads/'):
    subprocess.Popen('mkdir ~/Image\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Document Downloads/'):
    subprocess.Popen('mkdir ~/Document\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Powerpoint Downloads/'):
    subprocess.Popen('mkdir ~/Powerpoint\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Music Downloads/'):
    subprocess.Popen('mkdir ~/Music\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Compressed Files Downloads/'):
    subprocess.Popen('mkdir ~/Compressed\\ Files\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/App Downloads/'):
    subprocess.Popen('mkdir ~/App\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Video Downloads/'):
    subprocess.Popen('mkdir ~/Video\\ Downloads',shell=True).wait()

if not os.path.exists(HOME_DIR + '/Misc. Downloads/'):
    subprocess.Popen('mkdir ~/Misc.\\ Downloads',shell=True).wait()

#Move respective files from Downloads folder to their respective downloads folder
sourcepath = HOME_DIR + '/Downloads/'

while True:
    sourcefiles = os.listdir(sourcepath)

    for f in sourcefiles:
        if f.endswith('.pdf'):
            if not os.path.exists(HOME_DIR + '/PDF Downloads/' + f.split('/')[-1]):
                shutil.move(os.path.join(sourcepath,f),HOME_DIR + '/PDF Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,f),HOME_DIR + '/PDF Downloads/copy ' + f)

    if args.DEBUG == 1:
        print('PDFs done moving')

    move_compressed(sourcefiles,sourcepath)
    move_documents(sourcefiles,sourcepath)
    move_images(sourcefiles,sourcepath)
    move_music(sourcefiles,sourcepath)
    move_powerpoint(sourcefiles,sourcepath)
    move_apps(sourcefiles,sourcepath)
    move_videos(sourcefiles,sourcepath)
    move_texts(sourcefiles,sourcepath)

    sourcefiles = os.listdir(sourcepath)

    for f in sourcefiles:
        if not f.endswith('.download'):
            if not os.path.exists(HOME_DIR + '/Misc. Downloads/' + f.split('/')[-1]):
                shutil.move(os.path.join(sourcepath,f),HOME_DIR + '/Misc. Downloads/')
            else:
                shutil.move(os.path.join(sourcepath,f),HOME_DIR + '/Misc. Downloads/copy ' + f)
    sleep(10) #run every 5 seconds

