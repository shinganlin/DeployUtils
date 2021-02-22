## Deploy Jupyter Notebook / Jupyter Lab with reverse proxy Nginx
---
#### Jupyter Setting
1. Install jupyterlab
    `pip install jupyterlab` 
2. Generate jupyter_notebook_config.py 
    ```shell
    jupyter lab --generate-config
    or 
    jupyter notebook --generate-config
    ```

3. Revise jupyter_notebook_config.py

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
#### Nginx .conf Setting
1. Install Nginx 
2. Create a .conf in /etc/nginx/conf.d/ 
```
upstream jupyterurl {
        server XXX.XXX.XXX.XXX:1823;
}
server {
    listen 8787;
    listen [::]:8787;
    
    location /jupyter {
            rewrite ^/jupyter/(.*)$ /jupyter/$1 break;
            proxy_pass http://jupyterurl/;
            proxy_redirect http://jupyterurl/ $scheme://$http_host/jupyter/;
            
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-FOr $proxy_add_x_forwarded_for;
            proxy_set_header X-Nginx-Proxy true;

            proxy_http_version 1.1;
            proxy_set_header Upgrade \$http_upgrade;
            proxy_set_header Connection "Upgrade";
            proxy_read_timeout 86400;
            client_max_body_size 1024M;   
        }

    location ~* /jupyter/(api/kernels/[^/]+/(channels|iopub|shell|stdin)|terminals/websocket)/? {
            proxy_pass http://jupyterurl;
			
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-FOr $proxy_add_x_forwarded_for;
            proxy_set_header X-Nginx-Proxy true;

            proxy_http_version 1.1;
            proxy_set_header Upgrade "websocket";
            proxy_set_header Connection "Upgrade";
            proxy_read_timeout 86400;
            client_max_body_size 1024M;   
        }
}
```
