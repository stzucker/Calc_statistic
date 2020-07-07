class SMO:
    # переменные
  g_u, t, g_a, n, m = 1, 1, 1, 1, 1
  
  def factorial(value):
    result = 1
    if value == 0: return result
    for iter in range(1, value + 1):
      result *= iter

    return result

class ManyChannel_SMO_unlimited_queue(SMO):
  pass

class ManyChannel_SMO_limited_queue(SMO):
  pass

class ManyChannel_SMO_with_denial(SMO):
  pass

class OneChannel_SMO_unlimited_queue(SMO):
  pass

class OneChannel_SMO_limited_queue(SMO):
  pass

class OneChannel_SMO_with_denial(SMO):
  pass
