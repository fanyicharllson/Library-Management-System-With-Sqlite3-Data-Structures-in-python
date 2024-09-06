from library_main_interface_ubdate import library_interface
import logging


file_handler = logging.FileHandler("Application.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])


"""Main interface of the library Management system"""
def main():
    logging.info("Library Management System started...")
    library_interface()
    logging.debug("Library Management System ended.")

if __name__ == '__main__':
    main()    

