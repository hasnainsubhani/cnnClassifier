from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import PrepareBaseModel
from cnnClassifier import logger

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_and_clean()
        except Exception as e:
            raise e