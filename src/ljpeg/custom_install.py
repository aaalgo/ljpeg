from setuptools.command.install import install
import subprocess


class CustomInstallCommand(install):
    """Custom installation command."""

    def run(self):
        subprocess.call(['mkdir xxx && mkdir ~/Workspace/playground/xxx1'])
        install.run(self)
