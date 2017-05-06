# Image-Watermarker
Application for automatically watermarking multiple images created in Python 3.

While working on a website for a client, we decided to physically watermark every image that was being used. 
Now, to do this manually would have took quite a lot of time for something that was, overall, pretty simple.
So, I thought maybe I could come up with an algorithm to just automatically watermark all of the images for me, resulting in this.

The program allows users to select a folder of images, where they can specify the file type of the images in the folder, and then
select the watermark that they wish to apply to all of the images in that folder. The program will calculate the best dimensions
for the watermark relative to the dimensions of the image so that the watermark fits well regardless of size and orientation.

This application is rather bare-bones, as it was primarily made to just get my job done. I've re-purposed it somewhat and made it
slightly more user-friendly, but there's still plenty more that could be added in future if I ever felt like coming back to it.
