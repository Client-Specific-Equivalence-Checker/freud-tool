from symbolic.args import *

def lib1(a, b):
    c=1
    if b < 0:
        i = 1
        while i <= b:
            c += a
            i += 1
    return c

def lib2(a, b):
    c=0
    if a < 0:
        i = 1
        while i <= a:
            c += b
            i += 1
    return c

@uninterp(lib=lambda *x : 0)
def loopunreach20(x):
	if x >= 18 and x < 22:
		return lib(x,20)
	return 0

def wrap(x, lib):
	if x >= 18 and x < 22:
		return lib(x,20)
	return 0

def check_counter(x):
  return (wrap(x, lib1), wrap(x, lib2))