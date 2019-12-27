# -*- coding: utf-8 -*-
"""Billiards top-level module.

You can import the ``Billiard`` class from here for convenience::

    from billiard import Billiard

"""
__version__ = "0.2.0"


# Local
from . import physics, simulation, visualize
from .simulation import Billiard

__all__ = ["simulation", "physics", "visualize", "Billiard"]
