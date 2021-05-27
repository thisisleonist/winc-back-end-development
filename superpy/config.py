# Database field definitions

BOUGHT_FILE = 'db_bought.csv'
BOUGHT_FIELDS = [
    'id',               # number, auto increment from 1
    'product_name',     # string
    'buy_date',         # date in yyyy-mm-dd
    'buy_price',        # float
    'expiration_date',  # date in yyyy-mm-dd
]

SOLD_FILE = 'db_sold.csv'
SOLD_FIELDS = [
    'id',               # number, auto increment from 1
    'bought_id',        # string
    'sell_date',        # date in yyyy-mm-dd
    'sell_price',       # float
]

DATE_FILE = 'db_date.csv'
DATE_FIELDS = [
    'date',             # date in yyyy-mm-dd
]