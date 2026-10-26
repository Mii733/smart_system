import sys
from cx_Freeze import setup, Executable

# إعداد الحزم التي يحتاجها التطبيق.
build_exe_options = {
    "packages": ["os", "django", "waitress", "crispy_forms", "static", "templates"],  # اضغط على الحزم التي تحتاجها
    "include_files": ["static", "templates", "media"],  # إذا كان لديك ملفات ثابتة تحتاج إلى تضمينها.
}

# إعداد السكربت الرئيسي الخاص بك (عادةً manage.py في Django)
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # لا تظهر نافذة التيرمينال عند تشغيل exe على Windows

setup(
    name="MyDjangoApp",
    version="1.0",
    description="My Django Application Converted to EXE",
    options={"build_exe": build_exe_options},
    executables=[Executable("manage.py", base=base)],
)
