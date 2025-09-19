from mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage04_model_trainer import ModelTrainerPipeline
from mlProject.pipeline.stage05_model_evaluation import ModelEvaluationTrainingPipeline
from mlProject import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




STAGE_NAME = "Data Validation stage"

if __name__== '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_validation= DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e
    


STAGE_NAME = "Data Transformation stage"

if __name__== '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e
    


STAGE_NAME = "Model Trainer stage"

if __name__== '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        model_trainer = ModelTrainerPipeline()
        model_trainer.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e
    




STAGE_NAME = "model evaluation stage"

if __name__== '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        model_evaluation = ModelEvaluationTrainingPipeline()
        model_evaluation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e