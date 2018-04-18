from distutils.core import setup

setup(name='Dynamic_powerpoint',
      version='0.0.1',
      description='Create a dynamic powerpoint based on Google Calendar',
      package_dir={'dynamic_powerpoint': 'dynamic_powerpoint'},
      install_requires=[
          "google-api-python-client",
          "python-pptx"
      ],
      entry_points={
          'console_scripts': ['generate_powerpoint=dynamic_powerpoint.main:run']
      }
      )
