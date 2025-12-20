"""
FIELD Backend Configuration

Sacred Infrastructure layer managing the backend system.
Development path: /Volumes/Akron/FIELD-DEV/
Media storage: ~/Pictures/FIELD/
Intelligence: DOJO via MCP APIs only - NEVER direct access
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum


class DojoAPIEndpoint(Enum):
    """DOJO intelligence API endpoints (MCP only)"""
    GEOMETRY_ANALYSIS = "/api/dojo/geometry/analyze"
    FIELD_DISCOVERY = "/api/dojo/field/discover"
    SACRED_MAPPING = "/api/dojo/sacred/map"
    CHARACTER_GUIDANCE = "/api/dojo/character/guide"
    EPOCH_TRANSITION = "/api/dojo/epoch/transition"


@dataclass
class FIELDConfig:
    """Configuration for FIELD backend infrastructure"""
    dev_path: str = "/Volumes/Akron/FIELD-DEV/"
    media_path: str = "~/Pictures/FIELD/"
    
    # Intelligence layer - DOJO via MCP APIs only
    dojo_base_url: str = "https://dojo.field.system"
    dojo_access_mode: str = "MCP_ONLY"  # NEVER direct access
    
    # Backend services
    services: Dict[str, Dict] = None
    
    def __post_init__(self):
        if self.services is None:
            self.services = {
                "geometry_engine": {
                    "enabled": True,
                    "description": "Sacred geometry processing engine",
                    "port": 8001
                },
                "ar_bridge": {
                    "enabled": True,
                    "description": "Bridge to Unity AR layer",
                    "port": 8002
                },
                "physical_mapper": {
                    "enabled": True,
                    "description": "Physical reality mapping service",
                    "port": 8003
                },
                "dojo_connector": {
                    "enabled": True,
                    "description": "DOJO intelligence connector (MCP only)",
                    "port": 8004,
                    "access_mode": "MCP_ONLY"
                }
            }
    
    def get_dojo_endpoint(self, endpoint: DojoAPIEndpoint) -> str:
        """Get full DOJO API endpoint URL"""
        return f"{self.dojo_base_url}{endpoint.value}"
    
    def validate_dojo_access(self) -> bool:
        """Ensure DOJO is accessed via MCP only"""
        return self.dojo_access_mode == "MCP_ONLY"
    
    def to_dict(self) -> Dict:
        """Export configuration as dictionary"""
        return {
            "dev_path": self.dev_path,
            "media_path": self.media_path,
            "dojo_base_url": self.dojo_base_url,
            "dojo_access_mode": self.dojo_access_mode,
            "services": self.services,
            "dojo_endpoints": {
                endpoint.name: self.get_dojo_endpoint(endpoint)
                for endpoint in DojoAPIEndpoint
            }
        }


class MCPClient:
    """MCP (Message Control Protocol) Client for DOJO intelligence access"""
    
    def __init__(self, config: FIELDConfig):
        self.config = config
        if not config.validate_dojo_access():
            raise ValueError("DOJO must be accessed via MCP only")
    
    async def analyze_geometry(self, geometry_data: Dict) -> Dict:
        """Analyze sacred geometry patterns via MCP"""
        endpoint = self.config.get_dojo_endpoint(DojoAPIEndpoint.GEOMETRY_ANALYSIS)
        # Implementation would use MCP protocol
        return {
            "endpoint": endpoint,
            "method": "MCP",
            "geometry_data": geometry_data,
            "status": "pending"
        }
    
    async def discover_field(self, location: Dict) -> Dict:
        """Discover new field via MCP"""
        endpoint = self.config.get_dojo_endpoint(DojoAPIEndpoint.FIELD_DISCOVERY)
        return {
            "endpoint": endpoint,
            "method": "MCP",
            "location": location,
            "status": "pending"
        }
    
    async def map_sacred_pattern(self, pattern: str) -> Dict:
        """Map sacred pattern via MCP"""
        endpoint = self.config.get_dojo_endpoint(DojoAPIEndpoint.SACRED_MAPPING)
        return {
            "endpoint": endpoint,
            "method": "MCP",
            "pattern": pattern,
            "status": "pending"
        }
    
    async def get_character_guidance(self, character_symbol: str, context: Dict) -> Dict:
        """Get character guidance via MCP"""
        endpoint = self.config.get_dojo_endpoint(DojoAPIEndpoint.CHARACTER_GUIDANCE)
        return {
            "endpoint": endpoint,
            "method": "MCP",
            "character": character_symbol,
            "context": context,
            "status": "pending"
        }
    
    async def transition_epoch(self, current_epoch: str, next_epoch: str) -> Dict:
        """Manage epoch transition via MCP"""
        endpoint = self.config.get_dojo_endpoint(DojoAPIEndpoint.EPOCH_TRANSITION)
        return {
            "endpoint": endpoint,
            "method": "MCP",
            "current_epoch": current_epoch,
            "next_epoch": next_epoch,
            "status": "pending"
        }


@dataclass
class MediaStorage:
    """Media storage configuration for AR assets"""
    base_path: str = "~/Pictures/FIELD/"
    
    def get_path(self, category: str) -> str:
        """Get path for specific media category"""
        paths = {
            "geometry": f"{self.base_path}geometry/",
            "fields": f"{self.base_path}fields/",
            "characters": f"{self.base_path}characters/",
            "ar_markers": f"{self.base_path}ar_markers/",
            "epochs": f"{self.base_path}epochs/"
        }
        return paths.get(category, self.base_path)
    
    def to_dict(self) -> Dict:
        """Export media storage configuration"""
        return {
            "base_path": self.base_path,
            "categories": {
                "geometry": self.get_path("geometry"),
                "fields": self.get_path("fields"),
                "characters": self.get_path("characters"),
                "ar_markers": self.get_path("ar_markers"),
                "epochs": self.get_path("epochs")
            }
        }


def create_field_config() -> Dict:
    """Create complete FIELD backend configuration"""
    config = FIELDConfig()
    media = MediaStorage()
    
    return {
        "backend": config.to_dict(),
        "media": media.to_dict(),
        "warnings": [
            "DOJO intelligence must ONLY be accessed via MCP APIs",
            "NEVER use direct access to DOJO",
            "All intelligence requests go through MCPClient"
        ]
    }
