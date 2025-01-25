# Manim
Manim is an open-source animation engine for creating precise and high-quality mathematical animations.

## How to Run?
### STEP 1. Virtual Environment
```
$ python3.9 -m venv manim_venv
$ source manim_venv/bin/activate
```

### STEP 2. Dependency
```
$ sudo apt update
$ sudo apt install ffmpeg texlive texlive-fonts-recommended texlive-latex-extra libpango1.0-dev # FFmpeg, LaTeX, Pango
$ sudo apt install libgl1-mesa-glx libglu1-mesa libglew-dev # OpenGL
```

### STEP 3. Install Manimgl
```
$ pip install manimgl
$ manimgl start.py SquareToCircle
```