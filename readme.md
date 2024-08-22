python3 -m venv venv

source venv/bin/activate 

pip intall "packeges_name"

deactivate 

## Freezing Dependencies:
    pip freeze > requirements.txt


## Environment Setup Automation:
    pip install -r requirements.txt

## auto activate dependencies in conda 
    conda config --ser auto_activate_base false

## conda commands 

    conda env list 

## conda versioning 

    conda create  --name py310 python=3.10
    To activate this environment, use
    conda activate py310
    To deactivate an active environment, use
    conda deactivate