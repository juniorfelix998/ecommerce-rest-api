from flask import Flask
from flask_restful import Api

from resources.sellers import Sellers
from resources.products import Products
from resources.tokens import Tokens
import logging
import config

# config.configure_logging_relative('logging.ini')

logging.basicConfig(filename="ecommerce.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)

logger.info("Registering resources")
api.add_resource(Sellers, '/sellers')
api.add_resource(Products, '/products')
api.add_resource(Tokens, '/token')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
