#!/opt/conda/bin/python3 -i

import logging

import GeopsyPyCoreWave as gp
import numpy as np


def main() -> None:
    """Main function."""

    logging.basicConfig(
        filename="example.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    nmodes = 1  # fundamental mode

    freq = np.logspace(np.log10(1), np.log10(50), 500)
    omega = freq.copy()
    omega *= 2 * np.pi

    h = np.array([10, 20])
    vp = np.array([500, 1000, 3000])
    vs = np.array([200, 600, 1500])
    rho = np.array([2000, 2000, 2500])

    # slowRayleigh=gp.rayleighDispersionCurve(nmodes, 0, h, vp, vs, rho, omega)
    slowRayleighGroup = gp.rayleighDispersionCurve(
        nmodes, 1, h, vp, vs, rho, omega
    ).squeeze()

    logging.info(
        f"Rayleigh group velocities:\n{slowRayleighGroup}\nshape: "
        f"{slowRayleighGroup.shape}, type: {type(slowRayleighGroup)}"
    )


if __name__ == "__main__":
    main()
