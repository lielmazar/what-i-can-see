# ViewScape: Terrain Visibility Analyzer

> **Note:** Project name tentative

## Overview
ViewScape is a geospatial application that analyzes what a user can see from a specific viewpoint. By processing GPS coordinates, elevation data, and field-of-view parameters, the application generates a visual representation of visible terrain features from the user's perspective.

## Core Functionality

1. **Input Processing**
   - Collects user's GPS coordinates
   - Takes additional height above ground level
   - Accepts field-of-view parameters (viewing angle in degrees)
   - Generates corresponding map slice for analysis

2. **Visibility Analysis**
   - Extracts elevation data from the map along multiple GPS coordinates
   - Implements line-of-sight calculations to determine visible and non-visible points
   - Outputs a two-dimensional visibility array (indicating points that are visible/non-visible)

3. **Visualization**
   - Renders the visibility data in a user-friendly format
   - Generates printable graphics that illustrate visible landscape features
   - Provides optional terrain labeling for identified visible landmarks

## Development Setup

### Prerequisites
- Git
- [Additional dependencies to be specified]

### Git Workflow

#### Initial Repository Setup
```bash
# Clone the repository
git clone https://github.com/lielmazar/ViewScape.git

# Navigate to project directory
cd ViewScape

# Get the latest development branch
git pull origin dev

# Create your personal development branch
git checkout -b dev-[YourName]

# Push your branch to remote
git push origin dev-[YourName]
```

#### Daily Development Workflow
```bash
# Navigate to project directory
cd ViewScape

# Switch to your development branch
git checkout dev-[YourName]

# Pull latest changes from development branch
git pull origin dev

# [Work on your code changes]

# Stage and commit your changes
git add .
git commit -m 'descriptive commit message'

# Push changes to remote when ready
git push origin dev-[YourName]
```

### Code Review Process
1. When your feature is complete, create a Pull Request from your branch to `dev`
2. Notify the repository owner (lielmazar) for review
3. Address any feedback or requested changes
4. Once approved, your code will be merged into the development branch

## Technical Details

[This section will be expanded with implementation specifics, algorithms used, and technical requirements]

## Contributing
Contributions are welcome! Please follow the development workflow outlined above and adhere to the project's coding standards.

## License
MIT
