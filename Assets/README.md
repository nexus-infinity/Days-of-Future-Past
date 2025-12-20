# Assets

**Unity Project Core Directory**

This directory contains all Unity-specific assets for the *Days of Future Past* game.

## 📂 Standard Unity Structure

```
/Assets/
  /Scenes/              — Unity scene files (.unity)
  /Scripts/             — C# game logic
  /ScriptableObjects/   — Data-driven design patterns
  /Prefabs/             — Reusable game objects
  /Materials/           — Physical & Digital materials
  /Shaders/             — Shader Graph custom shaders
  /Models/              — 3D assets (organized by FIELD Bit type)
  /Textures/            — PBR texture sets
  /Audio/               — Sound effects, music, ambient
  /Resources/           — Runtime-loaded assets
  /Plugins/             — Third-party libraries
  /Editor/              — Editor-only scripts and tools
```

## 🎮 Key Scenes

### Episode1_HomeBase.unity

The first playable scene featuring:
- 10 Watts Parade HOME Bit
- Living Room (Physical Space)
- DOJO Training Room (Digital Space)
- Backyard AR ritual space

**Location:** `/Assets/Scenes/Episode1_HomeBase.unity`

## 💻 Scripts Organization

```
/Scripts/
  /Core/                — FIELD System, managers, utilities
    FIELDBit.cs         — Base class for all Bit types
    FIELDManager.cs     — Central registry and coordinator
    BitType.cs          — Enum definition
  
  /Rendering/           — Dual-space rendering system
    DualSpaceManager.cs — Camera switching, transitions
    DualSpaceObject.cs  — Material swapping
    SpaceType.cs        — Enum for Physical/Digital
  
  /Narrative/           — Story engine, dialogue, events
    StoryEngine.cs      — Event triggers, state machine
    NarrativeBit.cs     — ScriptableObject base
    DialogueManager.cs  — Conversation system
  
  /AR/                  — AR Foundation integration
    ARPortalManager.cs  — Sacred Node spawning
    GPSConverter.cs     — Geographic to Unity coords
    PetalGridRitual.cs  — Backyard AR interaction
  
  /UI/                  — Interface controllers
    HUDManager.cs       — On-screen info display
    SpaceToggleUI.cs    — Physical/Digital switcher
    TutorialManager.cs  — Onboarding guidance
  
  /BitTypes/            — Specific Bit implementations
    HomeBit.cs          — HOME type logic
    SpaceBit.cs         — SPACE type logic
    ObjectBit.cs        — OBJECT type logic
    ActorBit.cs         — ACTOR type logic
    EventBit.cs         — EVENT type logic
    SignalBit.cs        — SIGNAL type logic
    MemoryBit.cs        — MEMORY type logic
    ThresholdBit.cs     — THRESHOLD type logic
    FieldBit.cs         — FIELD type logic (network)
    VoidBit.cs          — VOID type logic
  
  /Examples/            — Reference implementations
    ExampleHomeBit.cs   — Sample HOME implementation
    ExampleInteraction.cs — Sample player interaction
```

## 🎨 Materials Organization

Materials are organized by **FIELD Bit type** and **space**:

```
/Materials/
  /Physical/
    /HOME/              — Warm, lived-in textures
    /SPACE/             — Environmental materials
    /OBJECT/            — Realistic object materials
  
  /Digital/
    /HOME/              — Gold, nested sphere geometry
    /SPACE/             — Cyan tesseract lattice
    /OBJECT/            — Silver crystalline facets
    /ACTOR/             — Violet aura materials
    /etc.../
  
  /UI/                  — Interface materials
  /Shaders/             — Custom Shader Graph assets
```

## 🗿 Models Organization

3D models organized by Bit type:

```
/Models/
  /HOME/                — Architectural structures
  /SPACE/               — Environment pieces
  /OBJECT/              — Props, interactables
    Photograph_Frame.fbx
    Sacred_Journal.fbx
    Ritual_Key.fbx
  /ACTOR/               — Character models, rigs
  /THRESHOLD/           — Portals, doorways, gateways
  /etc.../
```

## 🖼️ Textures Organization

PBR texture sets following standard naming:

```
/Textures/
  /HOME/
    HomeBase_Albedo.png
    HomeBase_Normal.png
    HomeBase_Metallic.png
    HomeBase_Roughness.png
  /OBJECT/
    Photograph_Albedo.png
    Photograph_Normal.png
  /etc.../
```

## 🎵 Audio Organization

```
/Audio/
  /Music/               — Background tracks
    Physical_Ambient.wav
    Digital_Ambient.wav
  
  /SFX/                 — Sound effects
    Space_Transition.wav
    Portal_Open.wav
    Bit_Register.wav
  
  /Dialogue/            — Voice lines (if implemented)
  
  /Ambient/             — Environmental sounds
```

## 📦 ScriptableObjects

Data-driven design patterns:

```
/ScriptableObjects/
  /Narrative/
    NarrativeBit_H001.asset   — 10 Watts Parade data
    NarrativeBit_A001.asset   — Protagonist data
  
  /Configuration/
    FIELDConfig.asset         — System settings
    RenderConfig.asset        — Graphics settings
  
  /Events/
    GameEvent_Awakening.asset — Event definitions
```

## 🔌 Plugins

Third-party dependencies (managed via Unity Package Manager when possible):

- **AR Foundation** — AR support
- **TextMeshPro** — UI text rendering
- **Cinemachine** — Camera control (optional)
- **Yarn Spinner** — Dialogue system (optional)

## ⚙️ Editor Scripts

Custom Unity Editor tools:

```
/Editor/
  FIELDValidatorWindow.cs   — Validates Bit classifications
  NarrativeImporterWindow.cs — CSV → ScriptableObjects
  ARNodeGeneratorWindow.cs  — GPS → AR portals
  DualSpacePreview.cs       — Side-by-side space preview
```

**Access in Unity:** `Tools > FIELD > [Tool Name]`

## 🛠️ Setup Requirements

### Unity Version
**Unity 2022.3 LTS** or later

### Required Packages
Install via Package Manager:
- Universal Render Pipeline (URP)
- AR Foundation
- TextMeshPro

### Platform Settings
- **Target:** Android/iOS (mobile AR)
- **Graphics API:** Vulkan (Android), Metal (iOS)
- **Minimum API Level:** Android 7.0+, iOS 12.0+

## 📚 Resources

- [ForDevelopers.md](../Docs/Onboarding/ForDevelopers.md) — Developer guide
- [FIELD_Geometry.md](../Docs/Architecture/FIELD_Geometry.md) — System architecture
- [DualSpaceRendering.md](../Docs/Architecture/DualSpaceRendering.md) — Rendering details

---

*This is where narrative becomes code.* 💻
