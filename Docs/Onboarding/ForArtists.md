# Artist Onboarding Guide

Welcome, visual creators! **Days of Future Past** is a living canvas where art and code interweave.

## 🎨 Vision

This project blends:
- **Physical Realism** — True-to-world environments (Pinterest aesthetic)
- **Sacred Geometry** — FIELD overlay with divine proportions
- **Dual-Space Design** — Two simultaneous visual languages

## 🛠️ Tools & Software

### Required
- **Unity 2022.3 LTS** or later (for scene assembly)
- **Blender 3.6+** or **Maya** (3D modeling)
- **Adobe Creative Suite** or **Affinity Designer** (2D assets)
- **Substance Painter** (texturing, optional but recommended)

### Recommended
- **Pinterest** (mood boarding and reference)
- **Figma** or **Miro** (collaborative design)
- **Git LFS** (large file versioning, configured automatically)

## 📂 Asset Organization

```
/Art/
  /Concepts/           - Mood boards, sketches, explorations
  /StyleGuides/        - Color palettes, typography, visual language
  /PinterestReferences/- Curated inspiration boards
  /3DModels/           - Source files (.blend, .ma, .fbx)
  /Textures/           - PBR texture sets
  /Materials/          - Unity material definitions
  /VFX/                - Visual effects and particle systems
  /UI/                 - Interface designs and assets
```

## 🌟 Visual Language

### Physical Space (Reality Layer)

**Aesthetic:** Warm, lived-in, Pinterest home aesthetic
- Natural lighting with soft shadows
- Real-world materials (wood, fabric, concrete)
- Nostalgic color palettes (warm neutrals, dusty rose, sage green)
- Imperfect details (wear, patina, personality)

**Reference:** 10 Watts Parade, Mount Eliza (coastal Australian home)

### Digital Space (FIELD Overlay)

**Aesthetic:** Sacred geometry meets Matrix
- Clean geometric forms (Platonic solids, Metatron's Cube)
- High-contrast palette (white void, electric accents)
- Glowing edges and ethereal materials
- Minimalist and precise

**Reference:** DOJO Training Room, sacred node visualizations

### Bit-Specific Aesthetics

Each FIELD Bit type has a unique visual signature:

| Bit Type    | Visual Motif              | Color        |
|-------------|---------------------------|--------------|
| HOME        | Nested spheres            | Gold         |
| SPACE       | Tesseract lattice         | Cyan         |
| OBJECT      | Crystalline facets        | Silver       |
| ACTOR       | Human silhouette + aura   | Violet       |
| EVENT       | Radiating pulse           | Orange       |
| SIGNAL      | Waveform geometry         | Green        |
| MEMORY      | Spiral helix              | Blue         |
| THRESHOLD   | Portal arch               | Magenta      |
| FIELD       | Interconnected web        | White/Iridescent |
| VOID        | Absence, negative space   | Black        |

## 🎯 Asset Pipeline

### 1. Concept & Approval

1. Create mood boards in `/Art/Concepts/`
2. Share with the team for feedback
3. Get approval before moving to production

### 2. Production

**3D Models:**
- Use real-world scale (1 Unity unit = 1 meter)
- Keep polycount optimized (target: <10k tris for props, <50k for environments)
- Use quads for organic forms, tris for export
- Apply modifiers non-destructively when possible

**Textures:**
- PBR workflow (Albedo, Normal, Metallic, Roughness)
- Target resolution: 2048x2048 for heroes, 1024x1024 for props
- Use texture atlases for multiple small objects
- Include alpha channels for transparency

**Materials:**
- Unity URP (Universal Render Pipeline)
- Use Shader Graph for custom effects
- Follow naming convention: `MAT_[BitType]_[ObjectName]`

### 3. Import to Unity

1. Export models as `.fbx` with appropriate settings
2. Place in `/Assets/Models/[BitType]/`
3. Textures go in `/Assets/Textures/[BitType]/`
4. Create Unity materials in `/Assets/Materials/[BitType]/`

### 4. Scene Integration

- Work with developers to place assets in scenes
- Use Unity's Prefab system for reusable objects
- Test in both Physical and Digital space modes
- Verify performance (60 FPS target on mobile)

## 🎮 Key Scenes to Know

### Episode 1: Home Base

**10 Watts Parade, Mount Eliza**
- Living room (cozy, Pinterest-styled)
- DOJO Training Room (white void, Matrix-inspired)
- Backyard (AR petal grid ritual space)

**Your Focus:**
- Create warm, inviting physical space
- Design clean, geometric FIELD overlay
- Ensure visual harmony when spaces blend

## 📐 Technical Constraints

- **Mobile-first:** Optimize for AR on smartphones
- **Dual-rendering:** Assets must work in both visual modes
- **LOD system:** Provide multiple detail levels for distance
- **Lighting:** Baked + real-time hybrid approach
- **File size:** Keep individual assets under 50MB

## 🎨 Style Guides

See `/Art/StyleGuides/` for detailed visual references:
- `PhysicalSpace_ColorPalette.pdf`
- `DigitalSpace_GeometryLibrary.pdf`
- `FIELD_BitVisuals.pdf`
- `UI_DesignSystem.pdf`

## 🤝 Collaboration

### With Developers
- Communicate technical constraints early
- Attend weekly art/tech sync meetings
- Use GitHub Issues for asset requests

### With Writers
- Visualize narrative moments described in `/Worldbuilding/`
- Contribute to character and environment design
- Maintain narrative consistency

### With Other Artists
- Share WIP in `/Art/Concepts/WIP/`
- Peer review before finalizing
- Build the shared asset library collaboratively

## 📚 Learning Resources

- [Unity URP Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)
- [Shader Graph Tutorials](https://unity.com/shader-graph)
- [PBR Texturing Guide](https://marmoset.co/posts/basic-theory-of-physically-based-rendering/)
- [Sacred Geometry in Design](https://www.goldennumber.net/)

## 🆘 Getting Help

- Review existing assets in `/Assets/` for reference
- Check `/Docs/MasterIndex.md` for comprehensive docs
- Reach out via GitHub Issues with `art` label

---

*Your vision shapes the world. Create boldly.* 🎨
