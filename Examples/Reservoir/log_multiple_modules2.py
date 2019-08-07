import logging
import otherMod2

def main():

    # create logger instance named exampleApp
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)
    
    # create the logging file handler
    fh = logging.FileHandler("sample_2.log")

    # create Formatter object
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    
    # add handler to logger object
    logger.addHandler(fh)

    # log stuff
    logger.info("Program started")
    # call function in other module so it logs stuff
    result = otherMod2.add(7, 8)
    logger.info("Done!")

if __name__ == "__main__":
    main()
