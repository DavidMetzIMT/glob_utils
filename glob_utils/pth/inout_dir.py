
from glob_utils.pth.path_utils import dir_exist, get_dir
from logging import getLogger
logger = getLogger(__name__)

################################################################################
# management of global default directory
################################################################################
class DefaultDir(object):
    """Contain the default input- and output path of an application"""    
    _dirs: dict =None

    def __init__(self, input_dir:str='input', output_dir:str='output') -> None:
        self._dirs = {'input': input_dir, 'output': output_dir}

    @property
    def input(self):
        return self._dirs['input']

    @property
    def output(self):
        return self._dirs['output']

    def set_dir(self, dir_path:str, dir_label:str='default_dir'):
        self._dirs[dir_label]= dir_path
        self.check_dirs()

    def check_dirs(self):
        """ check if the input and output directoryies exist

        if not ask the user to select some via explorer dialog

        """
        for dir_label, dir_path in self._dirs.items():

            if not dir_exist(dir_path, create_auto=False):
                new_dir=get_dir(
                            title=f'Select a default {dir_label} directory'
                )
                self._dirs[dir_label]=new_dir
                logger.info(f'Set "{dir_label}"-Directory to {new_dir}')
            else:
                logger.info(f'"{dir_label}"-Directory is : {new_dir}')

DEFAULT_DIRS= DefaultDir()   

if __name__ == "__main__":
    """"""
    print(DEFAULT_DIRS.input, DEFAULT_DIRS.output)
    DEFAULT_DIRS.check_dirs()