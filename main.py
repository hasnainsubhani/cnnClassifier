from cnnClassifier.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier import logger

STAGE_NAME = 'Data Ingestion stage'

try:
    
    logger.info(f">>>>>> stage {STAGE_NAME} STARTED <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX****************X")


except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare base model'

try:
    logger.info(f'*************************')
    logger.info(f">>>>>> stage {STAGE_NAME} STARTED <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX****************X")

except Exception as e:
    logger.exception(e)
    raise e

    
