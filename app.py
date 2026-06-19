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

# هيدر فخم ونظيف جداً بدون أي شعار بصري لتوفير أقصى درجات الراحة والوقار للعين
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

government_scenarios = {
    "1": {"salary": 25000, "has_contract": True, "contract_details": "عقد إيجار موثق (إيجاري) فعال ومطابق لكافة معايير الاستضافة"},
    "2": {"salary": 4500, "has_contract": True, "contract_details": "عقد إيجار موثق (إيجاري) فعال ومطابق لكافة معايير الاستضافة"},
    "3": {"salary": 18000, "has_contract": False, "contract_details": "لا يوجد عقد سكن فعال مسجل باسم الضامن في البلديات"}
}
str_lib.write("")
# خطوة 1: التحقق الرقمي ومحاذاة مركزية مريحة للعين
str_lib.markdown("<h3 style='text-align: center; direction: rtl;'>🔒 خطوة 1: التحقق الرقمي والربط السيادي</h3>", unsafe_allow_html=True)
if not str_lib.session_state.logged_in:
    if str_lib.button("🔐 تسجيل الدخول عبر الهوية الرقمية UAE Pass", type="primary", use_container_width=True):
        str_lib.session_state.logged_in = True
        str_lib.rerun()
else:
    str_lib.markdown("<div style='background-color: #C6F6D5; padding: 12px; border-radius: 6px; text-align: center; color: #22543D; font-weight: bold; font-family: Segoe UI; border: 1px solid #48BB78; width: 100%;'>✓ تم التحقق وتفعيل الهوية الرقمية بنجاح <br> الضامن: أحمد عبدالله (ملف نشط)</div>", unsafe_allow_html=True)

# خطوة 2: محاكاة السجلات بالتوسيط البصري التام
str_lib.write("")
str_lib.markdown("<h3 style='text-align: center; direction: rtl;'>📊 خطوة 2: محاكاة قواعد البيانات والشركاء المربوطين</h3>", unsafe_allow_html=True)

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
    /* كود تحريك الأشرطة الصوتية نيون حيوياً داخل المتصفح */
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

scenario_key = str_lib.selectbox("", [
    "🟢 الحالة 1: ملف ضامن مستوفي الشروط (نجاح واستحقاق تلقائي)",
    "🟡 الحالة 2: راتب الضامن أقل من الاشتراطات المعتمدة للاستضافة",
    "🔴 الحالة 3: عقد سكن الضامن غير مسجل أو منتهي في البلدية"
], index=0, label_visibility="collapsed")

selected_id = "1"
if "الحالة 2" in scenario_key: selected_id = "2"
elif "الحالة 3" in scenario_key: selected_id = "3"

# خطوة 3: منطقة الميكروفون والموجة التفاعلية المدمجة بنسبة 100%
str_lib.write("")
str_lib.markdown("<h3 style='text-align: center; direction: rtl;'>🎙️ خطوة 3: معالجة اللغات الطبيعية ومطابقة نبرة الصوت</h3>", unsafe_allow_html=True)

dialect = str_lib.radio("", ["🇦🇪 لهجة إماراتية", "🇱🇧 لهجة لبنانية", "🇪🇬 لهجة مصرية"], horizontal=True, label_visibility="collapsed")

# حقن الأشرطة المتحركة كودياً بداخل الصندوق الأسود لتتحرك حقيقة دون صور خارجية مكسورة
if str_lib.session_state.is_recording:
    str_lib.markdown("""
        <div style='display: flex; justify-content: center; align-items: center; background-color: #1A202C; padding: 10px; border-radius: 6px; height: 45px;'>
            <div class='bar' style='animation: pulse 0.6s infinite 0.1s;'></div>
            <div class='bar' style='animation: pulse 0.5s infinite 0.3s;'></div>
            <div class='bar' style='animation: pulse 0.7s infinite 0.2s;'></div>
            <div class='bar' style='animation: pulse 0.4s infinite 0.4s;'></div>
            <div class='bar' style='animation: pulse 0.6s infinite 0.1s;'></div>
            <div class='bar' style='animation: pulse 0.8s infinite 0.5s;'></div>
            <div class='bar' style='animation: pulse 0.5s infinite 0.2s;'></div>
        </div>
    """, unsafe_allow_html=True)
else:
    str_lib.markdown("<div style='background-color: #1A202C; padding: 10px; text-align: center; border-radius: 6px; color: #4A5568; font-weight: bold; letter-spacing: 2px;'>🚨 الميكروفون في وضع السكون - اضغط بالأسفل للتحدث</div>", unsafe_allow_html=True)
str_lib.write("")

if str_lib.button("🎙️ اضغط هنا للتحدث الآن والبدء الفوري", use_container_width=True):
    str_lib.session_state.is_recording = True
    str_lib.rerun()
# معالجة ثواني الاستماع وإطفاء الموجة آلياً بعد انتهاء النطق
if str_lib.session_state.is_recording and not str_lib.session_state.asked_before:
    time.sleep(3.0) 
    str_lib.session_state.is_recording = False
    str_lib.session_state.asked_before = True
    if not str_lib.session_state.logged_in:
        str_lib.session_state.trigger_process = True
    str_lib.rerun()

