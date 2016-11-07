
def main():
    tot = 0
    aa,bb = 0,0
    for a in range(-999,999,1):
        for b in range(-1000,1000,1):
            res = get_total(a,b)
            print(a,b,res)
            if res > tot:
                aa,bb = a,b
                tot = res
    print('a,b,tot,prod: %d,%d,%d,%d' % (aa,bb,tot,aa*bb))

def get_total(a,b):
    flag = True
    tot = 0
    n = 0
    while flag:
        val = (n**2) + (a*n) + b
        if is_prime(val):
            tot+=1
        else:
            flag = False
        n+=1
    return tot

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

if __name__ == '__main__':
    main()
