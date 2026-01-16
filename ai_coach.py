from digital_detox import guide_digital_detox
from small_jobs import small_jobs_guide
from sufficiency import sufficiency_guide
from support import support_section

def ai_route(profile):
    result = "## 🧭 แผนชีวิตเบื้องต้น\n\n"

    if profile["age_group"] == "เด็ก/วัยรุ่น (ต่ำกว่า 18)":
        result += guide_digital_detox(profile)
        result += support_section()
        return result

    result += small_jobs_guide()
    result += "\n"
    result += sufficiency_guide(profile["place"])
    result += "\n### 🧠 มุมมอง\nเริ่มเล็ก แต่ทำจริง ชีวิตจะค่อย ๆ ขยับ\n\n"
    result += support_section()

    return result
