import storm
import json
import pymongo
from bson import json_util


def connectDB():
    try:
        connection = pymongo.MongoClient('mongodb://172.25.33.205:27017')
        database = connection['testdb']
    except Exception as e:
        print('Error: Unable to Connect: ', e)
        connection = None

    return connection, database


def convertHexToDec(hexString):
    hexNumber = hexString
    decNumber = int(hexNumber, 16)
    return decNumber


def getTimeValue(timestamp, entity, database):

    doc = database[entity].find_one({'Time': timestamp})
    doc = json.dumps(doc, sort_keys=True,
                     indent=4, default=json_util.default)

    data = json.loads(doc)
    if data != None:
        storm.logInfo(
            "-------------------------------------------------------------------> ", data["Value"])
        return data["Value"]
    else:
        storm.logInfo("-------> 0"+str(timestamp))
        return 0


class SplitBolt(storm.BasicBolt):
    # There's nothing to initialize here,
    # since this is just a split and emit
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        storm.logInfo("Block-processing bolt instance starting...")
        self.connection,  self.database = connectDB()
        self.i = 0

    def process(self, tup):
        # Process block data here
        self.i = self.i+1

        if self.connection != None:

            if tup != None:

                data = tup.values[0]
                data = json.loads(data)
                data = json.loads(data)
                blockData = data["result"]

                # add decimal of hex number
                # blockData["blockNumber"] = str(
                #     convertHexToDec(blockData["number"]))

                # # adding decimal timestamp
                # blockData["timestamp"] = str(
                #     convertHexToDec(blockData["timestamp"]))

                # add btc

                # blockData["BTCValue"] = str(getTimeValue(
                #     int(blockData["timestamp"]), "pricebtc", self.database))
                # blockData["USDValue"] = str(getTimeValue(
                #     int(blockData["timestamp"]), "priceusd", self.database))
                # blockData["USDVolume"] = str(getTimeValue(
                #     int(blockData["timestamp"]), "volumeusd", self.database))
                # blockData["MarketCAP"] = str(getTimeValue(
                #     int(blockData["timestamp"]), "cap", self.database))

                storm.logInfo("Emitting from Block BOLT" + str(self.i))
                #     storm.emit([word])
                storm.emit([blockData])
            else:
                storm.logInfo("None Tuple Detected from Block BOLT")
        else:
            storm.logInfo("Mongo Connection Died from Block BOLT")



# Start the bolt when it's invoked
SplitBolt().run()
