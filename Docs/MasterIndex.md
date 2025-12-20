# Master Index

**Days of Future Past — Comprehensive Documentation Hub**

Welcome to the central navigation point for all project documentation.

---

## 🎯 Quick Start

### New to the Project?
Start here based on your role:

- **Developer** → [ForDevelopers.md](./Onboarding/ForDevelopers.md)
- **Artist** → [ForArtists.md](./Onboarding/ForArtists.md)
- **Writer/Worldbuilder** → [ForWriters.md](./Onboarding/ForWriters.md)
- **AI Agent** → [ForAI_Agents.md](./Onboarding/ForAI_Agents.md)

### Just Want to Understand the Concept?
Read these in order:

1. [README.md](../README.md) — Project vision
2. [FIELD_Geometry.md](./Architecture/FIELD_Geometry.md) — Core system
3. [DualSpaceRendering.md](./Architecture/DualSpaceRendering.md) — Visual architecture

---

## 📂 Documentation Structure

### 1. Onboarding

**Location:** `/Docs/Onboarding/`

| Document | Audience | Purpose |
|----------|----------|---------|
| [ForDevelopers.md](./Onboarding/ForDevelopers.md) | Programmers | Technical setup, architecture, workflow |
| [ForArtists.md](./Onboarding/ForArtists.md) | Visual creators | Asset pipeline, style guides, tools |
| [ForWriters.md](./Onboarding/ForWriters.md) | Storytellers | Narrative structure, FIELD taxonomy |
| [ForAI_Agents.md](./Onboarding/ForAI_Agents.md) | AI systems | Collaboration protocols, constraints |

---

### 2. Architecture

**Location:** `/Docs/Architecture/`

| Document | Topic | Description |
|----------|-------|-------------|
| [FIELD_Geometry.md](./Architecture/FIELD_Geometry.md) | Core System | 10 Bit types, relationships, philosophy |
| [DualSpaceRendering.md](./Architecture/DualSpaceRendering.md) | Visual System | Physical/Digital spaces, cameras, materials |

**Coming soon:**
- `DistributedCompute.md` — HOME FIELD pattern, server orchestration
- `ARIntegration.md` — GPS → Unity, Sacred Nodes, mobile AR
- `NarrativePipeline.md` — CSV → ScriptableObjects → Runtime

---

### 3. Community & Contribution

**Location:** `/Community/`

| Document | Purpose |
|----------|---------|
| [CONTRIBUTING.md](../Community/CONTRIBUTING.md) | How to contribute (code, art, narrative, docs) |
| [CODE_OF_CONDUCT.md](../Community/CODE_OF_CONDUCT.md) | Community standards and enforcement |

**Coming soon:**
- `CONTRIBUTORS.md` — Recognition of all contributors
- `GOVERNANCE.md` — Decision-making process, maintainer roles

---

### 4. Worldbuilding

**Location:** `/Worldbuilding/`

| Resource | Format | Purpose |
|----------|--------|---------|
| `NarrativeOntology.csv` | CSV | Master database of all story elements |
| `/Epochs/` | Markdown | Historical periods, timelines |
| `/Characters/` | YAML/Markdown | Protagonist, companions, antagonists |
| `/Nodes/` | YAML | Sacred sites, AR portal locations |
| `/Quests/` | YAML | Narrative arcs, missions |
| `/Dialogues/` | Yarn/JSON | Branching conversations |

---

### 5. FIELD System Reference

**Location:** `/FIELD_Bits/`

Canonical definitions of the 10 Bit types:

| Bit Type | File | Description |
|----------|------|-------------|
| HOME | `HOME_Bit.md` | Origin, identity, safety |
| SPACE | `SPACE_Bit.md` | Context, environment, field |
| OBJECT | `OBJECT_Bit.md` | Tools, artifacts, symbols |
| ACTOR | `ACTOR_Bit.md` | Characters, agents, entities |
| EVENT | `EVENT_Bit.md` | Turning points, conflicts |
| SIGNAL | `SIGNAL_Bit.md` | Messages, communication |
| MEMORY | `MEMORY_Bit.md` | Past echoes, flashbacks |
| THRESHOLD | `THRESHOLD_Bit.md` | Transitions, gateways |
| FIELD | `FIELD_Bit.md` | Systems, networks, web |
| VOID | `VOID_Bit.md` | Absence, mystery, potential |

---

### 6. Art & Style

**Location:** `/Art/StyleGuides/`

| Document | Purpose |
|----------|---------|
| `PhysicalSpace_ColorPalette.pdf` | Warm, Pinterest home aesthetic |
| `DigitalSpace_GeometryLibrary.pdf` | Sacred geometry forms |
| `FIELD_BitVisuals.pdf` | Archetypal colors and geometry per Bit |
| `UI_DesignSystem.pdf` | Interface design language |

**Reference Collections:**
- `/Art/PinterestReferences/` — Mood boards, inspiration
- `/Art/Concepts/` — Early explorations, WIP

---

### 7. Tests

**Location:** `/Tests/`

| Type | Location | Purpose |
|------|----------|---------|
| Unit Tests | `/Tests/Unit/` | Isolated component testing |
| Integration Tests | `/Tests/Integration/` | System interaction testing |
| Acceptance Tests | `/Tests/AcceptanceTests/` | User-story validation |

