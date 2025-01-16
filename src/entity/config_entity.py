import os
from src.constants import *
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP:str=datetime.now().strftime("%Y-%m-%d %H:%M:%")



@dataclass
class TrainingPipelineConfig:
    pipeline_name:str=PIPELINE_NAME
    artifact_dir:str= os.path.join(ARTIFACT_DIR,TIMESTAMP)
    timpstamp:str=TIMESTAMP
    
    
training_pipeline_config:TrainingPipelineConfig=TrainingPipelineConfig()