# تفويض حوكمة الوكيل الذكي (سؤال نعم/لا الموسط)
if str_lib.session_state.logged_in and str_lib.session_state.asked_before and not str_lib.session_state.trigger_process:
    str_lib.write("---")
    str_lib.markdown("""
        <div style='text-align: right; direction: rtl; background-color: #F7FAFC; padding: 15px; border-radius: 8px; color: #2B6CB0; font-weight: bold; font-family: Segoe UI; border-right: 5px solid #3182CE; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
            🧠 <b>تفويض حوكمة الوكيل الذكي (Contextual Authorization):</b><br>
            لقد رصد النظام رغبتك في التقديم على خدمة <span style='color: #D4AF37;'>[تأشيرة زيارة الأم]</span>.<br><br>
            هل تمنح الوكيل الذكي تفويضاً قانونياً للاتصال بالشركاء وسحب وثائقك الرسمية من الوزارات لإتمام المعاملة فوراً؟
        </div>
    """, unsafe_allow_html=True)
    str_lib.write("")
    
    col1, col2 = str_lib.columns(2)
    with col1:
        if str_lib.button("✅ نعم، أمنح التفويض وأبدأ المعاملة آلياً", use_container_width=True):
            str_lib.session_state.trigger_process = True
            str_lib.rerun() 
    with col2:
        if str_lib.button("❌ لا، إلغِ هذا الطلب", use_container_width=True):
            str_lib.session_state.asked_before = False
            str_lib.session_state.trigger_process = False
            str_lib.rerun()

# شاشة الرصد وفحص الشركاء بتوقيت التدفق الواقعي الصارم
if str_lib.session_state.trigger_process:
    str_lib.write("")
    str_lib.markdown("<h4 style='text-align: right; direction: rtl; color: #0F1E36;'>🖥️ شاشة رصد وتحليلات الوكيل الذكي الاستباقي (ICP Agent Log)</h4>", unsafe_allow_html=True)
    
    if "إماراتية" in dialect:
        voice_text = "أبا أسوي فيزا زيارة حق أمي الله يخليك"
    elif "لبنانية" in dialect:
        voice_text = "بدي قدم على تأشيرة زيارة لإمي لو سمحت"
    else:
        voice_text = "عايز أعمل تأشيرة زيارة لوالدتي لو تكرّمت"
        
    terminal_placeholder = str_lib.empty()
    html_content = "<div style='background-color: #1A202C; padding: 20px; border-radius: 8px; border: 2px solid #D4AF37; min-height: 250px;'>"
    
    lines = [
        get_rtl_html(f"\"{voice_text}\"", tag_text="[🎙️ المدخل الصوتي المكتشف]:"),
        get_rtl_html("جاري معالجة نية المتعامل وتحليل اللهجة المحلية الممررة سحابياً.", tag_text="[🧠 معالجة اللغات]:"),
        get_rtl_html("النية المكتشفة هي طلب إصدار تأشيرة زيارة أقارب (الأم).", tag_text="[🎯 الفحص الذكي]:")
    ]
    
    if not str_lib.session_state.logged_in:
        lines.extend([
            get_rtl_html("تنبيـه الحوكمة الأمنية - لم يتم كشف هوية رقمية نشطة بالمنصة.", is_error=True, tag_text="[🚫 حماية البيانات]:"),
            get_rtl_html("لإصدار هذه التأشيرة آلياً تطلب أنظمة الهيئة الاشتراطات والضوابط التالية:", is_error=True, tag_text="[📋 الاشتراطات المطلوبة]:"),
            get_rtl_html("فحص الراتب الشهري المعتمد لملف الضامن بحيث لا يقل عن عشرة آلاف درهم إماراتي.", is_error=True, tag_text="[💼 الشرط الأول - وزارة التوطين]:"),
            get_rtl_html("فحص صلاحية وتوثيق عقد سكن الضامن المسجل في السجلات السحابية للبلديات.", is_error=True, tag_text="[🏠 الشرط الثاني - البلديات المحلية]:"),
            get_rtl_html("يرجى تسجيل الدخول عبر الهوية الرقمية (UAE Pass) أولاً ليتمكن النظام من إتمام فحص الشركاء المترابطين.", is_error=True, tag_text="[🔒 إجراء أمني مطلوب]:")
        ])
        str_lib.session_state.trigger_process = False
    else:
        current_sc = government_scenarios[selected_id]
        lines.extend([
            get_rtl_html("الهوية الرقمية نشطة ومفوضة قانونياً. البدء فوراً في جلب ومطابقة سجلات الشركاء تلقائياً للضامن:", tag_text="[🚀 الوكيل الذكي]:"),
            get_rtl_html("جاري فتح منفذ آمن ومخاطبة أنظمة وزارة الموارد البشرية والتوطين سحابياً...", tag_text="[💼 ربط حكومي - MOHRE]:"),
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

    # انطلاق تأثير التدفق التتابعي التدريجي الفاخر
    for i in range(len(lines)):
        current_html = html_content + "".join(lines[:i+1]) + "</div>"
        terminal_placeholder.markdown(current_html, unsafe_allow_html=True)
        time.sleep(1.3)
