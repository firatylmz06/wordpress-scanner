import setuptools
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name='wordpress-scanner',
    version='1.0',
    author='Fırat YILMAZ',
    author_email='iletisim@firatyilmaz.com',    
    description='A theme, username, plugin name browser for Flask in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/firatylmz06/wordpress-scanner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
 