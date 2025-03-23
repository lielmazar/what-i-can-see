# Tentative Project Name: what-i-can-see
This project is all about looking at the landscape from a view point and get information about what you see.
## Program Work Flow
1. Getting from user GPS coordinate, additional height and the desired slice of view in degrees -> resulting in a map slice
2. Extract height data from a map along multiple GPS coordinate in the map slice, and calculate what the user can see  -> resulting in two dimanstional array point in the map which you can/cannot see)
3. draw the array in a printable from - probebly an image
## Develpoment Guidelines
### git
1. If you don't have a local repo, clone from remote using
   ```
   git clone https://github.com/lielmazar/what-i-can-see.git
   ```
3. Pull the dev branch
   ```
   git pull origin dev
   ```
4. Create and work on 'dev-[developerName]' branch
   ```
   git checkout -b dev-lielmazar
   ``` 
6. Work, develop and commit a lot
   ```
   git add .
   git commit
   ```
8. Push to remote repo when finished working
   ```
   git push origin feature-branch
   ```
