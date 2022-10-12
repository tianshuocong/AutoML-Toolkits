# NNI-Tutorial


# Installation
`pip install nni` or `pip install --latest nni`.

Check installation with `nnictl --version`


# HPO
- Modify the model for auto-tuning.

  a.`nni.get_next_parameter()` : fetch the hyperparameters to be evalutated.
  
  b. `nni.report_intermediate_result()`: report per-epoch accuracy metrics.
  
  c. `nni.report_final_result()`: report final accuracy.
  
  
- Define hyperparameters’ search space.
- Configure the experiment.
- Run the experiment.
