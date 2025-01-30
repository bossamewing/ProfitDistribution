import streamlit as st

# Fungsi untuk memformat angka dalam Rupiah Indonesia
def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")

def calculate_financials(income, modal):
    # Profit calculation
    profit = income - modal

    # Gross profit allocation (70% of profit)
    gross_profit = int(profit * 0.7)
    marketing = int(gross_profit * 0.2)
    production = int(gross_profit * 0.4)
    worker_share = int(gross_profit * 0.4)

    # Worker split (33.33% each)
    worker_split = worker_share // 3
    santana_gross = worker_split
    abrar_gross = worker_split
    satria_gross = worker_split

    # Net profit allocation (30% of profit)
    net_profit = int(profit * 0.3)
    santana_net = int(net_profit * 0.5)
    bossa_net = int(net_profit * 0.5)

    # Bossa split (25% each to Satria and Abrar)
    satria_net = int(bossa_net * 0.5)
    abrar_net = int(bossa_net * 0.5)

    return {
        "profit": profit,
        "gross_profit": gross_profit,
        "marketing": marketing,
        "production": production,
        "worker_share": worker_share,
        "santana_gross": santana_gross,
        "abrar_gross": abrar_gross,
        "satria_gross": satria_gross,
        "net_profit": net_profit,
        "santana_net": santana_net,
        "abrar_net": abrar_net,
        "satria_net": satria_net,
    }

# Streamlit UI
st.title("Bossanoface Profit Calculator")

# User input
income = st.number_input("Masukkan total omzet:", min_value=0, step=100000, format="%d")
modal = st.number_input("Masukkan modal:", min_value=0, step=100000, format="%d")

if st.button("Hitung"):
    result = calculate_financials(income, modal)

    # Display results
    st.header("Hasil Perhitungan")
    st.write(f"Total Omzet: {format_rupiah(income)}")
    st.write(f"Modal: {format_rupiah(modal)}")
    st.write(f"Profit: {format_rupiah(result['profit'])}")

    st.header("Gross Profit - 70%")
    st.write(f"Gross Profit: {format_rupiah(result['gross_profit'])}")
    st.write(f"- Marketing: {format_rupiah(result['marketing'])}")
    st.write(f"- Produksi: {format_rupiah(result['production'])}")
    st.write(f"- Pembagian untuk Pekerja: {format_rupiah(result['worker_share'])}")
    st.write(f"  \t- Santana: {format_rupiah(result['santana_gross'])}")
    st.write(f"  \t- Abrar: {format_rupiah(result['abrar_gross'])}")
    st.write(f"  \t- Satria: {format_rupiah(result['satria_gross'])}")

    st.header("Net Profit - 30%")
    st.write(f"Net Profit: {format_rupiah(result['net_profit'])}")
    st.write(f"- Santana (Founder & Investor): {format_rupiah(result['santana_net'])}")
    st.write(f"- Satria (Branding): {format_rupiah(result['satria_net'])}")
    st.write(f"- Abrar (Operasional): {format_rupiah(result['abrar_net'])}")
