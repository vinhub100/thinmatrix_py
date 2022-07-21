import numpy as np
import pyrr


class Maths:
    def createTransformationMatrix(self, translation, rx, ry, rz, scale):
        myarix = pyrr.matrix44.create_identity()

        scaleMat = pyrr.matrix44.create_from_scale(pyrr.Vector3([scale,scale,scale]))
        myarix = pyrr.matrix44.multiply(scaleMat, myarix)

        rx,ry,rz = np.deg2rad(rx),np.deg2rad(ry),np.deg2rad(rz)
        rotX = pyrr.matrix44.create_from_x_rotation(rx)
        rotY = pyrr.matrix44.create_from_y_rotation(ry)
        rotZ = pyrr.matrix44.create_from_z_rotation(rz)
        myarix = pyrr.matrix44.multiply(myarix, rotX )
        myarix = pyrr.matrix44.multiply(myarix, rotY )
        myarix = pyrr.matrix44.multiply(myarix, rotZ )
        
        trans = pyrr.matrix44.create_from_translation(pyrr.Vector3(translation))
        myarix = pyrr.matrix44.multiply( myarix , trans)

        return myarix
        
    def createViewMatrix(self, camera):

        rx,ry,rz = np.deg2rad(camera.getPitch()),np.deg2rad(camera.getYaw()),np.deg2rad(camera.getRoll())
        # rotX = pyrr.matrix44.create_from_x_rotation(rx)
        # rotY = pyrr.matrix44.create_from_y_rotation(ry)
        # rotZ = pyrr.matrix44.create_from_z_rotation(rz)

        # viewMat = pyrr.matrix44.multiply(viewMat, rotX)
        # viewMat = pyrr.matrix44.multiply(viewMat, rotY)
        eu = pyrr.euler.create(-rx,0,ry)
        viewMat = pyrr.matrix44.create_from_eulers(eu)

        # viewMat = pyrr.matrix44.multiply(viewMat, rotZ )

        camPos = camera.getPosition()
        trans = pyrr.matrix44.create_from_translation(pyrr.Vector3([-camPos[0],-camPos[1],-camPos[2]]))
        viewMat = pyrr.matrix44.multiply(trans, viewMat)

        return viewMat




def barryCentric(p1, p2, p3, pos):
    det = (p2[2]-p3[2])*(p1[0]-p3[0])+(p3[0]-p2[0])*(p1[2]-p3[2])
    l1 = ((p2[2]-p3[2])*(pos[0]-p3[0])+(p3[0]-p2[0])*(pos[1]-p3[2]))/det
    l2 = ((p3[2]-p1[2])*(pos[0]-p3[0])+(p1[0]-p3[0])*(pos[1]-p3[2]))/det
    l3 = 1.0 - l1 - l2
    return l1 * p1[1] + l2 * p2[1] + l3 * p3[1]

