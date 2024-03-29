
from distutils.core import setup
setup(
  name = 'Topsis-Anirudh-102283008',         # How you named your package folder (MyLib)
  packages = ['Topsis-Anirudh-102283008'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The provided Python script is a command-line tool for implementing the Topsis (Technique for Order Preference by Similarity to Ideal Solution) algorithm on a given dataset. The script takes input data in CSV format, along with weights and impacts specified by the user. It normalizes the data, calculates Topsis scores, assigns ranks, and saves the results, including the Topsis scores and ranks, to an output CSV file. The script includes error checking for input parameters, file existence, column requirements, and numeric data validation.',   # Give a short description about your library
  author = 'Anirudh Bansal',                   # Type in your name
  author_email = 'abansal11_be21@thapar.edu',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
