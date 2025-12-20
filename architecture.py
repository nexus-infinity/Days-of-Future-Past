"""
Days of Future Past - AR Discovery System Architecture

3-Layer Cohabitational Architecture:
- Physical Reality (Melbourne)
- Digital Overlay (Unity AR)
- Sacred Infrastructure (FIELD backend)

Philosophy: Story=OS, geometry=grammar
Layers exist simultaneously, not as replacements.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional


class Layer(Enum):
    """Three architectural layers of the system"""
    PHYSICAL_REALITY = "physical_reality"  # Melbourne
    DIGITAL_OVERLAY = "digital_overlay"    # Unity AR
    SACRED_INFRASTRUCTURE = "sacred_infrastructure"  # FIELD backend


class Epoch(Enum):
    """Four temporal epochs for field exploration"""
    EPOCH_1 = "epoch_1"
    EPOCH_2 = "epoch_2"
    EPOCH_3 = "epoch_3"
    EPOCH_4 = "epoch_4"


@dataclass
class GeometryNode:
    """Sacred geometry node representing a point in the grammar"""
    id: str
    layer: Layer
    coordinates: Dict[str, float]  # lat, lng for physical; x, y, z for digital
    geometry_type: str  # triangle, circle, square, etc.
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "layer": self.layer.value,
            "coordinates": self.coordinates,
            "geometry_type": self.geometry_type
        }


@dataclass
class Field:
    """Unexplored field in the AR discovery system"""
    id: str
    name: str
    epoch: Epoch
    geometry_nodes: List[GeometryNode]
    physical_location: Dict[str, float]  # Melbourne coordinates
    sacred_pattern: str  # The geometric pattern/grammar
    
    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "epoch": self.epoch.value,
            "geometry_nodes": [node.to_dict() for node in self.geometry_nodes],
            "physical_location": self.physical_location,
            "sacred_pattern": self.sacred_pattern
        }


@dataclass
class Character:
    """Character in the AR discovery system"""
    name: str
    symbol: str
    role: str
    archetype: str
    geometry_affinity: str
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "symbol": self.symbol,
            "role": self.role,
            "archetype": self.archetype,
            "geometry_affinity": self.geometry_affinity
        }


class Architecture:
    """Main architecture managing the 3-layer system"""
    
    def __init__(self):
        self.layers = {
            Layer.PHYSICAL_REALITY: {
                "location": "Melbourne",
                "description": "Physical world locations and landmarks"
            },
            Layer.DIGITAL_OVERLAY: {
                "platform": "Unity AR",
                "description": "Augmented reality layer overlaying physical reality"
            },
            Layer.SACRED_INFRASTRUCTURE: {
                "backend": "FIELD",
                "path": "/Volumes/Akron/FIELD-DEV/",
                "media_path": "~/Pictures/FIELD/",
                "intelligence": "DOJO via MCP APIs only",
                "description": "Backend infrastructure managing sacred geometry"
            }
        }
        self.characters = self._initialize_characters()
        self.fields = self._initialize_fields()
    
    def _initialize_characters(self) -> List[Character]:
        """Initialize the three main characters"""
        return [
            Character(
                name="Tala",
                symbol="▼TATA",
                role="Descender",
                archetype="Earth Walker",
                geometry_affinity="triangles_downward"
            ),
            Character(
                name="Kiran",
                symbol="▲ATLAS",
                role="Ascender",
                archetype="Sky Mapper",
                geometry_affinity="triangles_upward"
            ),
            Character(
                name="Ash",
                symbol="●OBI-WAN",
                role="Centerer",
                archetype="Balance Keeper",
                geometry_affinity="circles"
            )
        ]
    
    def _initialize_fields(self) -> List[Field]:
        """Initialize 10 unexplored fields across 4 epochs"""
        # Melbourne coordinates as reference points
        fields = [
            # Epoch 1: 3 fields
            Field(
                id="field_01",
                name="Federation Square Gateway",
                epoch=Epoch.EPOCH_1,
                geometry_nodes=[
                    GeometryNode("node_01_01", Layer.PHYSICAL_REALITY, 
                                {"lat": -37.8179, "lng": 144.9690}, "triangle_upward"),
                    GeometryNode("node_01_02", Layer.DIGITAL_OVERLAY,
                                {"x": 0, "y": 0, "z": 0}, "triangle_upward"),
                ],
                physical_location={"lat": -37.8179, "lng": 144.9690},
                sacred_pattern="▲-gateway"
            ),
            Field(
                id="field_02",
                name="Royal Botanic Gardens Spiral",
                epoch=Epoch.EPOCH_1,
                geometry_nodes=[
                    GeometryNode("node_02_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8304, "lng": 144.9796}, "spiral"),
                    GeometryNode("node_02_02", Layer.DIGITAL_OVERLAY,
                                {"x": 100, "y": 0, "z": 100}, "spiral"),
                ],
                physical_location={"lat": -37.8304, "lng": 144.9796},
                sacred_pattern="●-spiral"
            ),
            Field(
                id="field_03",
                name="Shrine of Remembrance Axis",
                epoch=Epoch.EPOCH_1,
                geometry_nodes=[
                    GeometryNode("node_03_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8304, "lng": 144.9733}, "vertical_axis"),
                    GeometryNode("node_03_02", Layer.DIGITAL_OVERLAY,
                                {"x": 50, "y": 100, "z": 50}, "vertical_axis"),
                ],
                physical_location={"lat": -37.8304, "lng": 144.9733},
                sacred_pattern="▲▼-axis"
            ),
            
            # Epoch 2: 3 fields
            Field(
                id="field_04",
                name="Yarra River Confluence",
                epoch=Epoch.EPOCH_2,
                geometry_nodes=[
                    GeometryNode("node_04_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8226, "lng": 144.9631}, "flowing_curve"),
                    GeometryNode("node_04_02", Layer.DIGITAL_OVERLAY,
                                {"x": 200, "y": 0, "z": 200}, "flowing_curve"),
                ],
                physical_location={"lat": -37.8226, "lng": 144.9631},
                sacred_pattern="●-flow"
            ),
            Field(
                id="field_05",
                name="State Library Triangle",
                epoch=Epoch.EPOCH_2,
                geometry_nodes=[
                    GeometryNode("node_05_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8098, "lng": 144.9652}, "triangle_downward"),
                    GeometryNode("node_05_02", Layer.DIGITAL_OVERLAY,
                                {"x": 150, "y": 50, "z": 150}, "triangle_downward"),
                ],
                physical_location={"lat": -37.8098, "lng": 144.9652},
                sacred_pattern="▼-knowledge"
            ),
            Field(
                id="field_06",
                name="Parliament House Hexagon",
                epoch=Epoch.EPOCH_2,
                geometry_nodes=[
                    GeometryNode("node_06_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8107, "lng": 144.9737}, "hexagon"),
                    GeometryNode("node_06_02", Layer.DIGITAL_OVERLAY,
                                {"x": 300, "y": 0, "z": 300}, "hexagon"),
                ],
                physical_location={"lat": -37.8107, "lng": 144.9737},
                sacred_pattern="●-power"
            ),
            
            # Epoch 3: 2 fields
            Field(
                id="field_07",
                name="Carlton Gardens Mandala",
                epoch=Epoch.EPOCH_3,
                geometry_nodes=[
                    GeometryNode("node_07_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8047, "lng": 144.9717}, "mandala"),
                    GeometryNode("node_07_02", Layer.DIGITAL_OVERLAY,
                                {"x": 250, "y": 0, "z": 250}, "mandala"),
                ],
                physical_location={"lat": -37.8047, "lng": 144.9717},
                sacred_pattern="●-wholeness"
            ),
            Field(
                id="field_08",
                name="Docklands Constellation",
                epoch=Epoch.EPOCH_3,
                geometry_nodes=[
                    GeometryNode("node_08_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8152, "lng": 144.9461}, "constellation"),
                    GeometryNode("node_08_02", Layer.DIGITAL_OVERLAY,
                                {"x": 350, "y": 50, "z": 350}, "constellation"),
                ],
                physical_location={"lat": -37.8152, "lng": 144.9461},
                sacred_pattern="▲-stars"
            ),
            
            # Epoch 4: 2 fields
            Field(
                id="field_09",
                name="Southbank Reflection Portal",
                epoch=Epoch.EPOCH_4,
                geometry_nodes=[
                    GeometryNode("node_09_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8219, "lng": 144.9673}, "mirror_plane"),
                    GeometryNode("node_09_02", Layer.DIGITAL_OVERLAY,
                                {"x": 400, "y": 0, "z": 400}, "mirror_plane"),
                ],
                physical_location={"lat": -37.8219, "lng": 144.9673},
                sacred_pattern="▼-reflection"
            ),
            Field(
                id="field_10",
                name="Crown Unity Sphere",
                epoch=Epoch.EPOCH_4,
                geometry_nodes=[
                    GeometryNode("node_10_01", Layer.PHYSICAL_REALITY,
                                {"lat": -37.8229, "lng": 144.9588}, "sphere"),
                    GeometryNode("node_10_02", Layer.DIGITAL_OVERLAY,
                                {"x": 500, "y": 0, "z": 500}, "sphere"),
                ],
                physical_location={"lat": -37.8229, "lng": 144.9588},
                sacred_pattern="●-unity"
            ),
        ]
        return fields
    
    def get_layer_info(self, layer: Layer) -> Dict:
        """Get information about a specific layer"""
        return self.layers.get(layer, {})
    
    def get_fields_by_epoch(self, epoch: Epoch) -> List[Field]:
        """Get all fields for a specific epoch"""
        return [field for field in self.fields if field.epoch == epoch]
    
    def get_character_by_symbol(self, symbol: str) -> Optional[Character]:
        """Get character by their symbol"""
        for char in self.characters:
            if symbol in char.symbol:
                return char
        return None
    
    def to_dict(self) -> Dict:
        """Export architecture as dictionary"""
        return {
            "layers": {layer.value: info for layer, info in self.layers.items()},
            "characters": [char.to_dict() for char in self.characters],
            "fields": [field.to_dict() for field in self.fields],
            "philosophy": {
                "story_os": "Story is the operating system",
                "geometry_grammar": "Geometry is the grammar",
                "cohabitation": "Layers exist simultaneously, not as replacements"
            }
        }
