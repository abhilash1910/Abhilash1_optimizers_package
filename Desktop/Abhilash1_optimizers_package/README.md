# HSBC_optimizers_package
Python package for stochastic optimizers for gradient convergence with activation functions.The package 'Abhilash1_optimizers' library contains:
## For algorithmic library
### 1.Initialize function-
Function Prototype
def initialize(data,max_itr):
Takes and input tuple,maximum iterations(int).For calling initiliaze function and running the algorithm the user has to first import the desired library- import Abhilash1_optimizers.*libraryname* . Example-import Abhilash1_optimizers.ADAM .Post inclusion the initialize can be called as- Abhilash1_optimizers.ADAM.initialize(data,max_itr) .Returns void as it calls ADAM_optimizer (function) and prints the final vector(list)

### 2.__init__ function-
Function Prototype
def __init__(alpha,b_1,b_2,epsilon,noise_g)
This function only returns hyperparameters which are input through the *hyperparameter* library .Example-return hyperparameters.hyperparameter.initialise(alpha,b_1,b_2,epsilon,noise_g).This class can be imported as Abhilash1_optimizers.hyperparameters. alpha is gradient learning rate,b_1,b_2 are first and second moments epsilon is decay rate and noise_g is a noise in eponential noise sample. Calling this function after importing
import Abhilash1_optimizer.SGD as sgd
sgd.__init__(*parameters*)  Returns hyperaparameters-5 learning rate,moment grad b_1,b_2,decay rate epsilon and noise. (floats)

### 3.init function-
Function Prototype
def init(m_t,v_t,t,theta):
This function is onlu used for initiliazation of certain parameters such as number of turns,first moment,second moment and loss function
It is initiliazed by the Moment_Initializer class -which can be imported as Abhilash1_optimizers.Moment_Initalizer.Usage is -return Moment_Initializer.Moment_Initializer.initialize(m_t,v_t,t,theta).Returns 4 obejcts-fist moment,second moment,turns,loss function (floats)

### 4. library_optimizer-
Example- ADAM_optimizer:
Function prototype-
def Adam_optimizer(data,len_data,max_itr,alpha,b_1,b_2,epsilon,noise_g,act_func,scale):
Takes input parameters as data(list),length of data(int),learning rate(alpha(float)),moments(b_1,b_2)(floats),noise(float),decay rate(epsilon)(float),acivation function(act_func)(string),scale(float for SELU activation function). Returns final weight vector(list).
Calling this function-
import Abhilash1_optimizers.NADAM as nadam
final_weight=nadam.NADAM.Nadam_optimizer(data,len_data,max_itr,alpha,b_1,b_2,epsilon,noise_g,act_func,scale)


## External library classes
### 1.Activation Functions:
Contains implementation of softSign,softPlus,tanh,linear,exponential,relu,elu,selu,hard_sigmoid,sigmoid
Calling it in an algorithm-
import Abhilash1_optimizers.Activation as activation
import Abhilash1_optimizers.RMSprop as rms
result=rms.activation.Activation.sigmoid(x)
Where x is an input value(float) and result is the sigmoid operator acting on the float value.
Returns 1 float value.

### 2.hyperparameter-
Used for setting up hyperparameters.
def initialise(alpha,first_moment,second_moment,epsilon,noise_g):
        return alpha,first_moment,second_moment,epsilon,noise_g
Calling it in an algorithm-
import Abhilash1_optimizers.hyperparameter as hyp
import Abhilash1_optimizers.ADAM as adam
alpha,b_1,b_2,epsilon,noise_g=adam.hyp.hyperparameter.initialise(alpha,first_moment,second_moment,epsilon,noise_g)
Return 4 floats

### 3.Moment_Initializer
Used for setting up moments.
 def initialize(momentum_1,momentum_2,turns,theta):
        return momentum_1,momentum_2,turns,theta
Calling it in an algorithm-
import Abhilash1_optimizers.Moment_Initializer as moment
import Abhilash1_optimizers.ADAM as adam
momentum_1,momentum_2,turns,theta=moment.hyp.hyperparameter.initialise(momentum_1,momentum_2,turns,theta)

        

## Algorithms
## 1.SGD
Stochastic Gradient Descent -Modification of Robins Monro Algorithm(https://projecteuclid.org/euclid.aoms/1177729586)
While accessing SGD in scripts,it is required to - import Abhilash1_optimizers.SGD library.
## 2.Classical Momentum-
https://arxiv.org/abs/1910.03197  Adding momentum operator with the SGD to have a better optimization function
While accessing ClassicMomentum in scripts,it is required to - import Abhilash1_optimizers.ClassicMomentum library
Polyak 1964-https://www.researchgate.net/publication/243648538_Some_methods_of_speeding_up_the_convergence_of_iteration_methods
## 3.Adagrad-
Duchi etal(2011)http://jmlr.org/papers/v12/duchi11a.html 
While accessing Adagrad in scripts,it is required to - import Abhilash1_optimizers.Adagrad library
## 4.ADAM-
Kingma, Ba(2014)-https://arxiv.org/abs/1412.6980
While accessing ADAM in scripts,it is required to - import Abhilash1_optimizers.ADAM_optimizer library
A Variation of ADAM using approximation of moments - import Abhilas1_optimizers.ADAM_modified_update library
### 5.Adamax-
Kingma,Ba(2014)-https://arxiv.org/abs/1412.6980
While accessing Adamax in scripts,it is required to - import Abhilash1_optimizers.Adamax library
### 6.RMSProp-
Hinton et al (2012)-http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf
While accessing RMSprop in scripts,it is required to - import Abhilash1_optimizers.RMSprop library
### 7.NADAM-
Dozat(2015)-http://cs229.stanford.edu/proj2015/054_report.pdf
While accessing NADAM in scripts,it is required to - import Abhilash1_optimizers.Nadam library

## Activation Functions
For any activation function- 
import Abhilash1_optimizers.Activation as activation
float output result= activation.Activation.*activation-name*(float input) where *activation-name*= relu,selu,elu ..etc
### 1.Relu-https://www.tensorflow.org/api_docs/python/tf/keras/activations/relu?version=stable
### 2.Elu-https://www.tensorflow.org/api_docs/python/tf/keras/activations/elu?version=stable
### 3.Selu-https://www.tensorflow.org/api_docs/python/tf/keras/activations/selu?version=stable 
### 4.SoftPlus-https://www.tensorflow.org/api_docs/python/tf/keras/activations/softplus?version=stable
### 5.SoftSign-https://www.tensorflow.org/api_docs/python/tf/keras/activations/softsign?version=stable
### 6.Linear-https://www.tensorflow.org/api_docs/python/tf/keras/activations/linear?version=stable
### 7.Exponential-https://www.tensorflow.org/api_docs/python/tf/keras/activations/exponential?version=stable
### 8.Hard_sigmoid-https://www.tensorflow.org/api_docs/python/tf/keras/activations/hard_sigmoid?version=stable
### 9.Sigmoid-https://www.tensorflow.org/api_docs/python/tf/keras/activations/sigmoid?version=stable

## Sample Test Template
The Test.py script contains the necessary sample test template code.It contains the description of usage of the library functions and general callback mechanisms.The project is hosted in PyPi and can be installed by 
### pip install Abhilash1_optimizers
It requires numpy and pandas libraries.The project is under MIT license and is made opensource to add more activation fucntions and optimizations.
### 5.SoftSign-https://www.tensorflow.org/api_docs/python/tf/keras/activations/softsign?version=stable
### 6.Sigmoid-https://www.tensorflow.org/api_docs/python/tf/keras/activations/sigmoid?version=stable
