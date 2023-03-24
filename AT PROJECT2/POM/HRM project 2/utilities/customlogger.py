import logging

def test_logDemo():
    logger = logging.getLogger()

    fileHandler = logging.FileHandler('.//logs//automation.log')

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)

    return logger