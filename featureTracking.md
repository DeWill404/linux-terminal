# linux-terminal
###Commands Available###
	1. rmdir _(Remove empty of filled directory)_
		- [x] Remove empty or filed directory
		- [x] Raise error when invalid directory is deleted
		- [ ] Raise error when current or parent directory is being deleted(./ or ../)
2. mkdir _(Make directory at specified valid location)_
	- [x] Make directory if path is correct
	- [x] Raise error if path is being in correct
3. ls _(List current directory content)_
	- [x] List all contents including hidden of current directory
	- [ ] List content of specified valid path, if not valid raise error
  4. touch _(Create new file at specified pat with new name)_
    - [x] Create new file at valid path
    - [x] Raise error when file is already present or invalid path
  5. cp _(Copy file or directory)_
    - [x] Copy dir or file from source to destination
    - [x] Raise error is directore is copied to file or to invalid dir
    - [ ] Raise error if copied to same directory(./ or ../)
  6. mv _(Move file or directory)_
    - [x] Move dir or file from source to destination
    - [x] Raise error if copied to same directory
    - [ ] Raise error is directore is copied to file
  7. ren _(Rename specified file or directory)_
    - [x] Rename file and directory
    - [ ] Raise error if current name is same as previous
    - [ ] Rename file or dir at distant location
  8. pwd _(Get current path)_
    - [x] Get current path with assest folder rename as '/'
  9. date _(Get current date and time)_
    - [x] Get current date n time and segregate date from time
  10. nano _(Text editor)_
    - [x] Create and edit file
    - [ ] Make editing possibile with arrow key and cursor
    - [ ] Allow keyboard shorcuts
    - [ ] Re display previous command after exiting nano
  11. cat _(display context of file)_
    - [x] List content of file in current directory
    - [ ] Raise error if file not found
    - [ ] Cat file at specified valid location
  12. python _(Python interpreter)_
    - [x] Make python interpretor
    - [ ] Minimize error result exit of code
    - [ ] Show error generatoed in code more specificaly
  13. clear _(Clear Screen)_
    - [x] Clear screen window
  14. cmatrix _(Falling matrix animation)_
    - [x] Make falling matrix animation
    - [ ] Make matrix animation for cmd in windows
