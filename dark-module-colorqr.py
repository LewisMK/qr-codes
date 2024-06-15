import segno

qr_code = segno.make_qr("Lewis Kothe")

qr_code.save(
    'my-name-dark-module-color.png',
    scale = 5,
    dark = 'blue',
)



