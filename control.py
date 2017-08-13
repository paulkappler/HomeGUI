
import sys
import logging
import socket

from PyQt5.QtWidgets import QApplication, QWidget, QListWidgetItem
from PyQt5.QtCore import Qt,QTimer,QObject
from datetime import datetime


import mywidget
from phue import Bridge

class UiEventFilter(QObject):
    def eventFilter(self, event):
        print(event)



class UiLogHandler(logging.Handler):
        
    def emit(self, record):
        logString = ui.debugText.toPlainText()
        logString = logString + self.format(record) + "\n"
        ui.debugText.setPlainText(logString)



def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def on_alloff():
    ui.allOffButton.setEnabled(False)
    
    b.set_group(0,"on", False)
    
    #lights = b.lights
    #for l in lights:
    #    print l.name + " " + str(l.on)
    #    l.on = False
        
    ui.allOffButton.setEnabled(True)
    refreshList()


def on_bathroom():
    ui.bathroomButton.setEnabled(False)
    logger = logging.getLogger('HomeGUI')
    logger.info( "bathroom")
    b.set_group(2,"on",True)

    ui.bathroomButton.setEnabled(True)
    refreshList()
    
def on_bathroom_off():
    ui.bathroomOffButton.setEnabled(False)
    logger = logging.getLogger('HomeGUI')
    logger.info( "bathroom off")
    b.set_group(2,"on",False)

    ui.bathroomOffButton.setEnabled(True)
    refreshList()    
    
    

def on_exit():
    print "exit button clicked"
    sys.exit(0)
    
def on_reset():
    print "exit button clicked"
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

        
def myMove (event): 
    global mCountdown 
    if mCountdown < 58:
        mCountdown = 60
        Widget.setMouseTracking(False)
        ui.tabWidget.show()
        refreshList()
        set_backlight(True)
        set_brightness(60)
        
        logger = logging.getLogger('HomeGUI')
        logger.info("myMove")

def on_timer():
    global mCountdown
    mCountdown = mCountdown -1
    if (mCountdown > 50 ):
        set_brightness(60)
    elif (mCountdown > 40 ):
        set_brightness(20)
    else:
        set_backlight(False)
        ui.tabWidget.hide()
        Widget.setMouseTracking(True)

        
        
mCountdown = 1
mBrightness = -1
mBacklight = False

    
  
    
#if __name__ == "__main__":


app = QApplication(sys.argv)
Widget = QWidget()
ui = mywidget.Ui_Widget()
ui.setupUi(Widget)

uiLogHandler = UiLogHandler()
uiLogHandler.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
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


b = Bridge("192.168.1.79")
groups = b.get_group()


def addList(): 
    groups = b.get_group()
    for groupId in groups:
        group = groups[groupId]
        if len(group['lights']) > 0:
            name = group['name'] 
            all_on = group['state']['all_on']
            any_on = group['state']['any_on']
           
            listItem = QListWidgetItem(ui.listWidget)
            listItem.setText(name)
            listItem.setData(Qt.UserRole, groupId)
            listItem.setFlags(Qt.ItemIsEnabled)
            if all_on:
                listItem.setCheckState(Qt.Checked)
            elif any_on:
                listItem.setCheckState(Qt.PartiallyChecked)
            else:
                listItem.setCheckState(Qt.Unchecked)
            
            
def refreshList(): 
    groups = b.get_group()
    count = ui.listWidget.count()
    index = 0
    while index < count:
        listItem = ui.listWidget.item(index)
        groupId = listItem.data(Qt.UserRole)
        group = groups[groupId]
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
ui.bathroomButton.clicked.connect(on_bathroom)
ui.bathroomOffButton.clicked.connect(on_bathroom_off)
ui.exitButton.clicked.connect(on_exit)



Widget.mouseMoveEvent = myMove

Widget.showFullScreen()

myMove(False)




timer = QTimer()
timer.setInterval(1000)
timer.setTimerType(Qt.PreciseTimer)
timer.timeout.connect(on_timer)
timestamp_start = datetime.now()
timer.start(1000)

sys.exit(app.exec_())

