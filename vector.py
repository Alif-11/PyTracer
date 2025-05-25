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
    For when our Vector is on the right side of the add symbol.

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
  
  def __radd__(self, other):
    """
    For when our Vector is on the right side of the add symbol.

    Args:
      other | To be added to this Vector. Has to be of type Vector, int, or float.
    
    Returns:
      A new Vector that results from adding other to this Vector.
    """
    if isinstance(other, Vector):
      return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    elif isinstance(other, (int, float)):
      return Vector(self.x + other, self.y + other, self.z + other)
    else:
      raise TypeError(f"Type '{type(other)}' cannot be added to type 'Vector'.")
  

  def __sub__(self, other):
    """
    For when our Vector is on the left side of the add symbol.

    Args:
      other | To be subtracted from this Vector. Has to be of type Vector, int, or float.
    
    Returns:
      A new Vector that results from subtractiong other from this Vector.
    """
    if isinstance(other, Vector):
      return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    elif isinstance(other, (int, float)):
      return Vector(self.x - other, self.y - other, self.z - other)
    else:
      raise TypeError(f"Type '{type(other)}' cannot be subtracted from type 'Vector'.")
  
  def __rsub__(self, other):
    """
    For when our Vector is on the right side of the add symbol.

    Args:
      other | To be subtracted from this Vector. Has to be of type Vector, int, or float.
    
    Returns:
      A new Vector that results from subtractiong other from this Vector.
    """
    if isinstance(other, Vector):
      return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    elif isinstance(other, (int, float)):
      return Vector(self.x - other, self.y - other, self.z - other)
    else:
      raise TypeError(f"Type 'Vector' cannot be subtracted from type '{type(other)}'.")
  

  def invert(self):
    """
    Args:
      None

    Returns:
      A new Vector whose components are the negative versions of this Vector's components.
    """
    return Vector(-1*self.x, -1*self.y, -1*self.z)

  def __mul__(self, other):
    """
    For when our Vector is on the left side of the multiplication symbol.

    Args:
      other | A scalar value, that will be multiplied to each component of this vector. Has to be of type int or float
      

    Returns:
      A new vector, which is just (other * [the self vector])
    """
    if isinstance(other, (int, float)):
      return Vector(self.x * other, self.y * other, self.z * other)
    else:
      raise TypeError(f"Type 'Vector' cannot be multiplied by non scalar type {type(other)}.")
  
  def __rmul__(self, other):
    """

    For when our Vector is on the right side of the multiplication symbol.

    Args:
      other | A scalar value, that will be multiplied to each component of this vector. Has to be of type int or float
      

    Returns:
      A new vector, which is just (other * [the self vector])
    """
    if isinstance(other, (int, float)):
      return Vector(self.x * other, self.y * other, self.z * other)
    else:
      raise TypeError(f"Type 'Vector' cannot be multiplied by non scalar type {type(other)}.")
  
  def euclideanDistance(self, other):
    """
    Args:
      other | A Vector. We will take the Euclidean distance between the invoking Vector and the 'other' Vector.
    
    Returns:
      A scalar value, most likely float, that represents the Euclidean distance between the invoking Vector and the 'other' Vector.
    """
    if isinstance(other, Vector):
      return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)
    else:
      raise TypeError(f"Type 'Vector' cannot have a Euclidean distance with non Vector type {type(other)}.")
  
  def magnitude(self):
    """
    Args:
      None
    
    Returns:
      The magnitude of this Vector.
    """
    return np.sqrt(self.x**2 + self.y**2 + self.z**2)

  def dotProduct(self, other):
    """
    Args:
      other | The Vector, along with this Vector, to take the dot product with
    
    Returns:
      The dot product between this Vector and the other Vector.
    """
    if isinstance(other, Vector):
      return (self.x*other.x + self.y*other.y + self.z*other.z)
    else:
      raise TypeError(f"Type 'Vector' cannot have a dot product with non Vector type {type(other)}.")
  
  def angleBetween(self, other):
    """
    Args:
      other | The Vector, along with this Vector, to find the angle between.
    
    Returns:
      The angle between this Vector and the other Vector.
    """
    if isinstance(other, Vector):
      cos_angle = self.dotProduct(other) / (self.magnitude() * other.magnitude())
      return np.arccos(cos_angle)
    else:
      raise TypeError(f"Type 'Vector' cannot have an angle between non Vector type {type(other)}.")
  
  def reflectOver(self, other):
    """
    Args:
      other | The Vector to reflect this Vector over.
    
    Returns:
      The reflected version - of this Vector - over the other Vector. Note that a new Vector is returned.
    """
    if isinstance(other, Vector):
      return ( (2 * (self.dotProduct(other) / other.magnitude()) * other) - self)
    else:
      raise TypeError(f"Type 'Vector' cannot have be reflected over non Vector type {type(other)}.")
  
  def crossProduct(self, other):
    """
    Args:
      other | The Vector, along with this Vector, to take the cross product with.
    
    Returns:
      The cross product between this Vector and the other Vector. Note that a Vector is returned.
    """
    if isinstance(other, Vector):
      return Vector(self.y * other.z - self.z * other.y,
                    self.z * other.x - self.z * other.z,
                    self.x * other.y - self.y * other.x)
    else:
      raise TypeError(f"Type 'Vector' cannot have a cross product with non Vector type {type(other)}.")
  
  def normalize(self):
    """
    Args:
      None
    
    Returns:
      The normalized version of this Vector. note that a new Vector is returned.
    """
    normalizing_denominator = self.magnitude()
    x,y,z = self.getComponents()
    return Vector(x/normalizing_denominator, y/normalizing_denominator, z/normalizing_denominator)
  
  def multiplyVectorByNpMatrix(self, other):
    """
    Args:
      other | The NumPy matrix to multiply with this Vector.
    
    Returns:
      A new Vector, that is the result of multiplying the invoking vector with the other Vector.
    """
    if isinstance(other, np.ndarray):
      assert other.shape == (3,3), f"Shape of np.ndarray variable 'other' must be (3,3). The actual shape of other is {other.shape} instead."
      return Vector.newVectorFromNpArray(np.matmul(self.toNpArray(), other))
    else:
      raise TypeError(f"Type 'Vector' cannot be multiplied with non NumPy-matrix type {type(other)}.")

  def rotate(self, angles):
    """
    Args:
      angles | A (1,3) NumPy array, where elements at indices 0, 1, and 2 are the amounts we want to rotate our Vector by in the x, y, and z axes respectively. Please note that we are rotating about the local axes of the vector, not the global axes of the global coordinate system.    
    Returns:
      A new Vector, that is the result of rotating this Vector by the angles specified in the 'angles' parameter.
    """
    if isinstance(angles, np.ndarray):
      assert angles.shape == (3,), f"Shape of np.ndarray variable 'angles' must be (3,). The actual shape of angles is {angles.shape} instead."
      x, y, z = angles
      rotation_matrix = np.array([ 
        [np.cos(z)*np.cos(y)*np.cos(x) - np.sin(z)*np.sin(x), 
        np.cos(z)*np.cos(y)*np.sin(x) + np.sin(z)*np.cos(x), 
        np.cos(z)*np.sin(y)],
        [-np.sin(z)*np.cos(y)*np.cos(x) - np.cos(z)*np.sin(x),
        -np.sin(z)*np.cos(y)*np.sin(x) + np.cos(z)*np.cos(x),
        np.sin(z)*np.sin(y)],
        [np.sin(y)*np.cos(x),
        np.sin(y)*np.sin(x),
        np.cos(y)]
      ])
      return self.multiplyVectorByNpMatrix(rotation_matrix)
    else:
      raise TypeError(f"Type 'Vector' cannot be rotated by non NumPy-array type {type(angles)}.")

    

