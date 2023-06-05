import sys
from os.path import join

from settings import proj_settings

python_version = sys.version_info.major
db_path = join(proj_settings.PROJECT_ROOT, 'database', 'data.db')
export_csv_path = join(proj_settings.PROJECT_ROOT, 'database', 'data.csv')

