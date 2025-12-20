# Days of Future Past - AR Discovery System

An AR discovery system mapping sacred geometry to real world locations in Melbourne, Australia.

## Architecture

The system implements a **3-layer cohabitational architecture** where all layers exist simultaneously, not as replacements:

### 1. Physical Reality (Melbourne)
- Real-world locations across Melbourne
- GPS coordinates for each sacred field
- 10 unexplored fields mapped across the city

### 2. Digital Overlay (Unity AR)
- Unity AR Foundation integration
- Real-time geometry rendering
- AR markers and scene management
- GPS to Unity coordinate conversion

### 3. Sacred Infrastructure (FIELD Backend)
- Development path: `/Volumes/Akron/FIELD-DEV/`
- Media storage: `~/Pictures/FIELD/`
- **Intelligence: DOJO via MCP APIs only—NEVER direct access**
- Backend services for geometry processing

## Core Concepts

**Story=OS**: The narrative structure acts as the operating system for the experience.

**Geometry=Grammar**: Sacred geometry patterns form the language of interaction.

**Cohabitational Space**: All three layers exist simultaneously, creating a unified experience.

## Characters

Three main characters guide the discovery:

- **Tala▼TATA**: Descender, Earth Walker (triangles downward)
- **Kiran▲ATLAS**: Ascender, Sky Mapper (triangles upward)
- **Ash●OBI-WAN**: Centerer, Balance Keeper (circles)

## Fields

10 unexplored fields distributed across 4 epochs:

### Epoch 1 (3 fields)
1. Federation Square Gateway
2. Royal Botanic Gardens Spiral
3. Shrine of Remembrance Axis

### Epoch 2 (3 fields)
4. Yarra River Confluence
5. State Library Triangle
6. Parliament House Hexagon

### Epoch 3 (2 fields)
7. Carlton Gardens Mandala
8. Docklands Constellation

### Epoch 4 (2 fields)
9. Southbank Reflection Portal
10. Crown Unity Sphere

## Installation

```bash
# Clone the repository
git clone https://github.com/nexus-infinity/Days-of-Future-Past.git
cd Days-of-Future-Past

# Install dependencies (Python 3.8+)
pip install -r requirements.txt
```

## Usage

### Run the main application

```bash
python main.py
```

This will:
- Initialize the 3-layer architecture
- Generate Unity AR scenes for all fields
- Export configuration files
- Demonstrate field discovery

### Output Files

The application generates:
- `unity_config.json` - Unity AR configuration
- `field_config.json` - FIELD backend configuration
- `architecture.json` - Complete system architecture

## Module Structure

```
Days-of-Future-Past/
├── architecture.py      # Core 3-layer architecture
├── field_backend.py     # FIELD backend & DOJO MCP client
├── unity_ar.py          # Unity AR integration
├── main.py              # Main application
└── README.md            # This file
```

## Development Paths

- **FIELD Development**: `/Volumes/Akron/FIELD-DEV/`
- **Media Assets**: `~/Pictures/FIELD/`

## DOJO Intelligence

⚠️ **IMPORTANT**: DOJO intelligence must ONLY be accessed via MCP (Message Control Protocol) APIs. Direct access is prohibited.

All intelligence operations go through the `MCPClient` class:
- Geometry analysis
- Field discovery
- Sacred pattern mapping
- Character guidance
- Epoch transitions

## Unity AR Integration

The system uses Unity AR Foundation for the digital overlay:
- AR markers for geometry nodes
- Real-time GPS to Unity coordinate conversion
- Sacred geometry rendering with custom shaders
- Field portal visualization

## Sacred Geometry Types

The system supports various sacred geometry patterns:
- Triangles (upward ▲, downward ▼)
- Circles (●)
- Spirals
- Hexagons
- Mandalas
- Constellations
- Mirror planes
- Spheres
- Vertical axes
- Flowing curves

## License

See [LICENSE](LICENSE) file for details.

## Philosophy

> "In the cohabitational architecture, layers don't replace each other—they enhance, reveal, and complete. The physical world is not left behind when we enter AR; it becomes more itself through the sacred patterns we overlay. The story is not separate from the system; it IS the system."

---

**Story is the operating system. Geometry is the grammar. The layers exist simultaneously.**
