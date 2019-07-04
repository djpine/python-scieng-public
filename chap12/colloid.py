from numpy import pi, inf


class Colloid():
    """A class to model a microparticle suspended in a liquid.
    """

    def __init__(self, pdiam, pdens, lvisc=0.00089,
                 ldens=1000., tempC=25.0):
        """Initialize suspension properties in SI units."""
        self.pdiam = pdiam  # particle diameter (m)
        self.pdens = pdens  # particle density (kg/m^3)
        self.lvisc = lvisc  # solvent viscosity (Pa-s)
        self.ldens = ldens  # solvent density (kg/m^3)
        self.tempC = tempC  # temperature (degrees C)
        self.tempK = tempC + 273.15  # temperature (K)

    def pmass(self):
        """Calculate particle mass"""
        return self.pdens * pi * self.pdiam ** 3 / 6.0

    def friction(self):
        return 3.0 * pi * self.lvisc * self.pdiam

    def vsed(self):
        """Calculate particle sedimentation velocity"""
        g = 9.80  # gravitational acceleration
        grav = (pi / 6.0) * (self.pdens - self.ldens) * g * self.pdiam ** 3
        return grav / self.friction()

    def diff_coef(self):
        """Calculate particle diffusion coefficient"""
        kB = 1.38064852e-23
        return kB * self.tempK / self.friction()

    def grav_height(self):
        """Calculate gravitational height of particles"""
        D = self.diff_coef()
        v = self.vsed()
        try:
            hg = D / v
        except ZeroDivisionError:
            hg = inf  # when liquid & particle density equal
        return hg

    def set_tempC(self, tempC):
        """Sets temperature to a specified value"""
        self.tempC = tempC
        self.tempK = tempC + 273.15


class HairyColloid(Colloid):
    """A class to model hairy colloids"""

    def __init__(self, pdiam, pdens, lvisc, ldens, tempC,
                 hlen):
        """Initialize properties from parent Colloid"""
        super().__init__(pdiam, pdens, lvisc, ldens, tempC)
        self.hlen = hlen  # length of hairs on particles
        self.hdiam = pdiam + 2.0 * hlen

    def friction(self):
        return 3.0 * pi * self.lvisc * self.hdiam


if __name__ == "__main__":
    au_h2o = Colloid(7.5e-9, 19320., 0.00089, 1000., 25.)
    # print instance variables
    print("Colloid instance variables")
    print(au_h2o.__dict__)
    print("Colloid methods")
    print([method for method in dir(au_h2o)
           if callable(getattr(au_h2o, method))
           and not method.startswith("__")])
    # run methods
    print("Colloid methods output")
    print("particle mass = {0:5.3g} kg".format(au_h2o.pmass()))
    print("sedimentation velocity = {0:5.3g} m/s".format(au_h2o.vsed()))
    print("particle diffusion coefficient = {0:5.3g} m^2/s"
          .format(au_h2o.diff_coef()))
    print("particle gravitational height = {0:5.3g} m"
          .format(au_h2o.grav_height()))
    au_h2o.set_tempC(35.0)

    print('***********************************')

    au_h2o_hc = HairyColloid(7.5e-9, 19320., 0.00089, 1000., 25., 12e-9)
    # print instance variables
    print("HairyColloid instance variables")
    print(au_h2o_hc.__dict__)
    print("HairyColloid methods")
    print([method for method in dir(au_h2o_hc)
           if callable(getattr(au_h2o_hc, method))
           and not method.startswith("__")])
    # run methods
    print("HairyColloid methods output")
    print("particle mass = {0:5.3g} kg".format(au_h2o_hc.pmass()))
    print("sedimentation velocity = {0:5.3g} m/s".format(au_h2o_hc.vsed()))
    print("particle diffusion coefficient = {0:5.3g} m^2/s"
          .format(au_h2o_hc.diff_coef()))
    print("particle gravitational height = {0:5.3g} m"
          .format(au_h2o_hc.grav_height()))
    au_h2o_hc.set_tempC(35.0)

"""
Introduction to Python for Science & Engineering
by David J. Pine
Last edited: 2018-09-15

Colloid class to calculate various properties of colloids.
"""
