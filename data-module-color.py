import segno

qr_code = segno.make_qr("Lewis Kothe")

qr_code.save(
    'my-name-data-module-color.png',
    scale = 5,
    dark = 'blue',
    quiet_zone = "green",
    data_dark = "red",
    data_light = "yellow"
)








