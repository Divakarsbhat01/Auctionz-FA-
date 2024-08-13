import pymongo # type: ignore

mongoConnectionUrl ="mongodb://localhost:27017/"
conn = pymongo.MongoClient()
db = conn.AuctionZ
user_login_var = db.user_login #Here spam is my collection
user_id_counter_var=db.user_id_counter
pAB=db.ProductsandBidders