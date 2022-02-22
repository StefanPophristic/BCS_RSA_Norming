# BCS_RSA_Norming

## General Information

This is a norming study for the stimuli which will be used in Stefan Pophristic's
and Judith Degen's cross linguistic reference project in BCS (Serbo-Croatian). We
created a set of 105 stimuli images, each occurring in four different colors
(blue, red, yellow, white or purple, green, orange, black). In the two experiments
we allow participants to label the object or the object's color however they wish.
Based on consistency of naming conventions (of both the objects and their colors),
we will choose which stimuli provide good testing ground for the cross linguistic project.

## Experiments
### Experiment 1: Noun Norming
We show the 105 images, and for each image we ask "Kako se zove ovaj objekat?"
(what is this object called?). Each participant is shown all 105 unique objects
in a randomized order. The color of each object is chosen at random at the start
of the experiment. Therefore each participant sees every unique object once and
only in one color.

### Experiment 2: Color Norming
The experiment is identical to experiment 1, except we ask "Koje je boje ovaj objekat?"
(what color is this object?).

## Repo Organization

**Experiments**: Folder that contains all materials for running the study
- **1_noun_norming**: Folder containing experimental materials for experiment 1
- **2_color_norming**: Folder containing experimental materials for experiment 2

**Analysis**: Folder that contains all materials for analysis of the two studies
- **1_noun_norming**:
  - **main_native**: analysis folder with all participants recruited over prolific
  who listed BCS as a first language
    - **analysis.Rmd**: Markdown file that outputs all relevant data. This file requires
    a csv file named "1_noun_norming_main-merged_cleaned.csv" in the data folder. This
    file should be created by running the participant_status.py file in the shared folder.
    This script outputs a pdf with all the relevant graphs and information. It likewise
    outputs a demographic.R file, a analysis.md file that supports the output pdf, and
    a folder called analysis_files that contains images of all the graphs.
  - **data**: Folder containing all csv files from prolific.
- **2_color_norming**
  - **main_native**: analysis folder with all participants recruited over prolific
  who listed BCS as a first language
- **shared**
  - **analysis.R**: Main analysis script that creates all the graphs. Analysis files
  in the other folders call on this analysis file. Any changes to this file will be reflected
  in the analyses for both color and noun norming.
  - **participant_status.py**: this python script appends a column to the csv file
  stating whether participants are {heritage, native, simk, foreign} speakers of BCS.
  This file should be run before the analysis scripts. Instructions on how to run this file
  are found in the file itself

## Analysis Pipeline:
Open terminal and navigate to analysis > shared. Run participant_status.py based on
the instructions found in that script. Then run the analysis.Rmd file found in either
1_noun_norming or 2_color_norming.
