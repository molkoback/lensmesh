# lensmesh
Python module for generating 3D lens objects.

## Requirements
* `$ pip3 install -r requirements.txt`
* Blender 2.79 or OpenSCAD

## Example
```python
from lensmesh import PlanoConvex

lens = PlanoConvex(38.10, 33.09, 10.04, accuracy=4, engine="blender")
lens.show()
lens.save("lens.stl")
```
