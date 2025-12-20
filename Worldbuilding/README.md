# Worldbuilding

**Narrative Source-of-Truth for Days of Future Past**

This directory contains all canonical narrative content that drives the game's systems, characters, and experiences.

## 🌀 Philosophy

> **Story is infrastructure.**

In this project, worldbuilding isn't decoration — it's the data layer that **generates** gameplay, art direction, and technical systems. Everything flows from narrative.

## 📂 Structure

```
/Worldbuilding/
  NarrativeOntology.csv     — Master database (all story elements)
  /Epochs/                  — Historical periods, timelines
  /Characters/              — Protagonist, companions, antagonists
  /Nodes/                   — Sacred sites, AR portal locations
  /Quests/                  — Narrative arcs, missions
  /Dialogues/               — Branching conversations
  /Drafts/                  — Work-in-progress narrative content
```

## 📊 NarrativeOntology.csv

The **single source of truth** for all narrative elements.

### Format

```csv
ID, Name, BitType, Description, Location, Epoch, RelatedIDs, Status
```

### Column Definitions

| Column | Type | Description |
|--------|------|-------------|
| **ID** | String | Unique identifier (e.g., H001, A001, M003) |
| **Name** | String | Human-readable name |
| **BitType** | Enum | One of 10 FIELD Bit types (HOME, SPACE, OBJECT, etc.) |
| **Description** | String | Narrative description and significance |
| **Location** | String | Physical location (GPS coords or place name) |
| **Epoch** | String | Time period (Present, Past, Future, or specific year) |
| **RelatedIDs** | List | Comma-separated IDs of related Bits |
| **Status** | Enum | Active, Pending, Conditional, Locked, Mystery |

### ID Prefixes

Use these prefixes for readability:

- `H###` — HOME Bits
- `S###` — SPACE Bits
- `O###` — OBJECT Bits
- `A###` — ACTOR Bits
- `E###` — EVENT Bits
- `SG###` — SIGNAL Bits (to avoid confusion with SPACE)
- `M###` — MEMORY Bits
- `T###` — THRESHOLD Bits
- `F###` — FIELD Bits
- `V###` — VOID Bits

### Example Entry

```csv
H001,"10 Watts Parade",HOME,"Childhood home in Mount Eliza","-38.2134, 145.0889",Present,"S001,S002,A001",Active
```

## 🗂️ Subdirectories

### /Epochs/

Historical periods and timelines.

**Format:** Markdown files with chronological information

**Example:**
```markdown
# The Fracture Era (2015-2019)

Period when protagonist's dual-space vision was suppressed...
```

### /Characters/

Detailed character profiles.

**Format:** YAML or Markdown

**Example:**
```yaml
name: "Protagonist"
bitType: ACTOR
id: A001
agency: Active
relationships:
  - HOME: H001
  - MEMORY: M001, M002, M003
arc: "From denial to acceptance of dual-space perception"
```

### /Nodes/

Sacred sites and AR portal locations.

**Format:** YAML with GPS coordinates

**Example:**
```yaml
nodeName: "Mount Eliza Lookout"
id: S004
bitType: SPACE
coordinates:
  lat: -38.1847
  lng: 145.0789
physicalDescription: "Clifftop with sweeping bay views"
digitalDescription: "THRESHOLD portal, magenta arch over void"
```

### /Quests/

Narrative arcs and mission structures.

**Format:** YAML with event chains

**Example:**
```yaml
questName: "The Awakening"
id: Q001
episodes: [1]
stages:
  - trigger: FirstVision
    outcome: UnlockDOJO
  - trigger: ExaminePetalGrid
    outcome: ARActivation
```

### /Dialogues/

Branching conversations.

**Format:** Yarn Spinner or JSON

**Example (Yarn):**
```
title: GuideAI_Introduction
---
GuideAI: Welcome to the FIELD.
GuideAI: You've always seen it. Now you remember.
-> I don't understand.
    GuideAI: You will. Let's begin.
    <<jump Training_Part1>>
-> I'm ready.
    GuideAI: Good. Trust your perception.
    <<jump Training_Part2>>
===
```

## 🔄 Workflow

### 1. Create Narrative Content

Writers work in `/Drafts/` folder:

```
/Drafts/
  Episode1_Outline.md
  Character_Protagonist_v2.yaml
  Memory_BeachScene.md
```

### 2. Formalize and Tag

Move finalized content to appropriate subfolder and add to `NarrativeOntology.csv`.

**Critical:** Every element must have a FIELD Bit type assigned.

### 3. Import to Unity

Developers run **Narrative Importer** tool:

```
Unity Editor → Tools → FIELD → Import Narrative
```

This converts CSV/YAML to Unity ScriptableObjects.

### 4. Playtest and Iterate

Test in-game, gather feedback, update narrative files as needed.

## 🎯 Writing Guidelines

### FIELD-Aligned Thinking

When creating narrative elements, ask:

1. **What Bit type is this?** (HOME, SPACE, OBJECT, etc.)
2. **What relationships does it have?** (contains, affects, triggers, etc.)
3. **Which space does it inhabit?** (Physical, Digital, both?)
4. **What role in the system?** (anchor, connector, catalyst, mystery?)

### Dual-Space Descriptions

Every location needs **two descriptions**:

**Physical Space:**
> "The living room smells of eucalyptus. Afternoon sun streams through gauze curtains."

**Digital Space:**
> "In the FIELD overlay, the room resolves into a golden HOME node, nested spheres pulsing."

### Temporal Anchoring

Use the `Epoch` field to place elements in time:

- **Present** — Current narrative moment
- **Past** — Historical events, memories
- **Future** — Potential outcomes, unwritten choices
- **Specific years** — e.g., 2015, 2019 (for timeline clarity)

## 📚 Resources

- [ForWriters.md](../Docs/Onboarding/ForWriters.md) — Writer onboarding guide
- [FIELD_Geometry.md](../Docs/Architecture/FIELD_Geometry.md) — Bit type reference
- [NarrativeOntology.csv](./NarrativeOntology.csv) — Current narrative database

## 🤝 Contributing

1. Draft new content in `/Drafts/`
2. Share for feedback (GitHub Issue or PR)
3. Finalize and move to appropriate subfolder
4. Update `NarrativeOntology.csv`
5. Submit PR with clear narrative arc explanation

See [CONTRIBUTING.md](../Community/CONTRIBUTING.md) for full process.

---

*The story writes itself. We are merely scribes.* 📖
