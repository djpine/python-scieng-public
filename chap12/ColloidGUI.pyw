#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QDialog, QLabel, QGridLayout,
                             QDoubleSpinBox, QApplication)
from scipy.constants import pi, g, Boltzmann
from numpy import abs, inf


class Form(QDialog):

    def __init__(self):
        super().__init__()
        # inputs
        self.pdiamSpinBox = QDoubleSpinBox()
        self.pdiamSpinBox.setRange(1., 50000.)
        self.pdiamSpinBox.setValue(500)
        self.pdiamSpinBox.setSuffix(" nm")
        self.pdiamSpinBox.setDecimals(1)
        pdiamLabel = QLabel("Particle Diameter:")

        self.pdensSpinBox = QDoubleSpinBox()
        self.pdensSpinBox.setRange(1., 50000.)
        self.pdensSpinBox.setValue(1050.)
        self.pdensSpinBox.setSuffix(" kg/m\u00B3")
        self.pdensSpinBox.setDecimals(0)
        pdensLabel = QLabel("Particle Density:")

        self.lviscSpinBox = QDoubleSpinBox()
        self.lviscSpinBox.setRange(0.5, 1e6)
        self.lviscSpinBox.setValue(0.89)
        self.lviscSpinBox.setSuffix(" mPa-s")
        self.lviscSpinBox.setDecimals(2)
        lviscLabel = QLabel("Liquid viscosity:")

        self.ldensSpinBox = QDoubleSpinBox()
        self.ldensSpinBox.setRange(100., 20000.)
        self.ldensSpinBox.setValue(997.)
        self.ldensSpinBox.setSuffix(" kg/m³")
        self.ldensSpinBox.setDecimals(0)
        ldensLabel = QLabel("Liquid Density:")

        self.tempCSpinBox = QDoubleSpinBox()
        self.tempCSpinBox.setRange(-40., 400.)
        self.tempCSpinBox.setValue(25.)
        self.tempCSpinBox.setSuffix("°C")
        self.tempCSpinBox.setDecimals(1)
        tempLabel = QLabel("Temperature:")

        self.brushSpinBox = QDoubleSpinBox()
        self.brushSpinBox.setRange(0., 500.)
        self.brushSpinBox.setValue(0.)
        self.brushSpinBox.setSuffix(" nm")
        self.brushSpinBox.setDecimals(1)
        brushLabel = QLabel("Brush length:")
        # outputs
        self.hydroDiam = QLabel()
        hydroDiamLabel = QLabel("Hydrodynamic diameter:")
        self.diffCoef = QLabel()
        diffCoefLabel = QLabel("Diffusion coefficient:")
        self.vsed = QLabel()
        vsedLabel = QLabel("Sedimentation velocity:")
        self.gravHeight = QLabel()
        gravHeightLabel = QLabel("Gravitational height:")

        grid = QGridLayout()
        # inputs
        grid.addWidget(pdiamLabel, 0, 0)  # Diameter
        grid.addWidget(self.pdiamSpinBox, 0, 1)
        grid.addWidget(pdensLabel, 1, 0)  # Density
        grid.addWidget(self.pdensSpinBox, 1, 1)
        grid.addWidget(lviscLabel, 2, 0)  # Viscosity
        grid.addWidget(self.lviscSpinBox, 2, 1)
        grid.addWidget(ldensLabel, 3, 0)  # Densiity
        grid.addWidget(self.ldensSpinBox, 3, 1)
        grid.addWidget(tempLabel, 4, 0)  # Temp (C)
        grid.addWidget(self.tempCSpinBox, 4, 1)
        grid.addWidget(brushLabel, 0, 2)  # Brush length
        grid.addWidget(self.brushSpinBox, 0, 3)
        # outputs
        grid.addWidget(hydroDiamLabel, 1, 2)  # Hydro diam
        grid.addWidget(self.hydroDiam, 1, 3)
        grid.addWidget(diffCoefLabel, 2, 2)  # Diff coef
        grid.addWidget(self.diffCoef, 2, 3)
        grid.addWidget(vsedLabel, 3, 2)  # Sed vel
        grid.addWidget(self.vsed, 3, 3)
        grid.addWidget(gravHeightLabel, 4, 2)  # Grav height
        grid.addWidget(self.gravHeight, 4, 3)
        self.setLayout(grid)
        # Set up event loop with signals & slots
        self.pdiamSpinBox.valueChanged.connect(self.updateUi)
        self.pdensSpinBox.valueChanged.connect(self.updateUi)
        self.lviscSpinBox.valueChanged.connect(self.updateUi)
        self.ldensSpinBox.valueChanged.connect(self.updateUi)
        self.tempCSpinBox.valueChanged.connect(self.updateUi)
        self.brushSpinBox.valueChanged.connect(self.updateUi)
        # Window title & initialize values of outputs
        self.setWindowTitle("Colloidal Suspension")
        self.updateUi()

    def updateUi(self):
        tempK = self.tempCSpinBox.value() + 273.15
        eta = self.lviscSpinBox.value() * 0.001   # SI units
        pdiam = self.pdiamSpinBox.value() * 1e-9  # SI units
        pdens = self.pdensSpinBox.value()         # SI units
        ldens = self.ldensSpinBox.value()         # SI units
        hdiam = pdiam + 2.0e-9 * self.brushSpinBox.value()  # SI units
        friction = 3.0 * pi * eta * hdiam
        D = Boltzmann * tempK / friction
        vsed = (pi / 6.0) * (pdens - ldens) * g * pdiam ** 3 / friction
        try:
            hg = D / vsed  # gravitational height in SI units
        except ZeroDivisionError:
            hg = inf  # when liquid & particle density equal
        self.diffCoef.setText("{0:0.3g} \u03BCm\u00B2/s"
                              .format(D * 1e12))
        self.vsed.setText("{0:0.3g} nm/s".format(vsed * 1e9))
        self.hydroDiam.setText("{0:0.3g} nm"
                               .format(hdiam * 1e9))
        # Set gravitational height, with exception for vsed=0
        if abs(hg) < 0.001:  # small values in microns
            self.gravHeight.setText("{0:0.3g} \u03BCm"
                                    .format(hg * 1e6))
        elif abs(hg) < inf:  # large values in millimeters
            self.gravHeight.setText("{0:0.3g} mm"
                                    .format(hg * 1e3))
        else:  # infinity (\u221E)
            self.gravHeight.setText("\u221E")
        return


app = QApplication(sys.argv)
form = Form()
form.show()
sys.exit(app.exec_())

"""
Introduction to Python for Science & Engineering
by David J. Pine
Last edited: 2018-09-15

Colloid GUI to calculate various properties of colloids.
"""
