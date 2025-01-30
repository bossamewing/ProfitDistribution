import streamlit as st

def calculate_profit(income):
    # Calculate gross income
    gross_income = income * 0.7

    # Gross distribution
    marketing = gross_income * 0.2
    production = gross_income * 0.4
    worker_share = gross_income * 0.4

    # Worker split
    worker_split = worker_share / 3
    santana_share = worker_split
    abrar_share = worker_split
    satria_share = worker_split

    # Net income
    net_income = income * 0.3

    # Net distribution
    santana_net = net_income * 0.5
    bossa_net = net_income * 0.5
    satria_net = bossa_net * 0.5
    abrar_net = bossa_net * 0.5

    return {
        "gross_income": gross_income,
        "marketing": marketing,
        "production": production,
        "worker_share": worker_share,
        "santana_gross": santana_share,
        "abrar_gross": abrar_share,
        "satria_gross": satria_share,
        "net_income": net_income,
        "santana_net": santana_net,
        "abrar_net": abrar_net,
        "satria_net": satria_net,
    }

# Streamlit UI
st.title("Profit Distribution Calculator")

# User input
income = st.number_input("Enter total income:", min_value=0.0, step=1000.0)

if st.button("Calculate"):
    result = calculate_profit(income)

    # Display results
    st.header("Results")
    st.write(f"Gross Income: {result['gross_income']:.2f}")
    st.write(f"- Marketing: {result['marketing']:.2f}")
    st.write(f"- Production: {result['production']:.2f}")
    st.write(f"- Workers: {result['worker_share']:.2f}")
    st.write(f"  - Santana: {result['santana_gross']:.2f}")
    st.write(f"  - Abrar: {result['abrar_gross']:.2f}")
    st.write(f"  - Satria: {result['satria_gross']:.2f}")

    st.write(f"Net Income: {result['net_income']:.2f}")
    st.write(f"- Santana: {result['santana_net']:.2f}")
    st.write(f"- Abrar: {result['abrar_net']:.2f}")
    st.write(f"- Satria: {result['satria_net']:.2f}")
