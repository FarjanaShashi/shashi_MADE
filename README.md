# Impact of CO2 and Greenhouse Gas Emissions on Sea-Level Rise
Climate change is one of the most important challenges of our time. One of the key factors responsible for this is CO₂ and Greenhouse Gas Emissions. These emissions are causing effects on mean sea levels around the world. This project uses historical data to analyze the correlation between CO₂ levels and sea level rise. The analysis will employ statistical methods to establish the relationship between these variables. And give you a clear picture of how rising CO2 and Greenhouse Gas Emissions correlate with changes in mean sea levels. 

***How do rising CO2 and Greenhouse Gas Emissions correlate with changes in mean sea levels?***


> ##### Used Data

This project utilized two open datasets from the well-regarded ***[`[INTERNATIONAL MONETARY FUND]`](https://www.imf.org)*** repository. They provided essential information for my research. These datasets are freely available for academic use, as specified in the ***[`[Terms]`](https://www.imf.org/external/terms.htm)***. The datasets I employed are:

- **[Data on CO2 and Greenhouse Gas Emissions by Our World in Data}(https://climatedata.imf.org/datasets/9c3764c0efcc4c71934ab3988f219e0e/explore)**
- **[Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection
Agency using data from CSIRO, 2015; NOAA, 2015](https://climatedata.imf.org/datasets/b84a7e25159b4c65ba62d3f82c605855/explore)**

The comprehensive data in these datasets facilitated in-depth analysis. To maximize their utility, I developed and executed a data pipeline, detailed in the *[`[Source Code]`](https://github.com/tanvirtanjum/MADE-SS-24/blob/main/project/pipeline.py)* to streamline the data backend workflow.


# Exercise Badges

![](https://byob.yarr.is/FarjanaShashi/shashi_MADE/score_ex1) ![](https://byob.yarr.is/FarjanaShashi/shashi_MADE/score_ex2) ![](https://byob.yarr.is/FarjanaShashi/shashi_MADE/score_ex3) ![](https://byob.yarr.is/FarjanaShashi/shashi_MADE/score_ex4) ![](https://byob.yarr.is/FarjanaShashi/shashi_MADE/score_ex5)

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. 
For example, if your user is _myuser_ and your repo is _myrepo_, then update the badge for _exercise 1_ to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
