# Write an if statement to create a new folder named if_folder if a folder named new_folder already exists
if (Test-Path -Path "new_folder") {
    mkdir if_folder
}
#  Within the same file, write an if-else statement to check whether a folder named if_folder exists. If it does, create a new folder named hyperionDev otherwise, create a new folder named new-projects.
if (Test-Path -Path "if_folder") {
    mkdir hyperionDev
} else {
    mkdir new-projects
}
