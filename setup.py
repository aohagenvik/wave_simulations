from setuptools import setup

setup(

    name = 'WaveSimulations',
    version = '0.1.0',
    description = 'A python package for wave simulations, used in my teaching in Norwegian high school.',
    py_modules = ["WaveSimulations"],
    package_dir = {'':'src'},
#     packages = ['ThePackageName1',
#                 'ThePackageName2',
#                 ...
#  ],
    author = 'Anne Oline Hågenvik',
    author_email = 'haaagenvik@icloud.com',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    url='https://github.com/aohagenvik/wave_simulations',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Topic :: Wave simulation',
        'Operating System :: OS Independent',
    ],
    install_requires = [
        'pandas ~= 1.2.4',  # Sier at pandas (minste versjon 1.2.4) må installeres for å bruke pakken
    ],
    keywords=['Wave simulation', "Reflection", "Refraction", "Naturfag", "Tvedestrand VGS"],
    
)
