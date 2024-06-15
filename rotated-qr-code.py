# install pillow and qrcode-artistic modules

import segno


qr_code = segno.make_qr("Lewis Kothe")

qr_code_rotated = qr_code.to_pil(
    scale=5,
    light="lightblue",
    dark="green",
).rotate(45, expand=True)   # the expand argument enables you to keep the whole image during rotation

qr_code_rotated.save("rotated_qrcode_my_name.png")







