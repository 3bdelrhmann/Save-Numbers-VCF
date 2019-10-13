from random import randrange
FileName = input(str('What is your file name :?: '))
while '.' in FileName:
    print("Please write file name without extention")
    FileName = input(str('What is your file name :?: '))
def MainFunc(ListFileName):
    try:
        Mobile_List_File = open(ListFileName+".txt",'r')
    except:
        print("Please check your file name,exist,..etc cannot opened this file")
    
    List_contents = Mobile_List_File.readline()
    OutoputFileName = 'YourContants-' + str(randrange(92399)) + '.VCF'
    with open(OutoputFileName,'w') as OutputFile:
        counter = 0
        while List_contents:
            counter += 1
            i = str(counter)
            OutputFile.write('BEGIN:VCARD\n')
            OutputFile.write('VERSION:3.0\n')
            OutputFile.write('FN:'+ListFileName+'-'+i+'\n')
            OutputFile.write('TEL:+2' + str(List_contents.strip())+'\n')
            OutputFile.write('END:VCARD'+'\n')
            List_contents = Mobile_List_File.readline()
        OutputFile.close()
        Mobile_List_File.close()
MainFunc(FileName)
