# Developer Onboarding Guide

Welcome to **Days of Future Past** — a FIELD-aligned, narrative-driven Unity game.

## 🎯 Prerequisites

- **Unity 2022.3 LTS** or later
- **Git** for version control
- **Visual Studio 2022** or **Rider** (recommended IDE)
- Basic understanding of C# and Unity workflows
- Familiarity with AR Foundation (for AR modules)

## 🚀 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nexus-infinity/Days-of-Future-Past.git
cd Days-of-Future-Past
```

### 2. Open in Unity

1. Launch Unity Hub
2. Click "Add" and select the repository root
3. Unity will detect the project and import assets
4. Wait for initial compilation (this may take several minutes)

### 3. Verify Setup

- Open the scene: `Assets/Scenes/Episode1_HomeBase.unity`
- Press Play to test the basic environment
- Check the Console for any errors

## 🏗️ Architecture Overview

### FIELD System

The **FIELD System** is our core architectural pattern based on sacred geometry. Every object in the game is classified into one of **10 Bit types**:

```
HOME, SPACE, OBJECT, ACTOR, EVENT, SIGNAL, MEMORY, THRESHOLD, FIELD, VOID
```

See `/Docs/Architecture/FIELD_Geometry.md` for details.

### Dual-Space Rendering

The game operates in two simultaneous spaces:

1. **Physical Space** — Realistic rendering of real-world locations
2. **Digital Space** — Sacred geometry overlay with FIELD visualization

See `/Docs/Architecture/DualSpaceRendering.md` for implementation details.

### Project Structure

```
/Assets/
  /Scripts/           - Core game logic
  /ScriptableObjects/ - Data-driven design patterns
  /Scenes/            - Unity scenes
  /Prefabs/           - Reusable game objects
  /Materials/         - Shaders and materials
  /Resources/         - Runtime-loaded assets

/EditorTools/         - Custom Unity Editor extensions
/Tests/               - Unit, integration, and acceptance tests
/FIELD_Bits/          - Canonical Bit type definitions
/Worldbuilding/       - Narrative source-of-truth
```

## 🔧 Development Workflow

### 1. Branching Strategy

- `main` — Production-ready code
- `develop` — Integration branch
- `feature/*` — New features
- `fix/*` — Bug fixes

### 2. Coding Standards

- Follow **C# Conventions** (PascalCase for public, camelCase for private)
- Use **ScriptableObjects** for data-driven design
- All FIELD Bit types must inherit from `FIELDBit` base class
- Document public APIs with XML comments

### 3. Testing

```bash
# Run unit tests
Unity -runTests -testPlatform playmode -projectPath .

# Run acceptance tests
# See /Tests/AcceptanceTests/ for criteria
```

### 4. Editor Tools

Custom tools are available under `Tools > FIELD`:

- **FIELD Validator** — Ensures all objects have correct Bit classification
- **Narrative Importer** — Converts `/Worldbuilding/` data to ScriptableObjects
- **AR Node Generator** — Creates AR portals from geographic data

## 🎮 Key Systems

### 1. FIELD Bit System

```csharp
using FIELD;

public class MyObject : FIELDBit
{
    public override BitType Type => BitType.OBJECT;
    
    void Start()
    {
        RegisterWithFIELD();
    }
}
```

### 2. Dual-Space Manager

```csharp
using DualSpace;

public class DualSpaceController : MonoBehaviour
{
    public void SwitchSpace(SpaceType space)
    {
        DualSpaceManager.Instance.TransitionTo(space);
    }
}
```

### 3. Narrative Integration

Worldbuilding data is stored in `/Worldbuilding/` and imported via Editor tools:

```
/Worldbuilding/
  /Epochs/
  /Characters/
  /Nodes/
  NarrativeOntology.csv
```

## 📚 Resources

- [Unity Documentation](https://docs.unity3d.com/)
- [AR Foundation Guide](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/)
- [C# Coding Conventions](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
- [FIELD Geometry](/Docs/Architecture/FIELD_Geometry.md)

## 🤝 Contributing

1. Read `/Community/CONTRIBUTING.md`
2. Create a feature branch
3. Write tests for new functionality
4. Submit a pull request
5. Await code review

## 🆘 Getting Help

- Check `/Docs/MasterIndex.md` for comprehensive documentation
- Review existing code examples in `/Assets/Scripts/Examples/`
- Reach out to the team via GitHub Issues

---

*Welcome to the spiral. Let's build together.* 🌀
