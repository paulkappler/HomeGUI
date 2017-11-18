
import logging
from phue import Bridge


b = Bridge("192.168.1.79")

formatter = logging.Formatter('%(name)-8s:%(asctime)-12s %(levelname)-8s %(message)s')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)

logger = logging.getLogger('HomeGUI')
logger.addHandler(console)
logger.setLevel(logging.DEBUG)

groups = b.get_group()
for groupId in groups:
    group = groups[groupId]
    if len(group['lights']) > 0:
        recycle = group['recycle']
        type = group['type']
        name = group['name']
        all_on = group['state']['all_on']
        any_on = group['state']['any_on']
        
        logger.info("Group:" + str(name) )
        logger.info("Group ID:" + str(groupId))
        
        logger.info("Group:" + str(group))

