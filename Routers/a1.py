from fastapi import APIRouter, Depends
from Models import models
from sqlalchemy.orm import Session 
from Database import mysqlDatabaseConfig
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sqlalchemy import func
router=APIRouter()
@router.get("/all_count")
def student_course(db:Session=Depends(mysqlDatabaseConfig.get_db)):
    x=["Auctioneers","Bidders"]
    y=[]
    z=reasult=db.query(models.auctioneerDetails).count()
    y.append(z)
    z=reasult=db.query(models.bidderDetails).count()
    y.append(z)
    x=plt.bar(x,y)
    plt.xlabel("Type of People") 
    plt.ylabel("No of People") 
    plt.title("Count of Auctioneers and Bidders") 
    plt.grid(True)
    plt.savefig('C:/Users/Divakar/Desktop/figures/count_of_all.png')
    plt.close()

@router.get("/auctioneer_count_by_country")
def student_course(db:Session=Depends(mysqlDatabaseConfig.get_db)):
    reasult=db.query(models.auctioneerDetails,models.auctioneerDetails.country,
                       func.count(models.auctioneerDetails.first_name)).group_by(models.auctioneerDetails.country).all()
    country=[]
    people=[]
    for i in reasult:
        country.append(i[1])
        people.append(i[2])
    x=plt.bar(country,people,width = 0.4)
    plt.xlabel("Country") 
    plt.ylabel("No of People") 
    plt.title("Auctioneers by Country") 
    plt.grid(True) 
    plt.savefig('C:/Users/Divakar/Desktop/figures/auctioneers_by_country.png')
    plt.close()

@router.get("/bidder_count_by_country")
def student_course(db:Session=Depends(mysqlDatabaseConfig.get_db)):
    reasult=db.query(models.bidderDetails,models.bidderDetails.country,
                       func.count(models.bidderDetails.first_name)).group_by(models.bidderDetails.country).all()
    country=[]
    people=[]
    for i in reasult:
        country.append(i[1])
        people.append(i[2])
    x=plt.bar(country,people,width = 0.4)
    plt.xlabel("Country") 
    plt.ylabel("No of People") 
    plt.title("Bidders by Country") 
    plt.grid(True) 
    plt.savefig('C:/Users/Divakar/Desktop/figures/bidders_by_country.png')
    plt.close()