import tweepy
import time
from PIL import Image
import glob
from datetime import datetime
from datetime import date
from random import randint


#enter in your own keys from the twitter dev site
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def post_tweet():
    today = date.today()
    releaseDate = date(2020,12, 11)
    delta = releaseDate - today

    includeMedia = spinTheWheel()
    if(includeMedia):
        pictureList= pick_media()
        numPic= len(pictureList)
        numPic = randint(0,numPic-1)
        picOfTheDay = api.media_upload(pictureList[numPic].filename)
        picID = [picOfTheDay.media_id]
        api.update_status(status = 'Bobby Shmurda will be free in ' + str(delta.days) + ' days. #freebobby',  media_ids = picID)
    else:
        api.update_status(status = 'Bobby Shmurda will be free in ' + str(delta.days) + ' days')


def pick_media():
    #picked images from a local file
        image_list = []
        for filename in glob.glob('pictures/*.jpg'):
            im=Image.open(filename)
            image_list.append(im)
        return image_list

def spinTheWheel():
    mediaValue = randint(0,2)
    if mediaValue % 2 == 0:
        print('There will be a picture')
        return True
    else:
        print('There will not be a picture')
        return False

while True:
    postTime = datetime.now().time()
    print(postTime)
    #post_tweet()
    if postTime.hour == 9 and postTime.minute == 0 and postTime.second == 0:
        post_tweet()
        print('just printed out a tweet')

    time.sleep(1)
