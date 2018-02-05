from distutils.core import setup

setup(
    name='omsender',
    packages= ['omsender'],
    version='0.02',
    description='Your path send other person with Output Messenger on Blackmagic Fusion.',
    author='Aydin Uzmez',
    author_email='aydinuzmez@gmail.com',
    url='https://github.com/aydinuzmez/omsender',
    download_url= 'https://github.com/aydinuzmez/omsender.git',
    keywords = ['Output Messenger sender','Lan Messenger sender'],
    classifiers = [  
	'Development Status :: 4 - Beta',
    'Environment :: Plugins',
	'Operating System :: MacOS',
	'Operating System :: Microsoft :: Windows',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2',
	'Programming Language :: Python :: 3',
	'Topic :: Communications :: Chat'],
)