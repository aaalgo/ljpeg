from setuptools.command.install import install
import subprocess


class CustomInstallCommand(install):
    """Custom installation command."""

    def run(self):
        install.run(self)
        subprocess.call(['cd jpegdir; make'])
