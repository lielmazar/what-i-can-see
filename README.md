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
- Python 3.8 or higher
- pip (Python package installer)
- [Additional dependencies to be specified]

### Python Environment Setup

```bash
# Navigate to project directory
cd ViewScape

# Upgrade Pip
python3 -m pip install --upgrade pip

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt

# If you add new dependencies, update requirements.txt
pip freeze > requirements.txt
```
Remember to commit and push if changing requirements.txt!

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

# Best to be ensure all python dependencies are up to date
pip install -r requirements.txt

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

### Dependencies
The project relies on the following Python packages (detailed in `requirements.txt`):
- numpy - For numerical operations and array handling
- matplotlib - For visualization and image generation
- argparse - For command-line argument parsing
- logging - For application logging
- pathlib - For cross-platform file path handling
- [Additional packages may be required for GIS data processing]

### Core Components

#### InputProcessor
Responsible for handling and validating user input:
- Processes GPS coordinates (latitude, longitude)
- Handles additional height parameters
- Calculates the appropriate map slice based on field-of-view angles
- Returns a structured map slice object for further processing

#### VisibilityAnalyzer
Performs the core visibility calculations:
- Fetches elevation data for the specified map slice
- Implements line-of-sight algorithms to determine visible points
- Generates a visibility grid (boolean matrix) indicating visible/non-visible areas
- Handles various terrain scenarios and edge cases

#### Visualizer
Creates visual representations of the analysis results:
- Renders terrain data with appropriate coloring and hillshading
- Overlays visibility information on the terrain model
- Produces high-quality output images for printing or display
- Supports various output formats and customization options

### Command-Line Interface
The application provides a comprehensive CLI with the following parameters:
- `--latitude`, `-lat`: Viewer's latitude in decimal degrees (required)
- `--longitude`, `-lon`: Viewer's longitude in decimal degrees (required)
- `--height`, `-ht`: Additional height above ground level in meters (default: 1.8m)
- `--fov`, `-f`: Field of view in degrees (default: 120°)
- `--output`, `-o`: Path to save the output visualization
- `--verbose`, `-v`: Enable verbose logging

test it with 
```
python3 main.py -lat 47.6062 -lon -122.3321 -ht 2.0 -f 120 -o visibility_map.png
```

### Project Structure
```
ViewScape/
├── README.md
├── requirements.txt
├── main.py           # Entry point for the application
├── src/              # Source code directory
│   ├── __init__.py
│   ├── InputProcessor.py      # Advanced input processing
│   ├── Elevation.py  # Elevation data handling
│   ├── VisibilityAnalyzer.py # Visibility calculation algorithms
│   └── Visualizer.py # Visualization components
├── tests/
│   ├── __init__.py
│   ├── test_InputProcessor.py
│   ├── test_Elevation.py
│   ├── test_VisibilityAnalyzer.py
│   └── test_Visualizer.py
├── data/             # Sample data and elevation models
│   └── sample_dem/
└── outputs/
```

### Algorithm Details

#### Line-of-Sight Calculation
The visibility analysis uses ray casting from the viewpoint to determine what terrain features are visible:
1. The viewer position (latitude, longitude, height) serves as the origin point
2. Rays are cast in the specified field-of-view
3. For each ray, terrain elevation is sampled at regular intervals
4. A point is considered visible if no previous point along the ray blocks the line of sight
5. The algorithm accounts for Earth's curvature for large distances

#### Visualization Techniques
- Terrain is rendered using a digital elevation model with hillshading
- Visible areas are highlighted with a semi-transparent green overlay
- Contour lines can be added to represent elevation changes
- Optional terrain feature labeling identifies prominent landmarks in view

## Contributing
Contributions are welcome! Please follow the development workflow outlined above and adhere to the project's coding standards.

## License
MIT
