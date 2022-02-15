
###
#
#
#
#
# Return data frame with new column which includes participant status which is
#   native: native speaker
#   heritage: heritage speaker
#   simk: Slovenian or Macedonian who speaks BCS
#   foreign: non-native speaker of BCS

import sys
import pandas as pd


# read in csv file of responses
df = pd.read_csv(str(sys.argv[1]))

# rename columns for ease
df = df.rename(columns={'subject_information.firstLanguage': 'firstLanguage',
    'subject_information.bcsPrimaryLanguageSchool': 'schoolLanguage',
    'subject_information.otherLanguage': "otherLanguage",
    'subject_information.country': 'country'})

#make all responses lower case
df['firstLanguage'] = df['firstLanguage'].str.lower()
df['schoolLanguage'] = df['schoolLanguage'].str.lower()
df['otherLanguage'] = df['otherLanguage'].str.lower()

# variable that will hold all statuses of participants
statusArray = []
firstLanguageArray = []
schoolLanguageArray = []
otherLanguageArray = []

# Add the values from the dataframe to the arrays, splitting all answers up by
# spaces
#MAKE SURE THAT YOU GET INDEXING RIGHT!!!!!!!!!!!!!!!!!!
for x in range(len(df)) :
    firstLanguageArray.append(df.at[x, 'firstLanguage'].split())
    schoolLanguageArray.append(df.at[x, 'schoolLanguage'].split())
    otherLanguageArray.append(df.at[x, 'otherLanguage'].split())

languages = ["croatian", "serbian", "bosnian", "montenegrian", "serbo-croatian",
            "hrvatski", "srpski", "bosanski", "bošnjački", "bosnjacki", "crnogorski",
            "maternji", "srpskohrvatski", "hrvatskosrpski", "srpsko-hrvatski",
            "hrvatsko-srpski", "bhs", "bcs"]

# x is an array
def commonelems(langs):
    for a in range(len(langs)):
        if (langs[a] in languages):
            return(True)
    return(False)

# Add statuses to status array
for x in range(len(df)) :
    if ((df.at[x, 'country'] == "MK") or (df.at[x, 'country'] == 'SI') ) :
        statusArray.append("simk")
    elif (commonelems(schoolLanguageArray[x]) and commonelems(firstLanguageArray[x])) :
        statusArray.append("native")
    elif (not commonelems(schoolLanguageArray[x]) and commonelems(firstLanguageArray[x])) :
        statusArray.append("heritage")
    else :
        statusArray.append("foreign")

# Add status Array to dataframe

df = df.assign(status = statusArray)

df.to_csv(str(sys.argv[2]))
