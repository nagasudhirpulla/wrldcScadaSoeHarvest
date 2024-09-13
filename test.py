from src.soeFetcher import fetchSoeFromCsv
import datetime as dt
from src.jsonConfig import loadJsonConfig

conf = loadJsonConfig()

reqDt = dt.datetime.now()-dt.timedelta(days=conf.daysOffset)
soeRecords = fetchSoeFromCsv(reqDt, conf.soeFilesBaseUrl)