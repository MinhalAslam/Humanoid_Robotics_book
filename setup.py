from setuptools import setup, find_packages

setup(
    name='physical_ai_robot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'rclpy>=3.0.0',
        'opencv-python>=4.5.0',
        'numpy>=1.21.0',
        'torch>=1.12.0',
        'transformers>=4.20.0',
        'openai-whisper',
        'gymnasium',
        'stable-baselines3',
        'nvidia-isaac-gym',
    ],
    author='Physical AI Team',
    author_email='team@physicalai.example.com',
    description='Physical AI & Humanoid Robotics System',
    license='MIT',
    entry_points={
        'console_scripts': [
            'physical-ai-bringup = src.physical_ai_bringup.main:main',
        ],
    },
)