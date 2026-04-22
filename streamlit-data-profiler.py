import streamlit as st
import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
import io

def get_sample_datasets():
    datasets = {
        "Diamonds": sns.load_dataset("diamonds"),
        "Iris": sns.load_dataset("iris"),
        "Titanic": sns.load_dataset("titanic"),
        "Tips": sns.load_dataset("tips")
    }
    return datasets

def main():
    st.set_page_config(page_title="Data Profiling App", layout="wide")
    
    st.title("📊 Automated Data Profiling App")
    st.write("Upload your dataset or select a sample dataset to generate a detailed profiling report.")

    # Sidebar for dataset selection
    st.sidebar.header("Dataset Selection")
    dataset_option = st.sidebar.radio(
        "Choose your data source:",
        ["Upload Your Data", "Use Sample Dataset"]
    )

    df = None

    if dataset_option == "Upload Your Data":
        uploaded_file = st.file_uploader("Upload your CSV, Excel, or JSON file", 
                                       type=["csv", "xlsx", "json"])
        
        if uploaded_file is not None:
            try:
                file_extension = uploaded_file.name.split(".")[-1].lower()
                if file_extension == "csv":
                    df = pd.read_csv(uploaded_file)
                elif file_extension == "xlsx":
                    df = pd.read_excel(uploaded_file)
                elif file_extension == "json":
                    df = pd.read_json(uploaded_file)
            except Exception as e:
                st.error(f"Error: {str(e)}")
                return

    else:  # Use Sample Dataset
        sample_datasets = get_sample_datasets()
        selected_dataset = st.sidebar.selectbox(
            "Select a sample dataset:",
            list(sample_datasets.keys())
        )
        df = sample_datasets[selected_dataset]

    if df is not None:
        st.write("### Dataset Preview")
        st.dataframe(df.head())
        
        st.write("### Dataset Information")
        st.write(f"Number of rows: {df.shape[0]}")
        st.write(f"Number of columns: {df.shape[1]}")

        if st.button("Generate Profiling Report"):
            with st.spinner("Generating profiling report..."):
                profile = ProfileReport(df, 
                                     title="Data Profiling Report",
                                     explorative=True)
                
                # Generate and display the report
                report_html = profile.to_html()
                
                # Display the report using streamlit components
                st.write("### Data Profiling Report")
                components.html(report_html, height=800, scrolling=True)

if __name__ == "__main__":
    main()
