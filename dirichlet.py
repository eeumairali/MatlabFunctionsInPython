#dirichlet  function is not avaialable in python so you can use it for dirichlet(1,contant) and it will return you results of matlab

def dirichlet(a,b):
    z = np.zeros([int(b)])
    k = a / b
    z[:] = k
    return z
    
# example

class_hyper_prior = dirichlet(1,4);
# it will return [0.25 0.25 0.25 0.25 ]
