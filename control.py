import sys
import logging
import socket

from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem 
from PyQt5.QtCore import Qt,QTimer,QObject,QEvent
from PyQt5.QtGui import QTextCursor

from datetime import datetime

import mywidget
from phue import Bridge

class UiEventFilter(QObject):
    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseMove:
            global mIdle
            if mIdle > 5:
                logger = logging.getLogger('HomeGUI')
                logger.info("MouseMove Event " + str(mIdle) )

                mIdle = 0
                Widget.setMouseTracking(False)
                refreshList()
                set_backlight(True)
                set_brightness(60)
            return False
        return False



class UiLogHandler(logging.Handler):
        
    def emit(self, record):
        #logString = ui.debugText.toPlainText()
        #logString = logString + self.format(record) + "\n"
        #ui.debugText.setPlainText(logString)

        ui.debugText.moveCursor(QTextCursor.End)
        ui.debugText.insertPlainText ( self.format(record) + "\n")
        ui.debugText.moveCursor(QTextCursor.End)




def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def on_alloff():
    ui.allOffButton.setEnabled(False)
    
    b.set_group(0,"on", False)
    b2.set_group(0,"on", False)
        
    ui.allOffButton.setEnabled(True)
    refreshList()


def downstairs_on():
    logger = logging.getLogger('HomeGUI')
    logger.info( "downstairs_on")
    #b.set_group(11,"on",True)
    b.run_scene("Kitchen", "Bright")
    b.run_scene("Living Room", "Bright")
    b.run_scene("Dining Room", "Bright")
   
    refreshList()

def upstairs_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "upstairs_off")
    b.set_group(1,"on",False)
    b.set_group(11,"on",False)

    refreshList()
    
def downstairs_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "downstairs_off")
    b.set_group(15,"on",False) #downstairs
    b2.set_group(0,"on",False) #all b2

    refreshList()
    
def downstairs_dim():
    logger = logging.getLogger('HomeGUI')
    logger.info( "downstairs_dim")
    
    b.run_scene("Downstairs", "Dim")

    refreshList()


def outside_on():
    logger = logging.getLogger('HomeGUI')
    logger.info( "OutsideBrightest")
    b.run_scene("Outside", "OutsideBrightest")

    refreshList()

def outside_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "outside_off")
    
    b.set_group(10,"on",False) #Outside
    
    refreshList()

def kitchen_on():
    logger = logging.getLogger('HomeGUI')
    logger.info( "kitchen_on")
    b.run_scene("Kitchen", "Brightest")
    refreshList()

def kitchen_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "kitchen_off")

    b.set_group(7,"on",False) #Kitchen

    refreshList()

def kitchen_dim():
    logger = logging.getLogger('HomeGUI')
    logger.info( "kitchen_dim")
    b.run_scene("Kitchen", "Nightlight")
    
    refreshList()


def hall_on():
    logger = logging.getLogger('HomeGUI')
    logger.info( "hall_on")
    #b.set_group(11,"on",True)
    b.run_scene("Hallway", "Bright")
    refreshList()
    

def hall_dim():
    logger = logging.getLogger('HomeGUI')
    logger.info( "hall_dim")
    b.run_scene("Hallway", "Nightlight")

    #b.set_group(11,"on",False)
    refreshList()
    
def on_bathroom():
    ui.bathroomButton.setEnabled(False)
    logger = logging.getLogger('HomeGUI')
    logger.info( "bathroom")
    b.set_group(2,"on",True)
    refreshList()

    ui.bathroomButton.setEnabled(True)

def on_bathroom_off():
    ui.bathroomOffButton.setEnabled(False)
    logger = logging.getLogger('HomeGUI')
    logger.info( "bathroom off")
    b.set_group(2,"on",False)

    refreshList()

    ui.bathroomOffButton.setEnabled(True)

def get_room_selection():
    listItem = ui.listWidgetRoom.currentItem()
    groupId = int(listItem.data(Qt.UserRole))
    bridgeId = int(listItem.data(Qt.UserRole + 1))
    bridge = bridges[bridgeId]
    return bridge, groupId

def on_room_off():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,"on",False)

    refreshRoomList()


def on_room_on():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,"on",True)

    refreshRoomList()

