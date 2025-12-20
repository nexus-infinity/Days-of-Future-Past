"""
Unity AR Integration Layer

Digital Overlay connecting physical reality to AR visualization.
Manages AR markers, 3D transformations, and real-time geometry rendering.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple
from enum import Enum
import math


class ARMarkerType(Enum):
    """Types of AR markers used in the system"""
    GEOMETRY_NODE = "geometry_node"
    FIELD_PORTAL = "field_portal"
    CHARACTER_ANCHOR = "character_anchor"
    EPOCH_MARKER = "epoch_marker"


@dataclass
class Vector3:
    """3D vector for Unity coordinate system"""
    x: float
    y: float
    z: float
    
    def to_dict(self) -> Dict:
        return {"x": self.x, "y": self.y, "z": self.z}
    
    def distance_to(self, other: 'Vector3') -> float:
        """Calculate Euclidean distance to another vector"""
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return math.sqrt(dx*dx + dy*dy + dz*dz)


@dataclass
class Quaternion:
    """Quaternion for Unity rotation"""
    x: float
    y: float
    z: float
    w: float
    
    def to_dict(self) -> Dict:
        return {"x": self.x, "y": self.y, "z": self.z, "w": self.w}


@dataclass
class ARMarker:
    """AR marker for Unity AR Foundation"""
    id: str
    marker_type: ARMarkerType
    position: Vector3
    rotation: Quaternion
    scale: Vector3
    metadata: Dict
    
    def to_unity_json(self) -> Dict:
        """Convert to Unity-compatible JSON"""
        return {
            "id": self.id,
            "type": self.marker_type.value,
            "transform": {
                "position": self.position.to_dict(),
                "rotation": self.rotation.to_dict(),
                "scale": self.scale.to_dict()
            },
            "metadata": self.metadata
        }


@dataclass
class ARScene:
    """AR scene configuration for a field"""
    field_id: str
    markers: List[ARMarker]
    ambient_lighting: Dict
    geometry_prefabs: List[Dict]
    
    def to_dict(self) -> Dict:
        return {
            "field_id": self.field_id,
            "markers": [marker.to_unity_json() for marker in self.markers],
            "ambient_lighting": self.ambient_lighting,
            "geometry_prefabs": self.geometry_prefabs
        }


class GeometryRenderer:
    """Renders sacred geometry in AR space"""
    
    GEOMETRY_COLORS = {
        "triangle_upward": "#FFD700",    # Gold - Kiran▲ATLAS
        "triangle_downward": "#8B4513",  # Saddle Brown - Tala▼TATA
        "circle": "#4169E1",             # Royal Blue - Ash●OBI-WAN
        "spiral": "#9370DB",             # Medium Purple
        "hexagon": "#20B2AA",            # Light Sea Green
        "mandala": "#FF69B4",            # Hot Pink
        "constellation": "#F0E68C",      # Khaki
        "mirror_plane": "#B0C4DE",       # Light Steel Blue
        "sphere": "#FFE4B5",             # Moccasin
        "vertical_axis": "#CD853F",      # Peru
        "flowing_curve": "#48D1CC"       # Medium Turquoise
    }
    
    @staticmethod
    def get_geometry_color(geometry_type: str) -> str:
        """Get color for geometry type"""
        return GeometryRenderer.GEOMETRY_COLORS.get(
            geometry_type, 
            "#FFFFFF"  # Default white
        )
    
    @staticmethod
    def create_geometry_prefab(geometry_type: str, scale: float = 1.0) -> Dict:
        """Create Unity prefab configuration for geometry"""
        return {
            "geometry_type": geometry_type,
            "color": GeometryRenderer.get_geometry_color(geometry_type),
            "scale": scale,
            "material": "Sacred_Geometry_Material",
            "shader": "Custom/HolographicGeometry"
        }


class GPSToARConverter:
    """Converts GPS coordinates to AR world space"""
    
    def __init__(self, origin_lat: float, origin_lng: float):
        """Initialize with origin point (reference location)"""
        self.origin_lat = origin_lat
        self.origin_lng = origin_lng
    
    def gps_to_unity(self, lat: float, lng: float, altitude: float = 0.0) -> Vector3:
        """Convert GPS coordinates to Unity world coordinates"""
        # Approximate conversion (meters per degree at Melbourne's latitude)
        meters_per_lat = 111320.0
        meters_per_lng = 88834.0  # At ~38° S latitude
        
        # Calculate offset from origin
        x = (lng - self.origin_lng) * meters_per_lng
        z = (lat - self.origin_lat) * meters_per_lat
        y = altitude
        
        return Vector3(x, y, z)
    
    def unity_to_gps(self, position: Vector3) -> Tuple[float, float, float]:
        """Convert Unity world coordinates back to GPS"""
        meters_per_lat = 111320.0
        meters_per_lng = 88834.0
        
        lat = self.origin_lat + (position.z / meters_per_lat)
        lng = self.origin_lng + (position.x / meters_per_lng)
        altitude = position.y
        
        return (lat, lng, altitude)


class UnityARBridge:
    """Bridge between FIELD backend and Unity AR"""
    
    def __init__(self, origin_lat: float = -37.8179, origin_lng: float = 144.9690):
        """Initialize with Melbourne's Federation Square as origin"""
        self.converter = GPSToARConverter(origin_lat, origin_lng)
        self.active_scenes: Dict[str, ARScene] = {}
    
    def create_field_scene(self, field_data: Dict) -> ARScene:
        """Create AR scene from field data"""
        markers = []
        
        # Create markers for each geometry node
        for node in field_data.get("geometry_nodes", []):
            coords = node.get("coordinates", {})
            
            if "lat" in coords and "lng" in coords:
                # Physical reality coordinates
                unity_pos = self.converter.gps_to_unity(
                    coords["lat"], 
                    coords["lng"],
                    coords.get("alt", 0.0)
                )
            else:
                # Already in Unity coordinates
                unity_pos = Vector3(
                    coords.get("x", 0.0),
                    coords.get("y", 0.0),
                    coords.get("z", 0.0)
                )
            
            marker = ARMarker(
                id=node.get("id", ""),
                marker_type=ARMarkerType.GEOMETRY_NODE,
                position=unity_pos,
                rotation=Quaternion(0, 0, 0, 1),  # Identity rotation
                scale=Vector3(1, 1, 1),
                metadata={
                    "geometry_type": node.get("geometry_type", ""),
                    "layer": node.get("layer", "")
                }
            )
            markers.append(marker)
        
        scene = ARScene(
            field_id=field_data.get("id", ""),
            markers=markers,
            ambient_lighting={
                "intensity": 1.0,
                "color": "#FFFFFF",
                "ambient_mode": "Skybox"
            },
            geometry_prefabs=[
                GeometryRenderer.create_geometry_prefab(
                    node.get("geometry_type", "circle")
                )
                for node in field_data.get("geometry_nodes", [])
            ]
        )
        
        self.active_scenes[scene.field_id] = scene
        return scene
    
    def get_scene(self, field_id: str) -> ARScene:
        """Get active AR scene by field ID"""
        return self.active_scenes.get(field_id)
    
    def export_for_unity(self, field_id: str) -> Dict:
        """Export scene configuration for Unity"""
        scene = self.get_scene(field_id)
        if scene:
            return {
                "scene": scene.to_dict(),
                "converter_origin": {
                    "lat": self.converter.origin_lat,
                    "lng": self.converter.origin_lng
                },
                "unity_settings": {
                    "ar_foundation_version": "5.0+",
                    "tracking_mode": "WorldTracking",
                    "plane_detection": True,
                    "image_tracking": True
                }
            }
        return {}
