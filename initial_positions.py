import numpy as np

"""Three possible solar systems are pre-defined.
1) The solar system we live in, with random starting positions
2) A random system (placeholder) to function as a gass bubble, current consensus is that giant gas clouds
    form a system of planets and stars by having multiple groups of particles accumulating. this can be simulated
    although extremely computationally intensive
3) An experiment where we can make multiple-sun systems.

Future idea: Make a system that exploits gravitational pull. This concept helps us to bring satellites in 
orbit around other planets. Sending a satellite to the position that it gets behind a planet and speeds up
by the gravitation of the planet and leaving the 'orbit' later with extra speed. This appears to be difficult
and specific algorithms such as simulated annealing may help
"""

def initial_conditions(type = 'Solar System'):
    if type == 'Solar System':
        phi = np.random.uniform(0, 2*np.pi, 9)

        angles_position = [np.array([np.sin(angle),np.cos(angle)]) for angle in phi]
        angles_velocity = [np.array([np.cos(-angle),np.sin(-angle)]) for angle in phi]

        body_names = np.array(['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune' ])
        body_positions = 1e9*np.array([0, 57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867, 4515])
        body_positions = [distances*angles for angles, distances in zip(angles_position, body_positions)]

        body_velocities = 1000*np.array([0, 47.4, 35.0, 29.8, 24.1, 13.1, 9.7, 6.8, 5.4]) #
        body_velocities = [distances*angles for angles, distances in zip(angles_velocity, body_velocities)]

        body_masses = 1e24*np.array([19890000, 0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102])
        
    elif type == 'Random Solar System':
        n_objects = 200
        
        phi = np.random.uniform(0, np.pi, n_objects)

        angles_position = [np.array([np.sin(angle),np.cos(angle)]) for angle in phi]
        angles_velocity = [np.array([np.cos(-angle),np.sin(-angle)]) for angle in phi]

        body_names = ['Particle ' + str(k) for k in range(n_objects)]
        body_positions = 1e9*np.random.uniform(-10, 10, n_objects)
        body_positions = [distances*angles for angles, distances in zip(angles_position, body_positions)]

        body_velocities = 10*np.random.normal(0, 23, n_objects) #
        body_velocities = [distances*angles for angles, distances in zip(angles_velocity, body_velocities)]

        body_masses = 1e21*np.random.normal(40,5, n_objects)
        
        
    elif type == 'Multiple suns':
        number_of_suns = 4
        phi_suns = np.linspace(0,2*np.pi, num=number_of_suns+1)[:-1]

        phi = np.concatenate((phi_suns, np.random.uniform(0, 2*np.pi, 9)))

        angles_position = [np.array([np.sin(angle),np.cos(angle)]) for angle in phi]
        angles_velocity = [np.array([np.cos(-angle),np.sin(-angle)]) for angle in phi]

        msun, xsun, vsun = 3e7/number_of_suns, 20/np.sqrt(number_of_suns), 30*np.sqrt(number_of_suns) ####

        body_names = np.concatenate((np.array(number_of_suns*['Sun']), np.array(['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'])))
                              
        body_positions = 1e9*np.concatenate((xsun * np.ones(number_of_suns), np.array([57.9, 108.2, 149.6, 228.0, 778.5, 1432.0, 2867, 4515])))
        body_positions = [distances*angles for angles, distances in zip(angles_position, body_positions)]

        body_velocities = 1000*np.concatenate((vsun * np.ones(number_of_suns), np.array([60, 35.0, 29.8, 24.1, 13.1, 9.7, 6.8, 5.4])))
        body_velocities = [distances*angles for angles, distances in zip(angles_velocity, body_velocities)]

        body_masses = 1e24*np.concatenate((msun * np.ones(number_of_suns), [0.330, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102]))
        
    return body_names, body_positions, body_velocities, body_masses