def on_room_100():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":254})
    
    refreshRoomList()

def on_room_50():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":128})
    
    refreshRoomList()

def on_room_25():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":64})
    
    refreshRoomList()

def on_room_12():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":32})
    
    refreshRoomList()

def on_room_dim():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":1})
    
    refreshRoomList()




def on_room_sky():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 153} )
    
    refreshRoomList()

def on_room_bright():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 213} )
    
    refreshRoomList()

def on_room_normal():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 333} )
    
    refreshRoomList()

def on_room_warm():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 500} )
    
    refreshRoomList()


def on_room_red():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "hue": 0, "sat": 254} )
    
    refreshRoomList()


def on_room_blue():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "hue": 46920, "sat": 254} )

    refreshRoomList()

def on_room_slider(value):
    logger = logging.getLogger('HomeGUI')

    global roomBridge, roomGroupId
    global roomValue, sliderDelay
    roomBridge, roomGroupId = get_room_selection()
    if slidetimer.isActive():
        roomValue = value
        sliderDelay = True
        logger.info("timer active  value:" + str(value) )

    else:
        result = roomBridge.set_group(roomGroupId,"bri",value,transitiontime=1)
        slidetimer.start(1000)
        logger.info("room slider value" + str(value) +  "groupID" + str(roomGroupId) + str(result) )

def on_slidetimer:
    global roomBridge, roomGroupId
    global roomValue, sliderDelay
    if sliderDelay:
        result = roomBridge.set_group(roomGroupId,"bri",value,transitiontime=1)


def on_exit():
    logger = logging.getLogger('HomeGUI')
    logger.info("Exit Button"  )
    sys.exit(0)
    
def on_reset():
    logger = logging.getLogger('HomeGUI')
    logger.info("reset Button")
    sys.exit(0)
    
def set_brightness(light):
    global mBrightness
    if mBrightness != light:
        mBrightness = light
        brightness = open("/sys/class/backlight/rpi_backlight/brightness", "w")
        brightness.write(str(int(light)))
        brightness.close()
        logger = logging.getLogger('HomeGUI')
        logger.info("mBrightness:" + str(mBrightness))


def set_backlight(light):
    global mBacklight
    if mBacklight != light:
        mBacklight = light
        bl_power = open("/sys/class/backlight/rpi_backlight/bl_power", "w")
        if light:
            bl_power.write("0")
        else:
            bl_power.write("1")
        bl_power.close()
        logger = logging.getLogger('HomeGUI')
        logger.info("mBacklight:" + str(mBacklight))




def on_timer():
    global mIdle
    mIdle = mIdle + 1
    if (mIdle < 10 ):
        set_brightness(60)
    elif (mIdle < 20 ):
        set_brightness(20)
    else:
        set_backlight(False)

mIdle = 0
mBrightness = -1
mBacklight = None


#if __name__ == "__main__":


app = QApplication(sys.argv)
Widget = QWidget()
ui = mywidget.Ui_Widget()
ui.setupUi(Widget)


uiLogHandler = UiLogHandler()
uiLogHandler.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-8s:%(asctime)-12s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
uiLogHandler.setFormatter(formatter)

logger = logging.getLogger('phue')
logger.addHandler(console)
logger.addHandler(uiLogHandler)
logger.setLevel(logging.INFO)

logger = logging.getLogger('HomeGUI')
logger.addHandler(console)
logger.addHandler(uiLogHandler)
logger.setLevel(logging.DEBUG)

bridges = {}

b = Bridge("192.168.1.79")
b2= Bridge("192.168.1.78")
bridges[0] = b
bridges[1] = b2


def addRoomList(listItem, name, bridgeId, groupId, all_on, any_on):
    listItem.setText(name)
    listItem.setData(Qt.UserRole, groupId)
    listItem.setData(Qt.UserRole+1, bridgeId)

    listItem.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
    if all_on:
        listItem.setCheckState(Qt.Checked)
    elif any_on:
        listItem.setCheckState(Qt.PartiallyChecked)
    else:
        listItem.setCheckState(Qt.Unchecked)

