import os, sys

try:
    Finput = sys.argv[1]
except IndexError:
    Finput = ""

try:
    Foutput = sys.argv[2]
except IndexError:
    Foutput = ""

def Ahelp():
    print("NetpbmKonv v0.9 by KoleckOLP, MobilePony Inc.\n\n" +
          "main.py \"input_file\" \"output_file\"\n\n" +
          "supported: .pbm, .pgm, .ppm (all in ASCII only)")

def Fconvert(inpt="", outp=""): #inpt says the input type, outp output type 
    PicData = [] # for deleting comments
    EdtData = [] # for removing heaqder
    FnlData = []
    pbmline = ""
    j = 0
    lein = []
    loin = []

    f = open(Finput, "r") # opening the input file as read
    lines = f.read().splitlines() # reading all lines into an array without new lines

    f2 = open(Foutput, "w") # opening output file as write
    if "pbm" in os.path.splitext(Foutput)[1].lower(): # PBM
        f2.write("P1\n# Converted by NetpbmKonv https://github.com/KoleckOLP/NetpbmKonv KoleckOLP, ArmoredMobilePony Inc. (C)2020\n") 
    elif "pgm" in os.path.splitext(Foutput)[1].lower(): # PGM
        f2.write("P2\n# Converted by NetpbmKonv https://github.com/KoleckOLP/NetpbmKonv KoleckOLP, ArmoredMobilePony Inc. (C)2020\n")
    else: #PPM (other files don't get here)
        f2.write("P3\n# Converted by NetpbmKonv https://github.com/KoleckOLP/NetpbmKonv KoleckOLP, ArmoredMobilePony Inc. (C)2020\n") 

    for line in lines: # removing comment lines from input
        if line[:1] != "#":
            PicData = PicData + [line]

    if PicData[0] in ["P2", "P3"]: # checking if PGM or PPM to fing the limit
        try:
            splitted = PicData[1].split(" ")
            limit = splitted[2]
            for i, line in enumerate(PicData): # removes the header
                if i > 1:
                    EdtData = EdtData + [line]
        except IndexError:
            limit = PicData[2]
            for i, line in enumerate(PicData): # removes the header
                if i > 2:
                    EdtData = EdtData + [line]
    else:
        limit = ""
        for i, line in enumerate(PicData): # removes the header
            if i > 1:
                EdtData = EdtData + [line]

    print(EdtData)

    if "pbm" in os.path.splitext(Finput)[1].lower() and "pgm" in os.path.splitext(Foutput)[1].lower():
        print("pbm to pgm")
        f2.write(f"{PicData[1]}\n")
        for i, data in enumerate(EdtData):
            for c in EdtData[i]:
                if c == "1":
                    output = "0\n"
                else:
                    output = "255\n"
                FnlData = FnlData+[output]
    elif "pbm" in os.path.splitext(Finput)[1].lower() and "ppm" in os.path.splitext(Foutput)[1].lower():
        f2.write(f"{PicData[1]}\n")
        for i, data in enumerate(EdtData):
            for c in EdtData[i]:
                if c == "1":
                    output = "0\n"
                else:
                    output = "255\n"
                FnlData = FnlData+[output]
    elif "pgm" in os.path.splitext(Finput)[1].lower() and "pbm" in os.path.splitext(Foutput)[1].lower():
        f2.write(f"{PicData[1]}\n{limit}\n")
        for i, data in enumerate(EdtData):
            if j == 70:
                j = 0
                FnlData = FnlData+[pbmline+"\n"]
                pbmline = ""
            if int(data) > -1 and int(data) < 128:
                output = "1"
            else: #elif int(data) > 128 and int(data) < 256:
                output = "0"
            j=j+1
            pbmline = pbmline + output
    elif "pgm" in os.path.splitext(Finput)[1].lower() and "ppm" in os.path.splitext(Foutput)[1].lower():
        f2.write(f"{PicData[1]}\n{limit}\n")
        for i, data in enumerate(PicData):
            output = f"{data}\n{data}\n{data}\n"
            FnlData = FnlData+[output]
    elif "ppm" in os.path.splitext(Finput)[1].lower() and "pbm" in os.path.splitext(Foutput)[1].lower():
        f2.write(f"{PicData[1]}\n{limit}\n")
        for line in EdtData:
            if j < 3:
                loin = loin + [line]
                j=j+1
            if len(loin) == 3:
                j = 0
                lein = lein + [round((int(loin[0]) + int(loin[1]) + int(loin[2])) / 3)]
                loin = []
            j = 0
        for i, data in enumerate(lein):
            if j == 70:
                j = 0
                FnlData = FnlData+[pbmline+"\n"]
                pbmline = ""
            if int(data) > -1 and int(data) < 128:
                output = "1"
            else: #elif int(data) > 128 and int(data) < 256:
                output = "0"
            j=j+1
            pbmline = pbmline + output
    else: # ppm and pgm
        f2.write(f"{PicData[1]}\n{limit}\n")
        for line in EdtData:
            if j < 3:
                loin = loin + [line]
                j=j+1
            if len(loin) == 3:
                j = 0
                lein = lein + [round((int(loin[0]) + int(loin[1]) + int(loin[2])) / 3)]
                loin = []
        for i, data in enumerate(lein):
            output = str(data)+"\n"
            FnlData = FnlData+[output]

    for data in FnlData:
        f2.write(data)
    f2.close()


