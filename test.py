from soeFetcher import fetchSoeFromCsv
import datetime as dt
from jsonConfig import loadJsonConfig

conf = loadJsonConfig()

reqDt = dt.datetime.now()-dt.timedelta(days=conf.daysOffset)
soeRecords = fetchSoeFromCsv(reqDt, conf.soeFilesBaseUrl)