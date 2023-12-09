# celestial_mechanics
Modelling solar systems using numerical methods and Newtonian physics. A PyGame is made to display the motion of the planets of our solar system. Different controls are added to speed up the simulation or to increase the gravitational force, or to change the perspective to where Earth is the centerpoint of the solar system. 

The most important law is the second law of motion: $F=ma$. In gravitational physics, the force applied between masses is quantified by the following formula.
$$F = ma = -G\frac{mM}{r^2}$$
where the acceleration $a$ is the second time-derivative of the position, $\frac{d^2x(t)}{dt^2}=a(t)$. Furthermore, $G$ is the gravitational constant.

The implicit euler forward method is applied to get a reasonably stable numerical result. To do so, the second order ODE needs to be translated into a system of first order ODE's, which can be solved:
$$\frac{dx(t)}{dt} = v(t)\\
\frac{dv(t)}{dt} = a(t) = -G\frac{mM}{r^2}$$




When two distinct objects are close, i.e., their euclidean distance is smaller than a given contant, we model this as a collision.  Physical laws such as conservation of momentum need to be respected. In short, this means that the combined momentum before the collision must equal the momentum after the collision. Say the objects have masses $m_0$ and $m_1$ and velocity vectors $v_0$ and $v_1$. The total energy equals 
$$m_{new}v_{new} = m_0v_0 + m_1v_1$$
After the collision, we assume the masses are combined and no other fragments are resulting from the collision. The new object has a mass of $m_0+m_1$, with momentum m_{new}v_{new}. From this, the speed of the new object is computed:
$$v_{new} = \frac{m_0v_0 + m_1v_1}{m_0+m_1}$$
Since each object is modelled as a point mass, the new objects location also needs a position. By convention, this is chosen to be the midpoint of the two objects: $\frac12(x_0+x_1)$.
