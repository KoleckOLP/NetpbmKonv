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