import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(messages)s:')

project_dir="US_VISA_Prediction"
list_of_files=[
    f"{project_dir}/src/__init__.py",
    f"{project_dir}/src/components/__init__.py",
    f"{project_dir}/src/utils/__init__.py/",
    f"{project_dir}/src/utils/common.py",
    f"{project_dir}/src/config/__init__.py",
    f"{project_dir}/src/config/configuration.py",
    f"{project_dir}/src/pipeline/__init__.py",
    f"{project_dir}/src/entity/__init__.py",
    f"{project_dir}/src/entity/config_entity.py",
    f"{project_dir}/src/constants/__init__.py",
    f"{project_dir}/config/config.yaml",
    f"{project_dir}/params.yaml", 
    f"{project_dir}/schema.yaml",
    f"{project_dir}/main.py",
    f"{project_dir}/app.py",
    f"{project_dir}/requirements.txt",
    f"{project_dir}/setup.py",
    f"{project_dir}/research/trials.ipynb",
    f"{project_dir}/templates/index.html",   
]

for filepath in list_of_files:
    filepath=Path(filepath)
    
    filedir,filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory;{filedir} for the file :{filename}")
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"creating empty file:{filepath}")
        
    else:
        logging.info(f"file already exists:{filepath}")
            