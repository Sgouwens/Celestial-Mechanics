import numpy as np
from itertools import permutations, combinations

G = 6.6743*1e-11
step_size = 360

class Celestial:
    """Class that generates planets and stars. Newtonian mechanics are
    implemented to make the planets interact with eachother in order to simulate
    the solar system and more."""
    
    def __init__(self, name: str, position, velocity, mass):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.position_step = 0
        self.velocity_step = 0
        self.position_new = 0
        self.velocity_new = 0
        self.old_positions = []
        self.collided = False
        self.color = (np.random.uniform(0,255), 
                      np.random.uniform(0,255) , 
                      np.random.uniform(0,255))
        
    #@jit    
    def gravitational_force(self, other, backward=False):
        """Using the law F = G*m1*m2/r^2 gravitational forces are computed"""
        
        # In case when a backward method is used         
        if backward:
            distance_vector = self.position_new - other.position_new
        else:
            distance_vector = self.position - other.position      
        
        distance = np.linalg.norm(distance_vector)
            
        # Calculate the gravitational force between the two masses
        force_magnitude = G * self.mass * other.mass / (distance ** 2)
        force_direction = distance_vector / distance
        
        return force_magnitude * force_direction
        
    # Easy numerical method that updates updates velocity and location
    def euler_forward(self, other, stepsize=step_size, backward=False):
        """Given the gravitational force, impact on velocity and position are approximated
        Summetry of forces is applied"""
        
        force = -self.gravitational_force(other, backward=backward)
        force_to_other = force / self.mass
        force_to_self = - force / other.mass
        
        self.velocity_step = self.velocity_step + stepsize * force_to_other
        self.position_step = self.position_step + stepsize * self.velocity            
        other.velocity_step = other.velocity_step + stepsize * force_to_self
        other.position_step = other.position_step + stepsize * other.velocity
        
    def apply_gravitational_forces(self, backward=False):
        """Given the gravitational effects of all other entities, the velocity
        and position are updated simultaneously"""
        
        if backward:
            self.position_new = self.position + self.position_step
            self.velocity_new = self.velocity + self.velocity_step
            self.position_step = 0
            self.velocity_step = 0  
        else:
            self.position = self.position + self.position_step
            self.velocity = self.velocity + self.velocity_step
            self.position_step = 0
            self.velocity_step = 0  
        
    def collision(self, other):
        """This function kills dinosaurs. Self gains mass of the planet it
        collided with, conservation of momentum is used to determine the new 
        velocity vector."""
        if np.linalg.norm(self.position - other.position) < 4e9: # use radii.
        
            if not other.collided:
                print('Oh no!', self.name, 'collided with', other.name)
                self.mass = self.mass + other.mass
                self.velocity = (self.mass*self.velocity + other.mass*other.velocity)/(self.mass+other.mass)
                self.position = (self.position + other.position)/2
                other.collided = True
               
        
class System:
    """The class Celestial defines behaviour of individual objects with respect to others,
    This class contains the functions that apply the individual behaviour to all objects
    to model the groups behaviour."""
    
    def __init__(self, names, positions, velocities, masses, collisions=True):
        self.objects = [Celestial(name, position, velocity, mass) \
                        for name, position, velocity, mass \
                            in zip(names, positions,velocities, masses)]
            
        self.collisions = collisions

    def __add__(self, body):
        """This function should add an asteroid to the system"""
        pass
         
    def shoot_asteroid(self):
        """This function should add in the pygame on mouse-click"""
        pass
            
    def system_euler_forward(self, stepsize):
        """Applies the euler forward method to each object"""
        for obj1, obj2 in combinations(self.objects, 2):
            obj1.euler_forward(obj2, stepsize)
        
        for obj in self.objects:
            obj.apply_gravitational_forces() 
            
    def system_euler_backward(self, stepsize=step_size):
        """Having computed all effects, we need to apply the numerical method"""
        for obj1, obj2 in combinations(self.objects, 2):
            obj1.euler_forward(obj2, stepsize, backward=False) # saves in *_step
            
        for obj in self.objects:
            obj.apply_gravitational_forces(backward=True) 
                        
        for obj1, obj2 in combinations(self.objects, 2):
            obj1.euler_forward(obj2, stepsize, backward=True)
            
        for obj in self.objects:
            obj.apply_gravitational_forces(backward=False) 
           
        if self.collisions:
            for obj1, obj2 in combinations(self.objects, 2):
                obj1.collision(obj2)
            
    def remove_collided_bodies(self):
        """Removes all objects that have been collided. All mass is transferred
        to the other object involved in the collision, keeping the momentum constant"""
        collided_bodies = []
        for idx, body in enumerate(self.objects):
            if body.collided:
                collided_bodies.append(idx)
        return(collided_bodies)
     
        
