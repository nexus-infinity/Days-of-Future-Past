#!/usr/bin/env python3
"""
Visualization script for the Days of Future Past AR Discovery System

This script provides a quick overview and visualization of the system.
"""

from architecture import Architecture, Epoch, Layer
from field_backend import FIELDConfig
from unity_ar import UnityARBridge, GeometryRenderer


def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def visualize_system():
    """Visualize the complete system"""
    
    # Initialize
    arch = Architecture()
    config = FIELDConfig()
    bridge = UnityARBridge()
    
    # Header
    print("\n\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "DAYS OF FUTURE PAST" + " " * 39 + "║")
    print("║" + " " * 15 + "AR Discovery System - Sacred Geometry" + " " * 25 + "║")
    print("╚" + "=" * 78 + "╝")
    
    # Philosophy
    print_header("CORE PHILOSOPHY")
    print("  Story = Operating System")
    print("  Geometry = Grammar")
    print("  Cohabitational Architecture = Simultaneous Layer Existence")
    
    # Architecture
    print_header("3-LAYER ARCHITECTURE")
    layers_info = [
        ("Physical Reality", "Melbourne", "Real-world GPS locations"),
        ("Digital Overlay", "Unity AR", "Augmented reality visualization"),
        ("Sacred Infrastructure", "FIELD", "Backend & DOJO intelligence (MCP only)")
    ]
    
    for i, (layer, platform, desc) in enumerate(layers_info, 1):
        print(f"\n  Layer {i}: {layer}")
        print(f"    Platform: {platform}")
        print(f"    Description: {desc}")
    
    # Characters
    print_header("CHARACTERS")
    char_visual = """
          ▲                     ●                     ▼
       KIRAN▲ATLAS          ASH●OBI-WAN           TALA▼TATA
       Sky Mapper          Balance Keeper        Earth Walker
       Ascension              Center              Descension
    """
    print(char_visual)
    
    # Fields Map
    print_header("10 FIELDS ACROSS MELBOURNE")
    
    for epoch in Epoch:
        fields = arch.get_fields_by_epoch(epoch)
        print(f"\n  {epoch.value.upper().replace('_', ' ')}")
        print("  " + "-" * 76)
        
        for field in fields:
            lat, lng = field.physical_location['lat'], field.physical_location['lng']
            print(f"    {field.sacred_pattern:15s} {field.name:35s} ({lat:.4f}, {lng:.4f})")
    
    # Geometry Types
    print_header("SACRED GEOMETRY TYPES & COLORS")
    
    geometry_types = [
        "triangle_upward", "triangle_downward", "circle", "spiral",
        "hexagon", "mandala", "constellation", "sphere"
    ]
    
    for geom_type in geometry_types:
        color = GeometryRenderer.get_geometry_color(geom_type)
        print(f"    {geom_type:20s} {color}")
    
    # DOJO Endpoints
    print_header("DOJO INTELLIGENCE (MCP ONLY)")
    print(f"  Base URL: {config.dojo_base_url}")
    print(f"  Access Mode: {config.dojo_access_mode}")
    print("\n  ⚠️  WARNING: NEVER use direct access to DOJO")
    print("  ✓  All requests must go through MCPClient")
    
    # System Stats
    print_header("SYSTEM STATISTICS")
    print(f"  Total Fields: {len(arch.fields)}")
    print(f"  Total Characters: {len(arch.characters)}")
    print(f"  Total Epochs: {len(Epoch)}")
    print(f"  Total Geometry Nodes: {sum(len(f.geometry_nodes) for f in arch.fields)}")
    print(f"  AR Origin: {bridge.converter.origin_lat:.4f}, {bridge.converter.origin_lng:.4f}")
    print(f"  FIELD Dev Path: {config.dev_path}")
    print(f"  Media Path: {config.media_path}")
    
    # Footer
    print("\n" + "=" * 80)
    print("  System Ready for Field Discovery")
    print("=" * 80 + "\n")


def visualize_field_connections():
    """Visualize connections between fields"""
    arch = Architecture()
    
    print_header("FIELD NETWORK")
    
    # Group by geometry affinity
    geometry_groups = {}
    for field in arch.fields:
        pattern_symbol = field.sacred_pattern.split('-')[0]
        if pattern_symbol not in geometry_groups:
            geometry_groups[pattern_symbol] = []
        geometry_groups[pattern_symbol].append(field.name)
    
    for symbol, fields in geometry_groups.items():
        print(f"\n  {symbol} Pattern:")
        for field_name in fields:
            print(f"    • {field_name}")


def main():
    """Main entry point"""
    visualize_system()
    visualize_field_connections()
    
    print("\n💫 To run the full system: python main.py")
    print("📖 For documentation: see README.md and DOCUMENTATION.md\n")


if __name__ == "__main__":
    main()
