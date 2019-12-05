# -*- coding: utf-8 -*-

import numpy as np

r = 5.4
h = 7.9

O = 2 * np.math.pi * 5.4
A = np.math.pi * 5.4**2

print("Har en sirkel med radius", r, "som er grunnflate i en sylinder med høyde", h)
print("Omkrets av sirkelen:", O)
print("Areal av sirkelen:", A)
print("Areal av sylinderen:", O * 7.9 + 2 * A)
