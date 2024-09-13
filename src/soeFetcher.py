import datetime as dt
import requests


def fetchSoeFromCsv(reqDt: dt.datetime, baseUrl: str) -> list[object]:
    soeFileName = f"SOE_{reqDt.strftime('%d%m%Y')}.csv"
    soeFileUrl = '/'.join(s.strip('/') for s in [baseUrl, soeFileName])

    res = requests.get(soeFileUrl)

    # check the response status code
    if not res.status_code == 200:
        print("The soe file URL is not accessible...")
        return []

    soeFileLines = res.text.splitlines()
    numSoeFileLines = len(soeFileLines)

    if numSoeFileLines < 4:
        print(f"only {numSoeFileLines} present in SOE file")
        return []

    # get headings from first line
    # soeFileHeaders = [x.strip() for x in soeFileLines[0].split(",")]

    # reject 1st, 2nd, last, last but one line
    soeFileLines = soeFileLines[2:-2]
    # print(soeFileLines)

    # get objects from rest of the lines
    soeRecords = []
    for l in soeFileLines:
        recordVals = [x.strip() for x in l.split(",")]
        area = recordVals[0]
        category = recordVals[1]
        location = recordVals[2]
        text = recordVals[3]
        compId = recordVals[4]

        fieldDateStr = recordVals[5]
        fieldTimeStr = recordVals[6]
        fieldTimeNs = int(recordVals[7])
        fieldDt = dt.datetime.strptime(f"{fieldDateStr} {
                                       fieldTimeStr}", "%d-%m-%Y %H:%M:%S") + dt.timedelta(microseconds=int(fieldTimeNs/1000))

        reportingTime = dt.datetime.strptime(
            recordVals[8]+"000", "%Y-%m-%d %H:%M:%S.%f")

        recordObj = {
            "source": "SCADA",
            "area": area,
            "category": category,
            "location": location,
            "text": text,
            "compId": compId,
            "fieldTime": fieldDt,
            "@timestamp": reportingTime
        }
        # recordId = hash(frozenset(recordObj.items()))
        # recordObj["_id"] = recordId
        soeRecords.append(recordObj)
    return soeRecords
