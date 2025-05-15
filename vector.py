# This file contains the Python code to represent vectors in 3D space
import numpy as np

class Vector:

  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  @staticmethod
  def newVectorFromNpArray(np_array):
    """
    Args:
      np_array | A numpy array, of type float/integer, of the following form (x, y, z)
    
    Returns:
      A new instance of the Vector class, where x is np_array[0], y is np_array[1], and z is np_array[2]
    """
    return Vector(x=np_array[0], y=np_array[1], z=np_array[2])


  def getVectorComponents(self):
    """
    Args:
      None
    
    Returns:
      The x, y, and z components of the invoking Vector instance, in that order. You can imagine the returned data as a tuple of the form (x, y, z).
      
    """
    return self.x, self.y, self.z

  def toNpArray(self):
    """
    Args:
      None
    
      Returns:
        A numpy array, of the form (x,y,z), where x, y, and z are the x, y, and z components of the invoking Vector instance.
    """
    array_version_of_vector = [self.x, self.y, self.z]
    return np.array(array_version_of_vector)