def addList():
    for bridgeId in bridges:
        bridge = bridges[bridgeId]
        groups = bridge.get_group()
        for groupId in groups:
            group = groups[groupId]
            if len(group['lights']) > 0:
                recycle = group['recycle']
                type = group['type']
                name = group['name']
                all_on = group['state']['all_on']
                any_on = group['state']['any_on']

                if type == 'Room':
                    listItem = QListWidgetItem(ui.listWidget)
                    addRoomList(listItem, name, bridgeId, groupId, all_on, any_on)
                    listItem = QListWidgetItem(ui.listWidgetRoom)
                    addRoomList(listItem, name, bridgeId, groupId, all_on, any_on)
            
def refreshList(): 
    count = ui.listWidget.count()
    index = 0
    while index < count:
        listItem = ui.listWidget.item(index)
        groupId = int(listItem.data(Qt.UserRole))
        bridgeId = int(listItem.data(Qt.UserRole + 1))
        bridge = bridges[bridgeId]
        group = bridge.get_group(groupId)

        listItem.setText(group['name'])
        all_on = group['state']['all_on']
        any_on = group['state']['any_on']
        if all_on:
            listItem.setCheckState(Qt.Checked)
        elif any_on:
            listItem.setCheckState(Qt.PartiallyChecked)
        else:
            listItem.setCheckState(Qt.Unchecked)
        index = index + 1

def refreshRoomList():
    count = ui.listWidgetRoom.count()
    index = 0
    while index < count:
        listItem = ui.listWidgetRoom.item(index)
        groupId = int(listItem.data(Qt.UserRole))
        bridgeId = int(listItem.data(Qt.UserRole + 1))
        bridge = bridges[bridgeId]
        group = bridge.get_group(groupId)

        listItem.setText(group['name'])
        all_on = group['state']['all_on']
        any_on = group['state']['any_on']
        if all_on:
            listItem.setCheckState(Qt.Checked)
        elif any_on:
            listItem.setCheckState(Qt.PartiallyChecked)
        else:
            listItem.setCheckState(Qt.Unchecked)
        index = index + 1


addList()
            
ui.ipValue.setText(get_ip_address())
ui.allOffButton.clicked.connect(on_alloff)

ui.hallOnButton.clicked.connect(hall_on)
ui.hallDimButton.clicked.connect(hall_dim)

ui.kitOnButton.clicked.connect(kitchen_on)
ui.kitDimButton.clicked.connect(kitchen_dim)
ui.kitOffButton.clicked.connect(kitchen_off)

ui.outOnButton.clicked.connect(outside_on)
ui.outOffButton.clicked.connect(outside_off)


ui.downOnButton.clicked.connect(downstairs_on)
ui.downOffButton.clicked.connect(downstairs_off)
ui.downDimButton.clicked.connect(downstairs_dim)
ui.upOffButton.clicked.connect(upstairs_off)

ui.roomOffButton.clicked.connect(on_room_off)
ui.roomOnButton.clicked.connect(on_room_on)
ui.room100Button.clicked.connect(on_room_100)
ui.room50Button.clicked.connect(on_room_50)
ui.room25Button.clicked.connect(on_room_25)
ui.room12Button.clicked.connect(on_room_12)
ui.roomDimButton.clicked.connect(on_room_dim)

ui.roomSkyButton.clicked.connect(on_room_sky)
ui.roomBrightButton.clicked.connect(on_room_bright)
ui.roomNormalButton.clicked.connect(on_room_normal)
ui.roomRedButton.clicked.connect(on_room_red)
ui.roomBlueButton.clicked.connect(on_room_blue)
ui.roomWarmButton.clicked.connect(on_room_warm)
ui.roomVerticalSlider.valueChanged.connect(on_room_slider)

ui.exitButton.clicked.connect(on_exit)

Widget.showFullScreen()

slidetimer = QTimer()
slidetimer.setInterval(1500)
slidetimer.setTimerType(Qt.PreciseTimer)
slidetimer.timeout.connect(on_slidetimer)
slidetimer.setSingleShot(True)

timer = QTimer()
timer.setInterval(1000)
timer.setTimerType(Qt.PreciseTimer)
timer.timeout.connect(on_timer)
timestamp_start = datetime.now()
timer.start(1000)

Widget.setMouseTracking(True)


eventFilter = UiEventFilter()
app.installEventFilter(eventFilter)
sys.exit(app.exec_())

import sys
