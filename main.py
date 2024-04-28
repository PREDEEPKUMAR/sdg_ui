import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder


data = {
        'Name': ['John', 'Alice', 'Bob', 'Emily'],
        'Age': [30, 25, 40, 35],
        'City': ['New York', 'Paris', 'London', 'Berlin']
    }
df = pd.DataFrame(data)

def page1():
# Title and header
    st.title('Interactive Sales Dashboard')
    st.header('Analyze your sales data')

    # Load your data (replace with your CSV loading logic)
    data = pd.read_csv("sale_data.csv")

    # Sidebar for user input
    st.sidebar.header("Filters")
    product_filter = st.sidebar.selectbox("Select a product", data['product_name'].unique())
    date_filter = st.sidebar.date_input("Select a date range", [])

    # Filter the data based on user selection
    filtered_data = data[data['product_name'] == product_filter]
    if date_filter:
        filtered_data = filtered_data[(filtered_data['date'] >= date_filter[0]) & (filtered_data['date'] <= date_filter[1])]

    # Display metrics
    st.metric("Total Sales", filtered_data['sales_amount'].sum())
    st.metric("Average Order Value", filtered_data['order_value'].mean())

    # Display charts
    st.subheader('Sales Trend')
    st.line_chart(filtered_data[['date', 'sales_amount']].set_index('date'))

def page2():
    # Display DataFrame using st.write()
    st.title("using write ")
    st.write(df)
    st.write(df.style.set_table_attributes('class="dataframe"'))

    # Alternatively, you can use st.dataframe() for additional customization
    st.title("Using dataframe")
    st.dataframe(df)

    # display table data

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_selection('single')  # Configure for single row selection
    grid_options = gb.build()

    st.title("Using aggrid")
    AgGrid(df, gridOptions=grid_options)

    st.title("using table")
    table = st.table(df)


def page3():
    st.title("Interactive Q&A Session")

    # Input field for user's question
    submit_choice = st.radio("Is the data displayed in the table correct? or you wanna make changes?", ("Yes", "No"))

    if submit_choice == "Yes":
        st.write("Perfect!!!")
    else:
        st.write("Which column you want to make changes?")
        selected_columns = st.multiselect("Select columns from DataFrame:", df.columns)
        generate_response(selected_columns)

def generate_response(columns):
    # Dummy function to generate response (replace with your logic)
    for i in columns:
        choice = st.radio(f"What changes you want to make for column {i}?", ("Length", "Regex"))
        if choice == "Length":
            user_question = st.text_input("Enter Desired Length")
            st.write("Desired length for the column ", i, ":", user_question)
        elif choice == "Regex":
            user_question = st.text_input("Enter Desired Regex")
            st.write("Desired Regex for the column ", i, ":", user_question)



def main():
    st.sidebar.title("Synthetic Data")
    page = st.sidebar.radio("Go to", ("Widgets", "Data Visualization", "Interactive Session"))

    if page == "Widgets":
        pass
        # page1()
    elif page == "Data Visualization":
        page2()
    elif page == "Interactive Session":
        page3()


if __name__=="__main__":
    main()
