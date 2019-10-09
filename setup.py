import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()
	
config = {
	'name': 'gothonweb_webapp_bebian',
	'version': '0.0.1',
	'author': 'bebian',
	'author_email': 'bebian@contact.com',
	'description': 'Web app for Zed A. Shaw\'s gothonweb game',
	'long_description': long_description,
	'long_description_content_type': 'text/markdown',
	'url': 'https://github.com/bhorlarh/Gothonweb',
	'packages': setuptools.find_packages(),
	'classifiers': [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	]
	'python_requires': '>=3.6',
	'install_requires': ['flask', 'flask_sqlalchemy', 'flask_login'
							'werkzeug.security', 'nose']
}
	
setuptools.setup(**config)