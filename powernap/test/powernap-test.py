# Imports
import os
import unittest
import sys
import imp

sys.path.append(os.path.abspath("../"))
imp.load_source('powernapd', '../sbin/powernapd')
import powernapd
import TestMonitor
import logging

logging.basicConfig(level=logging.DEBUG)

ACTION_FLAG = '/tmp/powernap-actionmethod'
RECOVERY_FLAG = '/tmp/powernap-recover'

class PowernapdTest(unittest.TestCase):

    def setUp(self):
        powernapd.powernap.CONFIG = "./powernapd.cfg"
        powernapd.CUSTOMACTION_FLAG = "/tmp/customactionflag"
        powernapd.powernap.load_config_file()
        
        if os.path.exists(ACTION_FLAG):
            os.remove(ACTION_FLAG)
        if os.path.exists(RECOVERY_FLAG):        	
            os.remove(RECOVERY_FLAG)
        if os.path.exists(powernapd.CUSTOMACTION_FLAG):
            os.remove(powernapd.CUSTOMACTION_FLAG)

        powernapd.RUNNING = 1

    def test_not_idle(self):
        monitor = TestMonitor.TestMonitor({"monitor":"TestMonitor", 
            "name":"notidle", "running":[0], "result":[True]})
        powernapd.MONITORS = [monitor]
        powernapd.powernapd_loop()
        self.assertEqual(monitor._absent_seconds, 0)
        self.assertFalse(os.path.exists(ACTION_FLAG))
        self.assertFalse(os.path.exists(RECOVERY_FLAG))

    def test_custom_action(self):
        monitor = TestMonitor.TestMonitor({"monitor":"TestMonitor", 
            "name":"customaction", "running":[0], "result":[False]})
        powernapd.MONITORS = [monitor]
        powernapd.powernapd_loop()
        self.assertTrue(os.path.exists(ACTION_FLAG))
        self.assertFalse(os.path.exists(RECOVERY_FLAG))

    def test_custom_action_recover(self):
        monitor = TestMonitor.TestMonitor({"monitor":"TestMonitor", 
            "name":"customactionrecover", "running":[1, 0], "result":[False, True]})
        powernapd.MONITORS = [monitor]
        powernapd.powernapd_loop()
        self.assertTrue(os.path.exists(ACTION_FLAG))
        self.assertTrue(os.path.exists(RECOVERY_FLAG))
        
# Main program
if __name__ == '__main__':
    unittest.main()
