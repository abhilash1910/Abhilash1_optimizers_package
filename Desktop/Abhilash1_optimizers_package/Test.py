# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 15:20:24 2019

@author: 45063883
"""
import Abhilash1_optimizers.Adagrad as adagrad
import Abhilash1_optimizers.Activation 
import Abhilash1_optimizers.hyperparameters
import Abhilash1_optimizers.Moment_Initializer
import Abhilash1_optimizers.ADAM_modified_update
import Abhilash1_optimizers.Adamax as adamax
import Abhilash1_optimizers.RMSprop as rmsprop
import Abhilash1_optimizers.SGD as sgd
import Abhilash1_optimizers.Adam_optimizer as adam
import Abhilash1_optimizers.Nadam as nadam
import Abhilash1_optimizers.ADAM_modified_update as adamm
import Abhilash1_optimizers.ClassicMomentum as momentum






if __name__=="__main__":
    s=[0.8,0.9,0.7,0.67]
    max_itr=5
    alpha,b_1,b_2,epsilon,noise=rmsprop.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=rmsprop.RMSPROP.RMSprop_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)
    alpha,b_1,b_2,epsilon,noise=adamax.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=adamax.ADAMAX.Adamax_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)
    alpha,b_1,b_2,epsilon,noise=adagrad.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=adagrad.ADAGRAD.Adagrad_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)
    alpha,b_1,b_2,epsilon,noise=nadam.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=nadam.NADAM.Nadam_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)
    alpha,b_1,b_2,epsilon,noise=adamm.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=adamm.ADAMM.Adam_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)
    alpha,b_1,b_2,epsilon,noise=momentum.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=momentum.Momentum.Momentum_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)
    alpha,b_1,b_2,epsilon,noise=adam.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=adam.ADAM.Adam_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)
    alpha,b_1,b_2,epsilon,noise=sgd.hyperparameters.hyperparameter.initialise(0.1,0.9,0.99,1e-8,1e-7)
    vi=sgd.SGD.SGD_optimizer(s,len(s),max_itr,alpha,b_1,b_2,epsilon,noise,"relu",0.2)
    print(vi)