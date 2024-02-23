import numpy as np
from matplotlib import pyplot as plt

def gaussian(x, a, b, c):
    """
    Compute the Gaussian function.

    Args:
        x (np.array): The input values.
        a (float): The height of the curve's peak.
        b (float): The position of the center of the peak.
        c (float): The standard deviation, which controls the width of the bell.

    Returns:
        np.array: The Gaussian function values.
    """
    return a * np.exp(-((x - b)**2) / (2 * c**2))

# def a inhomegene 2d space which looks like a bean
def bean(theta, scale=1, offset=0):
    """
    Create a bean shape in 2D space.
    
    Args:
        theta (float): The angle parameter that determines the shape of the bean.
        scale (float, optional): The scaling factor for the size of the bean. Defaults to 1.
    
    Returns:
        tuple: A tuple containing the x and y coordinates of the points that form the bean shape.
    """
    
    r = (np.sin(theta)**3 + np.cos(theta)**3) * scale
    
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Define the rotation angle in radians (45 degrees here)
    phi = np.pi 

    # Apply the rotation matrix to each (x, y) pair
    x_rotated = x * np.cos(phi) - y * np.sin(phi) 
    y_rotated = x * np.sin(phi) + y * np.cos(phi)

    x_rotated += offset
    y_rotated += offset
    
    return x_rotated, y_rotated

def baysian_inference_view():
    # Assuming the bean and gaussian functions are defined elsewhere in your code
    # These functions are assumed to generate the bean shapes and Gaussian curves

    # Define angular range for plotting
    theta = np.linspace(0, 2 * np.pi, 1000)  # Create an array of theta values from 0 to 2π

    # Create our reality space by generating bean shapes with different scales and offsets
    x1, y1 = bean(theta, scale=2, offset=1)  # Generate the first bean shape
    x2, y2 = bean(theta, scale=1, offset=0.75)  # Generate the second bean shape
    x3, y3 = bean(theta, scale=0.5, offset=0.625)  # Generate the third bean shape

    # Simulate power spectrum using a combination of Gaussian functions
    # These Gaussian functions are centered at different points along the theta axis
    # and are summed together to create a complex power spectrum curve
    smoothness = 0.4
    power = gaussian(theta, 0.4, np.pi, smoothness) + \
        gaussian(theta, 0.3, np.pi + 1/3 * np.pi, smoothness) +\
        gaussian(theta, 0.3, np.pi - 1/3 * np.pi, smoothness) + \
        gaussian(theta, 0.2, np.pi + 2/3 * np.pi, smoothness) + \
        gaussian(theta, 0.2, np.pi - 2/3 * np.pi, smoothness)

    # Create a figure with two subplots (vertically arranged)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))  # Update figsize to specify the smaller size of the entire figure

    # Plot bean shapes in the first subplot
    ax1.fill(x1, y1, label='bean1', alpha=0.5, color='skyblue')  # Fill the area under the first bean curve
    ax1.fill(x2, y2, label='bean2', alpha=0.75, color='lightgreen')  # Fill the area under the second bean curve
    ax1.fill(x3, y3, label='bean3', alpha=0.75, color='turquoise')  # Fill the area under the third bean curve
    ax1.axhline(y=0.5, color="red")  # Draw a horizontal line at the mean value
    ax1.set_aspect('equal')  # Ensure that the aspect ratio is equal to make the plot proportional
    ax1.xaxis.set_tick_params(labelbottom=False)  # Remove x-axis labels
    ax1.yaxis.set_tick_params(labelleft=False)  # Remove y-axis labels
    ax1.set_xticks([])  # Remove x-axis tick marks
    ax1.set_yticks([])  # Remove y-axis tick marks
    ax1.set_ylabel("data", fontsize = 15)  # Set the y-axis label
    ax1.set_xlabel("signal", fontsize = 15)  # Set the x-axis label
    ax1.set_title('Reality Space', fontsize = 15)  # Set the title of the first subplot


    # Plot power spectrum in the second subplot
    ax2.plot(theta, power, label='Power Spectrum', color='r', linewidth= 4)  # Plot the power spectrum curve
    ax2.set_title('Power Spectrum', fontsize = 15)  # Set the title of the second subplot
    ax2.xaxis.set_tick_params(labelbottom=False)  # Remove x-axis labels
    ax2.yaxis.set_tick_params(labelleft=False)  # Remove y-axis labels
    ax2.set_xticks([])  # Remove x-axis tick marks
    ax2.set_yticks([])  # Remove y-axis tick marks
    ax2.set_xlabel("signal", fontsize = 15)  # Set the x-axis label
    ax2.set_ylabel("$P(d^{obs}, s)$", fontsize = 15)  # Set the y-axis label

    plt.tight_layout()  # Adjust subplots to fit into the figure area
    return fig

