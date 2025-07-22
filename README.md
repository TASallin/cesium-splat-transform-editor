# Cesium SPZ Transform Editor

An interactive web application for positioning, scaling, and rotating SPZ (Gaussian Splat) files in Cesium with real-time preview and export capabilities.

## Features

- **Auto-Loading Interface**: Automatically loads SPZ files and reference GeoJSON on startup
- **Live Transform Controls**: Real-time positioning and scaling of SPZ files (scale range: 0-100)
- **Multi-File Support**: Load different SPZ datasets and reference GeoJSON files
- **Transform Analysis**: Parse and display existing transform matrices from tileset.json
- **Export System**: Generate transform matrices for use in other applications
- **Geographic Coordinates**: Convert between Cartesian and lat/lon coordinate systems
- **Streamlined UI**: Simplified interface with essential controls only

## Prerequisites

- Python 3.7 or higher
- SPZ files converted to Cesium-compatible format
- Modern web browser with SharedArrayBuffer support

## Quick Start

1. **Setup the environment**:
   ```bash
   python setup.py
   ```

2. **Start the server**:
   ```bash
   python server.py
   ```

3. **Open in browser**:
   Navigate to `http://localhost:5002`

## Manual Setup

If you prefer to set up manually:

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify Cesium build files**:
   Ensure `Build/CesiumUnminified/Cesium.js` exists

3. **Start the development server**:
   ```bash
   python server.py
   ```

## Usage

### Auto-Loading

The application automatically loads content on startup:
- Loads `reference.geojson` as a cyan reference overlay
- Loads `tileset.json` with its original transform matrix
- Sets up interactive transform controls for real-time editing

### Required Files

The application expects these files in the project directory:
- `tileset.json` - 3D Tiles tileset definition
- `content.gltf` - glTF file with SPZ extension  
- `content.bin` - Binary SPZ data
- `reference.geojson` - Reference GeoJSON for positioning context

### Transform Controls

- **Position**: Use X/Y/Z sliders for real-time geographic positioning (Z range: -200 to 10,000)
- **Scale**: Adjust scale factors from 0 to 100 with real-time preview
- **Rotation**: View rotation values from tileset.json (export-only)

### Exporting Transforms

1. Position your SPZ file using the live position and scale controls
2. Set desired rotation and scale values for export in the transform panel
3. Click "Export Current Transform Matrix" 
4. Use the generated JSON file in your applications

The exported JSON includes both the matrix and the individual transform control values for easy reuse.

## File Structure

```
cesium-splat-transform-editor/
├── Build/CesiumUnminified/     # Cesium build files
├── test-spz-positioning.html   # Main application
├── server.py                   # Python Flask server
├── requirements.txt            # Python dependencies
├── setup.py                    # Setup script
└── README.md                   # This file
```

## Technical Details

### Server Configuration

The Flask server includes required security headers for SharedArrayBuffer support:
- `Cross-Origin-Embedder-Policy: require-corp`
- `Cross-Origin-Opener-Policy: same-origin`

### Transform System

- Uses `tileset.root.transform` exclusively to avoid double transforms
- Position controls work in real-time
- Scale and rotation are export-only for stability
- Geographic coordinate conversion between Cartesian and lat/lon

## Troubleshooting

### Common Issues

1. **Zero Memory Usage**: Ensure `debugTreatTilesetAsGaussianSplats: true` is set
2. **Model Not Visible**: Check if model is positioned at origin (underground) 
3. **SharedArrayBuffer Not Available**: Verify server security headers
4. **File Not Loading**: Ensure `tileset.json`, `content.gltf`, `content.bin`, and `reference.geojson` exist in the project directory
5. **Favicon 404 Error**: Fixed with embedded SVG favicon (📐 icon)
6. **JavaScript Syntax Errors**: Resolved orphaned code fragments from cleanup operations

### Browser Requirements

- Modern browser with SharedArrayBuffer support
- HTTPS or localhost serving (required for security headers)
- JavaScript enabled

## License

This project includes Cesium build files which are subject to the [Cesium License](https://cesium.com/legal/cesium-license/). The transform editor components are provided as-is for educational and development purposes.

## Support

For issues related to:
- SPZ file format: Check the source SPZ conversion tools
- Cesium rendering: Refer to Cesium documentation
- Transform calculations: Review the positioning analysis documentation