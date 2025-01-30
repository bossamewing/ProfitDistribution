import streamlit as st

def calculate_profit(income):
    # Calculate gross income
    gross_income = int(income * 0.7)

    # Gross distribution
    marketing = int(gross_income * 0.2)
    production = int(gross_income * 0.4)
    worker_share = int(gross_income * 0.4)

    # Worker split
    worker_split = int(worker_share / 3)
    santana_share = worker_split
    abrar_share = worker_split
    satria_share = worker_split

    # Net income
    net_income = int(income * 0.3)

    # Net distribution
    santana_net = int(net_income * 0.5)
    bossa_net = int(net_income * 0.5)
    satria_net = int(bossa_net * 0.5)
    abrar_net = int(bossa_net * 0.5)

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
st.title("Kalkulator Distribusi Keuntungan")

# User input
income = st.number_input("Masukkan total pendapatan (Rp):", min_value=0, step=1000)

if st.button("Hitung"):
    result = calculate_profit(income)

    # Display results
    st.header("Hasil")
    st.write(f"Pendapatan Kotor: Rp {result['gross_income']:,}")
    st.write(f"- Marketing: Rp {result['marketing']:,}")
    st.write(f"- Produksi: Rp {result['production']:,}")
    st.write(f"- Pekerja: Rp {result['worker_share']:,}")
    st.write(f"  - Santana: Rp {result['santana_gross']:,}")
    st.write(f"  - Abrar: Rp {result['abrar_gross']:,}")
    st.write(f"  - Satria: Rp {result['satria_gross']:,}")

    st.write(f"Pendapatan Bersih: Rp {result['net_income']:,}")
    st.write(f"- Santana: Rp {result['santana_net']:,}")
    st.write(f"- Abrar: Rp {result['abrar_net']:,}")
    st.write(f"- Satria: Rp {result['satria_net']:,}")