**Key file:**
- `Episode1_Gates.cs` — Acceptance criteria for first playable scene

---

### 8. Unity Assets

**Location:** `/Assets/`

Standard Unity project structure:

```
/Assets/
  /Scenes/              — Unity scenes (.unity)
  /Scripts/             — C# game logic
    /Core/              — FIELD System, managers
    /Narrative/         — Story engine, dialogue
    /Rendering/         — Dual-space, shaders
    /AR/                — AR Foundation integration
    /UI/                — Interface controllers
    /Examples/          — Reference implementations
  /ScriptableObjects/   — Data-driven design
  /Prefabs/             — Reusable game objects
  /Materials/           — Physical & Digital materials
  /Shaders/             — Shader Graph custom shaders
  /Models/              — 3D assets (by Bit type)
  /Textures/            — PBR texture sets (by Bit type)
  /Audio/               — Sound effects, music
  /Resources/           — Runtime-loaded assets
  /Plugins/             — Third-party libraries
```

---

### 9. Editor Tools

**Location:** `/EditorTools/`

Custom Unity Editor extensions:

| Tool | Purpose |
|------|---------|
| `FIELD_Validator.cs` | Ensures all objects have correct Bit classification |
| `NarrativeImporter.cs` | Converts `/Worldbuilding/` CSV/YAML to ScriptableObjects |
| `ARNodeGenerator.cs` | Creates AR portals from GPS coordinates |
| `DualSpacePreview.cs` | Editor window to preview both spaces |

**Access in Unity:** `Tools > FIELD > [Tool Name]`

---

### 10. Distributed Systems

**Location:** `/DistributedSystems/`

**Coming soon:**
- `docker-compose.yml` — Local development environment
- `/kubernetes/` — Production deployment manifests
- `/monitoring/` — Prometheus, Grafana dashboards
- `HOME_FIELD_pattern.md` — Scalability architecture

---

### 11. AR Integration

**Location:** `/AR/`

**Coming soon:**
- `ARFoundation_Setup.md` — Unity AR configuration
- `GPS_Conversion.cs` — Geographic → Unity coordinates
- `SacredNode_Spawner.cs` — AR portal instantiation
- `/Nodes/` — Per-location AR content definitions

---

## 🎮 Episode Guide

### Episode 1: Home Base

**Location:** 10 Watts Parade, Mount Eliza

**Key Files:**
- Scene: `/Assets/Scenes/Episode1_HomeBase.unity`
- Narrative: `/Worldbuilding/Episodes/Episode1.md`
- Tests: `/Tests/AcceptanceTests/Episode1_Gates.cs`

**Playable Elements:**
- Living room (Physical space)
- DOJO Training Room (Digital space)
- AR petal grid ritual (backyard)
- Dual-space transition tutorial

---

## 🔧 Development Resources

### Linting & Building

```bash
# Unity command-line
Unity -quit -batchmode -projectPath . -executeMethod BuildScript.Build

# Run tests
Unity -runTests -testPlatform editmode -projectPath .
Unity -runTests -testPlatform playmode -projectPath .
```

### Common Commands

```bash
# Clone repo
git clone https://github.com/nexus-infinity/Days-of-Future-Past.git

# Update submodules (if any)
git submodule update --init --recursive

# Check Unity version
cat ProjectSettings/ProjectVersion.txt
```

---

## 📚 External References

### Official Links
- [GitHub Repository](https://github.com/nexus-infinity/Days-of-Future-Past)
- [Notion Master Index](https://www.notion.so/...) *(placeholder)*
- [FIELD Bit Library](https://www.notion.so/...) *(placeholder)*
- [Discord Community](#) *(coming soon)*

### Unity Documentation
- [Unity Manual](https://docs.unity3d.com/Manual/index.html)
- [Unity Scripting Reference](https://docs.unity3d.com/ScriptReference/)
- [Unity URP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)
- [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/)

### Learning Resources
- [Sacred Geometry](https://www.goldennumber.net/)
- [Narrative Design](https://www.gdcvault.com/browse/gdc-19/narrative)
- [Systems Thinking](https://thesystemsthinker.com/)

---

## 🆘 Need Help?

### Troubleshooting
**Coming soon:** `/Docs/Troubleshooting.md`

### FAQ
**Coming soon:** `/Docs/FAQ.md`

### Contact
- GitHub Issues: [Submit an issue](https://github.com/nexus-infinity/Days-of-Future-Past/issues)
- Maintainer: @nexus-infinity

---

## 📊 Project Status

### Current Phase
**Phase 1:** Foundation & Architecture (Q1 2025)

### Milestones
- [x] Repository setup
- [x] Documentation structure
- [ ] FIELD System implementation
- [ ] Dual-Space renderer
- [ ] Episode 1 first playable
- [ ] AR integration
- [ ] Distributed compute
- [ ] Public alpha

---

## 🌀 Philosophy Recap

Before diving deep, remember:

1. **Story is infrastructure** — Narrative generates systems
2. **Dual-space always** — Physical + Digital simultaneously
3. **FIELD taxonomy is sacred** — 10 Bit types are foundational
4. **Collaboration across intelligence** — Human + AI co-creation
5. **Open process** — Transparent, documented, inclusive

---

*Welcome to the spiral. Find your thread and pull.* 🌀
