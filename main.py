#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ViewScape: Terrain Visibility Analyzer

This is the main entry point for the ViewScape application that analyzes
what a user can see from a specific viewpoint based on GPS coordinates,
elevation data, and field-of-view parameters.
"""

import argparse
import logging
import sys

from src.InputProcessor import InputProcessor
#from src.Elevation import ElevationService
from src.VisibilityAnalyzer import VisibilityAnalyzer
from src.Visualizer import Visualizer

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger('viewscape')


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='ViewScape: Analyze what you can see from a specific viewpoint'
    )
    
    parser.add_argument(
        '--latitude', '-lat',
        type=float,
        required=True,
        help='Viewer\'s latitude in decimal degrees'
    )
    
    parser.add_argument(
        '--longitude', '-lon',
        type=float,
        required=True,
        help='Viewer\'s longitude in decimal degrees'
    )
    
    parser.add_argument(
        '--height', '-ht',
        type=float,
        default=1.8,
        help='Additional height above ground level in meters (default: 1.8m)'
    )
    
    parser.add_argument(
        '--fov', '-f',
        type=float,
        default=120.0,
        help='Field of view in degrees (default: 120°)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Path to save the output visualization'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging'
    )
    
    return parser.parse_args()


def main():
    """Main entry point for the application."""
    args = parse_arguments()
    
    # Set logging level based on verbosity
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    logger.debug("Starting ViewScape application")
    
    # Process input parameters
    input_processor = InputProcessor()
    map_slice = input_processor.process_coordinates(
        args.latitude,
        args.longitude,
        args.height,
        args.fov
    )
    
    # Analyze visibility
    analyzer = VisibilityAnalyzer()
    elevation_data = analyzer.fetch_elevation_data(map_slice)
    visibility = analyzer.calculate_visibility(elevation_data, map_slice)
    
    # Visualize the results
    visualizer = Visualizer()
    visualizer.create_visibility_image(
        elevation_data,
        visibility,
        args.output
    )
    
    logger.info("ViewScape analysis completed successfully")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
        sys.exit(1)