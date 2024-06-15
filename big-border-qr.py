import segno

qr_code = segno.make_qr("Lewis Kothe")

qr_code.save(
    'my-name-bigger-border.png',
    scale = 5,
    border = 10,
)



