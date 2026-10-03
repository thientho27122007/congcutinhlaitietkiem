import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính lãi tiền gửi ngân hàng",
    page_icon="🏦",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("🏦 Ứng dụng tính lãi tiền gửi ngân hàng")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi và tổng số tiền nhận được.")

# =========================
# NHẬP DỮ LIỆU
# =========================

st.subheader("📌 Thông tin khoản tiền gửi")

tien_gui = st.number_input(
    "Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=500_000_000.0,
    step=1_000_000.0,
    format="%.0f"
)

ky_han = st.number_input(
    "Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=3,
    step=1
)

lai_suat = st.number_input(
    "Lãi suất (%/năm)",
    min_value=0.0,
    value=6.0,
    step=0.1,
    format="%.2f"
)

hinh_thuc = st.selectbox(
    "Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# =========================
# TÍNH TOÁN
# =========================

if st.button("💰 Tính lãi", use_container_width=True):

    # Chuyển lãi suất từ % sang số thập phân
    lai_suat_nam = lai_suat / 100

    # Tính tổng tiền lãi
    # Công thức lãi đơn:
    # Tiền lãi = Tiền gốc × lãi suất năm × kỳ hạn / 12
    tong_lai = tien_gui * lai_suat_nam * ky_han / 12

    # Tổng tiền gốc + lãi
    tong_tien = tien_gui + tong_lai

    # =========================
    # TÍNH LÃI ĐỊNH KỲ
    # =========================

    if hinh_thuc == "Cuối kỳ":
        lai_dinh_ky = tong_lai
        so_ky_nhan_lai = 1
        don_vi = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":
        lai_dinh_ky = tong_lai / ky_han
        so_ky_nhan_lai = ky_han
        don_vi = "tháng"

    else:  # Hàng quý
        so_quy = ky_han / 3
        lai_dinh_ky = tong_lai / so_quy
        so_ky_nhan_lai = so_quy
        don_vi = "quý"

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

    st.success("✅ Đã tính toán thành công!")

    st.subheader("📊 Kết quả")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Tiền lãi định kỳ",
            f"{lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "Tổng tiền lãi",
            f"{tong_lai:,.0f} VNĐ"
        )

    st.metric(
        "💵 Tổng tiền gốc + lãi",
        f"{tong_tien:,.0f} VNĐ"
    )

    # =========================
    # CHI TIẾT
    # =========================

    st.divider()

    st.subheader("📋 Chi tiết khoản tiền gửi")

    st.write(f"**Số tiền gốc:** {tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
    st.write(f"**Số kỳ nhận lãi:** {so_ky_nhan_lai:g} {don_vi}")
    st.write(f"**Lãi mỗi kỳ:** {lai_dinh_ky:,.0f} VNĐ")
    st.write(f"**Tổng tiền lãi:** {tong_lai:,.0f} VNĐ")
    st.write(f"**Tổng tiền nhận được:** {tong_tien:,.0f} VNĐ")

    # =========================
    # CÔNG THỨC
    # =========================

    with st.expander("📐 Xem công thức tính"):

        st.write(
            "**Tổng tiền lãi = Tiền gốc × Lãi suất năm × Kỳ hạn / 12**"
        )

        st.write(
            "**Tiền lãi định kỳ:**"
        )

        if hinh_thuc == "Cuối kỳ":
            st.write("Tổng tiền lãi được nhận vào cuối kỳ.")

        elif hinh_thuc == "Hàng tháng":
            st.write("Tiền lãi mỗi tháng = Tổng tiền lãi / Số tháng.")

        else:
            st.write("Tiền lãi mỗi quý = Tổng tiền lãi / Số quý.")
