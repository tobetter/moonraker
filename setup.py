from setuptools import setup, find_packages

setup(
        name = 'moonraker',
        version = '0.2.8',
        description = 'API Web Server for Klipper',
        author = 'Eric Callahan',
        author_email = 'arksine.code@gmail.com',
        license = 'GPLv3',
        packages = find_packages(),
        install_requires = [
            'tornado == 6.1.0',
            'pyserial >= 3.4',
            'pillow == 8.0.1',
            ],
        entry_points = {
            'console_scripts': [
                'moonraker = moonraker.moonraker:main'
                ]
            },
        zip_safe = False)
