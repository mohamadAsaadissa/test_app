import streamlit as st
from streamlit.components.v1 import html
import json

st.title("📍 تحديد الموقع الجغرافي عبر GPS (بدون مكتبات خارجية)")

# عنصر لعرض النتائج
location_display = st.empty()

# كود JavaScript مدمج داخل HTML
html_code = """
<script>
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const coords = {
                latitude: position.coords.latitude,
                longitude: position.coords.longitude
            };
            const data = JSON.stringify(coords);
            const iframe = document.createElement('iframe');
            iframe.style.display = 'none';
            iframe.src = 'data:text/plain,' + encodeURIComponent(data);
            document.body.appendChild(iframe);
        },
        function(error) {
            const errorData = JSON.stringify({error: error.message});
            const iframe = document.createElement('iframe');
            iframe.style.display = 'none';
            iframe.src = 'data:text/plain,' + encodeURIComponent(errorData);
            document.body.appendChild(iframe);
        }
    );
</script>
"""

# تشغيل الكود
html(html_code, height=0)

# تعليمات للمستخدم
st.info("يرجى السماح للمتصفح بالوصول إلى موقعك، ثم أعد تحميل الصفحة بعد بضع ثوان.")

# إدخال يدوي كخطة بديلة
with st.expander("🔧 أو أدخل الموقع يدويًا إذا لم يعمل التحديد التلقائي"):
    lat = st.number_input("خط العرض (Latitude)", format="%.6f")
    lon = st.number_input("خط الطول (Longitude)", format="%.6f")
    if lat and lon:
        st.success(f"تم إدخال الإحداثيات يدويًا: {lat}, {lon}")
