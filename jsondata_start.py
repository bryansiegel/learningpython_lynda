import urllib.request
import json


def printResults(data):
    the_json = json.loads(data)
    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"])

    count = the_json["metadata"]["count"]
    print(str(count) + " events recorded")
    for i in the_json["features"]:
        print(i["properties"]["place"])

    for i in the_json["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("--------------------")

# felt
    for i in the_json["features"]:
        felt_reports = i["properties"]["felt"]
        if felt_reports is not None:
            if felt_reports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"]," reported" % i["properties"]["felt"])


urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"

webUrl = urllib.request.urlopen(urlData)
print("result code" + str(webUrl.getcode()))
if webUrl.getcode() == 200:
    data = webUrl.read()
    printResults(data)
else:
    print("cannot print results")
