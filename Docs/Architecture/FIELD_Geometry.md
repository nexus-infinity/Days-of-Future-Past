# FIELD Geometry: The Sacred System

## 🌀 Overview

**FIELD** (Fractal Interconnected Existential Logic Design) is the architectural foundation of *Days of Future Past*. It is a sacred geometric grammar that classifies all entities, relationships, and interactions in the game universe.

## 📐 Core Principle

> Every object, character, location, and event belongs to one of **10 archetypal Bit types**, derived from sacred geometry and systems thinking.

These Bit types are not arbitrary categories — they represent fundamental patterns of existence that appear across scales, from atoms to ecosystems to narratives.

## 🔟 The 10 Bit Types

### 1. HOME 🏠
**Archetype:** Origin, Identity, Safety  
**Geometry:** Nested spheres (matryoshka pattern)  
**Color:** Gold  
**Function:** Anchor points in space and narrative

**Properties:**
- Provides stability and context
- Can contain other Bits
- Represents belonging and rootedness

**Examples:**
- 10 Watts Parade (physical location)
- Protagonist's sense of self (abstract concept)
- A saved game state (technical system)

---

### 2. SPACE 🌌
**Archetype:** Context, Environment, Field  
**Geometry:** Tesseract lattice (4D projection)  
**Color:** Cyan  
**Function:** Container for action and interaction

**Properties:**
- Defines boundaries and physics
- Can be Physical or Digital
- Affects Bits within it

**Examples:**
- Mount Eliza (geographic region)
- DOJO Training Room (virtual void)
- The game world itself (meta-container)

---

### 3. OBJECT 🗿
**Archetype:** Tool, Artifact, Symbol  
**Geometry:** Crystalline facets (Platonic solids)  
**Color:** Silver  
**Function:** Interactable items with meaning

**Properties:**
- Can be collected, used, examined
- May have multiple states (locked/unlocked)
- Symbolic weight beyond utility

**Examples:**
- A key to a locked door
- A family photograph
- A sacred geometry diagram

---

### 4. ACTOR 🧍
**Archetype:** Agent, Character, Entity  
**Geometry:** Human silhouette + aura field  
**Color:** Violet  
**Function:** Beings with agency and intention

**Properties:**
- Can act, decide, communicate
- Have relationships with other Bits
- Undergo transformation arcs

**Examples:**
- The protagonist
- AI companions
- Memory echoes of past selves

---

### 5. EVENT ⚡
**Archetype:** Turning Point, Conflict, Climax  
**Geometry:** Radiating pulse (explosion from center)  
**Color:** Orange  
**Function:** Moments that change state

**Properties:**
- Trigger systemic changes
- Have preconditions and outcomes
- Cannot be "possessed," only experienced

**Examples:**
- The Fracture (narrative pivot)
- Completing a ritual
- Unlocking dual-space vision

---

### 6. SIGNAL 📡
**Archetype:** Message, Communication, Information  
**Geometry:** Waveform geometry (sine curves)  
**Color:** Green  
**Function:** Data transmission between Bits

**Properties:**
- Can be sent, received, intercepted
- May degrade or transform in transit
- Requires sender and receiver

**Examples:**
- A text message from a friend
- A vision or premonition
- AR waypoint markers

---

### 7. MEMORY 💭
**Archetype:** Past, Echo, Residue  
**Geometry:** Spiral helix (DNA-like)  
**Color:** Blue  
**Function:** Temporal anchors to previous states

**Properties:**
- Can be recalled, fragmented, or lost
- Influence present actions
- May be unreliable or subjective

**Examples:**
- A childhood flashback
- Muscle memory (embodied knowledge)
- Haunted locations (environmental memory)

---

### 8. THRESHOLD 🚪
**Archetype:** Transition, Gateway, Choice  
**Geometry:** Portal arch (Vesica Piscis)  
**Color:** Magenta  
**Function:** Boundaries that can be crossed

**Properties:**
- Separate two states or spaces
- May require conditions to pass
- Irreversible or repeatable

**Examples:**
- A physical door
- A decision point in dialogue
- The transition between Physical and Digital space

---

### 9. FIELD 🕸️
**Archetype:** System, Network, Web  
**Geometry:** Interconnected nodes (neural net)  
**Color:** White/Iridescent  
**Function:** The relational layer connecting all Bits

**Properties:**
- Emergent from relationships
- Cannot exist in isolation
- Self-organizing and adaptive

**Examples:**
- The FIELD System itself (meta)
- Social networks between Actors
- The AR grid overlaying reality

---

### 10. VOID ⚫
**Archetype:** Absence, Mystery, Potential  
**Geometry:** Negative space (defined by what surrounds it)  
**Color:** Black  
**Function:** The unknown, the not-yet, the unsaid

