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