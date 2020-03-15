from random import choice
from string import ascii_uppercase, ascii_lowercase, digits

def random_password_generator(size = 10):
  sample_set = ascii_uppercase + ascii_lowercase + digits
  def generate_password():
    password = ''.join([choice(sample_set) for i in range (size)])
    return password
  
  return generate_password