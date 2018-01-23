from setuptools import setup

__author__ = 'Umar Abdullahi'


setup(
    name='tvb-neurodebian',
    version='0.0.1',
    description='Simple Package(Example) for packaging Tvb to Neurodebian',
    author='Umar Abdullahi',
    author_email='umarbrowser20@gmail.com',
    license='GNU',
    url='https://github.com/umarbrowser/Neuropackage',
    packages=['tvb'],
    entry_points={
        'console_scripts': [
            'tvb=tvb:main',
        ]
    },
)
