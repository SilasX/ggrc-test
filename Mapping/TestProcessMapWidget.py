'''
Created on Sep 22, 2013

@author: diana.tzinov
'''



import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers
from helperRecip.GRCObject import GRCObject


class TestProcessMapWidget(WebDriverTestCase):

    
    def testProcessMapWidget(self):
        self.testname="TestProcessMapWidget"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers()
        do.setUtils(util)
        do.login()
        process_name = "Process for Auto Mapping from Widget"  +do.getTimeId()
        last_created_object_link = do.createObject("Process",process_name)
        #object_name = str(util.getTextFromXpathString(last_created_object_link)).strip() 
        do.navigateToObject("Process",last_created_object_link)
        for obj in grcobject.process_map_to_widget: 
            do.mapAObjectWidget(obj)
            #util.refreshPage()
       

        
if __name__ == "__main__":
    unittest.main()