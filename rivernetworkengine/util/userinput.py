import sys
from loghelper import Logger

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    log = Logger("query_yes_no")
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        log.info(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            log.warning("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

def querychoices(title, options, question):
    # cls()
    if len(options) == 1:
        return options[0]

    log = Logger("querychoices")
    log.title(title, "=")
    for idx, cstr in enumerate(options):
        log.info("({0}) {1}".format(idx+1, cstr) )

    while True:
        log.info(question + " [Choose One] ")
        choice = raw_input()

        try:
            nchoice = int(choice.strip())
            if nchoice < 1 or nchoice > len(options):
                raise ValueError("Choice is out of range")
            return options[nchoice-1]
        except ValueError as e:
            log.warning("Please respond with a single integer value. \n")