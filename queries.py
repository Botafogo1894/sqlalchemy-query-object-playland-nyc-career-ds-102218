import pandas as pd
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    main_category = Column(String)
    currency = Column(String)
    deadline = Column(Date)
    goal = Column(Float)
    launched = Column(Date)
    pledged = Column(Float)
    state = Column(String)
    backers = Column(Integer)
    country = Column(String)

engine = create_engine('sqlite:///kickstarter.db')

# chunks = pd.read_csv('./ks-projects-201801.csv')
# chunks.to_sql(name='projects', if_exists='append', con=engine)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


## Query Challenges

# 1. query the database with sqlalchemy to find the project named 'Beach Wrestling Documentary'
#     - set the variable `beach_wresting_documentary` equal to the result of this query
beach_wresting_documentary = session.query(Project).filter(Project.name == "Beach Wrestling Documentary").first()

print(beach_wresting_documentary.goal)
print(beach_wresting_documentary.backers)
print(beach_wresting_documentary.state)


# 2. collect a list of projects whose states are equal to 'successful'
successful = session.query(Project).filter(Project.state == "successful").all()
print(len(successful))
# 3. collect a list of projects whose pledged amounts are greater than or equal to their goal amounts
pledged = session.query(Project)filter(Proejct.pledged => Project.goal).all()
len(pledged) == len(successful)
#
# 4. Which project has the highest number of backers?
#
# 5. collect a list of `main_category`s and each of their respective average `pledge`s
#     - **BONUS**: rewrite the query to order the returned list by highest average pledge to lowest
#
# **Challenge**
#
# 6. Which country has the highest percentage of successful projects?
#
#
# 7. Plot a histogram for the number of items in each main_category.
#
#
# 8. Is there a correlation between time of year and whether or not your project will be successfully backed? Investigate!
