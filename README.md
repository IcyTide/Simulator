# Simulator

A pure-python based simulator for Monte Carlo simulation in JX3

## How to Deploy

All simulator codes are **pure-python** and using some features in latest python version.

So if you want to make contributions, please make sure your version of python is above **3.9**

## How to Startup
### Windows Application
Find exe file in directory : **output/app.dist/app.exe**


Open it directly.

### Web Browser with Gradio
(**Wasted, waiting for reorganize**)
```
  // clone repository
  git clone git@github.com:IcyTide/Simulator.git

  // cd working directory
  cd Simulator

  // install gradio package for UI support
  pip install gradio

  // start application
  python -m ui.app
```

After above steps, your default browser will pop out to show the UI.

You can share your **Host** and **Port** with others, so that they can take use of your computational resource.

### Client with QT
(**This approach is for developer to debug**)

```
  // clone repository
  git clone git@github.com:IcyTide/Simulator.git

  // cd working directory
  cd Simulator

  // install gradio package for UI support
  pip install pyside6

  // start application
  python -m qt.app
```