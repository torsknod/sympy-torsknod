# Check the plot docstring

from sympy import *
from sympy.plotting.newplot import plot

lx = range(5)
ly = [i**2 for i in lx]

x = Symbol('x')
y = Symbol('y')
u = Symbol('u')
v = Symbol('v')
expr = x**2 - 1

a = plot(lx, ly)  # list plot
b = plot(expr, (x, 2, 4)) # cartesian plot
c = plot((lx, ly), (expr, (x, 2, 4)), ('x*cos(x)', 'x*sin(x)', (x, 0, 15))) # list, cartesian and parametric plot
#d = plot(1/(x**2+y**2+1), (x, -10, 10), (y, -10, 10), 'contour') # contour plot
e = plot(exp(-x),(x, 0, 4)) # cartesian plot (and coloring, see below)
f = plot(sin(x), cos(x), x, (x,0,10))  # 3d parametric line plot
g = plot(sin(x)*cos(y), (x, -5, 5), (y, -10, 10)) # 3d surface cartesian plot
h = plot(cos(u)*v,sin(u)*v,u,(u,0,10),(v,-2,2)) # 3d parametric surface plot

#for p in [a,b,c,d,e,f,g,h]:
for p in [a,b,c,e,f,g,h]:
    p.show()

# Some global options
if 'c' in globals().keys():
    c.title = 'Big nice title'
    e.xlabel = 'my argument'
    e.ylabel = 'my function'
    c.legend = True
    c.axis_center = (0, 0)
    c.show()

# Some aesthetics
if 'e' in globals().keys():
    e[0].line_color = lambda x : x/4
    e.show()
if 'f' in globals().keys():
    f[0].line_color = lambda x, y, z : z/10
    f.show()
if 'g' in globals().keys():
    g[0].surface_color = lambda x, y : sin(x)
    g.show()

# To show what happens when the backend is even simpler
if 'a' in globals().keys() and 'b' in globals().keys():
    from sympy.plotting.newplot import TextBackend
    a.backend = TextBackend
    b.backend = TextBackend
    try:
        a.show() # Error raised by the backend.
    except:
        pass
    b.show()
    b.title = 'Blah' # Warning is raised on next show
    b.show()

# Some more stuff on aesthetics - coloring wrt coordinates or parameters
param_line_2d = plot((x*cos(x), x*sin(x), (x, 0, 15)), (1.1*x*cos(x), 1.1*x*sin(x), (x, 0, 15)))
param_line_2d[0].line_color = lambda u : sin(u) # parametric
param_line_2d[1].line_color = lambda u, v : u**2 + v**2 # coordinates
param_line_2d.title = 'The inner one is colored by parameter and the outher one by coordinates'
param_line_2d.show()

param_line_3d = plot((x*cos(x), x*sin(x), x, (x, 0, 15)),
                     (1.5*x*cos(x), 1.5*x*sin(x), x, (x, 0, 15)),
                     (2*x*cos(x), 2*x*sin(x), x, (x, 0, 15)))
param_line_3d[0].line_color = lambda u : u #parametric
param_line_3d[1].line_color = lambda u, v : u*v # first and second coordinates
param_line_3d[2].line_color = lambda u, v, w : u*v*w # all coordinates
param_line_3d.show()