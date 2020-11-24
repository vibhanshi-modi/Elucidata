
from flask import Flask, render_template, request
import pandas as pd
from pandas import ExcelWriter
import numpy as np

app = Flask(__name__)
df=pd.DataFrame()

#Initialise the dataframe
def init_df(input_df):
	global df
	df=input_df

@app.route('/')
def index():
   return render_template('home.html')

#To read the uploaded file	into a pd dataframe object
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file'] 
      init_df(pd.read_excel(f))
      if df.empty:
      	return '<h1> File was not uploaded<h2>Click back button on browser to return to homepage'
      else:
      	return '<h1> File uploaded successfully<h2>Click back button on browser to return to homepage'

#Function to round off rentention time to nearest natural number     
@app.route('/roundoff_ret_time')
def roundoff_ret_time():
	global df
	# To make sure file is uploaded before calculating roundoff
	if df.empty:
		return '<h1> Please upload a file first<h2>Click back button on browser to return to homepage'
	# Roundoff to nearest natural number is calculated using the following logic
	# If ceil(decimal_number)-decimal_number)>(decimal_number-floor(decimal_number), it means that nearest natural number will be floor(decimal_number)
	# else nearest natural number will be ceil(decimal_number)
	df['Retention Time Roundoff']=np.where((df['Retention time (min)'].apply(np.ceil)-df['Retention time (min)'])>(df['Retention time (min)']-df['Retention time (min)'].apply(np.floor)),df['Retention time (min)'].apply(np.floor),df['Retention time (min)'].apply(np.ceil))
	#To download the output files
	writer = ExcelWriter('df_with_roundoff_ret_time.xlsx')
	df.to_excel(writer)
	writer.save()
	return '<h1>Retention time roundoff coloumn successfully added to parent dataframe and resulting file(df_with_roundoff_ret_time) downloaded<h2>Click back button on browser to return to homepage'

#Function to calculate mean of metabolites having same rounded iff retention time across all samples
@app.route('/mean')
def mean():
	global df
	#To make sure file is uploaded before calculating mean
	if df.empty:
		return '<h1> Please upload a file first<h2>Click back button on browser to return to homepage'
	#To make sure round off retention time is calculated before calculating mean of metabolites having same rounded iff retention time across all samples
	if 'Retention Time Roundoff' not in df.columns:
		return '<h1>Please roundoff retention time first by clicking on 2nd button(Retention Time Roundoff) on the homepage<h2>Click back button on browser to return to homepage'
	#Use of groupby for getting all metabolites having same roundoff retention time
	res=df.groupby('Retention Time Roundoff').mean()
	res=res.drop(['m/z','Retention time (min)'],axis=1)
	#To download the output files
	writer = ExcelWriter('mean.xlsx')
	res.to_excel(writer)
	writer.save()
	return '<h1>Mean of metabolites having same Roundoff Retention Time calculated across all samples and resulting file(mean) downloaded successfully<h2>Click back button on browser to return to homepage'   
    
 #Function to create 3 child datasets based on Accepted Compound ID ending with LPC,PC and plasmalogen respectively
@app.route('/filter_data')
def filter_data():
	global df
	#To make sure file is uploaded before creating 3 datasets for IDs ending with LPC,PC and plasmalogen
	if df.empty:
		return '<h1> Please upload a file first<h2>Click back button on browser to return to homepage'
	# To select rows that have Accepted Compound ID column value ending with plasmalogen	
	plasmalogen=df['Accepted Compound ID'].str.endswith("plasmalogen",na=False)
	df_plasmalogen=df[plasmalogen]
	# To select rows that have Accepted Compound ID column value ending with PC
	PC=df['Accepted Compound ID'].str.endswith(" PC",na=False)
	df_PC=df[PC]
	# To select rows that have Accepted Compound ID column value ending with LPC
	LPC=df['Accepted Compound ID'].str.endswith("LPC",na=False)
	df_LPC=df[LPC]
	#To download the output files
	writer = ExcelWriter('endswith_plasmalogen.xlsx')
	df_plasmalogen.to_excel(writer)
	writer.save()
	writer = ExcelWriter('endswith_LPC.xlsx')
	df_LPC.to_excel(writer)
	writer.save()
	writer = ExcelWriter('endswith_PC.xlsx')
	df_PC.to_excel(writer)
	writer.save()
	return '<h1>Given dataset split into 3 datasets having Accepted Compound ID ending with PC, LPC, and plasmalogen respectively and all 3 files downloaded successfully<h2>Click back button on browser to return to homepage'
    
    
    
    
      
    


	  
