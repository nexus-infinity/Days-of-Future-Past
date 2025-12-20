# Editor Tools

**Custom Unity Editor Extensions**

This directory contains custom tools that enhance the Unity Editor workflow for *Days of Future Past* development.

## 🛠️ Overview

These tools bridge the gap between narrative content (in `/Worldbuilding/`) and Unity runtime systems, automate validation, and provide specialized workflows for FIELD-aligned development.

## 🎯 Available Tools

### 1. FIELD Validator

**File:** `FIELDValidatorWindow.cs`  
**Menu:** `Tools > FIELD > Validate Scene`

**Purpose:** Ensures all GameObjects in the scene have correct FIELD Bit type assignments.

**Features:**
- Scans scene for objects missing Bit components
- Validates Bit type consistency with NarrativeOntology.csv
- Checks for duplicate BitIDs
- Reports orphaned relationships
- Auto-fix common issues

### 2. Narrative Importer

**File:** `NarrativeImporterWindow.cs`  
**Menu:** `Tools > FIELD > Import Narrative`

**Purpose:** Converts `/Worldbuilding/NarrativeOntology.csv` into Unity ScriptableObjects.

**Process:**
1. Reads CSV file
2. Parses entries by Bit type
3. Generates ScriptableObject assets in `/Assets/ScriptableObjects/Narrative/`
4. Establishes relationships between objects
5. Validates data integrity

### 3. AR Node Generator

**File:** `ARNodeGeneratorWindow.cs`  
**Menu:** `Tools > FIELD > Generate AR Nodes`

**Purpose:** Creates AR portal GameObjects from geographic coordinates.

**Features:**
- Imports GPS data from `/Worldbuilding/Nodes/`
- Converts lat/lng to Unity world coordinates
- Instantiates Sacred Node prefabs
- Configures AR Foundation components
- Generates preview map in Scene view

### 4. Dual-Space Preview

**File:** `DualSpacePreviewWindow.cs`  
**Menu:** `Tools > FIELD > Preview Dual Space`

**Purpose:** Editor window showing side-by-side Physical and Digital space rendering.

**Features:**
- Split-screen preview (no need to play scene)
- Real-time material swapping visualization
- Toggle individual layers
- Export comparison screenshots

### 5. Bit Type Wizard

**File:** `BitTypeWizard.cs`  
**Menu:** `Assets > Create > FIELD > New Bit Type`

**Purpose:** Scaffolds new FIELD Bit type implementations.

**Generates:**
- C# script inheriting from FIELDBit
- ScriptableObject definition
- Test template
- Documentation stub

## 🔧 Usage

### Installing Tools

Tools are automatically available once scripts are in `/EditorTools/` directory.

**Refresh:** `Assets > Refresh` or restart Unity if tools don't appear.

### FIELD Validator Example

1. Open scene: `Assets/Scenes/Episode1_HomeBase.unity`
2. Menu: `Tools > FIELD > Validate Scene`
3. Review validation report in window
4. Click "Auto-Fix" for simple issues
5. Manually address complex problems

### Narrative Importer Example

1. Edit `/Worldbuilding/NarrativeOntology.csv`
2. Menu: `Tools > FIELD > Import Narrative`
3. Click "Import"
4. Wait for process to complete
5. Check `/Assets/ScriptableObjects/Narrative/` for generated assets

### AR Node Generator Example

1. Add node data to `/Worldbuilding/Nodes/`
2. Menu: `Tools > FIELD > Generate AR Nodes`
3. Select node file
4. Click "Generate"
5. AR portal prefabs instantiated in scene

## 📝 Creating Custom Tools

### Template Structure

```csharp
using UnityEngine;
using UnityEditor;

public class MyCustomToolWindow : EditorWindow
{
    [MenuItem("Tools/FIELD/My Custom Tool")]
    public static void ShowWindow()
    {
        GetWindow<MyCustomToolWindow>("My Tool");
    }
    
    void OnGUI()
    {
        GUILayout.Label("My Custom Tool", EditorStyles.boldLabel);
        
        if (GUILayout.Button("Execute"))
        {
            Execute();
        }
    }
    
    void Execute()
    {
        // Tool logic here
        Debug.Log("Tool executed");
    }
}
```

### Best Practices

- Use `EditorUtility.DisplayProgressBar()` for long operations
- Validate inputs before processing
- Provide clear error messages
- Add undo support: `Undo.RecordObject()`
- Document tool usage in comments

## 📚 Resources

- [Unity Editor Scripting](https://docs.unity3d.com/Manual/editor-EditorWindows.html)
- [ForDevelopers.md](../Docs/Onboarding/ForDevelopers.md)

---

*Automate the tedious. Focus on the creative.* 🛠️
