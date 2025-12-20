"""
Main application integrating all three layers of the AR discovery system.

Demonstrates cohabitational architecture where:
- Physical Reality (Melbourne)
- Digital Overlay (Unity AR)
- Sacred Infrastructure (FIELD backend)

All exist simultaneously, not as replacements.
"""

import json
from typing import Dict, List
from architecture import Architecture, Layer, Epoch
from field_backend import FIELDConfig, MCPClient, MediaStorage, create_field_config
from unity_ar import UnityARBridge, GeometryRenderer


class DaysOfFuturePast:
    """Main application class for the AR discovery system"""
    
    def __init__(self):
        """Initialize the three-layer system"""
        print("Initializing Days of Future Past AR Discovery System...")
        print("Philosophy: Story=OS, geometry=grammar")
        print("Architecture: Cohabitational layers (simultaneous existence)\n")
        
        # Initialize architecture
        self.architecture = Architecture()
        
        # Initialize FIELD backend
        self.field_config = FIELDConfig()
        self.mcp_client = MCPClient(self.field_config)
        self.media_storage = MediaStorage()
        
        # Initialize Unity AR bridge
        self.unity_bridge = UnityARBridge()
        
        print("✓ Physical Reality layer (Melbourne) initialized")
        print("✓ Digital Overlay layer (Unity AR) initialized")
        print("✓ Sacred Infrastructure layer (FIELD backend) initialized\n")
    
    def display_system_overview(self):
        """Display complete system overview"""
        print("=" * 80)
        print("DAYS OF FUTURE PAST - AR DISCOVERY SYSTEM")
        print("=" * 80)
        
        # Layers
        print("\n3-LAYER ARCHITECTURE:")
        print("-" * 80)
        for layer in Layer:
            info = self.architecture.get_layer_info(layer)
            print(f"  {layer.value.upper().replace('_', ' ')}")
            for key, value in info.items():
                if key != "path" and key != "media_path":
                    print(f"    • {key}: {value}")
        
        # Characters
        print("\n" + "=" * 80)
        print("CHARACTERS:")
        print("-" * 80)
        for char in self.architecture.characters:
            print(f"  {char.name} {char.symbol}")
            print(f"    Role: {char.role}")
            print(f"    Archetype: {char.archetype}")
            print(f"    Geometry: {char.geometry_affinity}\n")
        
        # Fields by epoch
        print("=" * 80)
        print("10 UNEXPLORED FIELDS ACROSS 4 EPOCHS:")
        print("-" * 80)
        for epoch in Epoch:
            fields = self.architecture.get_fields_by_epoch(epoch)
            print(f"\n  {epoch.value.upper().replace('_', ' ')} ({len(fields)} fields):")
            for field in fields:
                print(f"    • {field.name}")
                print(f"      Pattern: {field.sacred_pattern}")
                print(f"      Location: {field.physical_location['lat']:.4f}, "
                      f"{field.physical_location['lng']:.4f}")
        
        print("\n" + "=" * 80)
    
    def generate_field_ar_scenes(self):
        """Generate AR scenes for all fields"""
        print("\nGenerating Unity AR scenes for all fields...")
        print("-" * 80)
        
        scenes = {}
        for field in self.architecture.fields:
            scene = self.unity_bridge.create_field_scene(field.to_dict())
            scenes[field.id] = scene
            print(f"✓ Generated AR scene for {field.name}")
        
        print(f"\nTotal scenes created: {len(scenes)}")
        return scenes
    
    def export_unity_configuration(self, output_path: str = "unity_config.json"):
        """Export Unity AR configuration"""
        print(f"\nExporting Unity AR configuration to {output_path}...")
        
        config = {
            "project_name": "Days of Future Past AR",
            "scenes": []
        }
        
        for field in self.architecture.fields:
            scene_config = self.unity_bridge.export_for_unity(field.id)
            if scene_config:
                config["scenes"].append(scene_config)
        
        with open(output_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✓ Unity configuration exported successfully")
        return config
    
    def export_field_backend_config(self, output_path: str = "field_config.json"):
        """Export FIELD backend configuration"""
        print(f"\nExporting FIELD backend configuration to {output_path}...")
        
        config = create_field_config()
        
        with open(output_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"✓ FIELD backend configuration exported successfully")
        print("\nWARNING: DOJO intelligence must ONLY be accessed via MCP APIs")
        print("         NEVER use direct access to DOJO")
        return config
    
    def export_full_architecture(self, output_path: str = "architecture.json"):
        """Export complete architecture"""
        print(f"\nExporting complete architecture to {output_path}...")
        
        architecture_dict = self.architecture.to_dict()
        
        with open(output_path, 'w') as f:
            json.dump(architecture_dict, f, indent=2)
        
        print(f"✓ Complete architecture exported successfully")
        return architecture_dict
    
    def demonstrate_field_discovery(self, field_id: str):
        """Demonstrate discovering a specific field"""
        print(f"\n{'='*80}")
        print(f"FIELD DISCOVERY DEMONSTRATION: {field_id}")
        print(f"{'='*80}")
        
        # Find the field
        field = None
        for f in self.architecture.fields:
            if f.id == field_id:
                field = f
                break
        
        if not field:
            print(f"Field {field_id} not found")
            return
        
        print(f"\nField: {field.name}")
        print(f"Epoch: {field.epoch.value}")
        print(f"Sacred Pattern: {field.sacred_pattern}")
        print(f"Physical Location: {field.physical_location['lat']:.4f}, "
              f"{field.physical_location['lng']:.4f}")
        
        print(f"\nGeometry Nodes ({len(field.geometry_nodes)}):")
        for node in field.geometry_nodes:
            print(f"  • {node.id}")
            print(f"    Layer: {node.layer.value}")
            print(f"    Type: {node.geometry_type}")
            color = GeometryRenderer.get_geometry_color(node.geometry_type)
            print(f"    Color: {color}")
        
        # Get AR scene
        scene = self.unity_bridge.get_scene(field_id)
        if scene:
            print(f"\nAR Scene:")
            print(f"  Markers: {len(scene.markers)}")
            print(f"  Prefabs: {len(scene.geometry_prefabs)}")
        
        print(f"\n{'='*80}")


def main():
    """Main entry point"""
    # Initialize system
    app = DaysOfFuturePast()
    
    # Display overview
    app.display_system_overview()
    
    # Generate AR scenes
    app.generate_field_ar_scenes()
    
    # Export configurations
    app.export_unity_configuration()
    app.export_field_backend_config()
    app.export_full_architecture()
    
    # Demonstrate field discovery
    print("\n")
    app.demonstrate_field_discovery("field_01")
    app.demonstrate_field_discovery("field_05")
    app.demonstrate_field_discovery("field_10")
    
    print("\n" + "="*80)
    print("SYSTEM INITIALIZATION COMPLETE")
    print("="*80)
    print("\nCohabitational Architecture Active:")
    print("  → Physical Reality: Melbourne locations mapped")
    print("  → Digital Overlay: Unity AR scenes configured")
    print("  → Sacred Infrastructure: FIELD backend ready")
    print("\nStory=OS | Geometry=Grammar | Simultaneous Existence")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
