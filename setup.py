from setuptools import setup
from chembl_structure_pipeline.__version__ import __version__

setup(name='chembl_structure_pipeline',
      version=__version__,
      description='ChEMBL Structure Pipeline',
      url='https://www.ebi.ac.uk/chembl/',
      author='Greg Landrum',
      author_email='greg.landrum@t5informatics.com',
      license='MIT',
      packages=['chembl_structure_pipeline'],
      package_data={'chembl_structure_pipeline': ['data/*']},
      zip_safe=False)
