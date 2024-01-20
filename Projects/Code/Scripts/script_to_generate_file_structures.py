import os
from pathlib import Path

name_of_courses = ["ITD 145 - Applied Data Science Techniques",
                   "ITE 140 - Spreadsheet Software"]

sub_folders = ["Assignments",
               "Projects",
               "Notes",
	       "Discussions",
               "Presentation Slides",
               "Materials",
               "Videos",
               "Study Guides",
               "Quizzes",
               "Exams",
               "Other",]

main_directory = "/Users/G/Projects/"

for course in name_of_courses:

    new_directory = Path(main_directory, course)

    for folder in sub_folders:
        new_path = Path(new_directory,folder)
        os.makedirs(new_path, exist_ok=True)
        if folder in ["Assignments", "Projects"]:
            for sub_folder in ["Code", "Others"]:
                new_sub_folder = Path(new_path, sub_folder)
                os.makedirs(new_sub_folder, exist_ok=True)