# FIELD Bits: Canonical Definitions

This directory contains the **canonical definitions** of the 10 FIELD Bit types that form the architectural foundation of *Days of Future Past*.

## 🌀 Overview

The FIELD System organizes all game entities into **10 archetypal Bit types**, each representing a fundamental pattern of existence. These types are not arbitrary — they derive from sacred geometry, systems theory, and narrative archetypes.

## 📂 Structure

Each Bit type has its own definition file:

| Bit Type | File | Description |
|----------|------|-------------|
| HOME | [HOME_Bit.md](./HOME_Bit.md) | Origin, identity, safety |
| SPACE | [SPACE_Bit.md](./SPACE_Bit.md) | Context, environment, field |
| OBJECT | [OBJECT_Bit.md](./OBJECT_Bit.md) | Tools, artifacts, symbols |
| ACTOR | [ACTOR_Bit.md](./ACTOR_Bit.md) | Characters, agents, entities |
| EVENT | [EVENT_Bit.md](./EVENT_Bit.md) | Turning points, conflicts |
| SIGNAL | [SIGNAL_Bit.md](./SIGNAL_Bit.md) | Messages, communication |
| MEMORY | [MEMORY_Bit.md](./MEMORY_Bit.md) | Past echoes, flashbacks |
| THRESHOLD | [THRESHOLD_Bit.md](./THRESHOLD_Bit.md) | Transitions, gateways |
| FIELD | [FIELD_Bit.md](./FIELD_Bit.md) | Systems, networks, web |
| VOID | [VOID_Bit.md](./VOID_Bit.md) | Absence, mystery, potential |

## 🎯 Purpose

These definitions serve as:

1. **Design Reference** — What each Bit type represents conceptually
2. **Implementation Guide** — How to code each Bit in Unity
3. **Narrative Taxonomy** — How writers should classify story elements
4. **Visual Blueprint** — How artists should render each Bit type

## 🔧 Technical Implementation

All FIELD Bits inherit from the base `FIELDBit` class:

```csharp
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
        
        protected abstract void OnRegisterWithFIELD();
    }
}
```

See individual Bit definition files for specific implementation patterns.

## 🎨 Visual Signatures

Each Bit type has a unique visual identity in Digital Space:

| Bit | Geometry | Color | Glow Pattern |
|-----|----------|-------|--------------|
| HOME | Nested spheres | Gold | Pulsing (heartbeat) |
| SPACE | Tesseract lattice | Cyan | Rotating planes |
| OBJECT | Crystalline facets | Silver | Edge shimmer |
| ACTOR | Silhouette + aura | Violet | Breathing halo |
| EVENT | Radiating burst | Orange | Explosive flash |
| SIGNAL | Waveform | Green | Traveling pulse |
| MEMORY | Spiral helix | Blue | Flowing strands |
| THRESHOLD | Portal arch | Magenta | Rippling gateway |
| FIELD | Neural network | White/Iridescent | Interconnect flicker |
| VOID | Negative space | Black | Absence glow |

See `/Art/StyleGuides/FIELD_BitVisuals.pdf` for detailed visual reference.

## 📖 Usage Guidelines

### For Developers

When creating a new game object:

1. Determine which Bit type it represents
2. Inherit from the corresponding Bit class (or base `FIELDBit`)
3. Override `OnRegisterWithFIELD()` for custom initialization
4. Add to appropriate layer (Physical/Digital/Hybrid)

### For Writers

When creating narrative elements:

1. Tag each element with its Bit type in `NarrativeOntology.csv`
2. Use the Bit's archetypal meaning to inform its role in story
3. Consider relationships between Bits (contains, affects, triggers, etc.)
4. Ensure consistency with existing Bit definitions

### For Artists

When creating visual assets:

1. Reference the Bit's geometric form and color
2. Create dual materials (Physical + Digital versions)
3. Follow visual signature guidelines for Digital Space
4. Test in both rendering modes

## 🌐 Philosophy

The 10 Bit types are not merely categories — they are **lenses for understanding existence**:

- **HOME** — Where we come from
- **SPACE** — Where we are
- **OBJECT** — What we hold
- **ACTOR** — Who we are
- **EVENT** — What happens
- **SIGNAL** — What we communicate
- **MEMORY** — What we remember
- **THRESHOLD** — What we cross
- **FIELD** — How we connect
- **VOID** — What we don't know

Together, they form a complete ontology of experience.

## 📚 Further Reading

- [FIELD_Geometry.md](../Docs/Architecture/FIELD_Geometry.md) — Full system documentation
- [DualSpaceRendering.md](../Docs/Architecture/DualSpaceRendering.md) — Visual implementation
- [NarrativeOntology.csv](../Worldbuilding/NarrativeOntology.csv) — Applied examples

---

*The 10 Bits contain all possibilities. Choose wisely.* 🌀
