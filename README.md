[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LOuMvgtV)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11497130&assignment_repo_type=AssignmentRepo)
# MAST30034 Project 1 README.md
- Name: Harry Fisher
- Student ID: 1082897

Research Goal: My research goal to analyse the effects of shootings on taxi demand (number of trips per hour).

Timeline: The timeline for the research area is 2016-2019.

The first note is that the commits from my original repositary couldn't be pushed. To resolve the issue, the repo was cloned and already completed files were copied, committed and pushed to the origin so they could be accessed via GitHub. If you need proof the original commits are stuck on my GitDesktop.

To run the pipeline, please first visit the `scripts` directory and run the file:
1. `download.py`: This downloads the raw data into the `data/landing` directory.
Note in this section I had to manually upload data. My tutor Lucas Fern said it was ok. This was because the API limited the download to 1000 instances. The 'shooting_data.csv' shoould be used instead of 'shooting_data_1000.csv' as it contains the full dataset.
2. From the PreReq notebook in tutorial 1, there was the 'Taxi_Zones` folder containing relevant information for this project. Place it manually into the data directory - like this: 'data/taxi_zones'

Next in the pipeline, navigate to the 'notebooks' directory and run the files in order:
3. 'Preprocessing_Yellow_Taxi_Data.ipynb'
4. 'Preprocessing_Shooting.ipynb'
5. 'Visualising_Shooting_Data.ipynb' 
6. 'Shooting_Taxi_PreProcessing_Part1.ipynb'
7. 'Shooting_Taxi_PreProcessing_Part2.ipynb'
8. 'Shooting_Taxi_PreProcessing_Part3.ipynb'

Once the preprocessing is done, stay in the 'notebooks' directory. These next notebooks conduct the analysis and run the models. To continue along in the pipeline run the files in this order.
9. 'Visualising_Taxi_Geo.ipynb'
10. 'Models.ipynb'
11. 'Models_Plot_Results.ipynb'
12. 'Visualising_taxi_shooting-Part1.ipynb'
13. 'Visualising_taxi_shooting-Part2.ipynb'