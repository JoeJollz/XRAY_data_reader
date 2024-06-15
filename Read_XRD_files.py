# CHANGE YOUR FILE DIRECTORY TO SUIT WHERE YOUR .xrdml FILE IS LOCATED. #
import matplotlib.pyplot as plt
from lxml import etree
import numpy as np

def read_xrdml(file_path):
    # Parse the .xrdml file
    tree = etree.parse(file_path)
    root = tree.getroot()
    
    # Define the namespace
    ns = {"default": root.nsmap[None]}
    
    # Extract intensity values
    intensities = root.find(".//default:intensities", namespaces=ns).text.strip().split()
    intensities = list(map(int, intensities))
    
    # Extract start and end positions for 2Theta
    start_position = float(root.find(".//default:dataPoints/default:positions[@axis='2Theta']/default:startPosition", namespaces=ns).text)
    end_position = float(root.find(".//default:dataPoints/default:positions[@axis='2Theta']/default:endPosition", namespaces=ns).text)
    
    # Calculate the 2Theta range
    two_theta = np.linspace(start_position, end_position, len(intensities))
    
    return two_theta, intensities

def plot_intensities(two_theta, intensities):
    plt.figure(figsize=(10, 6))
    plt.plot(two_theta, intensities)
    plt.xlabel('2Theta (Degrees)')
    plt.ylabel('Intensity (counts)')
    plt.legend()
    plt.grid(False)
    plt.show()

#test plate 1
file_path = r'C:\Users\jrjol\Documents\Cambridge\Project\XRD data\11_06_2024\file_name.xrdml'
two_theta, intensities = read_xrdml(file_path)
plot_intensities(two_theta, intensities)


file_path = r'C:\Users\jrjol\Documents\Cambridge\Project\XRD data\11_06_2024\background_scan.xrdml'
two_theta, intensities_background = read_xrdml(file_path)

plt.plot(two_theta, intensities, label = 'Sample')
plt.plot(two_theta, intensities_background, label='Background')
plt.xlabel('2Theta (Degrees)')
plt.ylabel('Intesnity (counts)')
plt.title('XRD')
plt.legend()
plt.show()
