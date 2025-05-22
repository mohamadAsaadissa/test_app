from streamlit.components.v1 import html
import streamlit as st
import json

st.title("🌍 تحديد الموقع عبر GPS (المتصفح)")

html_code = """
<script>
navigator.geolocation.getCurrentPosition(
    (position) => {
        const coords = {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
        };
        const jsonStr = JSON.stringify(coords);
        window.parent.postMessage(jsonStr, "*");
    },
    (error) => {
        const jsonStr = JSON.stringify({error: error.message});
        window.parent.postMessage(jsonStr, "*");
    }
);
</script>
"""

location = st.empty()

def get_coords():
    return st.session_state.get("coords", None)

# Listen for message from JavaScript
html(html_code, height=0)

# Receive coords using streamlit events
from streamlit_javascript import st_javascript

coords = st_javascript("await new Promise(resolve => { window.addEventListener('message', e => resolve(e.data)); })")
if coords:
    try:
        parsed = json.loads(coords)
        if "latitude" in parsed and "longitude" in parsed:
            st.success(f"✅ الإحداثيات: {parsed['latitude']}, {parsed['longitude']}")
            st.session_state["coords"] = parsed
        else:
            st.error(f"❌ خطأ في تحديد الموقع: {parsed.get('error', 'غير معروف')}")
    except Exception:
        st.error("❌ لم يتمكن من قراءة البيانات.")

