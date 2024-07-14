# Camera capture (RPI)
Captures images from RPI camera

Installation Instructions:

git clone https://github.com/dsc333/cam-capture
cd cam-capture
python3 -m venv --system-site-packages env
source env/bin/activate
pip3 install opencv-contrib-python
python3 snap-photo.py 
Press 'q' to quit the program, 'p' to take a photo
Type deactivate when done
