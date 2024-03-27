Note that the description below is not complete

# Celestial Mechanics 
Modelling solar systems using numerical methods and Newtonian physics. A PyGame is made to display the motion of the planets of our solar system. Different controls are added to speed up the simulation or to increase the gravitational force, or to change the perspective to where Earth is the centerpoint of the solar system. 

The most important law is the second law of motion: $\vec F=m\vec a$. In gravitational physics, the force applied between masses is quantified by the following formula.
$$\vec F = m\vec a = -G\frac{mM}{\vec r^2}$$
where the acceleration $\vec a$ is the second time-derivative of the position, $\frac{d^2\vec x(t)}{dt^2}=\vec a(t)$. Furthermore, $G$ is the gravitational constant. 

The implicit euler forward method is applied to get a reasonably stable numerical result. To do so, the second order ODE needs to be translated into a system of first order ODE's, which can be solved:
$$\frac{d\vec x(t)}{dt} = \vec v(t)$$
$$\frac{d\vec v(t)}{dt} =-G\frac{M}{\vec r^2}$$

When two distinct objects are close, i.e., their euclidean distance is smaller than a given contant, we model this as a collision.  Physical laws such as conservation of momentum need to be respected. In short, this means that the combined momentum before the collision must equal the momentum after the collision. Say the objects have masses $m_0$ and $m_1$ and velocity vectors $\vec v_0$ and $\vec v_1$. The total energy equals 
$$\vec m_{new}v_{new} = m_0\vec v_0 + m_1\vec v_1$$
After the collision, we assume the masses are combined and no other fragments are resulting from the collision. The new object has a mass of $m_0+m_1$, with momentum m_{new}\vec v_{new}. From this, the speed of the new object is computed:
$$\vec v_{new} = \frac{m_0\vec v_0 + m_1\vec v_1}{m_0+m_1}$$
Since each object is modelled as a point mass, the new objects location also needs a position. By convention, this is chosen to be the midpoint of the two objects: $\frac12(\vec x_0+\vec x_1)$.
