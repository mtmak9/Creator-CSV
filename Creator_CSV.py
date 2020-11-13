import pandas as pd
import time
import os


#Introduction
print("Hello, this program will create CSV files for your Ebay Repricer & Amazon Importer, also will Create Full Product List File.")
time.sleep(2)
print("You need put in folder where program is RUN, this files: FE.csv,SKU.csv,ProductList.csv")
print(" ")
print("1.FE.csv - This is File Exchange File with ALL Active Listing Converted to UTF-8 Format and Changed Name for FE.csv")
print("2.SKU.csv - This is file from program named Listing Creator with data about your New listings")
print("3.ProductList.csv - This is your product list from program Amazon Importer where you have ASIN,ebayId.")
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
 SKU = pd.read_csv('IN\SKU.csv')

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
 SKU.head()
 SKU.drop(['Date added','Product:EAN','PicURL'],axis=1, inplace=True)
 print(SKU)

 SKU.to_csv('IN\SKU_Output.csv', index=False)

 #5.CREATE SKU-ASIN-EBAYID FILE

 #DEFINED NEW FILE NAME & PATH TO FILES
 FE_OUTPUT = pd.read_csv('IN\FE_OUTPUT.csv')
 SKU_OUTPUT = pd.read_csv('IN\SKU_OUTPUT.csv')
 merge = pd.merge(FE_OUTPUT, SKU_OUTPUT, on="CustomLabel")
 columns_names = ["ASIN","ItemID","CustomLabel"]
 new_merge = merge.reindex(columns=columns_names)

 print(new_merge)
 print(" ")
 print("|||||||||||||||||||||| 38%")
 print(" ")

 PRODUCT_LIST = pd.read_csv('IN\ProductList.csv')
 PRODUCT_LIST.columns
 PRODUCT_LIST.rename(columns = {'vendor_url':'ASIN','reprice_sku':'ItemID'}, inplace=True)
 PRODUCT_LIST.head()



 ALL_PRODUCT = pd.merge(PRODUCT_LIST, new_merge, on=['ASIN','ItemID'], how='outer')
 FE_OUTPUT2 = pd.read_csv('IN\FE_OUTPUT.csv')
 ALL_PRODUCT.drop(['CustomLabel'],axis=1, inplace=True)
 ALL_PRODUCT.head()
 print(ALL_PRODUCT)
 print("|||||||||||||||||||||||||| 50% ")

 ASIN_ID_SKU = pd.merge(ALL_PRODUCT, FE_OUTPUT2, on='ItemID', how='outer')
 ASIN_ID_SKU.to_csv("OUT\Complete Product List.csv", index=False)
 print(ASIN_ID_SKU)

 Amazon_Importer = pd.read_csv('OUT\Complete Product List.csv')
 Ebay_Repricer = pd.read_csv('OUT\Complete Product List.csv')

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
 os.remove("IN\SKU_Output.csv")

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
 print("Error.. I dont see one or more of requied files: FE.csv/SKU.csv/ProductList.csv")