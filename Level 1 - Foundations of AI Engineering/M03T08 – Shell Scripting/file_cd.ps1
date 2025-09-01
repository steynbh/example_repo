# Inside file_cd, insert commands to create three new folders (directories). Name your folders whatever you’d like
# but make sure they are different from each other. After creating the folders, use the appropriate command to
# display the contents of the current directory to confirm that the folders were created successfully.
mkdir Folder1
mkdir Folder2
mkdir Folder3
# Next, insert commands to navigate inside one of the folders you created and create three new folders inside this folder. Also, insert commands to emove two of the folders you created
cd Folder1
mkdir Subfolder1
mkdir Subfolder2
mkdir Subfolder3
Remove-Item Subfolder2
Remove-Item Subfolder3
0