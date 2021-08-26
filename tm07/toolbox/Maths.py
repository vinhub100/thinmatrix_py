import numpy as np
import pyrr


class Maths:
    def createTransformationMatrix(self, translation, rx, ry, rz, scale):
        myarix = pyrr.matrix44.create_identity()

        scaleMat = pyrr.matrix44.create_from_scale(pyrr.Vector3([scale,scale,scale]))
        myarix = pyrr.matrix44.multiply(scaleMat, myarix)

        rotX = pyrr.matrix44.create_from_x_rotation(np.deg2rad(rx))
        rotY = pyrr.matrix44.create_from_x_rotation(np.deg2rad(ry))
        rotZ = pyrr.matrix44.create_from_x_rotation(np.deg2rad(rz))
        myarix = pyrr.matrix44.multiply(myarix, rotX )
        myarix = pyrr.matrix44.multiply(myarix, rotY )
        myarix = pyrr.matrix44.multiply(myarix, rotZ )
        
        trans = pyrr.matrix44.create_from_translation(pyrr.Vector3(translation))
        myarix = pyrr.matrix44.multiply( myarix , trans)
        print(type(myarix))
        return myarix
        