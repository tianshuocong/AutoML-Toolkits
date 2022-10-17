import optuna


## naive

def objective(trial):
  
    # Categorical parameter
    optimizer = trial.suggest_categorical("optimizer", ["MomentumSGD", "Adam"])

    # Integer parameter
    num_layers = trial.suggest_int("num_layers", 1, 3)

    # Integer parameter (log)
    num_channels = trial.suggest_int("num_channels", 32, 512, log=True)

    # Integer parameter (discretized)
    num_units = trial.suggest_int("num_units", 10, 100, step=5)

    # Floating point parameter
    dropout_rate = trial.suggest_float("dropout_rate", 0.0, 1.0)

    # Floating point parameter (log)
    learning_rate = trial.suggest_float("learning_rate", 1e-5, 1e-2, log=True)

    # Floating point parameter (discretized)
    drop_path_rate = trial.suggest_float("drop_path_rate", 0.0, 1.0, step=0.1)
    
    
    
## conditional    
    
import sklearn.ensemble
import sklearn.svm


def objective(trial):
  
    classifier_name = trial.suggest_categorical("classifier", ["SVC", "RandomForest"])
    if classifier_name == "SVC":
        svc_c = trial.suggest_float("svc_c", 1e-10, 1e10, log=True)
        classifier_obj = sklearn.svm.SVC(C=svc_c)
    else:
        rf_max_depth = trial.suggest_int("rf_max_depth", 2, 32, log=True)
        classifier_obj = sklearn.ensemble.RandomForestClassifier(max_depth=rf_max_depth)
        

    optimizer_name = trial.suggest_categorical('optimizer',['RMSprop','SGD','Adam','Adadelta','Adagrad'])
    if optimizer_name in ['RMSprop','SGD']:
        momentum = trial.suggest_float('momentum',0.0,1.0)
        lr = trial.suggest_float('lr',1e-5,1e-1,log=True)
        optimizer = getattr(optim, optimizer_name)(model.parameters(),lr=lr, momentum=momentum)
    else:
        lr = trial.suggest_float('lr',1e-5,1e-1,log=True)
        optimizer = getattr(optim, optimizer_name)(model.parameters(),lr=lr)
    
    
## loop
        
import torch
import torch.nn as nn


def create_model(trial, in_size):
    n_layers = trial.suggest_int("n_layers", 1, 3)

    layers = []
    for i in range(n_layers):
        n_units = trial.suggest_int("n_units_l{}".format(i), 4, 128, log=True)
        layers.append(nn.Linear(in_size, n_units))
        layers.append(nn.ReLU())
        in_size = n_units
    layers.append(nn.Linear(in_size, 10))

    return nn.Sequential(*layers)       
        
        
        
