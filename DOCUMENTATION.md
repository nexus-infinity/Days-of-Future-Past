# System Documentation

## Days of Future Past - AR Discovery System

### Overview

This is a comprehensive AR discovery system that maps sacred geometry to real-world locations in Melbourne, Australia. The system employs a unique 3-layer cohabitational architecture where physical reality, digital AR overlays, and backend infrastructure exist simultaneously.

## Architecture Details

### 3-Layer Cohabitational Architecture

The fundamental principle is that layers exist **simultaneously**, not as replacements:

#### Layer 1: Physical Reality (Melbourne)
- **Location**: Melbourne, Australia
- **Purpose**: Ground truth for all discoveries
- **Data**: GPS coordinates, physical landmarks
- **10 Fields**: Real locations across Melbourne's urban landscape

#### Layer 2: Digital Overlay (Unity AR)
- **Platform**: Unity AR Foundation
- **Purpose**: Augmented reality visualization
- **Features**:
  - AR markers for geometry nodes
  - Real-time GPS to Unity coordinate conversion
  - Sacred geometry rendering
  - Custom holographic shaders

#### Layer 3: Sacred Infrastructure (FIELD Backend)
- **Development Path**: `/Volumes/Akron/FIELD-DEV/`
- **Media Storage**: `~/Pictures/FIELD/`
- **Intelligence**: DOJO system via MCP APIs only
- **Services**:
  - Geometry Engine (port 8001)
  - AR Bridge (port 8002)
  - Physical Mapper (port 8003)
  - DOJO Connector (port 8004)

## Core Philosophy

### Story=OS
The narrative structure **is** the operating system. Not a metaphor—the story actively organizes and coordinates all system operations.

### Geometry=Grammar
Sacred geometry patterns form the syntax and semantics of interaction. Each shape has meaning:
- **▲ Triangle Upward**: Ascension, sky, expansion (Kiran)
- **▼ Triangle Downward**: Descension, earth, grounding (Tala)
- **● Circle**: Center, balance, unity (Ash)
- **Spiral**: Growth, evolution, journey
- **Hexagon**: Structure, power, organization
- **Mandala**: Wholeness, completion
- **Constellation**: Connection, navigation
- **Sphere**: Unity, perfection

### Cohabitational Space
Layers don't replace each other—they enhance and reveal. When you see the AR overlay, you're not leaving physical reality; you're seeing it more fully through the sacred patterns.

## Characters

### Tala▼TATA
- **Symbol**: ▼TATA
- **Role**: Descender
- **Archetype**: Earth Walker
- **Geometry Affinity**: Triangles downward
- **Philosophy**: Grounding, connection to earth, bringing heaven to earth

### Kiran▲ATLAS
- **Symbol**: ▲ATLAS
- **Role**: Ascender
- **Archetype**: Sky Mapper
- **Philosophy**: Elevation, vision, lifting earth to heaven

### Ash●OBI-WAN
- **Symbol**: ●OBI-WAN
- **Role**: Centerer
- **Archetype**: Balance Keeper
- **Geometry Affinity**: Circles
- **Philosophy**: Balance, unity, holding the center

## The 10 Fields

Fields are organized across 4 temporal epochs, representing different stages of discovery.

### Epoch 1: Foundation (3 fields)

**1. Federation Square Gateway** (▲-gateway)
- Location: -37.8179, 144.9690
- Pattern: Upward triangle as entry point
- Meaning: Gateway to the system

**2. Royal Botanic Gardens Spiral** (●-spiral)
- Location: -37.8304, 144.9796
- Pattern: Circular spiral in nature
- Meaning: Growth and natural evolution

**3. Shrine of Remembrance Axis** (▲▼-axis)
- Location: -37.8304, 144.9733
- Pattern: Vertical axis connecting heaven and earth
- Meaning: Memory and connection

### Epoch 2: Expansion (3 fields)

**4. Yarra River Confluence** (●-flow)
- Location: -37.8226, 144.9631
- Pattern: Flowing curves following water
- Meaning: Flow and continuity

**5. State Library Triangle** (▼-knowledge)
- Location: -37.8098, 144.9652
- Pattern: Downward triangle grounding knowledge
- Meaning: Wisdom brought to earth

**6. Parliament House Hexagon** (●-power)
- Location: -37.8107, 144.9737
- Pattern: Hexagonal structure
- Meaning: Order and governance

### Epoch 3: Integration (2 fields)

**7. Carlton Gardens Mandala** (●-wholeness)
- Location: -37.8047, 144.9717
- Pattern: Mandala in gardens
- Meaning: Wholeness and completion

**8. Docklands Constellation** (▲-stars)
- Location: -37.8152, 144.9461
- Pattern: Constellation mapping
- Meaning: Navigation and connection

### Epoch 4: Transcendence (2 fields)

**9. Southbank Reflection Portal** (▼-reflection)
- Location: -37.8219, 144.9673
- Pattern: Mirror plane across river
- Meaning: Reflection and duality

