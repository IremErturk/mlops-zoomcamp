
# [MLOPs Maturity Models](https://docs.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model)

[Course Video from Alexey](https://youtu.be/XwTH8BDGzYk)

0. No Automation
    - All code sits in Jupyter Notebook. 
    - DS works alone and not belong to any team 

1. DEVOps, No MLOps
    - Developers, helps to DS to deploy a new model versions (but still works seperately)
    - Include good software engineering practices (Unit & Integration test, CI/CD, Ops Metrics)
    - Releases are automated (but not ml-aware) (No experiment tracking, No reproducibility)
    - It fits for POC level !!!

2. Automated Training
    - DS works closely with Developers
    - Training is happenning through Script/Pipeline (Notebooks go away...)
    - Includes experiement tracking & model registery
    - Low friction deployment

3. Automated Deployment
    - Easy to deploy model (by self-servcie ML Platform)
    - Include pipeline which does (data prep -> train model -> deploy model)
    - A/B testing to select the best model

4. Full MLOps Deployment



