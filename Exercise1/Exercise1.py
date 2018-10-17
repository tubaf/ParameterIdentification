'''
========================================================================
Exercise1.py
------------------------------------------------------------------------
solve an unconstrained optimization problem using the steepest decent
method with a line search algorithm and optimal step size
========================================================================
'''
#
# imports
#
import numpy as np
import matplotlib.pyplot as plt
#
# helper functions for line search
#
def ga(x,g,a,s):
  '''
  ======================================================================
  evaluate line search gradient dg/da
  g(x+a*s)=g(x)*s
  ----------------------------------------------------------------------
  x: start point of line 
  g: gradient function to evaluate (callable)
  a: step size
  s: line direction
  ----------------------------------------------------------------------
  return: gradient along a
  ======================================================================
  '''
  y=np.dot(s,g(x+a*s))
  return y

def ha(x,h,a,s):
  '''
  ======================================================================
  evaluate line search hessian d2g/da2
  h(x+a*s)=s*h(x)*s
  ----------------------------------------------------------------------
  x: start point of line 
  h: hessian function to evaluate (callable)
  a: step size
  s: line direction
  ----------------------------------------------------------------------
  return: hessian along a
  ======================================================================
  '''
  y=np.einsum('i,ij,j',s,h(x+s*a),s)
  return y
	
def plotfunc(f,opt=[0,0],n=[101,101,11],xlim=[0,6],ylim=[0,6],zlim=[0.1,250],levels=[0.1,0.2,0.5,1,2,5,10,20,40],fmt='%.0f',title=r'f(x)',figsize=(8,8),dpi=72):
  '''
  ======================================================================
  plot 2d objective function as contour plot
  ----------------------------------------------------------------------
  f: function 2d (callable)
  opt: [x,y] position of minimum
  n: [nx,ny,nz] resolution and number of contours
  xlim: [xmin,xmax]
  ylim: [ymin,ymax]
  zlim: [zmin,zmax]
  figsize: (xsize,ysize) in inches
  dpi: screen resolution in dots per inches (adapt to your screen) 
  ======================================================================
  '''
  #
  import matplotlib.colors as col
  abq = col.LinearSegmentedColormap.from_list("abq", [(0,0,1),(0,1,1),(0,1,0),(1,1,0),(1,0,0)],N=256)
  #
  x=np.linspace(xlim[0],xlim[1],n[0])
  y=np.linspace(ylim[0],ylim[1],n[1])
  X,Y=np.meshgrid(x,y)
  Z=f([X,Y])
  #
  if not levels:
    levels=np.geomspace(zlim[0],zlim[1],n[2])
  plt.figure(figsize=figsize,dpi=dpi)
  CP=plt.contour(X,Y,Z,cmap=abq,levels=levels)
  LP=plt.plot([opt[0]],[opt[1]],color='red',marker='x',linewidth=2,markersize=12,markeredgewidth=2)
  plt.clabel(CP,inline=True,fmt=fmt)
  plt.title(title)
  plt.xlabel(r'$x_0$', fontsize=0.2*dpi)
  plt.ylabel(r'$x_1$', fontsize=0.2*dpi)
  plt.grid()
#
# line search algorithm
#
def line_search_newton(x,f,g,fa,ga,s,gtol=1e-8,a=0):
  '''
  ======================================================================
  find root of f along direction s using newtons algorithm
  ----------------------------------------------------------------------
  x: start point
  f: function to evaluate (callable)
  g: gradient function to evaluate (callable)
  fa: function to evaluate f(x+a*s) (callable)
  ga: function to evaluate g(x+a*s) (callable)
  s: search direction
  gtol: stop criterion (g < gtol)
  a: initial step size
  ----------------------------------------------------------------------
  return: optimal step size
  ======================================================================
  '''
  #
  # code to compute optimal step size a
  #
  return aopt

#
# steepest decent algorithm
#
def steepest(x,f,g,fa,ga,gtol=1e-8):
  '''
  ======================================================================
  steepest decent method
  ----------------------------------------------------------------------
  x: start value
  f: objective function (callable)
  g: gradient of f (callable)
  fa: function to evaluate f(x+a*s) (callable)
  ga: function to evaluate g(x+a*s) (callable)
  gtol: stop criterion (g < gtol)
  ----------------------------------------------------------------------
  return: optimal point x which minimizes f(x)
  ======================================================================
  '''
  #
  # code for steepest decent method
  #
  return xopt
#
# main program
#
if __name__ == '__main__':

  def f(x):
    '''
    ====================================================================
    objective function
    --------------------------------------------------------------------
    x: point where to compute function value
    --------------------------------------------------------------------
    return: function value f(x)
    ====================================================================
    '''
    f=(x[0]-2*x[1])**2+(x[0]-2)**4
    return f

  def g(x):
    '''
    ====================================================================
    gradient of function
    --------------------------------------------------------------------
    x: point where to compute gradient
    --------------------------------------------------------------------
    return: gradient of f(x)
    ====================================================================		
    '''
    #
    # code for the gradient
    #
    return g

  def h(x):
    '''
    ====================================================================
    hessian of objective function
    -----------------------------
    x: point where to compute hessian
    --------------------------------------------------------------------
    return: hessian of f(x)
    ====================================================================		
    '''
    #
    # code for the gradient
    #
    return h

  plotfunc(f,opt=[2,1],n=[201,201,15],xlim=[-0,4],ylim=[-1,3],zlim=[0.1,25],fmt='%.1f',title=r'$f(x)=(x_0-2x_1)^2+(x_0-2)^4$')
  plt.show()
