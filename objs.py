from typing import overload
import projection

PROJECTION_TYPES = {}

class Vector3D:
    @property
    def x(self) -> float: return self.coords[0]
    @property
    def y(self) -> float: return self.coords[1]
    @property
    def z(self) -> float: return self.coords[2]
    @overload
    def __init__(self, coords: tuple) -> None: ...
    @overload
    def __init__(self, x: float, y: float, z: float = ...) -> None: ...
    def __init__(self, *args) -> None: self.coords = args[0] if len(args) == 1 else args

class Vector2D:
    @property
    def x(self) -> float: return self.coords[0]
    @property
    def y(self) -> float: return self.coords[1]
    @property
    @overload
    def __init__(self, coords: tuple) -> None: ...
    @overload
    def __init__(self, x: float, y: float) -> None: ...
    def __init__(self, *args) -> None: self.coords = args[0] if len(args) == 1 else args
    def to3d(self, depth: float = 0) -> Vector3D: return Vector3D(self.x, self.y, depth)

class Poly:
    def __init__(self, points = list[Vector3D]) -> None: ...
    def __add__(self, other: Poly) -> Poly: ...

class Camera:
    @property
    def x(self) -> float: return self.pos[0]
    @property
    def y(self) -> float: return self.pos[1]
    @property
    def z(self) -> float: return self.pos[2]
    @property
    def rotx(self) -> float: return self.rot[0]
    @property
    def roty(self) -> float: return self.rot[1]
    @property
    def rotz(self) -> float: return self.rot[2]
    def __init__(self, position: Vector3D, rotation: Vector3D) -> None: self.pos, self.rot = position, rotation
    def project_point(self, point: Vector3D, projectiontype = "1p-perspective") -> Vector2D: return PROJECTION_TYPES[projectiontype](point, self)
    def display_view(self, points: list[Vector3D]) -> list[Vector2D]: return [self.project_point(p) for p in points] 

class Space: ...
