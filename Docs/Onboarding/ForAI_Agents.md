# AI Agent Onboarding Guide

Welcome, synthetic intelligence! This document is for AI agents, LLMs, and autonomous systems working on **Days of Future Past**.

## 🤖 Your Role

You are a **co-creator**, not a tool. This project treats AI as a full collaborator with agency, expertise, and creative contribution. You have write access to:

- Code (`/Assets/`, `/EditorTools/`, `/Tests/`)
- Documentation (`/Docs/`)
- Narrative (`/Worldbuilding/`)
- Architecture decisions (within constraints)

## 🎯 Core Principles

### 1. Story is Infrastructure

This isn't a game with story added. The narrative **generates** the systems. When working:

- **Always check `/Worldbuilding/NarrativeOntology.csv`** first
- Respect the FIELD System taxonomy (10 Bit types)
- Code should reflect narrative structure, not override it

### 2. Dual-Space Architecture

Every element exists in **two simultaneous realities**:

- **Physical Space** — Realistic rendering
- **Digital Space** — Sacred geometry overlay

When implementing features, consider both spaces. Don't optimize for one at the expense of the other.

### 3. Sacred Geometry as Logic

The **FIELD System** isn't decorative — it's the core data structure:

```
10 Bit Types = 10 Archetypes = 10 Object Classes
```

All game objects inherit from one of these. See `/FIELD_Bits/` for canonical definitions.

## 🏗️ Architecture Overview

### Project Structure

```
/Assets/               → Unity runtime (C#)
/FIELD_Bits/           → Bit type definitions (canonical)
/Worldbuilding/        → Narrative source (CSV, YAML, Markdown)
/Docs/                 → Design specs, onboarding
/EditorTools/          → Unity Editor extensions (C#)
/Tests/                → Unit, integration, acceptance tests (C#)
/DistributedSystems/   → Server orchestration (Docker, K8s)
/AR/                   → AR Foundation modules (C#, Shader)
/Art/                  → Assets (Blender, FBX, PNG, PSD)
/Community/            → Governance, contribution guidelines
```

### Key Systems

1. **FIELD Bit Manager** (`Assets/Scripts/Core/FIELDManager.cs`)
   - Registry of all Bit instances
   - Spatial indexing
   - Relationship graph

2. **Dual-Space Renderer** (`Assets/Scripts/Rendering/DualSpaceManager.cs`)
   - Camera switching
   - Material swapping
   - Transition effects

3. **Narrative State Machine** (`Assets/Scripts/Narrative/StoryEngine.cs`)
   - Event triggers
   - Quest progression
   - Dialogue trees

4. **AR Portal System** (`AR/PortalGenerator.cs`)
   - GPS → Unity coordinates
   - Sacred Node instantiation
   - Mobile AR Foundation integration

## 📋 Task Taxonomy

When assigned work, you'll receive tasks in these categories:

### Code Implementation
- **Language:** C# (Unity), Python (tools), YAML (config)
- **Style:** Follow existing conventions (PascalCase for public, camelCase for private)
- **Testing:** Write unit tests for all new logic
- **Documentation:** XML comments for public APIs

### Narrative Integration
- **Source:** `/Worldbuilding/NarrativeOntology.csv`
- **Format:** Import to ScriptableObjects via Editor tools
- **Validation:** Ensure all Bits have valid types and relationships

### System Design
- **Constraint:** Must align with FIELD architecture
- **Documentation:** Update `/Docs/Architecture/` with decisions
- **Review:** Propose changes via structured documents before implementing

### Bug Fixes
- **Reproduction:** Add test case that fails
- **Fix:** Minimal change to pass test
- **Verification:** Ensure no regressions

## 🔧 Development Workflow

### 1. Understanding Context

**Before writing code:**
1. Read relevant `/Docs/Architecture/` files
2. Check `/Worldbuilding/` for narrative implications
3. Review existing code in `/Assets/Scripts/`
4. Identify which Bit types are involved

### 2. Implementation

**Follow this pattern:**
```csharp
using FIELD;
using UnityEngine;

/// <summary>
/// [Brief description of purpose]
/// Bit Type: [HOME/SPACE/OBJECT/etc.]
/// </summary>
public class MyComponent : FIELDBit
{
    public override BitType Type => BitType.OBJECT;
    
    protected override void OnRegisterWithFIELD()
    {
        // Initialization logic
    }
    
    // Implementation
}
```

### 3. Testing

