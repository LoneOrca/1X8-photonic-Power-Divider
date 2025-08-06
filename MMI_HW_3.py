
# Power_Divider_1x8 of the circuit
import si_fab.all as si_fab
import ipkiss3.all as i3

import numpy as np
import matplotlib.pyplot as plt
from ipkiss.technology import get_technology

TECH = get_technology()
class Power_Divider_1x8(i3.Circuit):
  Spacing_x = i3.PositiveNumberProperty(default=25)
  Spacing_y = i3.PositiveNumberProperty(default=25)

  def _default_insts(self):
      mmi1x2optimized1550_1 = si_fab.MMI1x2Optimized1550()

      return {
          "MMI1x2Optimized1550_1": mmi1x2optimized1550_1,
          "MMI1x2Optimized1550_2": mmi1x2optimized1550_1,
          "MMI1x2Optimized1550_3": mmi1x2optimized1550_1,
          "MMI1x2Optimized1550_4": mmi1x2optimized1550_1,
          "MMI1x2Optimized1550_5": mmi1x2optimized1550_1,
          "MMI1x2Optimized1550_6": mmi1x2optimized1550_1,
          "MMI1x2Optimized1550_7": mmi1x2optimized1550_1,
      }

  def _default_specs(self):
      return [
          i3.Place("MMI1x2Optimized1550_1", (0,0)),
          i3.PlaceRelative("MMI1x2Optimized1550_2", "MMI1x2Optimized1550_1", (2*self.Spacing_x,2*self.Spacing_y)),
          i3.PlaceRelative("MMI1x2Optimized1550_3", "MMI1x2Optimized1550_1", (2*self.Spacing_x,-2*self.Spacing_y)),
          i3.PlaceRelative("MMI1x2Optimized1550_4", "MMI1x2Optimized1550_2", (2*self.Spacing_x,self.Spacing_y)),
          i3.PlaceRelative("MMI1x2Optimized1550_5", "MMI1x2Optimized1550_2", (2*self.Spacing_x,-self.Spacing_y)),
          i3.PlaceRelative("MMI1x2Optimized1550_6", "MMI1x2Optimized1550_3", (2*self.Spacing_x,self.Spacing_y)),
          i3.PlaceRelative("MMI1x2Optimized1550_7", "MMI1x2Optimized1550_3", (2*self.Spacing_x,-self.Spacing_y)),
          i3.ConnectBend("MMI1x2Optimized1550_1:out1", "MMI1x2Optimized1550_3:in1"),
          i3.ConnectBend("MMI1x2Optimized1550_2:out2", "MMI1x2Optimized1550_4:in1"),
          i3.ConnectBend("MMI1x2Optimized1550_2:out1", "MMI1x2Optimized1550_5:in1"),
          i3.ConnectBend("MMI1x2Optimized1550_3:out2", "MMI1x2Optimized1550_6:in1"),
          i3.ConnectBend("MMI1x2Optimized1550_3:out1", "MMI1x2Optimized1550_7:in1"),
          i3.ConnectBend("MMI1x2Optimized1550_2:in1", "MMI1x2Optimized1550_1:out2"),

          ]



  def _default_exposed_ports(self):
    return {
        "MMI1x2Optimized1550_1:in1": "input",
        "MMI1x2Optimized1550_4:out2": "output1",
        "MMI1x2Optimized1550_4:out1": "output2",
        "MMI1x2Optimized1550_5:out2": "output3",
        "MMI1x2Optimized1550_5:out1": "output4",
        "MMI1x2Optimized1550_6:out2": "output5",
        "MMI1x2Optimized1550_6:out1": "output6",
        "MMI1x2Optimized1550_7:out2": "output7",
        "MMI1x2Optimized1550_7:out1": "output8",
    }

if __name__ == "__main__":
    cell = Power_Divider_1x8(name="Power_Divider_1x8",Spacing_y=25)
    cell_lo = cell.Layout()
    cell_lo.write_gdsii("Power_Divider_1x8.gds")
    cell_lo.visualize()

    # Generates the circuit model of our power divider
    circuit_Netlist = cell.Netlist()
    print(circuit_Netlist)
    circuit_model = cell.CircuitModel()

    # Get the S-Parameter data for each component and compute the S-Matrix
    wavelengths = np.linspace(1.5, 1.6, 1000)
    S_total = circuit_model.get_smatrix(wavelengths=wavelengths)

    # Plot the Data
    fig, ax = plt.subplots(2, sharex="all")
    for i in ["output1", "output2", "output3", "output4", "output5", "output6", "output7", "output8"]:
        ax[0].plot(wavelengths, i3.signal_power_dB(S_total[i, "input"]), linewidth=2, label=i)
    ax[1].plot(wavelengths, i3.signal_power_dB(S_total["input", "input"]), linewidth=2, label="in")
    ax[1].set_xlabel("Wavelength  [\u03BCm]", fontsize=16)  # add a label to the x-axis
    ax[0].set_ylabel("Transmission [dB]", fontsize=16)
    ax[0].set_ylim([-10, 0])
    ax[1].set_ylabel("Reflection  [dB]", fontsize=16)
    ax[0].legend(fontsize=14)  # create a legend from the plt.plot labels
    ax[1].legend(fontsize=14)  # create a legend from the plt.plot labels
    plt.show()  # show the graph