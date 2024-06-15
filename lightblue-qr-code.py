import segno

qr_code = segno.make_qr("Lewis Kothe")

qr_code.save(
    'my-name-lightblue.png',
    scale = 5,
    border = 5,
    light = 'lightblue',
)



