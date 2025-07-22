from setuptools import find_packages, setup
import os

package_name = 'robot_descriptions'

# Function to get all files in a directory recursively
def get_data_files(directory):
    data_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Calculate the relative path from the package directory
            relative_path = os.path.relpath(root, 'src/robot_descriptions')
            # Create the destination path in the share directory
            dest_path = os.path.join('share', package_name, relative_path)
            data_files.append((dest_path, [file_path]))
    return data_files

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ] + get_data_files('urdf') + get_data_files('meshes'),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='carson',
    maintainer_email='carson.kohlbrenner@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
