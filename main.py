import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D, art3d


def create_triangle_prism_stl():
    # Define the 6 vertices of the triangular prism
    vertices = np.array(
        [
            [0, 0, 0],  # Base vertex 1
            [1, 0, 0],  # Base vertex 2
            [0.5, np.sqrt(3) / 2, 0],  # Base vertex 3
            [0, 0, 1],  # Top vertex 1
            [1, 0, 1],  # Top vertex 2
            [0.5, np.sqrt(3) / 2, 1],  # Top vertex 3
        ]
    )

    # Define the 8 faces of the triangular prism
    faces = np.array(
        [
            [0, 1, 2],  # Base
            [3, 4, 5],  # Top
            [0, 1, 4],
            [0, 4, 3],  # Side 1
            [1, 2, 5],
            [1, 5, 4],  # Side 2
            [2, 0, 3],
            [2, 3, 5],  # Side 3
        ]
    )

    # Create the mesh
    prism = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            prism.vectors[i][j] = vertices[f[j], :]

    # Write the mesh to file "triangle_prism.stl"
    prism.save("triangle_prism.stl")

    return prism


def plot_stl(file_path):
    # Create a new plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Load the STL file
    your_mesh = mesh.Mesh.from_file(file_path)

    # Create a collection and add it to the axes
    collection = art3d.Poly3DCollection(your_mesh.vectors)
    ax.add_collection3d(collection)

    # Auto scale to the mesh size
    scale = your_mesh.points.flatten("C")
    ax.auto_scale_xyz(scale, scale, scale)

    # Show the plot
    plt.show()


# Path to your STL file
stl_file_path = "triangle_prism.stl"

# Plot the STL file
plot_stl(stl_file_path)
