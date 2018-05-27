import storm
import json


class SplitBolt(storm.BasicBolt):
    # There's nothing to initialize here,
    # since this is just a split and emit
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        storm.logInfo("Transaction-processing bolt instance starting...")

    def process(self, tup):
        # Process block data here

        data = tup.values[0]
        data = json.loads(data)
        data = json.loads(data)
        blockData = data["result"]

        trsansaction = blockData["transactions"]
        storm.logInfo("Emitting from Transaction BOLT")
        #     storm.emit([word])
        storm.emit([trsansaction])



# Start the bolt when it's invoked
SplitBolt().run()
