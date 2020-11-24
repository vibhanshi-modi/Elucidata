import unittest
import app
from app import init_df,filter_data,roundoff_ret_time,mean
import pandas as pd

class TestMethods(unittest.TestCase):

	def setUp(self):
		app.df = pd.DataFrame()

	#Test to check if file is uploaded before calling Task1(creating 3 child datasets based on Accepted Compound ID ending with LPC,PC and plasmalogen respectively)
	def test_api1_when_file_uploaded(self):
		msg1='<h1>Given dataset split into 3 datasets having Accepted Compound ID ending with PC, LPC, and plasmalogen respectively and all 3 files downloaded successfully<h2>Click back button on browser to return to homepage'
		init_df(pd.read_excel('C:\\Users\\vibha\\Downloads\\mass_spec_data_assgnmnt.xlsx.xlsx'))
		self.assertEqual(filter_data(),msg1)


	# Test to check if Task1 is called before uploading a file
	def test_api1_when_file_not_uploaded(self):
		msg2='<h1> Please upload a file first<h2>Click back button on browser to return to homepage'
		self.assertEqual(filter_data(),msg2)


	# Test to check if file is uploaded before calling Task2(round off retention time task) 
	def test_api2_when_file_uploaded(self):
		msg3='<h1>Retention time roundoff coloumn successfully added to parent dataframe and resulting file(df_with_roundoff_ret_time) downloaded<h2>Click back button on browser to return to homepage'
		init_df(pd.read_excel('C:\\Users\\vibha\\Downloads\\mass_spec_data_assgnmnt.xlsx.xlsx'))
		self.assertEqual(roundoff_ret_time(),msg3)

	#Test to check if Task2 is called before uplolading a file
	def test_api2_when_file_not_uploaded(self):
		msg4='<h1> Please upload a file first<h2>Click back button on browser to return to homepage'
		self.assertEqual(roundoff_ret_time(),msg4)

	# Test to check if file is uploaded before calling Task3(calcuating mean) and Task2 is called before Task3 
	def test_api3_when_file_uploaded_and_retention_time_roundoff_calcuated(self):
		msg='<h1>Mean of metabolites having same Roundoff Retention Time calculated across all samples and resulting file(mean) downloaded successfully<h2>Click back button on browser to return to homepage'
		init_df(pd.read_excel('C:\\Users\\vibha\\Downloads\\mass_spec_data_assgnmnt.xlsx.xlsx'))
		roundoff_ret_time()
		self.assertEqual(mean(),msg)

	# Test to check if file is uploaded before calling Task3(calcuating mean) and Task2 is not called before Task3 
	def test_api3_when_file_uploaded_and_retention_time_roundoff_not_calcuated(self):
		msg='<h1>Please roundoff retention time first by clicking on 2nd button(Retention Time Roundoff) on the homepage<h2>Click back button on browser to return to homepage'
		init_df(pd.read_excel('C:\\Users\\vibha\\Downloads\\mass_spec_data_assgnmnt.xlsx.xlsx'))
		self.assertEqual(mean(),msg)

	#Test to check if Task3(calculating mean task) is called before uplolading a file
	def test_api3_when_file_not_uploaded(self):
		msg='<h1> Please upload a file first<h2>Click back button on browser to return to homepage'
		self.assertEqual(mean(),msg)




