strVar = "Here are the instructions to install Drivers 1. After the download is completed go to where you saved the folder (By default everything you download from the Internet is saved to the Downloads folder) 2. Right-click on the folder and choose 'Extract All' and then choose ''Extract'' again. 3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon. 4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below *setup application *Asussetup *pnpinstal64 *pnputil *Igxpin 5. Please choose to 'repair' or 'update' the existing installation (driver) IF anyone of those options does appear during the setup."

print(len(strVar))
IndexNum = strVar.find("Drivers")
print(strVar.replace('Extract','EXTRACT'))
print(strVar.replace('setup','SETUP'))
IndexNum = strVar.find("4")
IndexNum = strVar.find("/n")
