import streamlit as str_lib
import time

# 1. إعدادات الصفحة المخصصة للهواتف والمتصفح
str_lib.set_page_config(page_title="الهيئة الاتحادية للهوية والجنسية والجمارك وأمن المنافذ", page_icon="🎙️", layout="centered")

# دالة ذكية لبناء نصوص الـ HTML المحاذية لليمين (RTL) بشكل صلب ومستقر
def get_rtl_html(text, is_error=False, tag_text=""):
    color = "#48BB78"  # أخضر نيون افتراضي للشاشة المظلمة
    if is_error:
        color = "#FEB2B2"  # أحمر ناعم وجذاب للاعتذار
    
    tag_html = f"<span style='color: #F6AD55; font-weight: bold;'>{tag_text}</span> " if tag_text else ""
    return f"<div style='text-align: right; direction: rtl; color: {color}; font-family: Segoe UI; font-weight: bold; line-height: 1.8; margin-bottom: 8px;'>{tag_html}{text}</div>"

# هيدر فخم ونظيف يحمل المسمى الرسمي الكامل والجديد للهيئة الموقرة
str_lib.markdown("""
    <div style='background-color: #0F1E36; padding: 25px; text-align: center; border-bottom: 4px solid #D4AF37; border-radius: 8px;'>
        <h2 style='color: white; font-family: Segoe UI; margin:0; font-size: 20px; font-weight: bold;'>الهيئة الاتحادية للهوية والجنسية والجمارك وأمن المنافذ</h2>
        <p style='color: #D4AF37; font-family: Segoe UI; font-size: 14px; margin: 8px 0 0 0; font-weight: bold;'>🎛️ ممر الابتكار الحكومي | منصة الوكيل الذكي الاستباقي (Agentic AI)</p>
    </div>
""", unsafe_allow_html=True)

# تهيئة الذاكرة السحابية للجلسة الحالية
if 'logged_in' not in str_lib.session_state:
    str_lib.session_state.logged_in = False
if 'asked_before' not in str_lib.session_state:
    str_lib.session_state.asked_before = False
if 'trigger_process' not in str_lib.session_state:
    str_lib.session_state.trigger_process = False
if 'is_recording' not in str_lib.session_state:
    str_lib.session_state.is_recording = False
if 'authorized' not in str_lib.session_state:
    str_lib.session_state.authorized = False

government_scenarios = {
    "1": {"salary": 25000, "has_contract": True, "contract_details": "عقد إيجار موثق (إيجاري) فعال ومطابق لكافة معايير الاستضافة"},
    "2": {"salary": 4500, "has_contract": True, "contract_details": "عقد إيجار موثق (إيجاري) فعال ومطابق لكافة معايير الاستضافة"},
    "3": {"salary": 18000, "has_contract": False, "contract_details": "لا يوجد عقد سكن فعال مسجل باسم الضامن في البلديات"}
}
str_lib.write("")
# بوابـة التحقق والتحكم الذكي المدمج
str_lib.markdown("<h3 style='text-align: center; direction: rtl;'>🔒 بوابـة التحقق والتحكم الذكي المدمج</h3>", unsafe_allow_html=True)

str_lib.markdown("""
    <style>
    div[data-testid="stSelectbox"] {
        display: flex;
        justify-content: center;
        text-align: center;
        width: 100%;
    }
    div[data-testid="stRadio"] > div {
        justify-content: center !important;
        text-align: center;
    }
    @keyframes pulse {
        0%, 100% { height: 8px; }
        50% { height: 28px; }
    }
    .bar {
        width: 5px;
        background-color: #3182CE;
        margin: 0 4px;
        border-radius: 3px;
    }
    </style>
""", unsafe_allow_html=True)

# عرض حالة الهوية الرقمية في الأعلى إذا كان مسجلاً للدخول
if str_lib.session_state.logged_in:
    str_lib.markdown("<div style='background-color: #C6F6D5; padding: 12px; border-radius: 6px; text-align: center; color: #22543D; font-weight: bold; font-family: Segoe UI; border: 1px solid #48BB78; width: 100%; margin-bottom: 15px;'>✓ تم التحقق وتفعيل الهوية الرقمية بنجاح <br> الضامن: أحمد عبدالله (ملف ضامن نشط)</div>", unsafe_allow_html=True)

# إنشاء أعمدة لوضع الأزرار بجانب بعضها البعض
col_login, col_voice = str_lib.columns(2)

