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


  def getComponents(self):
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
  
  def __add__(self, other):
    """
    Args:
      other: To be added to this Vector. Has to be of type Vector, int, or float.
    
    Returns:
      A new Vector that results from adding other to this Vector.
    """
    if isinstance(other, Vector):
      return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    elif isinstance(other, (int, float)):
      return Vector(self.x + other, self.y + other, self.z + other)
    else:
      raise TypeError(f"Type 'Vector' cannot be added to type '{type(other)}'.")
  

  def __sub__(self, other):
    """
    Args:
      other: To be subtracted from this Vector. Has to be of type Vector, int, or float.
    
    Returns:
      A new Vector that results from subtractiong other from this Vector.
    """
    if isinstance(other, Vector):
      return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    elif isinstance(other, (int, float)):
      return Vector(self.x - other, self.y - other, self.z - other)
    else:
      raise TypeError(f"Type '{type(other)}' cannot be subtracted from type 'Vector'.")
  

  def invert(self):
    """
    Args:
      None

    Returns:
      A new Vector whose components are the negative versions of this Vector's components.
    """
    return Vector(-1*self.x, -1*self.y, -1*self.z)
  

