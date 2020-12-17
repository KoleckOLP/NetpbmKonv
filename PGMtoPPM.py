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