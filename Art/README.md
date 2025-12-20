# Art Assets

**Visual Design and Aesthetic Resources**

This directory contains all art assets, style guides, references, and source files for *Days of Future Past*.

## 🎨 Philosophy

This project operates in **two visual languages simultaneously**:

1. **Physical Space** — Warm, Pinterest-style realism
2. **Digital Space** — Sacred geometry and minimalist precision

All art must support both modes.

## 📂 Structure

```
/Art/
  /Concepts/                    — Mood boards, sketches, explorations
  /StyleGuides/                 — Color palettes, visual language docs
  /PinterestReferences/         — Curated inspiration boards
  /3DModels/                    — Source files (.blend, .ma, .fbx)
  /Textures/                    — PBR texture sets (source + export)
  /Materials/                   — Unity material definitions
  /VFX/                         — Visual effects and particle systems
  /UI/                          — Interface designs and assets
  /SourceFiles/                 — PSDs, AI files, etc.
```

## 📐 Style Guides

### Physical Space Aesthetic

**Reference:** Pinterest "cozy home aesthetic," coastal Australian homes

**Color Palette:**
- Warm neutrals (cream, beige, soft white)
- Dusty rose, sage green, terracotta
- Natural wood tones (honey oak, weathered cedar)
- Soft blues (ocean-inspired)

**Materials:**
- Wood grain (realistic, with imperfections)
- Fabric (linen, cotton, slight wear)
- Concrete/stone (aged, organic)
- Glass (slightly imperfect, with light refraction)

**Lighting:**
- Natural sunlight through windows
- Warm lamps (Edison bulbs, soft glow)
- Golden hour ambiance
- Soft shadows, no harsh contrasts

### Digital Space Aesthetic

**Reference:** *The Matrix* white room, sacred geometry diagrams

**Color Palette:**
- Base: Pure white or deep black
- FIELD Bit colors (archetypal):
  - HOME: Gold (#FFD700)
  - SPACE: Cyan (#00FFFF)
  - OBJECT: Silver (#C0C0C0)
  - ACTOR: Violet (#9400D3)
  - EVENT: Orange (#FF8C00)
  - SIGNAL: Green (#00FF00)
  - MEMORY: Blue (#0000FF)
  - THRESHOLD: Magenta (#FF00FF)
  - FIELD: White/Iridescent
  - VOID: Black (#000000)

**Geometry:**
- Platonic solids (cube, tetrahedron, dodecahedron)
- Metatron's Cube, Flower of Life
- Perfect symmetry, clean edges
- Glowing wireframes

**Materials:**
- Emissive (self-illuminated, no external lights)
- HDR glow (bloom effect)
- Edge lighting (Fresnel)
- No textures (flat color or procedural)

## 🛠️ Asset Pipeline

### 3D Models

**Software:** Blender, Maya, or equivalent

**Export Settings:**
- Format: FBX (Unity-compatible)
- Scale: 1 unit = 1 meter
- Polycount: 
  - Props: <10k tris
  - Environment: <50k tris
  - Characters: <30k tris
- Normals: Calculated (smoothing groups)
- Tangents: Calculate in Unity

**File Structure:**
```
/3DModels/
  /Source/                  — .blend, .ma original files
    Photograph_Frame.blend
  /Export/                  — .fbx for Unity
    Photograph_Frame.fbx
```

### Textures

**Software:** Substance Painter, Photoshop, Blender

**PBR Workflow:**
- Albedo (base color, no lighting info)
- Normal (surface detail)
- Metallic (metallic vs. non-metallic)
- Roughness (smooth vs. rough)
- (Optional) AO, Height, Emission

**Resolution:**
- Hero objects: 2048x2048
- Props: 1024x1024
- Tiling textures: 1024x1024 or 512x512
- UI elements: Varies (maintain crisp at target res)

**Naming Convention:**
```
ObjectName_MapType.png

Examples:
HomeBase_Albedo.png
HomeBase_Normal.png
HomeBase_Metallic.png
HomeBase_Roughness.png
```

### Concept Art

**Location:** `/Concepts/`

**Process:**
1. Create initial sketches/mood boards
2. Share with team for feedback
3. Iterate based on narrative/technical needs
4. Move to `/Concepts/Approved/` when finalized
5. Use as reference for 3D/final assets

### Pinterest References

**Location:** `/PinterestReferences/`

Curated boards for visual inspiration:
- `PhysicalSpace_Interiors.md` — Living spaces
- `PhysicalSpace_Architecture.md` — Australian coastal homes
- `DigitalSpace_Geometry.md` — Sacred geometry, minimalism
- `DigitalSpace_SciFi.md` — Matrix, Tron, cyberspace
- `Characters_Mood.md` — Character design inspiration

Each file contains Pinterest board links + key images.

## 🎨 Art by FIELD Bit Type

### HOME Bits

**Physical:** Warm, inviting architecture
- Real-world buildings
- Detailed interiors
- Personal objects (photos, mementos)

**Digital:** Nested golden spheres
- Concentric sphere geometry
- Gold emissive material
- Pulsing animation (heartbeat rhythm)

### SPACE Bits

**Physical:** Environmental context
- Rooms, outdoor areas
- Natural landscapes
- Weather/lighting variations

**Digital:** Cyan tesseract lattice
- 4D wireframe projection
- Rotating plane animations
- Cyan glow

### OBJECT Bits

**Physical:** Realistic props
- True-to-life objects
- Wear and patina
- Interaction affordances (buttons, handles)

**Digital:** Crystalline facets
- Geometric simplification
- Silver reflective material
- Shimmer on edges

*(Continue pattern for all 10 Bit types...)*

## 📏 Technical Constraints

### Unity URP Requirements

- Materials must be URP-compatible
- Use Lit or Unlit shaders
- Shader Graph for custom effects
- No Legacy shaders

### Mobile Performance

- Target: 60 FPS on mid-range phones
- Use LOD (Level of Detail) system
- Optimize texture compression
- Limit overdraw (UI, particles)

### File Size

- Individual assets: <50MB
- Total art package: Aim for <500MB
- Use texture atlases when possible
- Compress audio appropriately

## 🤝 Collaboration

### With Developers

- Attend weekly art/tech sync
- Communicate technical constraints early
- Provide placeholder assets for testing
- Iterate based on performance metrics

### With Writers

- Visualize narrative descriptions
- Maintain consistency with worldbuilding
- Contribute to character/environment design
- Respect the FIELD Bit taxonomy

### With Other Artists

- Share WIP in `/Concepts/WIP/`
- Peer review before finalizing
- Build shared asset library
- Maintain style consistency

## 📚 Resources

- [ForArtists.md](../Docs/Onboarding/ForArtists.md) — Artist onboarding
- [FIELD_Geometry.md](../Docs/Architecture/FIELD_Geometry.md) — Bit types reference
- [DualSpaceRendering.md](../Docs/Architecture/DualSpaceRendering.md) — Technical details

### External Inspiration

- [Pinterest: Cozy Home Aesthetic](https://www.pinterest.com/search/pins/?q=cozy%20home%20aesthetic)
- [Sacred Geometry Reference](https://www.goldennumber.net/)
- [PBR Texturing Guide](https://marmoset.co/posts/basic-theory-of-physically-based-rendering/)

## 🆘 Getting Help

- Review existing assets in `/Assets/`
- Check style guides in `/StyleGuides/`
- Ask questions via GitHub Issues with `art` label

---

*Your vision shapes the world. Create with intention.* 🎨