**10. Crown Unity Sphere** (●-unity)
- Location: -37.8229, 144.9588
- Pattern: Perfect sphere
- Meaning: Final unity and wholeness

## DOJO Intelligence System

### CRITICAL: MCP-Only Access

⚠️ **DOJO intelligence MUST ONLY be accessed via MCP (Message Control Protocol) APIs.**

**NEVER use direct access to DOJO.** All requests go through the `MCPClient` class.

### MCP Endpoints

1. **Geometry Analysis**: `/api/dojo/geometry/analyze`
   - Analyze sacred geometry patterns
   - Return symbolic meanings
   - Suggest connections

2. **Field Discovery**: `/api/dojo/field/discover`
   - Discover new fields
   - Validate locations
   - Map patterns

3. **Sacred Mapping**: `/api/dojo/sacred/map`
   - Map sacred patterns to locations
   - Generate geometry overlays
   - Connect patterns across fields

4. **Character Guidance**: `/api/dojo/character/guide`
   - Get guidance from characters
   - Character-specific interpretations
   - Narrative progression

5. **Epoch Transition**: `/api/dojo/epoch/transition`
   - Manage transitions between epochs
   - Unlock new fields
   - Progress narrative

## Unity AR Implementation

### Coordinate System

The system uses Federation Square as the origin point:
- **Origin**: -37.8179°S, 144.9690°E
- **Conversion**: GPS → Unity world space
- **Meters per degree**:
  - Latitude: ~111,320 m
  - Longitude: ~88,834 m (at Melbourne's latitude)

### AR Markers

Each geometry node has an AR marker with:
- **ID**: Unique identifier
- **Type**: Geometry node, field portal, character anchor, or epoch marker
- **Transform**: Position, rotation, scale in Unity space
- **Metadata**: Geometry type, layer, color

### Rendering

Sacred geometry is rendered using:
- **Custom shaders**: `Custom/HolographicGeometry`
- **Material**: `Sacred_Geometry_Material`
- **Colors**: Specific to each geometry type
- **AR Foundation**: Version 5.0+

## File Structure

```
Days-of-Future-Past/
├── architecture.py       # Core 3-layer architecture system
├── field_backend.py      # FIELD backend and DOJO MCP client
├── unity_ar.py           # Unity AR integration and rendering
├── main.py               # Main application entry point
├── requirements.txt      # Python dependencies
├── README.md             # User-facing documentation
├── DOCUMENTATION.md      # This technical documentation
├── architecture.json     # Generated: Complete architecture export
├── field_config.json     # Generated: FIELD backend configuration
└── unity_config.json     # Generated: Unity AR scenes
```

## Usage Examples

### Initialize the System

```python
from main import DaysOfFuturePast

# Create application instance
app = DaysOfFuturePast()

# Display system overview
app.display_system_overview()
```

### Generate AR Scenes

```python
# Generate all AR scenes
scenes = app.generate_field_ar_scenes()

# Export Unity configuration
app.export_unity_configuration()
```

### Discover a Field

```python
# Demonstrate field discovery
app.demonstrate_field_discovery("field_01")
```

### Use DOJO Intelligence (via MCP)

```python
from field_backend import FIELDConfig, MCPClient

# Initialize MCP client
config = FIELDConfig()
client = MCPClient(config)

# Analyze geometry (async)
result = await client.analyze_geometry({
    "type": "triangle_upward",
    "location": {"lat": -37.8179, "lng": 144.9690}
})
```

## Development Guidelines

### Adding New Fields

1. Define field in `architecture.py` → `Architecture._initialize_fields()`
2. Add GPS coordinates for physical location
3. Define geometry nodes with types
4. Assign sacred pattern symbol
5. Associate with an epoch

### Adding New Geometry Types

1. Add to geometry type list
2. Define color in `GeometryRenderer.GEOMETRY_COLORS`
3. Create Unity prefab configuration
4. Update documentation

### Extending Characters

1. Add character in `Architecture._initialize_characters()`
2. Define symbol, role, archetype
3. Assign geometry affinity
4. Create guidance logic in DOJO

## Security & Privacy

- All DOJO access through MCP only
- No direct database access
- GPS data stays local until needed
- User consent required for location services
- AR data ephemeral by default

## Future Enhancements

- Real-time field activation based on user location
- Multiplayer field discovery
- Character-specific AR experiences
- Dynamic epoch transitions
- Community-discovered fields
- Integration with other sacred geometry systems

## Philosophical Notes

This system is designed around the principle that **technology should enhance rather than replace reality**. The AR layer doesn't take you "out of" Melbourne—it helps you see Melbourne more fully through the lens of sacred geometry.

The characters aren't NPCs in a game; they're archetypal guides representing different ways of moving through and perceiving space. Tala grounds, Kiran elevates, Ash centers. Together, they represent the full spectrum of spatial experience.

The story isn't decoration on top of a technical system. The story **is** the system. Every technical choice reflects a narrative choice and vice versa.

---

**Remember**: Story=OS | Geometry=Grammar | Simultaneous Existence
