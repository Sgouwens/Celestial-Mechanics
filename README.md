# celestial_mechanics
Modelling solar systems using numerical methods and Newtonian physics. 

$$
F = ma = -G\frac{mM}{r^2}
$$

When two distinct objects are close, i.e., their euclidean distance is smaller than a given contant, we model this as a collision.  Physical laws such as conservation of momentum need to be respected. In short, this means that the combined momentum before the collision must equal the momentum after the collision. Say the objects have masses $m_0$ and $m_1$ and velocity vectors $v_0$ and $v_1$. The total energy equals 
$$m_{new}v_{new} = m_0v_0 + m_1v_1$$
After the collision, we assume the masses are combined and no other fragments are resulting from the collision. The new object has a mass of $m_0+m_1$, with momentum m_{new}v_{new}. From this, the speed of the new object is computed:
$$v_new = /frac{m_0v_0 + m_1v_1}{m_0+m_1}$$
