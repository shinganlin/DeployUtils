# Deploy Jupyter Notebook / Jupyter Lab with reverse proxy Nginx
1. Generate jupyter_notebook_config.py
```
jupyter lab --generate-config
or 
jupyter notebook --generate-config
```

2. Revise jupyter_notebook_config.py

* File Path : `~/.jupyter/jupyter_notebook_config.py` 

* Revised Content (Uncomment below lines) 
    ```
    ## Full path of a config file
    c.JupyterApp.config_file = '~/.jupyter/jupyter_notebook_config.py'

    c.NotebookApp.allow_remote_access = True
    c.NotebookApp.base_url = '/jupyter'

    c.NotebookApp.enable_mathjax = True
    c.NotebookApp.ip = '0.0.0.0'
    c.NotebookApp.port = 1823

    ```
