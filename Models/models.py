from Database.mysqlDatabaseConfig import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class auctioneerDetails(Base):
    __tablename__="auctioneer_details"
    id=Column(Integer,primary_key=True,nullable=False)
    first_name=Column(String(255),nullable=False)
    last_name=Column(String(255),nullable=False)
    email=Column(String(255),nullable=False)
    code=Column(Integer,nullable=False)
    country=Column(String(255),nullable=False)
    city=Column(String(255),nullable=False)
    state=Column(String(255),nullable=False)
    phone=Column(Integer,nullable=False)
    verified=Column(Boolean,nullable=False)
    blocked=Column(Boolean,nullable=False)

class bidderDetails(Base):
    __tablename__="bidder_details"
    id=Column(Integer,primary_key=True,nullable=False)
    first_name=Column(String(255),nullable=False)
    last_name=Column(String(255),nullable=False)
    email=Column(String(255),nullable=False)
    code=Column(Integer,nullable=False)
    country=Column(String(255),nullable=False)
    city=Column(String(255),nullable=False)
    state=Column(String(255),nullable=False)
    phone=Column(Integer,nullable=False)
    verified=Column(Boolean,nullable=False)
    blocked=Column(Boolean,nullable=False)

class productDetails(Base):
    __tablename__="product_details"
    id=Column(Integer,primary_key=True,nullable=False)
    product_category=Column(String(255),nullable=False)
    product_name=Column(String(255),nullable=False)
    product_opening_value=Column(String(255),nullable=False)
    short_description=Column(String(255),nullable=False)
    auctioned_by=Column(Integer,ForeignKey("auctioneer_details.id",ondelete="CASCADE"),nullable=False)

class postAuction(Base):
    __tablename__="post_auction"
    id=Column(Integer,primary_key=True,nullable=False)
    opening_price=Column(Integer,nullable=False)
    closing_price=Column(Integer,nullable=False)
    auctioneer_id=Column(Integer,ForeignKey("auctioneer_details.id",ondelete="CASCADE"),nullable=False)
    bidder_id=Column(Integer,ForeignKey("bidder_details.id",ondelete="CASCADE"),nullable=False)
    product_id=Column(Integer,ForeignKey("product_details.id",ondelete="CASCADE"),nullable=False)

class productBidder(Base):
    __tablename__="product_bidder"
    b_id=Column(Integer,primary_key=True,nullable=False)
    p_id=Column(Integer,ForeignKey("product_details.id",ondelete="CASCADE"),primary_key=True,nullable=False)