with col_login:
    if not str_lib.session_state.logged_in:
        if str_lib.button("🔐 دخول عبر UAE Pass", type="primary", use_container_width=True, key="main_login_btn"):
            str_lib.session_state.logged_in = True
            str_lib.rerun()
    else:
        str_lib.button("🔒 الهوية الرقمية نشطة", type="secondary", use_container_width=True, disabled=True, key="disabled_active_btn")

with col_voice:
    if not str_lib.session_state.asked_before:
        if str_lib.button("🎙️ اضغط هنا للتحدث الآن", use_container_width=True, key="start_rec_btn"):
            str_lib.session_state.is_recording = True
            str_lib.session_state.asked_before = False
            str_lib.session_state.trigger_process = False
            str_lib.session_state.authorized = False
            str_lib.rerun()
    else:
        if str_lib.button("🔄 تصفير وتحدث مجدداً", use_container_width=True, key="reset_rec_btn"):
            str_lib.session_state.asked_before = False
            str_lib.session_state.trigger_process = False
            str_lib.session_state.is_recording = False
            str_lib.session_state.authorized = False
            str_lib.rerun()

# اختيار اللهجة الموائمة أسفل الأزرار المباشرة
dialect = str_lib.radio("", ["🇦🇪 لهجة إماراتية", "🇱🇧 لهجة لبنانية", "🇪🇬 لهجة مصرية"], horizontal=True, label_visibility="collapsed", key="user_dialect_selection")

# معالجة الأنيميشن الصوتي والانتظار دون تجميد الصفحة
if str_lib.session_state.is_recording and not str_lib.session_state.asked_before:
    str_lib.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; background-color: #1A202C; padding: 10px; border-radius: 6px; height: 45px; margin-top: 10px;'>
            <div class='bar' style='animation: pulse 0.6s infinite 0.1s;'></div>
            <div class='bar' style='animation: pulse 0.5s infinite 0.3s;'></div>
            <div class='bar' style='animation: pulse 0.7s infinite 0.2s;'></div>
            <div class='bar' style='animation: pulse 0.4s infinite 0.4s;'></div>
            <div class='bar' style='animation: pulse 0.6s infinite 0.1s;'></div>
            <div class='bar' style='animation: pulse 0.8s infinite 0.5s;'></div>
            <div class='bar' style='animation: pulse 0.5s infinite 0.2s;'></div>
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(2.5)
    str_lib.session_state.is_recording = False
    str_lib.session_state.asked_before = True
    str_lib.session_state.trigger_process = True 
    str_lib.rerun()

# خطوة محاكاة قواعد البيانات والشركاء المربوطين
str_lib.write("---")
str_lib.markdown("<h3 style='text-align: center; direction: rtl;'>📊 محاكاة قواعد البيانات والشركاء المربوطين</h3>", unsafe_allow_html=True)

scenario_key = str_lib.selectbox("", [
    "🟢 الحالة 1: ملف ضامن مستوفي الشروط (نجاح واستحقاق تلقائي)",
    "🟡 الحالة 2: راتب الضامن أقل من الاشتراطات المعتمدة للاستضافة",
    "🔴 الحالة 3: عقد سكن الضامن غير مسجل أو منتهي في البلدية"
], index=0, label_visibility="collapsed", key="system_scenario_selection")

