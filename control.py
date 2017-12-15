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
    #b.set_group(2,"on",False) #Little Bathroom
    #b.set_group(4,"on",False) #Garage
    #b.set_group(5,"on",False) #Changing Closet
    #b.set_group(6,"on",False) #Changing Room
    #b.set_group(7,"on",False) #Kitchen
    #b.set_group(8,"on",False) #Dining Room
    #b.set_group(9,"on",False) #Living Room
    b.set_group(15,"on",False) #downstairs
    refreshList()
    
def downstairs_dim():
    logger = logging.getLogger('HomeGUI')
    logger.info( "downstairs_dim")
    
    #b.set_group(15,"on",True) #downstairs

    b.run_scene("Downstairs", "Dim")
    #b.run_scene("Living Room", "Nightlight")
    #b.run_scene("Dining Room", "Nightlight")

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

    

def on_exit():
    logger = logging.getLogger('HomeGUI')
    logger.info("Exit Button"  )
    sys.exit(0)
    
def on_reset():
    logger = logging.getLogger('HomeGUI')
    logger.info("reset Button"  )
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


b = Bridge("192.168.1.79")
groups = b.get_group()



def addList(): 
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
            if type == 'Room':
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

ui.hallOnButton.clicked.connect(hall_on)
ui.hallDimButton.clicked.connect(hall_dim)

ui.downOnButton.clicked.connect(downstairs_on)
ui.downOffButton.clicked.connect(downstairs_off)
ui.downDimButton.clicked.connect(downstairs_dim)
ui.upOffButton.clicked.connect(upstairs_off)



ui.exitButton.clicked.connect(on_exit)


Widget.showFullScreen()

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

