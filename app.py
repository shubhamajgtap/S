import streamlit as st
from datetime import date, time

# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="For Manju ❤️",
    page_icon="💕",
    layout="centered"
)

# ==================================================
# CSS DESIGN
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Poppins:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #ffd6e7, #fff5f9);
    font-family: 'Poppins', sans-serif;
}

.title {
    text-align: center;
    font-family: 'Dancing Script', cursive;
    color: #d63384;
    font-size: 55px;
    font-weight: 700;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #7a3858;
    font-size: 19px;
}

.heart {
    text-align: center;
    font-size: 55px;
}

.card {
    background: rgba(255, 255, 255, 0.92);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0 10px 35px rgba(200, 70, 120, 0.20);
    margin: 20px 0;
}

.question {
    color: #c2185b;
    font-size: 27px;
    font-weight: 600;
}

.final {
    text-align: center;
    color: #c2185b;
    font-size: 30px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = 1

if "selected_date" not in st.session_state:
    st.session_state.selected_date = None

if "selected_time" not in st.session_state:
    st.session_state.selected_time = None

if "food" not in st.session_state:
    st.session_state.food = None

if "confirmed" not in st.session_state:
    st.session_state.confirmed = False


# ==================================================
# PAGE 1 - ASK MANJU
# ==================================================

if st.session_state.page == 1:

    st.markdown(
        '<div class="heart">💗</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Hey Manju ❤️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'I have something very important to ask you...'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <div class="question">
            Manju, will you go on a date with me? 🥺💕
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # YES BUTTON
    with col1:

        if st.button(
            "YES! ❤️",
            use_container_width=True
        ):

            st.session_state.page = 2
            st.rerun()

    # NO BUTTON
    with col2:

        if st.button(
            "NO 😭",
            use_container_width=True
        ):

            st.warning(
                "Nooo Manju 😭💕 Please choose YES!"
            )


# ==================================================
# PAGE 2 - DATE + TIME
# ==================================================

elif st.session_state.page == 2:

    st.markdown(
        '<div class="heart">🌸💕🌸</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Our Date ❤️</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <div class="question">
            When should we go? 🥰
        </div>
    </div>
    """, unsafe_allow_html=True)

    # DATE

    st.write("📅 **Select Date**")

    selected_date = st.date_input(
        "Choose our date",
        min_value=date.today(),
        label_visibility="collapsed"
    )

    st.write("")

    # TIME

    st.write("⏰ **Select Time**")

    selected_time = st.time_input(
        "Choose our time",
        value=time(18, 0),
        label_visibility="collapsed"
    )

    st.write("")

    # ONLY NEXT BUTTON

    if st.button(
        "Next ❤️",
        use_container_width=True
    ):

        st.session_state.selected_date = selected_date
        st.session_state.selected_time = selected_time

        st.session_state.page = 3
        st.rerun()


# ==================================================
# PAGE 3 - FOOD
# ==================================================

elif st.session_state.page == 3:

    st.markdown(
        '<div class="heart">🍕🍝💕</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">What are we eating? 😋</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <div class="question">
            Choose our food ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

    foods = [
        "🍕 Pizza",
        "🍣 Sushi",
        "🍔 Burger",
        "🍝 Pasta",
        "🌮 Tacos",
        "🍜 Ramen"
    ]

    columns = st.columns(2)

    for i, food in enumerate(foods):

        with columns[i % 2]:

            if st.button(
                food,
                key=f"food_{i}",
                use_container_width=True
            ):

                st.session_state.food = food

                st.session_state.page = 4

                st.rerun()


# ==================================================
# PAGE 4 - CONFIRM DATE
# ==================================================

elif st.session_state.page == 4:

    st.markdown(
        '<div class="heart">💕</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Confirm Our Date 🥰</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <div class="question">
            Everything looks perfect! ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

    # DATE

    st.write("### 📅 Date")

    st.info(
        str(st.session_state.selected_date)
    )

    # TIME

    st.write("### ⏰ Time")

    st.info(
        str(st.session_state.selected_time)
    )

    # FOOD

    st.write("### 🍴 Food")

    st.info(
        st.session_state.food
    )

    st.write("")

    # CONFIRM DATE BUTTON

    if st.button(
        "Confirm Date ❤️",
        use_container_width=True
    ):

        st.session_state.confirmed = True

        st.session_state.page = 5

        st.rerun()


# ==================================================
# PAGE 5 - PAYMENT
# ==================================================

elif st.session_state.page == 5:

    st.markdown(
        '<div class="heart">💳💕</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">Make a Payment</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

        <div class="question">
            Date Confirmed! ❤️
        </div>

        <p style="font-size:20px;">
            Our date is officially planned! 🥰
        </p>

        <p style="font-size:18px;">
            Now just one little thing...
        </p>

    </div>
    """, unsafe_allow_html=True)

    # PAYMENT AMOUNT

    st.markdown("""
    <div class="card">

        <div style="
            font-size:22px;
            color:#c2185b;
            font-weight:bold;
        ">
            💳 Make a Payment
        </div>

        <div style="
            font-size:40px;
            color:#d63384;
            font-weight:bold;
            margin-top:10px;
        ">
            ₹500
        </div>

    </div>
    """, unsafe_allow_html=True)

    # ==================================================
    # UPI PAYMENT
    # ==================================================

    # CHANGE THIS TO YOUR REAL UPI ID

    upi_id = "YOURUPIID@upi"

    upi_link = (
        f"upi://pay?"
        f"pa={upi_id}&"
        f"pn=Date%20with%20Manju&"
        f"am=500&"
        f"cu=INR"
    )

    st.link_button(
        "💳 Make a Payment ₹500",
        upi_link,
        use_container_width=True
    )

    st.caption(
        "Tap the button to open your UPI payment app."
    )

    st.write("")

    # AFTER PAYMENT

    if st.button(
        "Payment Done ❤️",
        use_container_width=True
    ):

        st.session_state.page = 6

        st.rerun()


# ==================================================
# PAGE 6 - FINAL PAGE
# ==================================================

elif st.session_state.page == 6:

    st.balloons()

    st.markdown(
        '<div class="heart">💖💖💖</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="title">It\'s a Date! 🥰</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

        <div class="final">
            Manju ❤️
        </div>

        <br>

        <div style="font-size:21px;">
            You and me. 💕
            <br><br>
            A perfect date. 🌸
            <br><br>
            Lots of food. 🍕
            <br><br>
            And lots of memories. 🥰
        </div>

        <br>

        <div style="
            font-size:19px;
            color:#7a3858;
        ">

            📅 Our Date
            <br><br>

            ⏰ Our Time
            <br><br>

            🍴 Our Food

        </div>

    </div>
    """, unsafe_allow_html=True)

    st.success(
        f"📅 {st.session_state.selected_date}  |  "
        f"⏰ {st.session_state.selected_time}  |  "
        f"🍴 {st.session_state.food}"
    )

    st.markdown("""
    <div class="card">

        <div class="heart">
            💌
        </div>

        <div class="final">
            I can't wait to see you, Manju! ❤️
        </div>

        <p style="font-size:17px;">
            This isn't just a date...
            <br>
            It's another beautiful memory for us. 🥹💕
        </p>

    </div>
    """, unsafe_allow_html=True)