import sys
import logging
import socket
import requests


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
                #logger = logging.getLogger('HomeGUI')
                #logger.info("MouseMove Event " + str(mIdle) )

                mIdle = 0
                Widget.setMouseTracking(False)
                refresh()
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

class UiStatusHandler(logging.Handler):
    def emit(self, record):
        ui.statusLabel.setText(self.format(record))
        app.processEvents()


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def put_value(idNumber, value):
    r = requests.put("https://autodiscover.kappler.us/internet_test/id/" + str(int(idNumber)), data=str(value))

def get_value(idNumber):
    r = requests.get("https://autodiscover.kappler.us/internet_test/id/" + str(int(idNumber)))
    return r.text



def on_alloff():
    logger.info( "All Off B")
    b.set_group(0,"on", False)
    
    logger.info( "All Off B2")
    b2.set_group(0,"on", False)

    logger.info( "All Off refresh")
    refresh()
    logger.info( "All Off complete")


def downstairs_on():
    logger = logging.getLogger('HomeGUI')
    logger.info( "Kitchen Bright")
    b.run_scene("Kitchen", "Bright")
    
    logger.info( "Living Room Bright")
    b.run_scene("Living Room", "Bright")
    
    logger.info( "Dining Room Bright")
    b.run_scene("Dining Room", "Bright")
    
    logger.info( "downstairs on refresh")
    refresh()
    logger.info( "downstairs on complete")


def upstairs_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "upstairs off")
    b.set_group(6,"on",False)

    logger.info( "upstairs off refresh")

    refresh()
    logger.info( "upstairs off complete")

    
def downstairs_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "downstairs off")
    b.set_group(15,"on",False) #downstairs
    
    logger.info( "All Off B2")
    b2.set_group(0,"on",False) #all b2

    logger.info( "downstairs off refresh")
    
    refresh()
    logger.info( "downstairs off complete")

    
def downstairs_dim():
    logger = logging.getLogger('HomeGUI')
    logger.info( "downstairs_dim")
    
    b.run_scene("Downstairs", "Dim")
    logger.info( "downstairs_dim refresy")

    refresh()
    logger.info( "downstairs_dim complete")


def outside_on():
    logger = logging.getLogger('HomeGUI')
    logger.info( "OutsideBrightest")
    b.run_scene("Outside", "OutsideBrightest")
    logger.info( "OutsideBrightest refresh")
    refresh()
    logger.info( "OutsideBrightest complete")


def outside_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "outside off")
    b.set_group(10,"on",False) #Outside
    logger.info( "outside off refresh")
    refresh()
    logger.info( "outside off complete")


def kitchen_on():
    logger = logging.getLogger('HomeGUI')
    logger.info("Kitchen Brightest")
    b.run_scene("Kitchen", "Brightest")
    logger.info("Kitchen Brightest refresh")
    refresh()
    logger.info("Kitchen Brightest complete")


def kitchen_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "kitchen_off")

    b.set_group(7,"on",False) #Kitchen

    refresh()
    logger.info("Kitchen off complete")


def kitchen_dim():
    logger = logging.getLogger('HomeGUI')
    logger.info("Kitchen Nightlight")
    b.run_scene("Kitchen", "Nightlight")
    logger.info("Kitchen Nightlight refresh")
    refresh()
    logger.info("Kitchen Nightlight complete")


def downhall_on():
    logger = logging.getLogger('HomeGUI')
    
    logger.info("Down Hallway Bright in progress")
    b.set_light('Downstairs Hall', {"on": True, "bri": 254, "ct": 333})

    
    logger.info("DownHallway Bright refresh ")
    refresh()
    
    logger.info("DownHallway Bright complete")



def downhall_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "Downstairs Hall off in progress" )
    b.set_light('Downstairs Hall', "on", False)

    
    logger.info("DownHallway off refresh")
    refresh()
    logger.info("DownHallway off complete")


def downhall_dim():
    logger = logging.getLogger('HomeGUI')
    
    logger.info("DownHallway Nightlight")
    b.set_light('Downstairs Hall', {"on": True, "bri": 1, "ct": 500})

    logger.info("DownHallway Nightlight refresh")
    refresh()
    
    logger.info("DownHallway Nightlight complete")



def hall_on():
    logger = logging.getLogger('HomeGUI')

    logger.info("Hallway Bright in progress")
    b.run_scene("Hallway", "Bright")

    
    logger.info("Hallway Bright refresh ")
    refresh()
    
    logger.info("Hallway Bright complete")



def hall_off():
    logger = logging.getLogger('HomeGUI')
    logger.info( "Hallway off in progress" )
    b.set_group(11,"on", False)
    logger.info("Hallway off refresh")
    refresh()
    logger.info("Hallway off complete")


def hall_dim():
    logger = logging.getLogger('HomeGUI')
    
    logger.info("Hallway Nightlight")
    b.run_scene("Hallway", "Nightlight")
    
    logger.info("Hallway Nightlight refresh")
    refresh()
    
    logger.info("Hallway Nightlight complete")


def get_room_selection():
    listItem = ui.listWidgetRoom.currentItem()
    groupId = int(listItem.data(Qt.UserRole))
    bridgeId = int(listItem.data(Qt.UserRole + 1))
    bridge = bridges[bridgeId]
    return bridge, groupId

def on_room_off():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,"on",False)

    refresh()


def on_room_on():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,"on",True)

    refresh()

def on_room_100():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":254})
    
    refresh()

def on_room_50():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":128})
    
    refresh()

def on_room_25():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":64})
    
    refresh()