selected_id = "1"
if "الحالة 2" in scenario_key: selected_id = "2"
elif "الحالة 3" in scenario_key: selected_id = "3"
# تفعيل منطق تفويض حوكمة الوكيل الذكي وعرض الـ Logs بناء على تسجيل الدخول
if str_lib.session_state.trigger_process:
    
    # 1. إذا كان المستخدم غير مسجل دخول: يظهر اللوج ومعه زر الدخول الفوري المدمج أسفله
    if not str_lib.session_state.logged_in:
        str_lib.write("---")
        str_lib.markdown("<h4 style='text-align: right; direction: rtl; color: #0F1E36;'>🖥️ شاشة رصد وتحليلات الوكيل الذكي الاستباقي (ICP Agent Log)</h4>", unsafe_allow_html=True)
        
        voice_text = "أبا أسوي فيزا زيارة حق أمي الله يخليك" if "إماراتية" in dialect else ("بدي قدم على تأشيرة زيارة لإمي لو سمحت" if "لبنانية" in dialect else "عايز أعمل تأشيرة زيارة لوالدتي لو تكرّمت")
        
        html_content = "<div style='background-color: #1A202C; padding: 20px; border-radius: 8px; border: 2px solid #D4AF37; min-height: 250px;'>"
        lines = [
            get_rtl_html(f"\"{voice_text}\"", tag_text="[🎙️ المدخل الصوتي المكتشف]:"),
            get_rtl_html("جاري معالجة نية المتعامل وتحليل اللهجة المحلية الممررة سحابياً.", tag_text="[🧠 معالجة اللغات]:"),
            get_rtl_html("النية المكتشفة هي طلب إصدار تأشيرة زيارة أقارب (الأم).", tag_text="[🎯 الفحص الذكي]:"),
            get_rtl_html("تنبيـه الحوكمة الأمنية - لم يتم كشف هوية رقمية نشطة بالمنصة.", is_error=True, tag_text="[🚫 حماية البيانات]:"),
            get_rtl_html("يرجى تسجيل الدخول الفوري عبر الزر المتاح أدناه للربط السيادي واستكمال الفحص آلياً دون الحاجة للصعود للأعلى.", is_error=True, tag_text="[🔒 إجراء أمني مطلوب]:")
        ]
        
        full_html = html_content + "".join(lines) + "</div>"
        str_lib.markdown(full_html, unsafe_allow_html=True)
        
        str_lib.write("")
        if str_lib.button("🔐 تسجيل دخول فوري ومتابعة الحوكمة والربط", type="primary", use_container_width=True, key="terminal_login_btn"):
            str_lib.session_state.logged_in = True
            str_lib.rerun()

    # 2. إذا كان مسجل دخول لكن لم يعطِ التفويض والحوكمة بعد: تظهر نافذة الحוكمة
    elif str_lib.session_state.logged_in and not str_lib.session_state.authorized:
        str_lib.write("---")
        str_lib.markdown("""
            <div style='text-align: right; direction: rtl; background-color: #F7FAFC; padding: 15px; border-radius: 8px; color: #2B6CB0; font-weight: bold; font-family: Segoe UI; border-right: 5px solid #3182CE; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
                🧠 <b>تفويض حوكمة الوكيل الذكي (Contextual Authorization):</b><br>
                لقد رصد النظام رغبتك في التقديم على خدمة <span style='color: #D4AF37;'>[تأشيرة زيارة الأم]</span>.<br><br>
                هل تمنح الوكيل الذكي تفويضاً قانونياً للاتصال بالشركاء وسحب وثائقك الرسمية من الوزارات لإتمام المعاملة فوراً؟
            </div>
        """, unsafe_allow_html=True)
        str_lib.write("")
        
        col_auth_yes, col_auth_no = str_lib.columns(2)
        with col_auth_yes:
            if str_lib.button("✅ نعم، أمنح التفويض وأبدأ المعاملة آلياً", use_container_width=True, key="grant_auth_btn"):
                str_lib.session_state.authorized = True
                str_lib.rerun() 
        with col_auth_no:
            if str_lib.button("❌ لا، إلغِ هذا الطلب", use_container_width=True, key="deny_auth_btn"):
                str_lib.session_state.asked_before = False
                str_lib.session_state.trigger_process = False
                str_lib.session_state.authorized = False
                str_lib.rerun()

    # 3. إذا كان مسجل دخول ومفوض: يبدأ عرض شاشة الفحص والتحليل الكامل والنهائي بدون تكرار
    elif str_lib.session_state.logged_in and str_lib.session_state.authorized:
        str_lib.write("---")
        str_lib.markdown("<h4 style='text-align: right; direction: rtl; color: #0F1E36;'>🖥️ شاشة رصد وتحليلات الوكيل الذكي الاستباقي (ICP Agent Log)</h4>", unsafe_allow_html=True)
        
        voice_text = "أبا أسوي فيزا زيارة حق أمي الله يخليك" if "إماراتية" in dialect else ("بدي قدم على تأشيرة زيارة لإمي لو سمحت" if "لبنانية" in dialect else "عايز أعمل تأشيرة زيارة لوالدتي لو تكرّمت")
        
        terminal_placeholder = str_lib.empty()
        html_content = "<div style='background-color: #1A202C; padding: 20px; border-radius: 8px; border: 2px solid #D4AF37; min-height: 250px;'>"
        
        lines = [
            get_rtl_html(f"\"{voice_text}\"", tag_text="[🎙️ المدخل الصوتي المكتشف]:"),
            get_rtl_html("جاري معالجة نية المتعامل وتحليل اللهجة المحلية الممررة سحابياً.", tag_text="[🧠 معالجة اللغات]:"),
            get_rtl_html("النية المكتشفة هي طلب إصدار تأشيرة زيارة أقارب (الأم).", tag_text="[🎯 الفحص الذكي]:"),
            get_rtl_html("الهوية الرقمية نشطة ومفوضة قانونياً. البدء فوراً في جلب ومطابقة سجلات الشركاء تلقائياً للضامن:", tag_text="[🚀 الوكيل الذكي]:"),
            get_rtl_html("جاري فتح منفذ آمن ومخاطبة أنظمة وزارة الموارد البشرية والتوطين سحابياً...", tag_text="[💼 ربط حكومي - MOHRE]:")
        ]
        
        current_sc = government_scenarios[selected_id]
        lines.extend([
            get_rtl_html(f"تم جلب شهادة راتب الضامن الرقمية الموثقة بقيمة: {current_sc['salary']:,} درهم إماراتي.", tag_text="[📋 استجابة الشريك]:"),
            get_rtl_html("جاري فتح منفذ آمن ومخاطبة أنظمة دائرة الأراضي والأملاك والبلديات المحلية...", tag_text="[🏠 ربط حكومي - دائرة الأراضي والبلديات]:"),
            get_rtl_html(f"حالة سكن الضامن المسجل سحابياً: {current_sc['contract_details']}", tag_text="[📋 استجابة الشريك]:"),
            get_rtl_html("فحص حوكمة البيانات ومطابقة الاشتراطات والسياسات المعتمدة للهيئة الاتحادية.", tag_text="[⚖️ التدقيق الذاتي]:")
        ])
        
        if selected_id == "2":
            lines.extend([
                get_rtl_html("قرار الوكيل الذكي هو تعليق الطلب واعتذار تلقائي للمتعامل.", is_error=True, tag_text="[❌ قرار النظام]:"),
                get_rtl_html("الراتب المرصود بملف الضامن الرقمي أقل من الحد الأدنى المعتمد للاستضافة وهو 10,000 درهم.", is_error=True, tag_text="[سبب التعليق]:"),
                get_rtl_html("نعتذر منك يا أحمد، لا يمكننا إتمام الطلب لأن راتبك الحالي كضامن أقل من المتطلبات المالية التي وضعتها الهيئة للاستضافة الأسرية.", is_error=True, tag_text="[💬 الرد الصوتي المقترح]:")
            ])
        elif selected_id == "3":
            lines.extend([
                get_rtl_html("قرار الوكيل الذكي هو تعليق الطلب واعتذار تلقائي للمتعامل.", is_error=True, tag_text="[❌ قرار النظام]:"),
                get_rtl_html("لم يتم العثور على عقد سكن أو عقد إيجاري معتمد فعال باسم الضامن لدى البلديات المحلية.", is_error=True, tag_text="[سبب الرفض]:"),
                get_rtl_html("نعتذر منك، لم نجد عقد إيجار موثق مسجل باسم الضامن، وهو أحد المتطلبات الأساسية لإصدار تأشيرة الزيارة للاستضافة الأسرية.", is_error=True, tag_text="[💬 الرد الصوتي المقترح]:")
            ])
        else:
            lines.extend([
                get_rtl_html("تم إنجاز وتدقيق المعاملة الاستباقية بنجاح واقتدار بناءً على تفويض ملف الضامن المعتمد.", tag_text="[🎉 قرار النظام]:"),
                get_rtl_html("تم صياغة المعاملة وإرسالها مباشرة لنظام التدقيق النهائي والاعتماد الداخلي بالهيئة.", tag_text="[📋 القرار التشغيلي]:"),
                get_rtl_html("إرسال إشعار فوري وتنبيه لهاتف الضامن لسداد الرسوم المالية المقررة والاعتماد اللحظي.", tag_text="[💬 الإجراء القادم]:")
            ])

        # تشغيل حلقة العرض التدريجي لمرة واحدة وبثبات تام
        for i in range(len(lines)):
            current_html = html_content + "".join(lines[:i+1]) + "</div>"
            terminal_placeholder.markdown(current_html, unsafe_allow_html=True)
            time.sleep(0.9)
