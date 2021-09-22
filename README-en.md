:earth_americas:
*[Portuguese](README.md) ∙ [Español](README-es.md)*

<h1 align="center">Audio-based Automated Video Editing</h1>

<div align="center">
 :ear::loud_sound::film_strip::scissors:
</div>

<br />

## Description

*Note: Project not yet finished*

The purpose of this work is to provide an automated video editing solution in order to save human work for editing very large videos and with certain editing standards. To do this, we used the energy of the audio from the video to identify the key editing points, and cut the original video at all these key/interest points and edit them all together in a single file.

## Suggestion on how to import the virtual environment

It is highly recommended when working with python projects, to use from [virtual environments](https://csguide.cs.princeton.edu/software/virtualenv), Python virtual environments help decouple and isolate Python versions and associated pip packages. This allows end users to install and manage their own set of packages that are independent of those provided by the system. Virtual environments allow you to have a stable, reproducible and portable environment. You control which versions of packages are installed and when they are updated.
There are several ways to configure a virtual environment in python, I'm going to list here some good links that can help with this configuration: [:link:](https://docs.python.org/3/library/venv.html), [:link:](https://realpython.com/lessons/creating-virtual-environment/), [:link:](https://towardsdatascience.com/virtual-environments-for-absolute-beginners-what-is-it-and-how-to-create-one-examples-a48da8982d4b), [:link:](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

Once the method for creating the virtual environment is chosen, just check a way to create the environment according to the file  `requirements.txt`. I'll also list some good ways to do this here: [:link:](https://developer.akamai.com/blog/2017/06/21/how-building-virtual-python-environment), [:link:](https://gist.github.com/luiscape/19d2d73a8c7b59411a2fb73a697f5ed4), [:link:](https://www.jetbrains.com/help/pycharm/managing-dependencies.html), [:link:](https://www.codegrepper.com/code-examples/python/conda+create+requirements.txt).

My recommendation is to use the [Anaconda](https://conda.io/projects/conda/en/latest/index.html) to carry out the management of dependencies and virtualized environments, in a simpler way. And follow these steps:

- [Anaconda dowload](https://www.anaconda.com/products/individual)
- To create the environment [open Anaconda cmd](https://stackoverflow.com/questions/47914980/how-to-access-anaconda-command-prompt-in-windows-10-64-bit/55545141#:~:text=Go%20with%20the%20mouse%20to,%22Anaconda%20Prompt%22%20will%20open.), type on terminal `pip install -r requirements.txt` or if prefered conda syntax `conda create --name <env_name> --file requirements.txt`
- It is interesting to verify at [anaconda navigator](https://docs.anaconda.com/anaconda/navigator/getting-started/) if environment was created right
- Once the environment is created, you should check how to work with this environment within the IDE used, here are some links that exemplify this: [:link:](https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html), [:link:](https://stackoverflow.com/questions/43351596/activating-anaconda-environment-in-vscode), [:link:](https://docs.anaconda.com/anaconda/user-guide/tasks/integration/sublime/)
- After following this step by step, it is now possible to run the project in a suitable environment in the IDE that is preferred.

## References for Audio Manipulation

The techniques used for audio treatment were based on the following materials: 
- [Basic Audio Handling in Python](https://medium.com/behavioral-signals-ai/basic-audio-handling-d4cc9c70d64d)
- [Guide to Digital Signal Processing](https://www.dspguide.com/)




