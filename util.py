def get_items(data):
  keys, values = [], []
  for k, v in data.items():
    keys.append(k)
    values.append(v)
  keys = ', '.join(keys)

  return keys, values

def generate_placeholders(n):
  return ', '.join(['%s']*n)