**Properties:**
- Cannot be directly interacted with
- Implies presence through absence
- Source of emergence and creativity

**Examples:**
- The DOJO white void (paradoxically)
- Unanswered questions in narrative
- The player's unwritten choices

---

## 🔗 Relationships

Bits don't exist in isolation — they form a **relational graph**.

### Connection Types

| Relationship    | Description                          | Example                        |
|-----------------|--------------------------------------|--------------------------------|
| **Contains**    | A includes B                         | HOME contains OBJECTs          |
| **Affects**     | A influences B's state               | SPACE affects ACTOR movement   |
| **Triggers**    | A causes B to activate               | EVENT triggers SIGNAL          |
| **Recalls**     | A brings B into present awareness    | ACTOR recalls MEMORY           |
| **Connects**    | A and B are linked                   | FIELD connects multiple Bits   |
| **Transforms**  | A becomes B                          | THRESHOLD transforms ACTOR     |
| **Emerges From**| A arises from interaction of B+C     | FIELD emerges from Bits        |

### Example Graph

```
HOME (10 Watts Parade)
  ├─ contains → OBJECT (Family Photo)
  ├─ contains → SPACE (Living Room)
  │    ├─ affects → ACTOR (Protagonist)
  │    └─ recalls → MEMORY (Childhood)
  └─ connects → FIELD (AR Grid)
       └─ triggers → EVENT (Ritual Activation)
            └─ transforms → THRESHOLD (Dual-Space Access)
```

## 💻 Technical Implementation

### Base Class

All game objects inherit from `FIELDBit`:

```csharp
using UnityEngine;

namespace FIELD
{
    public enum BitType
    {
        HOME, SPACE, OBJECT, ACTOR, EVENT, 
        SIGNAL, MEMORY, THRESHOLD, FIELD, VOID
    }

    public abstract class FIELDBit : MonoBehaviour
    {
        public abstract BitType Type { get; }
        public string BitID { get; private set; }
        
        protected virtual void Awake()
        {
            BitID = GenerateID();
            RegisterWithFIELD();
        }
        
        protected virtual void OnRegisterWithFIELD()
        {
            // Override in derived classes
        }
        
        private void RegisterWithFIELD()
        {
            FIELDManager.Instance.Register(this);
            OnRegisterWithFIELD();
        }
        
        private string GenerateID()
        {
            return $"{Type}_{GetInstanceID()}";
        }
    }
}
```

### Example Derived Class

```csharp
using FIELD;
using UnityEngine;

public class HomeBase : FIELDBit
{
    public override BitType Type => BitType.HOME;
    
    [SerializeField] private List<FIELDBit> containedBits;
    
    protected override void OnRegisterWithFIELD()
    {
        Debug.Log($"HOME registered: {BitID}");
        
        // Establish contains relationships
        foreach (var bit in containedBits)
        {
            FIELDManager.Instance.AddRelationship(
                this, bit, RelationshipType.Contains
            );
        }
    }
}
```

## 🎨 Visual Language

Each Bit type has a unique visual signature in **Digital Space**:

- **Geometry:** Distinct 3D form
- **Color:** Archetypal hue
- **Glow:** Edge lighting intensity
- **Animation:** Idle movement pattern

See `/Art/StyleGuides/FIELD_BitVisuals.pdf` for reference.

## 🧩 Design Patterns

### Pattern: HOME-SPACE-OBJECT Hierarchy

Most scenes follow this structure:
```
HOME (top-level container)
  └─ SPACE (room or area)
      ├─ OBJECT (interactable)
      ├─ OBJECT (prop)
      └─ ACTOR (character)
```

### Pattern: EVENT-SIGNAL-THRESHOLD Chain

Narrative progression:
```
EVENT (story beat)
  → SIGNAL (notification to player)
  → THRESHOLD (choice or transition)
  → STATE CHANGE (world update)
```

### Pattern: ACTOR-MEMORY-VOID Triangle

Character depth:
```
ACTOR (present self)
  ↔ MEMORY (past experience)
  ↔ VOID (unknown future)
```

## 🌐 Philosophical Foundation

The FIELD System is inspired by:

- **Sacred Geometry** — Universal patterns (Flower of Life, Metatron's Cube)
- **Systems Theory** — Everything is interconnected
- **Narrative Archetypes** — Joseph Campbell's monomyth, Jungian psychology
- **Ontological Design** — Categories shape what's possible

By encoding these principles into the game's architecture, we ensure that **form follows meaning** at every level.

## 📚 Further Reading

- `/Docs/Architecture/DualSpaceRendering.md` — How FIELD visualizes
- `/Worldbuilding/NarrativeOntology.csv` — FIELD in narrative data
- `/FIELD_Bits/` — Canonical Bit definitions

---

*The geometry is not decoration. It is the logic.* 🌀
