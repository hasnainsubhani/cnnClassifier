from cnnClassifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logger

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} STARTED <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
except Exception as e:
    logger.exception(e)
    raise e