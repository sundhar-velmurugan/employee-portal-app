def get_items(data):
  keys, values = [], []
  for k, v in data.items():
    keys.append(k)
    values.append(v)
  keys = ', '.join(keys)

  return keys, values

def generate_placeholders(n):
  return ', '.join(['%s']*n)


def get_update_items(data):
  items = []
  for k, v in data.items():
    items.append(f"{k} = '{v}'")
  return ', '.join(items)


def get_table_name(type):
  return type.capitalize()+'Info'