def on_room_12():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":32})
    
    refresh()

def on_room_dim():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId,{"on": True,"bri":1})
    
    refresh()




def on_room_sky():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 153} )
    
    refresh()

def on_room_bright():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 213} )
    
    refresh()

def on_room_normal():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 333} )
    
    refresh()

def on_room_warm():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "ct": 500} )
    
    refresh()


def on_room_red():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "hue": 0, "sat": 254} )
    
    refresh()


def on_room_blue():
    bridge, groupId = get_room_selection()
    bridge.set_group(groupId, {"on": True, "hue": 46920, "sat": 254} )

    refresh()

def on_room_slider(value):
    logger = logging.getLogger('HomeGUI')

    global roomBridge, roomGroupId
    global roomValue, sliderDelay
    roomBridge, roomGroupId = get_room_selection()
    roomValue = value
    sliderDelay = True
    if slidetimer.isActive():
        logger.info("timer active  value:" + str(value) )
    else:
        slidetimer.start(500)
        logger.info("timer start  value" + str(value) )

def on_slidetimer():
    global roomBridge, roomGroupId
    global roomValue, sliderDelay
    if sliderDelay:
        result = roomBridge.set_group(roomGroupId,"bri",roomValue,transitiontime=5)
        logger.info("room slider timer value" + str(roomValue) + str(result) )

def on_open_window():
    put_value(5,1.0)

    put_value(6,0.0)


def on_close_window():
    put_value(5,0.0)

    put_value(6,0.0)

def on_auto_window():
    put_value(6,1.0)


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
        #logger = logging.getLogger('HomeGUI')
        #logger.info("mBrightness:" + str(mBrightness))


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
        #logger = logging.getLogger('HomeGUI')
        #logger.info("mBacklight:" + str(mBacklight))




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

uiStatusHandler = UiStatusHandler()
uiStatusHandler.setLevel(logging.DEBUG)
statusFormatter = logging.Formatter('%(message)s')
uiStatusHandler.setFormatter(statusFormatter)


logger = logging.getLogger('phue')
logger.addHandler(console)
logger.addHandler(uiLogHandler)
logger.setLevel(logging.INFO)

logger = logging.getLogger('HomeGUI')
logger.addHandler(console)
logger.addHandler(uiLogHandler)
logger.addHandler(uiStatusHandler)
logger.setLevel(logging.DEBUG)


bridges = {}

b = Bridge("192.168.1.79")
b2= Bridge("192.168.1.78")
bridges[0] = b
bridges[1] = b2

bridge_groups={}
bridge_groups[0] = {}
bridge_groups[1] = {}

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

def refreshBridgeGroups():
    for bridgeId in bridges:
        bridge = bridges[bridgeId]
        groups = bridge.get_group()
        for groupIdStr in groups:
            group = groups[groupIdStr]
            groupId = int(groupIdStr)
            bridge_groups[bridgeId][groupId] = group

def refreshList(): 
    count = ui.listWidget.count()
    index = 0
    refreshBridgeGroups()
    while index < count:
        listItem = ui.listWidget.item(index)
        groupId = int(listItem.data(Qt.UserRole))
        bridgeId = int(listItem.data(Qt.UserRole + 1))

        bridge = bridges[bridgeId]
        group = bridge_groups[bridgeId][groupId]

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
        group = bridge_groups[bridgeId][groupId]
        bri = group['action']['bri']
        all_on = group['state']['all_on']
        any_on = group['state']['any_on']
        if all_on:
            listItem.setCheckState(Qt.Checked)
            listItem.setText(group['name'] + ' ' + str(bri))

        elif any_on:
            listItem.setCheckState(Qt.PartiallyChecked)
            listItem.setText(group['name'] + ' ' + str(bri))

        else:
            listItem.setCheckState(Qt.Unchecked)
            listItem.setText(group['name'])

        index = index + 1

def refresh():
    refreshBridgeGroups()
    refreshList()
    refreshRoomList()

addList()
            
ui.ipValue.setText(get_ip_address())
ui.allOffButton.clicked.connect(on_alloff)

ui.downHallOffButton.clicked.connect(downhall_off)
ui.downHallOnButton.clicked.connect(downhall_on)
ui.downHallDimButton.clicked.connect(downhall_dim)


ui.hallOnButton.clicked.connect(hall_on)
ui.hallDimButton.clicked.connect(hall_dim)
ui.hallOffButton.clicked.connect(hall_off)

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
ui.openWindowButton.clicked.connect(on_open_window)
ui.closeWindowButton.clicked.connect(on_close_window)


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

r = requests.get("https://autodiscover.kappler.us/internet_test/id/2")
ui.label_2.setText(r.text)

r = requests.get("https://autodiscover.kappler.us/internet_test/id/1")
ui.label_4.setText(r.text)


import requests
import pyqtgraph as pg
import numpy as np

r = requests.get("https://autodiscover.kappler.us/internet_test/id/log/1")
log1 = str(r.text).strip("[]")
y1 = np.fromstring(log1,sep=',') * 9 / 5 + 32

r = requests.get("https://autodiscover.kappler.us/internet_test/id/log/2")
log2 = str(r.text).strip("[]")
y2 = np.fromstring(log2,sep=',') * 9 / 5 + 32


x = np.arange(128)
plotWidget = pg.plot(title="Three plot curves")
plotWidget.plot(x, y1, pen=(1,3))
plotWidget.plot(x, y2, pen=(2,3))

ui.gridLayout_6.addWidget(plotWidget, 0, 0, 1, 1)


sys.exit(app.exec_())

import sys
