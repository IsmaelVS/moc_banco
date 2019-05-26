import pyqrcode


def gerar_qrcode(uuid):
    code = pyqrcode.create('{}'.format(uuid))
    code.png('app/views/static/{}.png'.format(uuid), scale=6)
