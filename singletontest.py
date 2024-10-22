class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance
  
class SingletonChild(SingletonClass):
    pass
  
singleton = SingletonClass()  
child = SingletonChild()

print(child is singleton)


singleton.singl_variable = "Complex"
print(child.singl_variable)