#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#					Input File								!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Propagation method [can be CCS, MCEv1, MCEv2, or MCE12 (uses both MCE methods)]
method='MCEv1'

# Flag for adaptive altering of the compression parameter in 
# swarms/grid-swarms/train-swarms or the grid spacing for grids. [YES/NO]
cmprss='YES'

# Conjugate repeats flag. Allows even number repeats to start at the complex conjugate 
# of the previous runs initial position. Not compatible with V1 cloning [YES/NO]
Conjugate_Repeats='NO'

# V1 cloning type. Determines the type of the cloning used for V1, using 1s and 0s or trig functions.
# 1 is the rigid type, 2 is the angular version. [1,2]
# V1cloning = 1

# # Normweighting flag for whether or not normweighting is used in the cloning procedure. [YES/NO]
# V1normweighting='YES'

systems={
    # System (Currently can be SB [Spin Boson], HP [Harmonic Potential], FP [Free Particle], MP [Morse Potential])
    #  SB works only with MCE, all others with CCS.
    'System':'SB',

    # Spectral Density (only valid for Spin Boson, with values EXP [exponential cutoff], DL [Drude Lorentz/Debye],
    # or UBO [Underdamped Brownian Oscillator]. LHC [Light-Harvesting complex] to come later)
    'SpecDen':'EXP',

    # frequency flag for using a set of precalculated frequencies with the spin boson model
    # freqflg = 1 enables reading of precalculated frequencies, freqflg = 0 mean they are calculated withing the program
    'freqflg':0
}

parameters={
    # Number of dimensions
    'ndim':50,

    # Number of basis functions 
    'in_nbf':2,

    # Random Number generation function (ZBQL - using ZBQLNOR subroutine, GAUS - using function based on numerical recipes)
    'randfunc':'ZBQL',

    #determine n.o of configurations for MCE
    'npes':2,

    #determine which PES you are on initially
    'in_PES':1,

    # determines shape of the initial basis [SWARM/SWTRN]
    'basis':'SWARM',

    # allows for the use of the quantum superposition sampling amplitudes [1/0]. 0=standard initial sampling, 1=quantum superposition sampling.
    'qss':0
}

Train={
    # spacing between trajectories for train type basis set. Used for swarm-trains
    'trainsp':300,
    # length of train in carriages. Used for swarm-trains only
    'train_len':10,
    # Size of the central swarm for swtrn basis. Used for swarm-trains only
    'swtrn_swarm_size':50
}

clone={
    # Flag for cloning basis functions (yes/no/blind/blind+/QSC/v1)
    'Cloning':'V1',

    # Cloning threshold (value of |sum_r(a_{r,k})|) - must be >= 0.05 and < 0.25, default 0.249
    'Threshold':'0.23d0',

    # Maximum number of Cloning events allowed
    'max_cloning':4,

    # Minimum cloning frequency (ie how many timesteps since last cloning is new cloning event allowed)
    'clon_freq':1,

    #Quantum Superposition Cloning exclusion paramter between the two child trajectories should >= ??? and < ???
    'QSC_epsilon':'0.1d0',

    # Automatic cloning (NBF/POP/NO)
    'Auto_clone':'POP',

    # Cloning block (the space between cloning events for MCEv1)
    'Clon_block':1365,

    # Threshold for cloning, serves as percentage of basis functions of percentage of population exchange
    'Bfsthresh': 0.04

}

paramz={
    # Compression parameter (can be tweaked to allow better norm value, or altered automatically)   Used for swarms/swarm-trains
    'ALCMP':'1.0d0',

    # gamma factor
    'gamma':'1.0d0',

    # center of initial random gaussian
    'mu':'0.0d0',

    # hbar if left commented or blank, defaults to 1.0d0
    'hbar':'1.0d0'
}

#Propagation Parameters
prop={
    #Minimum stepsize - used in adaptive stepsize
    'dtmin':'0.5d1',
    #Maximum stepsize - used in adaptive stepsize
    'dtmax':'500.d0',
    #Starting stepsize of adaptive / Constant stepsize for Static stepsize
    'dtinit':'10.0d-3',
    #End Time of propagation
    'time_end':'1.0+1', #1.00d+1
    #Start time of propagation
    'time_start':'0.0d+00',
    #Propagation size - either "static" or "adaptive"
    'step':'static'
}
# end of input
