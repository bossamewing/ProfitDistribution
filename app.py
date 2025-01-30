import streamlit as st

# Fungsi untuk memformat angka dalam Rupiah Indonesia
def format_rupiah(amount):
    return f"Rp {amount:,.0f}".replace(",", ".")

def calculate_financials(income):
    # Omzet allocation
    operational = int(income * 0.2)  # 20% untuk operasional (sewa, listrik, dll.)
    marketing = int(income * 0.1)    # 10% untuk marketing & branding
    reinvestment = int(income * 0.1) # 10% untuk modal usaha & pengembangan

    # Sisa omzet yang dihitung sebagai gross income
    gross_income = income - (operational + marketing + reinvestment)

    # Gross distribution
    marketing_expense = int(gross_income * 0.2)
    production = int(gross_income * 0.4)
    worker_share = int(gross_income * 0.4)

    # Worker split
    worker_split = worker_share // 3
    santana_gross = worker_split
    abrar_gross = worker_split
    satria_gross = worker_split

    # Net income
    net_income = int(gross_income * 0.3)

    # Net distribution
    santana_net = int(net_income * 0.5)
    bossa_net = int(net_income * 0.5)
    satria_net = bossa_net // 2
    abrar_net = bossa_net // 2

    return {
        "operational": operational,
        "marketing": marketing,
        "reinvestment": reinvestment,
        "gross_income": gross_income,
        "marketing_expense": marketing_expense,
        "production": production,
        "worker_share": worker_share,
        "santana_gross": santana_gross,
        "abrar_gross": abrar_gross,
        "satria_gross": satria_gross,
        "net_income": net_income,
        "santana_net": santana_net,
        "abrar_net": abrar_net,
        "satria_net": satria_net,
    }

# Streamlit UI
st.title("Bossanoface Financial Calculator")

# User input
income = st.number_input("Masukkan total omzet:", min_value=0, step=100000, format="%d")

if st.button("Hitung"):
    result = calculate_financials(income)

    # Display results
    st.header("📌 Alokasi Omzet")
    st.write(f"- Biaya Operasional: {format_rupiah(result['operational'])}")
    st.write(f"- Marketing & Branding: {format_rupiah(result['marketing'])}")
    st.write(f"- Investasi Kembali (Pengembangan Bisnis): {format_rupiah(result['reinvestment'])}")

    st.header("💰 Pembagian Keuntungan (Gross Income)")
    st.write(f"Pendapatan Kotor: {format_rupiah(result['gross_income'])}")
    st.write(f"- Biaya Marketing: {format_rupiah(result['marketing_expense'])}")
    st.write(f"- Produksi: {format_rupiah(result['production'])}")
    st.write(f"- Pembagian untuk Pekerja: {format_rupiah(result['worker_share'])}")
    st.write(f"  - Santana: {format_rupiah(result['santana_gross'])}")
    st.write(f"  - Abrar: {format_rupiah(result['abrar_gross'])}")
    st.write(f"  - Satria: {format_rupiah(result['satria_gross'])}")

    st.header("📈 Distribusi Keuntungan Bersih")
    st.write(f"Keuntungan Bersih: {format_rupiah(result['net_income'])}")
    st.write(f"- Santana (Founder & Investor): {format_rupiah(result['santana_net'])}")
    st.write(f"- Abrar (Operasional): {format_rupiah(result['abrar_net'])}")
    st.write(f"- Satria (Branding): {format_rupiah(result['satria_net'])}")