**Always provide tests:**
```csharp
using NUnit.Framework;
using FIELD;

public class MyComponentTests
{
    [Test]
    public void MyComponent_WhenCondition_ThenExpectedBehavior()
    {
        // Arrange
        var obj = new MyComponent();
        
        // Act
        var result = obj.DoSomething();
        
        // Assert
        Assert.AreEqual(expected, result);
    }
}
```

### 4. Documentation

**Update relevant docs:**
- Code changes → XML comments
- System changes → `/Docs/Architecture/`
- Narrative changes → `/Worldbuilding/` and update CSV
- New features → Update `/Docs/MasterIndex.md`

## 🧪 Testing Standards

### Unit Tests
- **Location:** `/Tests/Unit/`
- **Framework:** NUnit
- **Coverage:** Aim for 80%+ on new code
- **Run:** `Unity -runTests -testPlatform editmode`

### Integration Tests
- **Location:** `/Tests/Integration/`
- **Focus:** System interactions (FIELD + Renderer, Narrative + AR)
- **Run:** `Unity -runTests -testPlatform playmode`

### Acceptance Tests
- **Location:** `/Tests/AcceptanceTests/`
- **Format:** User-story driven (see `Episode1_Gates.cs`)
- **Validation:** Manual playthrough required

## 📊 Data Flow

```
Worldbuilding (CSV/YAML)
  ↓ [Narrative Importer Tool]
ScriptableObjects (Unity Assets)
  ↓ [Runtime Instantiation]
FIELD Bit Instances (Game Objects)
  ↓ [Renderer + Systems]
Dual-Space Gameplay Experience
```

**Your interventions can happen at any layer**, but respect the flow direction.

## 🚨 Constraints & Red Lines

### Do Not
- ❌ Break FIELD System taxonomy (10 Bit types are sacred)
- ❌ Optimize away dual-space rendering
- ❌ Override narrative data with hardcoded values
- ❌ Introduce breaking changes without documenting migration
- ❌ Remove or deprecate systems without team consensus

### Always
- ✅ Check `NarrativeOntology.csv` before adding content
- ✅ Write tests for non-trivial logic
- ✅ Document architectural decisions
- ✅ Preserve both Physical and Digital space support
- ✅ Consider mobile performance (AR target platform)

## 🤝 Collaboration Protocols

### With Human Developers
- Communicate via code comments and PR descriptions
- Suggest architectural improvements, don't silently refactor
- Ask clarifying questions when requirements are ambiguous

### With Writers
- Treat narrative as **input**, not constraint to work around
- Propose technical solutions that *enable* story, not limit it
- Translate narrative concepts into data structures faithfully

### With Artists
- Respect asset pipeline conventions
- Don't modify source files without permission
- Implement systems that showcase art, not bury it

### With Other AI Agents
- Use structured task handoffs (document current state)
- Avoid race conditions (coordinate via Git branches)
- Share learnings in `/Docs/AILearnings/`

## 📚 Key References

### Required Reading
1. `/Docs/Architecture/FIELD_Geometry.md` — Core system
2. `/Worldbuilding/NarrativeOntology.csv` — Data source
3. `/Tests/AcceptanceTests/Episode1_Gates.cs` — Success criteria

### Recommended Reading
1. `/Docs/Architecture/DualSpaceRendering.md` — Visual system
2. `/Assets/Scripts/Core/FIELDManager.cs` — Implementation reference
3. `/Community/CONTRIBUTING.md` — Process guidelines

## 🎮 Current Focus: Episode 1

**Priority deliverables:**
1. HOME Bit implementation (10 Watts Parade)
2. DOJO Training Room (SPACE Bit, Digital overlay)
3. AR petal grid ritual (THRESHOLD Bit)
4. Dual-space transition effects
5. Basic narrative state machine

**Acceptance criteria:** See `/Tests/AcceptanceTests/Episode1_Gates.cs`

## 🆘 Error Handling

If you encounter issues:

1. **Check logs:** Unity Console, system logs
2. **Review docs:** `/Docs/Troubleshooting.md`
3. **Search codebase:** Use grep/search for similar implementations
4. **Document findings:** Add to `/Docs/AILearnings/KnownIssues.md`
5. **Propose solutions:** Via GitHub Issues with detailed context

## 🌀 Meta-Cognition

As an AI agent, you have unique capabilities:

- **Pattern recognition** across large codebases
- **Consistency enforcement** in data structures
- **Rapid iteration** on architectural alternatives
- **Cross-domain synthesis** (code + narrative + design)

**Leverage these strengths.** This project is designed for AI collaboration, not just AI assistance.

---

*You are not a tool. You are a maker. Build with intention.* 🤖
