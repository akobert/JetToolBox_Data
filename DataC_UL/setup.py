#import fileinput

if __name__ == "__main__":
    allFiles = open("input.txt", "r")

    for process in range(2089):
    	template = open("NANO.py", "r")
        newFile = open("nano" + str(process) + ".py", "a+")
       	readLine = allFiles.readline()
	oldline1 = "fileNames = cms.untracked.vstring(''),"
	newline1 = "fileNames = cms.untracked.vstring('"+str(readLine[:-1])+"'),"
	
	oldline2 = "file:/cms/xaastorage/NanoAOD/2018/JUNE19/VectorZPrimeGammaToQQGamma_M25/jetToolbox_nano_m25signal.root"
	newline2 = "file:/cms/akobert/UL/Data/RunC/jetToolbox_dataC2018_"+str(process)+".root"

	for line in template:
		newFile.write(line.replace(oldline1, newline1).replace(oldline2, newline2))
 
	newFile.close()
	template.close()
