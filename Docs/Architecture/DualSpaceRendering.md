# Dual-Space Rendering System

## 🌓 Overview

**Dual-Space Rendering** is the visual architecture of *Days of Future Past*. It enables players to experience **two simultaneous realities**:

1. **Physical Space** — Realistic rendering of real-world environments
2. **Digital Space** — Sacred geometry overlay with FIELD visualization

Both spaces occupy the same 3D coordinates but use different rendering pipelines, materials, and visual languages.

## 🎯 Core Concept

> The world is not "real" or "virtual" — it is **both, always, simultaneously**.

Players don't switch between modes; they **shift perception** to reveal different truths about the same space.

## 🏗️ Technical Architecture

### Rendering Pipeline

```
Unity URP (Universal Render Pipeline)
  ├─ Physical Camera (Layer: Physical)
  │    ├─ Realistic materials (PBR)
  │    ├─ Natural lighting (baked + realtime)
  │    └─ Post-processing (color grading, bloom)
  │
  └─ Digital Camera (Layer: Digital)
       ├─ Sacred geometry materials (emissive, Shader Graph)
       ├─ Procedural lighting (FIELD node glow)
       └─ Post-processing (edge detection, glow, HDR)
```

### Layer System

Unity Layers organize objects by space:

| Layer         | Content                          | Camera      |
|---------------|----------------------------------|-------------|
| **Physical**  | Real-world geometry, textures    | Physical Cam|
| **Digital**   | FIELD geometry, glowing overlays | Digital Cam |
| **Hybrid**    | Visible in both spaces           | Both Cams   |
| **UI**        | Interface elements               | UI Cam      |

### Material Swapping

Each game object has **two materials**:

```csharp
public class DualSpaceObject : MonoBehaviour
{
    [SerializeField] private Material physicalMaterial;
    [SerializeField] private Material digitalMaterial;
    
    private Renderer objectRenderer;
    
    void Start()
    {
        objectRenderer = GetComponent<Renderer>();
        UpdateMaterial(DualSpaceManager.CurrentSpace);
    }
    
    void UpdateMaterial(SpaceType space)
    {
        objectRenderer.material = space == SpaceType.Physical 
            ? physicalMaterial 
            : digitalMaterial;
    }
}
```

## 🎨 Visual Languages

### Physical Space

**Aesthetic:** Warm, lived-in, Pinterest home  
**Goal:** Grounded realism that evokes nostalgia and comfort

**Characteristics:**
- Natural lighting (sun through windows, warm lamps)
- PBR materials (wood grain, fabric texture, worn surfaces)
- Color palette: Warm neutrals, dusty rose, sage green, terracotta
- Imperfection: Scratches, patina, asymmetry
- Camera: Slight depth of field, subtle bloom

**Reference:**
- Interior photography (Pinterest "cozy home aesthetic")
- Australian coastal homes (10 Watts Parade, Mount Eliza)
- Analog film look (slight grain, soft highlights)

### Digital Space

**Aesthetic:** Sacred geometry meets Matrix  
**Goal:** Reveal hidden order and systemic relationships

**Characteristics:**
- High-contrast (white void or black background + glowing objects)
- Emissive materials (self-illuminated, no external light sources)
- Color palette: FIELD Bit colors (gold, cyan, violet, etc.)
- Perfect geometry: Platonic solids, fractals, symmetry
- Camera: Edge detection shader, HDR glow, no depth of field

