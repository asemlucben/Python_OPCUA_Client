import asyncio
import logging
import datetime
from asyncua import Client
from asyncua.ua import NodeId

_logger = logging.getLogger(__name__)

class SubHandler(object):
    def datachange_notification(self, node, val, data):
        print(f"Received value for node ${node}")

async def main():
    url = "opc.tcp://172.19.17.68:59100"

    async with Client(url = url, timeout = 15) as client:
        projectName = "OpcReadTime"
        idx = await client.get_namespace_index(projectName)
        _logger.info(f"Index of namespace ${projectName} is ${idx}")

        nodesToReadStr = [
            # f"ns={idx};g=15c90e92-2171-d537-1458-45496e6edb4a",
            f"ns={idx};g=0bd2dca9-0f76-17ca-c11d-fb328f5d85b6",
            # f"ns={idx};g=060143d9-3aeb-b140-5ed6-b031d749a980",
            # f"ns={idx};g=5fef0356-f697-3b57-b2fc-1a9a6a4c9046",
            # f"ns={idx};g=1f66a878-0cd4-09c2-8d83-4f0354664fce",
            # f"ns={idx};g=c4a1dd43-1d2b-a795-584e-708ebb2d70c9",
            # f"ns={idx};g=c53b7260-783a-0840-fbc8-b9b4fe9d44aa"
        ]

        nodesToRead = []
        for nodeToReadStr in nodesToReadStr:
            nodesToRead.append(client.get_node(NodeId.from_string(nodeToReadStr)))

        while True:
            startTime = datetime.datetime.now()
            values = await client.read_values(nodesToRead)
            endTime = datetime.datetime.now()
            print(f"ReadMode time: ${endTime - startTime}")
            await asyncio.sleep(1)

        # for value in values:
        #     print(value)

        # handler = SubHandler()
        # subscription = await client.create_subscription(100, handler)
        # await subscription.subscribe_data_change(nodesToRead[0])

        # while True:
        #     await asyncio.sleep(1)

if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  logging.getLogger('asyncua').setLevel(logging.ERROR)
  asyncio.run(main())