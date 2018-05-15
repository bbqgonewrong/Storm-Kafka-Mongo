import storm
import json


class SplitBolt(storm.BasicBolt):
    # There's nothing to initialize here,
    # since this is just a split and emit
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        storm.logInfo("DB bolt instance starting...")

    def process(self, tup):
        # Split the inbound sentence at spaces

                # process touples here
        # data = json.loads(tup)

        # words = tup.values[0].split()
        # # Loop over words and emit
        # for word in words:
        storm.logInfo("Emitting from DB BOLT")
        #     storm.emit([word])
        storm.emit([tup])



# Start the bolt when it's invoked
SplitBolt().run()
