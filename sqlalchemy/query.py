"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)
# or 
Brand.query.filter_by(id=8).first()
# or 
Brand.query.filter_by(id=8).one()
# or (result in a list)
Brand.query.filter_by(id=8).all()
#or 
Brand.query.filter(Brand.id==8).first()
#or 
Brand.query.filter(Brand.id==8).one()
#or 
Brand.query.filter(Brand.id==8).first()
#or
Brand.query.filter(Brand.id==8).all()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette').filter_by(brand_name='Chevrolet').all()
#or
Model.query.filter(Model.name=='Corvette').filter(Model.brand_name=='Chevrolet').all()
# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Does this mean if they have 'cor' in it ? 
#Model.query.filter(Model.name.like('%Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter((Brand.founded==1903) & (Brand.discontinued == None)).all()
#or 
Brand.query.filter(Brand.founded==1903, Brand.discontinued == None).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter((Brand.discontinued != None)|(Brand.founded < 1950)).all()
#or
Brand.query.filter(db.or_(Brand.discontinued != None, Brand.founded < 1950)).all()
#or 
Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()
#or 
Brand.query.filter((Brand.discontinued.isnot(None))|(Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()
#why does this not work
# Model.query.filter_by(brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    
    models = db.session.query(Model.name, 
                              Model.brand_name, 
                              Brand.headquarters).join(Brand).filter(Model.year == year).all()
    
    for model in models:
        print "Model: %s, Brand: %s, HQ: %s" % (model[0], model[1], model[2]) 


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
     brand_models = Brand.query.options(db.joinedload('models')).all()

     for brand in brand_models:
        print "Brand: %s" % (brand.name)
        for model in brand.models:
            print "\t%s" % (model.name)
        print "\n"
 



# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
        #<flask_sqlalchemy.BaseQuery object at 0x7fc917a5b750>
        #The datatype is a Query Object 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
    # A secondary table. There is a table in the middle that has only the purpose 
    # to serve as a connector between two other tables 
    # Many to Many

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    name_query = Brand.query.filter_by(name=mystr).all()
    return name_query


def get_models_between(start_year, end_year):
    models_between = Model.query.filter((Model.year >= start_year) & (Model.year < end_year)).all()

    return models_betweens
