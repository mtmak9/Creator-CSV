import pandas as pd
import time
import os


#Introduction
print("Hello, this program will create CSV files for your Ebay Repricer & Amazon Importer, also will Create Full Product List File.")
time.sleep(2)
print("You need put in folder where program is RUN, this files: FE.csv, Complete Product List.csv")
print(" ")
print("1.FE.csv - This is File Exchange File with ALL Active Listing Converted to UTF-8 Format and Changed Name for FE.csv")
print("2.Complete Product List.csv - This is file from Creator_CSV, when you last time create your product list")
print(" ")
time.sleep(2)
print("Program will be working based on this Three File and will generate for you Complete for Copy&Paste File where you can use it in:")
print(" ")
print("1.Amazon Importer")
print("2.Ebay Repricer")
print("3.Google Sheet for keep your All product list with ASIN/EbayID/Ebay SKU number")
print(" ")
time.sleep(1)
input('If you want to Continue press any button...')

try:
 #DEFINED FILE NAME & PATH TO FILES
 FE = pd.read_csv('IN\FE.csv')
 CP = pd.read_csv('IN\Complete Product List.csv')

 #1.PREPARED 'FileExchange' COLUMN NAMES File from Ebay 
 FE.columns
 FE.rename(columns = {'Item ID':'ItemID','Custom label':'CustomLabel'}, inplace=True)
 FE.head()

 #2.REMOVED UNREQUIED COLUMN FROM 'FileExchange' File
 FE.drop(['Product ID type','Product ID value','Product ID value 2',
 'Quantity available','Purchases','Bids','Price','Start date','End date','Condition','Type','Item title',
 'Category leaf name','Category number','Private notes','Site listed','Download date','Variation details',
 'Product reference ID','Condition ID','OutOfStockControl'], axis=1, inplace=True)

 

 #3.CREATE OUTPUT CSV FILE WITH ItemID and SKU
 print(FE)
 FE.to_csv('IN\FE_Output.csv', index=False)

 print("|||||||||| 25%")

 #4.PREPARED SKU FILE FOR MERGE PROCESS
 CP.head()
 CP.drop(['ItemID'],axis=1, inplace=True)
 print(CP)

 CP.to_csv('IN\CP_Output.csv', index=False)

 #5.CREATE SKU-ASIN-EBAYID FILE

 #DEFINED NEW FILE NAME & PATH TO FILES
 FE_OUTPUT = pd.read_csv('IN\FE_OUTPUT.csv')
 CP_OUTPUT = pd.read_csv('IN\CP_OUTPUT.csv')
 merge = pd.merge(FE_OUTPUT, CP_OUTPUT, on="CustomLabel")
 columns_names = ["ASIN","ItemID","CustomLabel"]
 new_merge = merge.reindex(columns=columns_names)

 print(new_merge)
 new_merge.to_csv("OUT\CPL.csv", index=False)
 print(" ")
 print("|||||||||||||||||||||| 38%")
 print(" ")

 Amazon_Importer = pd.read_csv('OUT\CPL.csv')
 Ebay_Repricer = pd.read_csv('OUT\CPL.csv')

 print("|||||||||||||||||||||||||||||||||||| 75% ")

 #Process of Create new File for Programs Amazon Importer and Ebay Repricer
 Amazon_Importer.drop(['CustomLabel'],axis=1, inplace=True)
 Amazon_Importer.head()
 Amazon_Importer.rename(columns = {'ASIN':'vendor_url','ItemID':'reprice_sku'}, inplace=True)

 print(Amazon_Importer)
 Amazon_Importer.to_csv("OUT\Amazon Importer.csv", index=False)

 print("||||||||||||||||||||||||||||||||||||||||||||||| 88% ")

 Ebay_Repricer.drop(['CustomLabel'],axis=1, inplace=True)
 Ebay_Repricer.head()
 Ebay_Repricer.rename(columns = {'ItemID':'EBAYID'}, inplace=True)
 print(Ebay_Repricer)
 Ebay_Repricer.to_csv("OUT\Ebay Repricer Listings.csv", index=False)

 #REMOVED OPERATIONAL FILES
 os.remove("IN\FE_Output.csv")
 os.remove("IN\CP_Output.csv")

 os.system('explorer')
 os.startfile("OUT")  

 print(" ")
 print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||| 100% ")
 print(" ")
 print("Process is Complete, check OUT directory and copy your Files ")
 input('To close program, press any button... ')

except SyntaxError:
 print("Error.. Syntax, something went wrong with the program or pathway..")
 time.sleep(1)
 print("Check Folder/Name/Format of Your Files")

except UnicodeDecodeError:
 print("Error.. Wrong format of FE.csv file, please check UTF-8 Format")

except FileNotFoundError:
 print("Error.. I dont see one or more of requied files: FE.csv/CP.csv")