**Reference:**
- *The Matrix* (white training room)
- Sacred geometry diagrams (Metatron's Cube, Flower of Life)
- Tron-style minimalism
- Cymatics (sound made visible)

## 🔄 Transition Effects

### Instant Switch (for testing)

```csharp
DualSpaceManager.Instance.SetSpace(SpaceType.Digital);
```

### Smooth Transition (production)

```csharp
DualSpaceManager.Instance.TransitionTo(
    SpaceType.Digital, 
    duration: 2.0f, 
    curve: AnimationCurve.EaseInOut
);
```

**Visual effect during transition:**
1. Screen desaturates (Physical → Grayscale)
2. Geometry wireframes appear
3. Materials cross-fade
4. FIELD nodes pulse into visibility
5. Digital space fully resolves

### Blend Mode (advanced)

For ritual moments, both spaces visible at partial opacity:

```csharp
DualSpaceManager.Instance.SetBlendMode(
    physicalOpacity: 0.4f, 
    digitalOpacity: 0.8f
);
```

## 🎮 Gameplay Integration

### Space-Dependent Interactions

Some objects only exist in one space:

```csharp
public class SpaceRestrictedObject : MonoBehaviour
{
    [SerializeField] private SpaceType requiredSpace;
    
    void OnMouseDown()
    {
        if (DualSpaceManager.CurrentSpace == requiredSpace)
        {
            Interact();
        }
        else
        {
            ShowHint("Switch to " + requiredSpace + " space to interact.");
        }
    }
}
```

### Hybrid Objects

Some objects reveal different aspects in each space:

```csharp
public class HybridObject : FIELDBit
{
    [SerializeField] private string physicalDescription;
    [SerializeField] private string digitalDescription;
    
    public void Examine()
    {
        string desc = DualSpaceManager.CurrentSpace == SpaceType.Physical
            ? physicalDescription
            : digitalDescription;
        
        UIManager.ShowDescription(desc);
    }
}
```

**Example:**
- **Physical:** "An old wooden door, paint peeling at the edges."
- **Digital:** "A magenta THRESHOLD portal, shimmering with potential."

## 📐 Camera Setup

### Physical Camera

```csharp
Camera physicalCamera = GameObject.Find("PhysicalCamera").GetComponent<Camera>();
physicalCamera.cullingMask = LayerMask.GetMask("Physical", "Hybrid");
physicalCamera.clearFlags = CameraClearFlags.Skybox;
physicalCamera.farClipPlane = 1000f;

// Post-processing
var volume = physicalCamera.GetComponent<Volume>();
volume.profile.TryGet<ColorAdjustments>(out var colorAdj);
colorAdj.saturation.value = 0.1f; // Slight boost
```

### Digital Camera

```csharp
Camera digitalCamera = GameObject.Find("DigitalCamera").GetComponent<Camera>();
digitalCamera.cullingMask = LayerMask.GetMask("Digital", "Hybrid");
digitalCamera.clearFlags = CameraClearFlags.SolidColor;
digitalCamera.backgroundColor = Color.white; // or Color.black
digitalCamera.farClipPlane = 1000f;

// Post-processing
var volume = digitalCamera.GetComponent<Volume>();
volume.profile.TryGet<Bloom>(out var bloom);
bloom.intensity.value = 3.0f; // Heavy glow
```

## 🛠️ Implementation Details

### Dual-Space Manager (Singleton)

```csharp
using UnityEngine;
using System.Collections;

public enum SpaceType { Physical, Digital }

public class DualSpaceManager : MonoBehaviour
{
    public static DualSpaceManager Instance { get; private set; }
    
    public SpaceType CurrentSpace { get; private set; }
    
    [SerializeField] private Camera physicalCamera;
    [SerializeField] private Camera digitalCamera;
    
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
        
        SetSpace(SpaceType.Physical); // Default
    }
    
    public void SetSpace(SpaceType space)
    {
        CurrentSpace = space;
        
        physicalCamera.enabled = (space == SpaceType.Physical);
        digitalCamera.enabled = (space == SpaceType.Digital);
        
        NotifyAllObjects();
    }
    
    public void TransitionTo(SpaceType space, float duration, AnimationCurve curve)
    {
        StartCoroutine(TransitionCoroutine(space, duration, curve));
    }
    
    private IEnumerator TransitionCoroutine(SpaceType space, float duration, AnimationCurve curve)
    {
        float elapsed = 0f;
        
        while (elapsed < duration)
        {
            elapsed += Time.deltaTime;
            float t = curve.Evaluate(elapsed / duration);
            
            // Blend cameras (simplified)
            physicalCamera.targetDisplay = 0;
            digitalCamera.targetDisplay = 0;
            
            // TODO: Implement proper blend via post-processing or render textures
            
            yield return null;
        }
        
        SetSpace(space);
    }
    
    private void NotifyAllObjects()
    {
        var dualSpaceObjects = FindObjectsOfType<DualSpaceObject>();
        foreach (var obj in dualSpaceObjects)
        {
            obj.OnSpaceChanged(CurrentSpace);
        }
    }
}
```

### Shader Graph for Digital Materials

**Inputs:**
- Base color (FIELD Bit archetypal color)
- Emission intensity (controlled by distance to player or time)
- Edge glow (Fresnel effect)

**Outputs:**
- Unlit surface (no lighting calculations)
- HDR emission (for bloom)

**Example nodes:**
```
Color (Gold) 
  → Multiply (Emission Intensity)
  → Add (Fresnel for edge glow)
  → Emission output
```

## 🎭 Narrative Integration

Dual-Space rendering is not just visual flair — it's **narrative mechanic**:

### Story Beats Tied to Space

- **Act 1:** Player only sees Physical space (normal world)
- **Inciting Incident:** First glimpse of Digital space (glitch, vision)
- **Act 2:** Player gains ability to switch at will
- **Climax:** Both spaces must be navigated simultaneously (puzzle)
- **Resolution:** Spaces merge (hybrid mode, acceptance)

### Example Scene

**Location:** DOJO Training Room

- **Physical Space:** A dusty garage with workout equipment
- **Digital Space:** Infinite white void with floating geometric forms

**Narrative:** "The room is both a garage and a void. Which is more real?"

## 🧪 Testing & Debug

### Debug View

Toggle a debug mode that shows both spaces side-by-side:

```csharp
[SerializeField] private bool debugMode = false;

void Update()
{
    if (Input.GetKeyDown(KeyCode.F1))
    {
        debugMode = !debugMode;
        
        if (debugMode)
        {
            // Split screen: left = Physical, right = Digital
            physicalCamera.rect = new Rect(0, 0, 0.5f, 1);
            digitalCamera.rect = new Rect(0.5f, 0, 0.5f, 1);
            
            physicalCamera.enabled = true;
            digitalCamera.enabled = true;
        }
        else
        {
            physicalCamera.rect = new Rect(0, 0, 1, 1);
            digitalCamera.rect = new Rect(0, 0, 1, 1);
            
            SetSpace(CurrentSpace);
        }
    }
}
```

### Performance Monitoring

- Target: 60 FPS on mobile (AR device)
- Monitor: GPU overhead of dual materials
- Optimize: LOD system, occlusion culling per layer

## 📚 Further Reading

- `/Docs/Architecture/FIELD_Geometry.md` — What gets rendered
- `/Art/StyleGuides/` — Visual reference guides
- [Unity URP Documentation](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest)

---

*Two spaces. One truth. Shift your perception.* 🌓
