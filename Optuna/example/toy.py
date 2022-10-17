import optuna

def objective(trial):
    x = trial.suggest_float('x', -10, 10)
    return (x - 2) ** 2

study = optuna.create_study()
study.optimize(objective, n_trials=50)


study.best_params  ## optimization process

trial = study.best_trial

print("  Value: ", trial.value)  ##   Value:  0.001120575172121384

print("  Params: ")
for key, value in trial.params.items():
    print("    {}: {}".format(key, value))  ##  x: 2.033474993235569
