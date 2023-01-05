import matplotlib.pyplot as plt
import numpy as np
from math import tan, radians

sigma_ak = float(input("Please enter sigma_ak: "))
sigma_D = float(input("Please enter sigma_D: "))
b0 = float(input("Please enter b0: "))
b1 = float(input("Please enter b1: "))
beta_k = float(input("Please enter beta_k: "))
sigma_vü = float(input("Please enter sigma_vü: "))
sigma_vm = float(input("Please enter sigma_vm: "))

sigma_ak_prime = sigma_ak*b0
sigma_D_prime = sigma_D*b0
sigma_şd = sigma_D*b0*b1/beta_k
tana = sigma_vü/sigma_vm
tan40 = tan(radians(40))

def plot45():
    xpoints = np.array([0, sigma_ak+sigma_ak/5])
    ypoints = np.array([0, sigma_ak+sigma_ak/5])

    plt.plot(xpoints, ypoints)

def plotaxises():
    xpoints = np.array([0, sigma_ak+sigma_ak/5])
    ypoints = np.array([0, 0])
    plt.plot(xpoints, ypoints, color = "r", linewidth = "4")

    xpoints = np.array([0, 0])
    ypoints = np.array([0, sigma_ak+sigma_ak/5])
    plt.plot(xpoints, ypoints, color = "r", linewidth = "4")

def sigmaD_to_sigma_ak():
    xpoints = np.array([0, (sigma_ak-sigma_D)/tan40])
    ypoints = np.array([sigma_D, sigma_ak])
    plt.plot(xpoints, ypoints, color = "b")

    xpoints = np.array([(sigma_ak-sigma_D)/tan40, sigma_ak])
    ypoints = np.array([sigma_ak, sigma_ak])
    plt.plot(xpoints, ypoints, color = "b")

def sigmaDprime_to_sigma_akprime():
    xpoints = np.array([0, (sigma_ak_prime-sigma_D_prime)/tan40])
    ypoints = np.array([sigma_D_prime, sigma_ak_prime])
    plt.plot(xpoints, ypoints, color = "b", linestyle = "dashed")

    xpoints = np.array([(sigma_ak_prime-sigma_D_prime)/tan40, sigma_ak_prime])
    ypoints = np.array([sigma_ak_prime, sigma_ak_prime])
    plt.plot(xpoints, ypoints, color = "b", linestyle = "dashed")

def sigma_şd_to():
    xpoints = np.array([0, (sigma_ak_prime-sigma_D_prime)/tan40])
    ypoints = np.array([sigma_şd, sigma_şd+(sigma_ak_prime-sigma_D_prime)])
    plt.plot(xpoints, ypoints, color = "b")

    xpoints = np.array([(sigma_ak_prime-sigma_D_prime)/tan40, sigma_ak_prime])
    ypoints = np.array([sigma_şd+(sigma_ak_prime-sigma_D_prime), sigma_ak_prime])
    plt.plot(xpoints, ypoints, color = "b")

def plot_tana():
    xpoints = np.array([0, sigma_D_prime/tana])
    ypoints = np.array([0, sigma_D_prime])
    plt.plot(xpoints, ypoints, color = "green", linewidth = "3")

sigma_şü = tana*sigma_şd/(tana-tan40)
S = sigma_şü / sigma_vü

def plotting():
    plot45()
    plotaxises()
    sigmaD_to_sigma_ak()
    sigmaDprime_to_sigma_akprime()
    sigma_şd_to()
    plot_tana()

    plt.title("Smith Diagram")
    plt.xlabel("sigma_m (N/mm^2)")
    plt.ylabel("sigma (N/mm^2)")

    plt.show()


print(f"Safety = {S}")
plotting()