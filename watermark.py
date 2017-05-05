#Image Watermarker
#Written by Shaun Clift, 2017

import PIL
from PIL import Image
import glob, os, fnmatch, time, sys, tkinter
from tkinter.filedialog import askopenfilename, askdirectory

rates = []

def mark(folder, fileType, watermarkFile):

    print('Watermarking images in '+folder)
    count = 1
    #for loop counter

    #for loop that applies watermark to all images in specified folder
    for filename in glob.glob(folder+'/*.'+fileType):
        start = time.time()
        background = Image.open(filename)
        bg_w, bg_h = background.size
        #open image and get image dimensions

        img = Image.open(watermarkFile)
        #open watermark

        if (bg_h > bg_w):
            if (bg_w > 1000 and bg_w < 1500):
                img_w, img_h = img.size
                size = (img_w / 2, img_h / 2)
                img.thumbnail(size,Image.ANTIALIAS)
            elif (bg_w < 1000):
                img_w, img_h = img.size
                size = (img_w / 4, img_h / 4)
                img.thumbnail(size,Image.ANTIALIAS)
        #scale watermark down for smaller portrait images

        elif (bg_w > bg_h):
            if (bg_h > 700 and bg_h < 1500):
                img_w, img_h = img.size
                size = (img_w / 3, img_h / 3)
                img.thumbnail(size,Image.ANTIALIAS)
            elif (bg_h < 700):
                img_w, img_h = img.size
                size = (img_w / 4, img_h / 4)
                img.thumbnail(size,Image.ANTIALIAS)
        #scale watermark down for smaller landscape images

        img_w, img_h = img.size
        #get watermark dimensions

        o1 = int((bg_w - img_w) / 2)
        o2 = int((bg_h - img_h) / 2)
        #calculate watermark offset values

        background.paste(img, (o1, o2), img)
        #paste watermark onto image

        count = str(count)
        if not os.path.exists(folder):
            os.makedirs(folder)
        background.save(folder+'/'+'0'+count+'.jpg')
        #export watermarked file

        end = time.time()
        count = int(count)

        total = len(fnmatch.filter(os.listdir(folder), '*.jpg'))
        #total number of images to watermark
        bar = int((count / total) * 50)
        #bar counter value
        progress = int((count / total) * 100)
        #percentage of files watermarked
        rate = (end-start)
        #speed of watermarking
        rates.append(rate)
        #append calculated speed to rates list
        ratesb = sum(rates)
        #calculate total of all rates
        ratesb = ratesb / len(rates)
        #calculate mean speed
        left = total - count
        #how many images left to watermark
        eta = ratesb * left
        #estimated time left until all images are watermarked

        if progress < 100:
            print(str(progress)+"%  ["+"#"*bar, end="\r")
            sys.stdout.flush()
        elif progress == 100:
            print(str(progress)+"% ["+"#"*bar, end="\r")
            sys.stdout.flush()
        #print percentages and progress hashtags

        if eta < 60.00:
            print("\t\t\t\t\t\t\t] "+"%.2f" % ratesb+" img/s ETA: "+"%.2f" % eta +"s", end="\r")
            sys.stdout.flush()
        elif eta > 60.00:
            eta = eta*60
            print("\t\t\t\t\t\t\t] "+"%.2f" % ratesb+" img/s ETA: "+"%.2f" % eta +"m", end="\r")
            sys.stdout.flush()
        #print progress bar suffixes with closing bracket, speed and eta

        count = count+1
        #add on to the for loop counter

    print("\nWatermarking complete")
    exitInput = input("Do you wish to exit? (Y/N) ")
    if exitInput == "Y" or "y":
        exit()

while True:
    root = tkinter.Tk()
    root.withdraw()
    print("Please select the folder of images to watermark: ")
    folder = askdirectory()
    fileType = input("What file type are your images? (.jpg, .png...) ")
    print("Please select the watermark image to use: ")
    watermark = askopenfilename()

    mark(folder, fileType, watermark)
