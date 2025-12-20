# Writer & Worldbuilder Onboarding Guide

Welcome, storytellers! In **Days of Future Past**, narrative is the operating system.

## 📖 Philosophy

This project operates on a radical principle:

> **Story is not content. Story is infrastructure.**

Worldbuilding doesn't decorate the game — it *generates* the game. Your words become:
- ScriptableObjects (data structures)
- Quest logic (narrative state machines)
- AR portal locations (geographic coordinates)
- Character behavior trees (dialogue and agency)

You write once. The code listens. The world responds.

## 🌀 The FIELD System (For Writers)

Every element in the universe belongs to one of **10 archetypal Bit types**:

### The 10 Bits

| Bit        | Narrative Role                  | Examples                          |
|------------|---------------------------------|-----------------------------------|
| **HOME**   | Origin point, safety, identity  | 10 Watts Parade, a childhood room |
| **SPACE**  | Context, environment, setting   | Mount Eliza, the DOJO void        |
| **OBJECT** | Tools, artifacts, symbols       | A photograph, a key, a journal    |
| **ACTOR**  | Characters, agents, entities    | Protagonist, AI companion, ghost  |
| **EVENT**  | Turning points, conflicts       | The fracture, a revelation        |
| **SIGNAL** | Messages, communication         | A text, a vision, a warning       |
| **MEMORY** | Past echoes, flashbacks         | Childhood trauma, lost love       |
| **THRESHOLD** | Transitions, gateways         | A door, a choice, a ritual        |
| **FIELD**  | Systems, networks, connections  | The AR grid, relationships        |
| **VOID**   | Absence, mystery, the unknown   | What's missing, the unsaid        |

**Your task:** When creating narrative elements, tag them with their Bit type. The system will handle the rest.

## 📂 Where You Work

### Primary Files

```
/Worldbuilding/
  /Epochs/              - Historical periods and timelines
  /Characters/          - Protagonist, companions, antagonists
  /Nodes/               - Sacred sites, AR portal locations
  /Quests/              - Narrative arcs and missions
  /Dialogues/           - Branching conversations
  NarrativeOntology.csv - Master database of all story elements
```

### Narrative Ontology (CSV Format)

The **single source of truth** for all narrative data.

**Columns:**
```
ID, Name, BitType, Description, Location, Epoch, RelatedIDs, Status
```

**Example:**
```csv
H001, "10 Watts Parade", HOME, "Childhood home in Mount Eliza", "-38.2134, 145.0889", Present, "S001, A001", Active
A001, "Protagonist", ACTOR, "The one who remembers", "", Present, "H001, M003", Active
M003, "Fracture Memory", MEMORY, "The day everything changed", "", 2019, "E005", Revealed
```

The system auto-imports this CSV into Unity ScriptableObjects.

## ✍️ Writing Guidelines

### 1. Physical + Digital Duality

Every location exists in **two spaces simultaneously:**

**Physical Space:** Realistic, sensory, grounded
> *"The living room smells of eucalyptus and old books. Afternoon sun streams through gauze curtains, casting soft shadows on the floorboards."*

**Digital Space:** Abstract, symbolic, geometric
> *"In the FIELD overlay, the living room resolves into a golden HOME node, nested spheres pulsing in rhythm with your heartbeat."*

Write both. The renderer will show them based on player state.

### 2. Sacred Geography

Real-world locations are **Sacred Nodes** in the AR layer.

When defining a place:
1. Provide GPS coordinates (use Google Maps)
2. Describe physical appearance
3. Describe FIELD signature (Bit type, geometry, color)
4. Note narrative significance

**Example:**
```yaml
Node: "Mount Eliza Lookout"
Coordinates: -38.1847, 145.0789
Physical: "A clifftop with sweeping bay views. Wooden bench etched with initials."
Digital: "A THRESHOLD portal, magenta arch suspended over the void."
Narrative: "Where the protagonist first saw the fracture between worlds."
```

### 3. Character as Actor Bits

Characters aren't just profiles — they're **Actors in the FIELD System**.

**Required Info:**
- **Name:** Full and aliases
- **BitType:** ACTOR (always)
- **Agency:** Active, Passive, or Reactive
- **Relationships:** Connected to which other Bits?
- **Arc:** What transformation do they undergo?
- **Voice:** Sample dialogue (we need their "sound")

**Example:**
```yaml
Name: "Ash Morgan"
BitType: ACTOR
Agency: Active
Relationships: [HOME:H001, MEMORY:M003, ACTOR:A007]
Arc: "From denial to acceptance of dual-space perception"
Voice: 
  - "I've been here before. Or I will be. Time feels... recursive."
  - "Show me the FIELD. I'm ready."
```

### 4. Event-Driven Story Beats

Major plot points are **EVENT Bits** that trigger systemic changes.

**Structure:**
```yaml
Event: "The Fracture"
BitType: EVENT
Trigger: "Player enters DOJO for first time"
Conditions: [HasItem:KEY001, CompletedQuest:Q002]
Outcomes:
  - UnlockSpace: "Digital overlay"
  - SpawnActor: A012
  - RevealMemory: M005
Narrative: "The boundary shatters. You see both worlds at once."
```

The system executes the outcomes. You define the meaning.

## 🎮 Episode 1: Home Base

**Your focus:** 10 Watts Parade, Mount Eliza

### Setting
- **Location:** Coastal Australian home, nostalgic and warm
- **Time:** Present day, with echoes of past
- **Mood:** Comfort tinged with uncanny recognition

### Key Narrative Beats
1. **Arrival:** Protagonist returns to childhood home
2. **Discovery:** First encounter with DOJO Training Room (white void)
3. **Ritual:** AR petal grid activation in backyard
4. **Threshold:** Choice to accept dual-space vision

### Your Deliverables
- [ ] Character profiles for protagonist + 2 companions
- [ ] Location descriptions for 5 rooms + backyard
- [ ] 3 memory fragments (flashbacks)
- [ ] 1 branching dialogue tree (DOJO encounter)
- [ ] Populate `NarrativeOntology.csv` with all elements

## 🔄 Workflow

### 1. Ideation
- Draft in `/Worldbuilding/Drafts/`
- Share with team for feedback
- Iterate based on technical constraints

### 2. Formalization
- Structure data in CSV or YAML format
- Tag all elements with Bit types
- Add to `NarrativeOntology.csv`

### 3. Integration
- Run **Narrative Importer** tool in Unity (`Tools > FIELD > Import Narrative`)
- System generates ScriptableObjects
- Developers hook up to gameplay logic

### 4. Testing
- Playtest in Unity (read-only)
- Verify narrative triggers
- Adjust based on player experience

## 🤝 Collaboration

### With Developers
- Communicate narrative logic clearly
- Attend weekly story/system sync
- Be flexible when technical constraints arise

### With Artists
- Provide vivid visual descriptions
- Collaborate on character/environment design
- Maintain tonal consistency

### With Other Writers
- Share drafts early and often
- Peer review for continuity
- Build the lore collectively

## 📚 Resources

- [Narrative Design Fundamentals](https://www.gdcvault.com/browse/gdc-19/narrative)
- [Systems Thinking for Writers](https://www.gamasutra.com/)
- [Sacred Geometry Symbolism](https://www.goldennumber.net/)
- `/Docs/Architecture/FIELD_Geometry.md` (understand the system you're writing for)

## 🆘 Getting Help

- Review existing narrative files in `/Worldbuilding/`
- Check `/Docs/MasterIndex.md` for structure
- Reach out via GitHub Issues with `narrative` label

---

*Your words build worlds. Write with intention.* 📖
