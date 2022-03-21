from loguru import logger


def start_msg(M, mx):

    logger.info(
        "Initialization..."
        + "\n"
        + f"Massive star mass: \t\t{M:.5} Mo\n"
        + f"Dark matter particle mass: \t{mx:.5} GeV\n"
    )
