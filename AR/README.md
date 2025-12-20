# AR (Augmented Reality)

**AR Foundation Integration Modules**

This directory contains AR-specific code and assets for *Days of Future Past*.

## 📱 Overview

AR transforms real-world locations into **Sacred Nodes** — portals where physical and digital spaces interweave.

## 🛠️ Technology

- **Unity AR Foundation** — Cross-platform AR framework
- **ARCore** (Android) and **ARKit** (iOS)
- **GPS integration** — Geographic coordinates → Unity coordinates
- **Plane detection** — Ground/surface recognition

## 📂 Planned Structure

```
/AR/
  /Scripts/
    ARPortalManager.cs      — Sacred Node spawning
    GPSConverter.cs         — Coordinate conversion
    PetalGridRitual.cs      — Backyard AR interaction
    SacredNodeBehavior.cs   — AR portal logic
  
  /Prefabs/
    SacredNode_Portal.prefab
    PetalGrid.prefab
  
  /Nodes/                   — Per-location AR content definitions
```

## 🎯 Key Features

### 1. Sacred Node Portals

Real-world GPS locations become interactive AR gateways:
- Mount Eliza locations as portals
- Visual: THRESHOLD Bit geometry (magenta arch)
- Interaction: Enter portal to trigger narrative events

### 2. Petal Grid Ritual

Backyard AR experience in Episode 1:
- Geometric pattern overlaid on ground
- Interactive ritual sequence
- Unlocks full FIELD vision

### 3. GPS-to-Unity Conversion

Convert geographic coordinates to Unity world space:
```csharp
Vector3 unityPos = GPSConverter.LatLngToUnity(latitude, longitude);
```

## 📚 Resources

- [AR Foundation Documentation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@5.0/)
- [ForDevelopers.md](../Docs/Onboarding/ForDevelopers.md)

---

*The physical world is the interface.* 📱
