import model
from sqlalchemy import create_engine

USER = 'ckan'
PASS = 'Cotesa2016'

alchemyurl = 'postgresql://%s:%s@srvbbdd.es/ckan' % (USER, PASS)

print 'Creating table for SPARQL endpoint storage'
engine = create_engine(alchemyurl, echo=True)
model.metadata.drop_all(engine)
model.metadata.create_all(engine)
