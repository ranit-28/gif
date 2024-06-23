from moviepy.editor import *

vd=VideoFileClip("assesment/video.mp4").subclip(00,5)
vd.write_gif("vd2.gif")