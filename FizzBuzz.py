def data_type(n):
  if isinstance(n, str):
    return len(n)
  elif isinstance(n, bool):
    return n
  elif n is None:
    return 'no value'
  elif isinstance(n, int):
    if n < 100:
      return 'less than 100'
    elif n == 100:
      return 'equal to 100'
    else:
      return 'more than 100'
  elif isinstance(n, list):
    if len(n) <= 2:
      return None
    else:
      return n[2]
  else:
    None