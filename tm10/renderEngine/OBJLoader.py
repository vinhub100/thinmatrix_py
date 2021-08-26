
def loadObjModel(filename, loader):
    objFile = None
    vertices,textures,normals,indices = [],[],[],[]
    verticesArray,normalsArray,textureArray,indicesArray = [],[],[],[]

    try:
        with open(filename) as file:
            objFile = file.read()
    except Exception as e:
        print(e ,"Unable to Open OBJ File")
    
    objFile = objFile.split("\n")

    for line in objFile:
        curLine = line.split(" ")
        if line.startswith("v "):
            vertices.append([float(curLine[1]),float(curLine[2]),float(curLine[3])])
        elif line.startswith("vt "):
            textures.append([float(curLine[1]),float(curLine[2])])
        elif line.startswith("vn "):
            normals.append([float(curLine[1]),float(curLine[2]),float(curLine[3])])
        elif line.startswith("f "):
            pass
    
    textureArray = [0.0] * (len(vertices)*2)
    normalsArray = [0.0] * (len(vertices) *3)

    def processVertex(vertexData):
        currentVertexPointer = int(vertexData[0])-1
        indices.append(currentVertexPointer)
        currentTex = textures[int(vertexData[1])-1]
        textureArray[currentVertexPointer*2] = currentTex[0]
        textureArray[currentVertexPointer*2+1] = currentTex[1]
        currentNorm = normals[int(vertexData[2])-1]
        normalsArray[currentVertexPointer * 3] = currentNorm[0]
        normalsArray[currentVertexPointer * 3 + 1] = currentNorm[1]
        normalsArray[currentVertexPointer * 3 + 2] = currentNorm[2]
        

    for line in objFile:
        if line.startswith("f "):
            curLine = line.split(" ")
            vertex1 = curLine[1].split("/")
            vertex2 = curLine[2].split("/")
            vertex3 = curLine[3].split("/")

            processVertex(vertex1)
            processVertex(vertex2)
            processVertex(vertex3)
    

    verticesArray = [item for sublist in vertices for item in sublist]
    indicesArray = indices
    
    return loader.loadToVAO(verticesArray,textureArray,indicesArray)

    