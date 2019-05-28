from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-noregistration',
	version=version,
	description="Disable user registration",
	long_description="""\
	""",
	classifiers=[],
	keywords='',
	author='Liip AG',
	author_email='ogd@liip.ch',
	url='http://www.liip.ch',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.noregistration'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
    [ckan.plugins]
	noregistration=ckanext.noregistration.plugins:NoSelfRegistration
	""",
)
