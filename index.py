from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from src.soeFetcher import fetchSoeFromCsv
import datetime as dt
from src.jsonConfig import loadJsonConfig

conf = loadJsonConfig()

reqDt = dt.datetime.now()-dt.timedelta(days=conf.daysOffset)
soeRecords = fetchSoeFromCsv(reqDt, conf.soeFilesBaseUrl)

# Create an Elasticsearch client
es = Elasticsearch(conf.esHost,
                   basic_auth=(conf.esUname, conf.esPwd))

# Define the Elasticsearch index and document type
index = conf.esSoeIndex

# Use the bulk API to insert the data
actions = [
    {"_index": index, "_op_type": "update", "doc": item,
        "doc_as_upsert": True, "_id": hash(frozenset(item.items()))}
    for item in soeRecords
]
bulk(es, actions)

print("soe data insertion complete...")
