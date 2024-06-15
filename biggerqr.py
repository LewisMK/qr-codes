import segno

qr_code = segno.make_qr("Lewis Kothe")

qr_code.save(
    'my-name-bigger.png',
    scale = 5,
)