if Finput != "" and Foutput !="": # filters out files that are not Netpbm
    if "pbm" in os.path.splitext(Finput)[1].lower():
        if "pgm" in os.path.splitext(Foutput)[1].lower():
            Fconvert(os.path.splitext(Finput)[1], os.path.splitext(Foutput)[1])
        elif "ppm" in Foutput.lower():
            Fconvert(os.path.splitext(Finput)[1], os.path.splitext(Foutput)[1])
        else:
            print("wrong wrong output")
            Ahelp()
    elif "pgm" in os.path.splitext(Finput)[1].lower():
        if "pbm" in os.path.splitext(Foutput)[1].lower():
            Fconvert(os.path.splitext(Finput)[1], os.path.splitext(Foutput)[1])
        elif "ppm" in Foutput.lower():
            Fconvert(os.path.splitext(Finput)[1], os.path.splitext(Foutput)[1])
        else:
            print("wrong wrong output")
            Ahelp()
    elif "ppm" in os.path.splitext(Finput)[1].lower():
        if "pbm" in os.path.splitext(Foutput)[1].lower():
            Fconvert(os.path.splitext(Finput)[1], os.path.splitext(Foutput)[1])
        elif "pgm" in Foutput.lower():
            Fconvert(os.path.splitext(Finput)[1], os.path.splitext(Foutput)[1])
        else:
            print("wrong wrong output")
            Ahelp()
    else:
        print("wrong input")
        Ahelp()
else:
    Ahelp()






#print("write path to a pbm, pgm, ppm")
#picture = input("#")

