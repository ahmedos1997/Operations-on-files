import re

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


credential = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scope)
file = gspread.authorize(credential)

new_file = file.open('example')

worksheet = new_file.worksheet('sheet1')

worksheet.update_cell(8, 2, '=sum(B2:B7)')
worksheet.update_cell(9, 2, '=max(B2:B7)')
worksheet.update_cell(9, 2, '=AVERAGE(B2:B7)')
# طريقة معرفة ماهي الدالة المستخدمة في خلية معينة

cell = worksheet.acell('B8', value_render_option='FORMULA').value
print(cell)

