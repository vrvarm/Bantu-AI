import logging#-

# Set up logging for the project
def setup_logging():
    logging.basicConfig(filename='project_errors.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')