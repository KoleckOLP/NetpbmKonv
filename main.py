import os

print("write path to a pbm, pgm, ppm")
picture = input("#")

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