import unittest
import pytest

from exercise1 import SerialAverage
class TestSerialAverage(unittest.TestCase):
	
	def createObject(value):
		return SerialAverage(value)


	def test_alphabeticalString(self):
		obj = createObject('abd-aa.ef-jj.li')
		with pytest.raises(Exception) as e:  
		    obj.getAverage()
		    message = "Both the values are equal"
                    assertEqual(e.type, TypeError, message)

	def test_alphanumericString(self):
		obj = createObject('002-aa.00-ss.00')
		with pytest.raises(Exception) as e:  
		    obj.getAverage()
		    message = "Both the values are equal"
                    assertEqual(e.type, TypeError, message)

	def test_numericString_proper_format(self):
		obj = createObject('002-10.00-20.00')
		with pytest.raises(Exception) as e:  
		    obj.getAverage()
		    message = "Both the values are equal"
                    assertEqual(e.type, TypeError, message) 
	
	def test_numericString_improper_format(self):
		obj = createObject('002-15.00')
		with pytest.raises(Exception) as e:  
		    obj.getAverage()
		    message = "Both the values are equal"
                    assertEqual(e.type, TypeError, message)

	def test_numericString_noformat(self):
		obj = createObject('00215000909')
		with pytest.raises(Exception) as e:  
		    obj.getAverage()
		    message = "Both the values are equal"
                    assertEqual(e.type, TypeError, message) 
	
	def test_AlphabeticalString_noformat(self):
		obj = createObject('gfjjdhksfksjfbwehdev')
		with pytest.raises(Exception) as e:  
		    obj.getAverage()
		    message = "Both the values are equal"
                    assertEqual(e.type, TypeError, message)
