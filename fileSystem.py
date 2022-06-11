def openFile(path, inputVar):
    f = open(path)
    compile(inputVar + "=" + f.read())
    f.close()
    