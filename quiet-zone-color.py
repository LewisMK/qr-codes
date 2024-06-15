import segno

qr_code = segno.make_qr("Lewis Kothe")

qr_code.save(
    'my-name-quiet-zone-color.png',
    scale = 5,
    dark = 'blue',
    quiet_zone = "green",
)








