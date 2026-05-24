import streamlit as st
import random

# Page Configuration for Advanced UI
st.set_page_config(page_title="Akira Phantom Advanced OS", page_icon="⚡", layout="wide")

# Custom CSS for Dark Gaming Aesthetic (Black and Cyan theme)
st.markdown("""
    <style>
    .main { background-color: #0f111a; color: #cfd0d3; }
    h1, h2, h3, h4 { color: #00ffcc !important; font-weight: bold; }
    .stButton>button { background-color: #1f2335; color: #00ffcc; border-radius: 12px; border: 1px solid #00ffcc; font-size: 16px; padding: 10px 20px; }
    .stButton>button:hover { background-color: #00ffcc; color: #1f2335; box-shadow: 0 0 10px #00ffcc; }
    .stTextInput>div>div>input { background-color: #1a1c23; border: 1px solid #00ffcc; color: #cfd0d3; }
    .stTextArea>div>div>textarea { background-color: #1a1c23; border: 1px solid #00ffcc; color: #cfd0d3; }
    .box-style { background-color: #1a1c23; border-radius: 15px; padding: 15px; border: 1px solid #333; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "current_page" not in st.session_state:
    st.session_state.current_page = "page1"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "app_lang" not in st.session_state:
    st.session_state.app_lang = "မြန်မာ"
if "auto_lang" not in st.session_state:
    st.session_state.auto_lang = False
if "minimize_mode" not in st.session_state:
    st.session_state.minimize_mode = False

# Dictionary for Multi-language Text (Myanmar & Japanese)
lang_dict = {
    "မြန်မာ": {
        "title": "⚡ Akira Phantom Dashboard (ပင်မ)",
        "game": "🎮 ဂိမ်းရွေးချယ်ရန်",
        "work": "📝 အကောင့်လုပ်ငန်း",
        "field": "🌐 နယ်ပယ်လေ့လာခြင်း",
        "strat": "⚔️ ဗျူဟာမြောက်လုပ်ဆောင်နိုင်စွမ်း",
        "strat_desc": "ဗျူဟာမြောက် algorithms များ နောက်ကွယ်တွင် အဆင်သင့် အလုပ်လုပ်နေသည်။",
        "icon": "⚡ အိုင်ကွန်",
        "voice": "〰️ အသံနဲ့စကားပြောရန်နေရာ",
        "setting": "⚙️ ဆက်တင်",
        "call": "📞 ခေါ်ထားခြင်း",
        "btn_p2": "🚀 EXECUTE SYSTEM CALL (ဒုတိယစာမျက်နှာသို့ သွားရန်)",
        "recording_active": "🔴 SCREEN RECORDING ACTIVE: အိုင်ကွန်ဖော်ထားခြင်းနှင့် ဂိမ်းမှတ်တမ်းယူခြင်းစနစ် မောင်းနှင်နေသည်...",
        "p2_title": "🍏 iPhone ကိုယ်ပိုင်စနစ် (Active Console)"
    },
    "日本語": {
        "title": "⚡ Akira Phantom ダッシュボード (メイン)",
        "game": "🎮 ゲーム選択",
        "work": "📝 アカウントタスク",
        "field": "🌐 フィールド調査",
        "strat": "⚔️ 戦術分析プロセッサ",
        "strat_desc": "バックグラウンドで高度な戦術アルゴリズムが作動中。",
        "icon": "⚡ アイコン",
        "voice": "〰️ 音声コマンド入力エリア",
        "setting": "⚙️ 設定",
        "call": "📞 システム起動",
        "btn_p2": "🚀 システムコール実行 (セカンドページへ移行)",
        "recording_active": "🔴 画面録画中: アイコン表示およびゲームログ保存システムが作動しています...",
        "p2_title": "🍏 iPhone 専用システム (アクティブコンソール)"
    }
}

# Auto Language Logic Simulator
if st.session_state.auto_lang:
    st.session_state.app_lang = "日本語" # Defaults to Japanese if auto is ticked (simulating Japan region detection)

L = lang_dict[st.session_state.app_lang]

# If Minimize Mode is activated, present a compact overlay UI
if st.session_state.minimize_mode:
    st.warning("🗖 Mini Mode Active (ဆော့ဝဲလ်ကို ပုံသေးထားသည်)")
    if st.button("🗖 Maximize App (ပုံပြန်ချဲ့ရန်)"):
        st.session_state.minimize_mode = False
        st.rerun()
    st.stop()

# ==========================================
# 📱 PAGE 1: ဒါက ပထမစာမျက်နှာ
# ==========================================
if st.session_state.current_page == "page1":
    st.title(L["title"])
    st.write("---")
    
    # ROW 1: Top 3 Blocks
    r1_col1, r1_col2, r1_col3 = st.columns(3)
    with r1_col1:
        st.markdown(f"<div class='box-style'><h3>{L['game']}</h3></div>", unsafe_allow_html=True)
        selected_game = st.selectbox("Select Game:", ["Art of War 3", "Wuthering Waves"], label_visibility="collapsed")
        st.caption(f"Active: {selected_game}")
        
    with r1_col2:
        st.markdown(f"<div class='box-style'><h3>{L['work']}</h3></div>", unsafe_allow_html=True)
        st.button("Open Log", key="p1_acc_log")
        
    with r1_col3:
        st.markdown(f"<div class='box-style'><h3>{L['field']}</h3></div>", unsafe_allow_html=True)
        st.button("Explore Field", key="p1_field")
        
    st.write("---")
    
    # ROW 2: Middle Strategy Block
    st.markdown(f"<div class='box-style' style='text-align: left;'><h3>{L['strat']}</h3><p>{L['strat_desc']}</p></div>", unsafe_allow_html=True)
    st.progress(86, text="Tactical Readiness: 86%")
    
    st.write("---")
    
    # ROW 3: Controls (Icon, Voice Placeholder, Settings)
    r3_col1, r3_col2, r3_col3 = st.columns([1, 2, 1])
    with r3_col1:
        st.markdown(f"#### {L['icon']}")
        st.info("🤖 **AKIRA**")
        
    with r3_col2:
        st.markdown(f"#### {L['voice']}")
        st.markdown("""
            <div style='background-color:#1a1c23; border-radius:15px; padding:15px; text-align:center; border: 1px dashed #00ffcc;'>
                <span style='color:#00ffcc; font-size:20px;'>🎵 〰️ 🎙️ 〰️ 🎵</span>
            </div>
        """, unsafe_allow_html=True)
        
    with r3_col3:
        st.markdown(f"#### {L['setting']}")
        show_settings = st.checkbox("⚙️ Open Settings Menu", value=False)
        
    # --- ⚙️ ADVANCED SETTINGS PANEL ---
    if show_settings:
        st.write("---")
        st.markdown("### ⚙️ Akira Phantom Settings Panel")
        
        set_col1, set_col2 = st.columns(2)
        with set_col1:
            st.session_state.app_lang = st.radio("🌐 ဘာသာစကား ရွေးချယ်ရန် (Language):", ["မြန်မာ", "日本語"], index=0 if st.session_state.app_lang == "မြန်မာ" else 1)
            st.session_state.auto_lang = st.checkbox("🤖 အလိုအလျောက် ဘာသာစကားပြောင်းခြင်း (Auto-Detect Region)", value=st.session_state.auto_lang)
            st.session_state.minimize_mode = st.checkbox("🗖 ပုံသေးထားခြင်း စနစ်ဖွင့်ရန် (Minimize Mode)", value=st.session_state.minimize_mode)
            
        with set_col2:
            st.markdown("**ℹ️ ဆော့ဝဲလ်အချက်အလက်များ (App Info)**")
            st.code("🚀 Software Version: v1.2.0 (Official Stable)\n⚡ System Engine: Akira Phantom OS Core\n🔒 Security Matrix: Encrypted", language="markdown")
            st.markdown("""
            **🛠️ လုပ်ဆောင်နိုင်စွမ်း အချက်အလက်များ (Active Features Log):**
            * Real-time Multi-Language Processing (MM / JP)
            * Background Screen Recording Simulator
            * AI Tactical Interactive Chat Logs
            """)
            if st.button("Apply and Reload Settings"):
                st.rerun()
                
    st.write("---")
    
    # ROW 4: Bottom Trigger to Go to Page 2
    st.markdown(f"### {L['call']}")
    if st.button(L["btn_p2"], use_container_width=True):
        st.session_state.current_page = "page2"
        st.rerun()

# ==========================================
# 🍏 PAGE 2: ဒါက ဒုတိယစာမျက်နှာ (iPhone ကိုယ်ပိုင်စနစ်)
# ==========================================
elif st.session_state.current_page == "page2":
    st.title(L["p2_title"])
    st.error(L["recording_active"])
    st.write("---")
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("💬 AI နှင့် စကားပြောရန်နေရာ (Talk to AI)")
        chat_placeholder = st.container(height=250)
        with chat_placeholder:
            if not st.session_state.chat_history:
                st.write("*စကားပြောဆိုမှုကို စတင်လိုက်ပါ...*")
            for msg in st.session_state.chat_history:
                st.markdown(f"**{msg['user']}:** {msg['text']}")
                
        st.write("---")
        in_col1, in_col2, in_col3 = st.columns([1, 4, 1])
        with in_col1:
            st.button("🎙️ Hold", key="p2_hold")
            
        with in_col2:
            user_msg = st.text_input("Message input", placeholder="စာရိုက်ရန် သို့မဟုတ် စိတ်ကြိုက်ရွေးချယ်နိုင်သည်...", label_visibility="collapsed", key="chat_input")
            
        with in_col3:
            if st.button("Send", key="p2_send"):
                if user_msg:
                    st.session_state.chat_history.append({"user": "You", "text": user_msg})
                    ai_responses = ["ဗျူဟာမြောက် လမ်းကြောင်း ဖွင့်ပေးထားပါတယ် ဆရာကြီး။", "ရန်သူ့တိုက်စစ်ကို ကောင်တာပြန်ချဖို့ Heavy Assault ပြင်ဆင်ပါ။", "ဂိမ်းမှတ်တမ်းကို စနစ်ထဲမှာ ဗီဒီယို ဖမ်းယူနေပါတယ်။"]
                    st.session_state.chat_history.append({"user": "Akira AI", "text": f"*`{random.choice(ai_responses)}`*"})
                    st.rerun()

    with col_right:
        st.subheader("📝 မှတ်တမ်းနှင့် အခြေအနေ")
        st.markdown("**📊 စစ်ဆက်တန်း / ဂိမ်းအခြေအနေ:**")
        st.code("🕒 Time: 12:45\n⚔️ Score: 3-1\n📈 Status: Winning", language="markdown")
        st.markdown("---")
        st.markdown("**📝 မှတ်တမ်းမေးမြန်းခြင်း / Notes:**")
        st.text_area("Notes log", placeholder="ဂိမ်းအတွင်း သတိပြုမိသည်များကို ရေးမှတ်ရန်...", label_visibility="collapsed", key="p2_notes")
        st.markdown("---")
        st.markdown("**📋 ပြီးခဲ့သော မှတ်တမ်းအကျဉ်း (History):**")
        st.markdown("- 🔴 Recording Started (00:01)")

    st.write("---")
    if st.button("⬅️ ပထမစာမျက်နှာသို့ ပြန်သွားရန်", use_container_width=True):
        st.session_state.current_page = "page1"
        st.rerun()

# Universal System Footer Status
st.success("Manager System: Connected & Operational! 🚀")