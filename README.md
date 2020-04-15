# COVID19_SEIR
SEIR model (epidemiology model) for MacOS, 64bit kernel, Python 3.7 (implemented with 3.7.6). Calculation starts from the initial state where there is an infected person in the population, and everyone else is susceptible. </br>
If you have different types of computer or are curious about codes and models, </br>
- GUI_SEIR_corona.py: python code with the model and GUI
- SEIR_covid19.ipynb: Jupyter notebook with the codes of SEIR model. This can run interactively on binder https://mybinder.org/
- environment.yml: python environment setting for SEIR_covid19.ipynb to interactively run on binder.

### Parameters
1. Total population size (assuming a fixed population size over time simulated)
2. Average latency (asymptomatic) period: Latency period is usually the period after a person is exposed to a source of infection, the person does not show symptoms and not infectious. However, there seems to be cases with COVID-19 in which asymptomatic people are infectious. (select one of these assumptions in 6th parameter). Default 5 days, estimation for COVID-19.
3. Average symptomatic period: Default 10 days, estimation for COVID-19
4. How many timesteps (days) to run simulation for. Default 400 days.
5. Basic reproduction number: the expected number of cases directly generated by one case of infection. Default 2.5, 1 (either a number $\ge$ 0, or such numbers separated by comma)
6. Whether people in latency period (asymptomatic) are infectious.

### Instruction and Note
Download GUI_SEIR_corona and open it with command line application such as terminal. You may need to change the access permission to executable manually (chmod 700 GUI_SEIR_corona). Mac computer's Security & Privacy settion may also need to be changed to allow download/open files from unidentified developers.

### The original model description
http://www.bs.s.u-tokyo.ac.jp/content/files/SEIR%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AB%E3%82%88%E3%82%8BCOVID-19%E6%B5%81%E8%A1%8C%E4%BA%88%E6%B8%AC%20200331ver3.1.pdf </br>
COVID19.pdf describes the same model.
