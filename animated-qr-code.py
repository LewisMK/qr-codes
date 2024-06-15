# animated_qrcode.py

import segno
from urllib.request import urlopen

slts_qrcode = segno.make_qr("https://kothe.hashnode.dev")

gif_url = urlopen("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmVrbnBmMWoydXRjZndjbGp4bTRzenFrZ3Y2MGZqM2x0a2Fnd3hhOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1qB3EwE3c54A/giphy.gif")  # we get the animated gif from an online source

slts_qrcode.to_artistic(

    background = gif_url,
    target = "animated_qrcode.gif",  #note that the save name has a .gif extension
    scale = 5,
)