'''
f = open(picture, "r")

lines = f.read().splitlines()

f.close()

PicData = []
EditedData = []

if "P1" in lines[0]:
    print("1. to pgm 2. to ppm")
    cmd = input("#")
    if cmd ==  "1": #PGM
        name = os.path.splitext(picture)[0]
        name = name+"_pbm.pgm"
        f2 = open(name, "w")
        f2.write("P2\n# Jsem mega funny KoleckOLP 2020 (C) Make it stop.\n")
        if "#" in lines[1]: #mrd tam má koment
            f2.write(lines[2]+" 255"+"\n")
            for i, line in enumerate(lines):
                if i > 2:
                    PicData = PicData + [line]
        else: #nemá takm koment :3
            f2.write(lines[1]+"\n")
            for i, line in enumerate(lines):
                if i > 1:
                    PicData = PicData + [line]
        for i, data in enumerate(PicData):
            for c in PicData[i]:
                if c == "1":
                    output = "0\n"
                else:
                    output = "255\n"
                EditedData = EditedData+[output]
        for data in EditedData:
            f2.write(data)
        f2.close()
    elif(cmd == "2"): ##PPM
        name = os.path.splitext(picture)[0]
        name = name+"_pbm.ppm"
        f2 = open(name, "w")
        f2.write("P3\n# Jsem mega funny KoleckOLP 2020 (C) Make it stop.\n")
        if "#" in lines[1]: #mrd tam má koment
            f2.write(lines[2]+" 255"+"\n")
            for i, line in enumerate(lines):
                if i > 2:
                    PicData = PicData + [line]
        else: #nemá takm koment :3
            f2.write(lines[1]+"\n")
            for i, line in enumerate(lines):
                if i > 1:
                    PicData = PicData + [line]
        for i, data in enumerate(PicData):
            for c in PicData[i]:
                if c == "1":
                    output = "0\n0\n0\n"
                else:
                    output = "255\n255\n255\n"
                EditedData = EditedData+[output]
        for data in EditedData:
            f2.write(data)
        f2.close()

j = 0
pbmline = ""
    
if "P2" in lines[0]:
    print("1. to pbm 2. to ppm")
    cmd = input("#")
    if cmd == "1": #PBM
        name = os.path.splitext(picture)[0]
        name = name+"_pgm.pbm"
        f2 = open(name, "w")
        f2.write("P1\n# Jsem mega funny KoleckOLP 2020 (C) Make it stop.\n")
        if "#" in lines[1]: #mrd tam má koment
            f2.write(lines[2]+"\n")
            for i, line in enumerate(lines):
                if i > 3:
                    PicData = PicData + [line]
        else: #nemá takm koment :3
            f2.write(lines[1]+"\n")
            for i, line in enumerate(lines):
                if i > 2:
                    PicData = PicData + [line]
        for i, data in enumerate(PicData):
            if j == 70:
                j = 0
                EditedData = EditedData+[pbmline+"\n"]
                pbmline = ""
            if int(data) > -1 and int(data) < 128:
                output = "1"
            else: #elif int(data) > 128 and int(data) < 256:
                output = "0"
            j=j+1
            pbmline = pbmline + output
        for data in EditedData:
            f2.write(data)
        f2.close()
    elif cmd == "2": #PPM
        name = os.path.splitext(picture)[0]
        name = name+"_pgm.ppm"
        f2 = open(name, "w")
        f2.write("P3\n# Jsem mega funny KoleckOLP 2020 (C) Make it stop.\n")
        if "#" in lines[1]: #mrd tam má koment
            f2.write(lines[2]+" 255"+"\n")
            for i, line in enumerate(lines):
                if i > 3:
                    PicData = PicData + [line]
        else: #nemá takm koment :3
            f2.write(lines[1]+"\n")
            for i, line in enumerate(lines):
                if i > 2:
                    PicData = PicData + [line]
        for i, data in enumerate(PicData):
            output = f"{data}\n{data}\n{data}\n"
            EditedData = EditedData+[output]
        for data in EditedData:
            f2.write(data)
        f2.close()

j = 0
loin = []
lein = []

if "P3" in lines[0]:
    print("1. to pbm 2. to pgm")
    cmd = input("#")
    if cmd == "1": #PBM
        name = os.path.splitext(picture)[0]
        name = name+"_ppm.pbm"
        f2 = open(name, "w")
        f2.write("P1\n# Jsem mega funny KoleckOLP 2020 (C) Make it stop.\n")
        if "#" in lines[1]: #mrd tam má koment
            f2.write(lines[2]+"\n")
            for i, line in enumerate(lines):
                if i > 3:
                    if j < 3:
                        loin = loin + [line]
                        j=j+1
                    if len(loin) == 3:
                        j = 0
                        lein = lein + [round((int(loin[0]) + int(loin[1]) + int(loin[2])) / 3)]
                        loin = []
        else: #nemá takm koment :3
            f2.write(lines[1]+"\n")
            for i, line in enumerate(lines):
                if i > 2:
                    if j < 3:
                        loin = loin + [line]
                        j=j+1
                    if len(loin) == 3:
                        j = 0
                        lein = lein + [round((int(loin[0]) + int(loin[1]) + int(loin[2])) / 3)]
                        loin = []
        j = 0
        for i, data in enumerate(lein):
            if j == 70:
                j = 0
                EditedData = EditedData+[pbmline+"\n"]
                pbmline = ""
            if int(data) > -1 and int(data) < 128:
                output = "1"
            else: #elif int(data) > 128 and int(data) < 256:
                output = "0"
            j=j+1
            pbmline = pbmline + output
        for data in EditedData:
            f2.write(data)
        f2.close()
    elif cmd == "2": #PGM
        name = os.path.splitext(picture)[0]
        name = name+"_ppm.pgm"
        f2 = open(name, "w")
        f2.write("P2\n# Jsem mega funny KoleckOLP 2020 (C) Make it stop.\n")
        if "#" in lines[1]: #mrd tam má koment
            f2.write(lines[2]+" 255"+"\n")
            for i, line in enumerate(lines):
                if i > 3:
                    if j < 3:
                        loin = loin + [line]
                        j=j+1
                    if len(loin) == 3:
                        j = 0
                        lein = lein + [round((int(loin[0]) + int(loin[1]) + int(loin[2])) / 3)]
                        loin = []
        else: #nemá takm koment :3
            f2.write(lines[1]+"\n")
            for i, line in enumerate(lines):
                if i > 2:
                    if j < 3:
                        loin = loin + [line]
                        j=j+1
                    if len(loin) == 3:
                        j = 0
                        lein = lein + [round((int(loin[0]) + int(loin[1]) + int(loin[2])) / 3)]
                        loin = []       
        for i, data in enumerate(lein):
            output = str(data)+"\n"
            EditedData = EditedData+[output]
        for data in EditedData:
            f2.write(data)
        f2.close()
'''