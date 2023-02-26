"""
    Setup file for ljpeg.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 4.4.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
from setuptools import setup
from setuptools.command.install import install
import subprocess
import pkg_resources


class CustomInstallCommand(install):
    """Custom installation command."""

    def run(self):
        # Replace "your_library_name" with the name of your library
        distribution = pkg_resources.get_distribution('ljpeg')
        installation_path = distribution.location
        print(installation_path)
        print("==============")
        subprocess.call(['mkdir', "/home/cest/Workspace/playground/xxx123"])
        print("==============")
        install.run(self)
        print("==============3")


if __name__ == "__main__":
    try:
        setup(
            use_scm_version={"version_scheme": "no-guess-dev"},
            cmdclass={
                'install': CustomInstallCommand,
            })
    except:  # noqa
        print(
            "\n\nAn error occurred while building the project, "
            "please ensure you have the most updated version of setuptools, "
            "setuptools_scm and wheel with:\n"
            "   pip install -U setuptools setuptools_scm wheel\n\n"
        )
        raise
