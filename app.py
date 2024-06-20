import streamlit as st
import pyvista as pv
from stl import mesh
import tempfile
from pyvista.plotting import plot as pv_plot

# Function to display STL file
def display_stl(file_path):
    mesh = pv.read(file_path)
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color="lightgrey")
    plotter.camera_position = 'iso'
    
    # Save the plot to a temporary file
    temp_plot_path = tempfile.mktemp(suffix=".png")
    plotter.show(screenshot=temp_plot_path, window_size=[800, 600])
    
    return temp_plot_path

# Streamlit app
st.title("STL File Viewer")
#st.write("Upload an STL file to view it:")

# File uploader
uploaded_file = st.file_uploader("Choose an STL file", type="stl")

if uploaded_file is not None:
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".stl") as temp_stl:
        temp_stl.write(uploaded_file.read())
        temp_stl_path = temp_stl.name

    # Display the STL file
    display_stl(temp_stl_path)

