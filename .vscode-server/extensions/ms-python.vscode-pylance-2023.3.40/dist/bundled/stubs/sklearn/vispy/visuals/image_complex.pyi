from numpy.typing import NDArray, ArrayLike
from .image import ImageVisual, _APPLY_CLIM_FLOAT, _APPLY_GAMMA_FLOAT
import numpy as np
from .shaders import Function, FunctionChain

# In a complex Image, the texture will be rg32f, where:
# data.r contains the real component
# data.g contains the imaginary component
COMPLEX_TRANSFORMS: dict = ...
CPU_COMPLEX_TRANSFORMS: dict = ...

class ComplexImageVisual(ImageVisual):
    COMPLEX_MODES = ...

    def __init__(self, data: NDArray | None = None, complex_mode: str = "magnitude", **kwargs): ...
    def _init_texture(self, data, texture_format, **texture_kwargs): ...
    def set_data(self, image: ArrayLike): ...
    @staticmethod
    def _convert_complex_to_float_view(complex_arr): ...
    @property
    def complex_mode(self): ...
    @complex_mode.setter
    def complex_mode(self, value): ...
    def _build_color_transform(self): ...
    @ImageVisual.clim.setter
    def clim(self, clim): ...
    def _calc_complex_clim(self, data=None): ...
