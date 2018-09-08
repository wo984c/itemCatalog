from helpers import *
from handlers.online_oauth import *
from handlers.endpoint import *
from handlers.category import *
from handlers.item import *


if __name__ == '__main__':

    app.debug = False
    app.run(host='0.0.0.0', port=5000, ssl_context=('ssl/server.crt',
                                                    'ssl/server.key'))
