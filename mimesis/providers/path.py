import sys

from mimesis.data import FOLDERS, PROGRAMMING_LANGS, PROJECT_NAMES
from mimesis.providers import BaseProvider
from mimesis.providers.personal import Personal


class Path(BaseProvider):
    """Class that provides methods and property for generate paths."""

    def __init__(self, platform=sys.platform, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__p = Personal('en')
        self.platform = platform

    @property
    def root(self):
        """Generate a root dir path.

        :return: Root dir.
        :Example:
            /
        """
        if self.platform == 'win32':
            return 'C:\\'
        else:
            return '/'

    @property
    def home(self):
        """Generate a home path.

        :return: Home path.
        :Example:
            /home/
        """
        if self.platform == 'win32':
            return self.root + 'Users\\'
        else:
            return self.root + 'home/'

    def user(self, gender='female'):
        """Generate a random user.

        :param gender: Gender of user.
        :return: Path to user.
        :Example:
            /home/oretha
        """
        user = self.__p.name(gender)
        user = user.capitalize() if \
            self.platform == 'win32' else user.lower()
        return self.home + user

    def users_folder(self, user_gender='female'):
        """Generate a random path to user's folders.

        :return: Path.
        :Example:
            /home/taneka/Pictures
        """
        folder = self.random.choice(FOLDERS)
        user = self.user(user_gender)
        path = '\\' if self.platform == 'win32' else '/'
        return (user + '{}' + folder).format(path)

    def dev_dir(self, user_gender='female'):
        """Generate a random path to development directory.

        :param user_gender: Path to dev directory.
        :return: Path.
        :Example:
            /home/sherrell/Development/Python/mercenary
        """
        dev_folder = self.random.choice(['Development', 'Dev'])
        stack = self.random.choice(PROGRAMMING_LANGS)
        user = self.user(user_gender)
        path = '\\' if self.platform == 'win32' else '/'
        return (user + '{}' + dev_folder + '{}' + stack).format(path, path)

    def project_dir(self, user_gender='female'):
        """Generate a random path to project directory.

        :param user_gender: Gender of user.
        :return: Path to project.
        :Example:
            /home/sherika/Development/Falcon/mercenary
        """
        project = self.random.choice(PROJECT_NAMES)
        path = '\\' if self.platform == 'win32' else '/'
        return (self.dev_dir(user_gender) + '{}' + project).format(path)
