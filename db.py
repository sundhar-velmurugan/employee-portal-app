class MySQLConnection:
  def __init__(self, mysql_object):
    self.mysql_object = mysql_object
    self.connection = None
  
  def __enter__(self):
    self.connection = self.mysql_object.connect()
    return self.connection

  def __exit__(self, *args):
    self.connection.close()