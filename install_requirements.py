from xblog.settings_pro import PRODUCTION_SECRET_FILE
import os

if True == os.path.exists(PRODUCTION_SECRET_FILE):
	os.system("pip install -r ./requirements/pro.txt")
else:
	os.system("pip install -r ./requirements/dev.txt")
