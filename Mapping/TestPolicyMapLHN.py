'''
Created on Sep 15, 2013

@author: diana.tzinov
'''


import unittest
import time
from helperRecip.testcase import *
from helperRecip.Elements import Elements
from helperRecip.WebdriverUtilities import WebdriverUtilities
from helperRecip.Helpers import Helpers
from helperRecip.GRCObject import GRCObject


class TestPolicyMapLHN(WebDriverTestCase):

    
    def testPolicyMapLHN(self):
        self.testname="TestPolicyMapLHN"
        self.setup()
        util = WebdriverUtilities()
        util.setDriver(self.driver)
        element = Elements()
        grcobject = GRCObject()
        do = Helpers()
        do.setUtils(util)
        do.login()
        program_name = "Policy for Auto Mapping from LHN"  +do.getTimeId()
        last_created_object_link = do.createObject("Policy", program_name)
        #object_name = str(util.getTextFromXpathString(last_created_object_link)).strip() 
        do.navigateToObject("Policy",last_created_object_link)
        for obj in grcobject.policy_map_to_lhn: 
            do.mapAObjectLHN(obj)
            util.refreshPage()
       

        
if __name__ == "__main__":
    unittest.main()