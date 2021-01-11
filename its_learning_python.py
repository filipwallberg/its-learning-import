import csv

with open('import.csv') as csv_file:

	csv_reader = csv.reader(csv_file, delimiter=';')
	line_count = 0
	uge = ""

	print('<?xml version="1.0" encoding="utf-8"?>\n<plan xmlns="xsdLessonPlan">\n  <columns xmlns="">\n    <theme_columns>\n      <column id="19312" colType="1" colName="" showOnCoursePage="false" visibleFor="everyone" />\n      <column id="19324" colType="0" colName="Description" showOnCoursePage="false" visibleFor="everyone" />\n    </theme_columns>\n    <lesson_columns>\n      <column id="19315" colType="13" colName="" showOnCoursePage="true" visibleFor="everyone" />\n      <column id="19316" colType="3" colName="" showOnCoursePage="true" visibleFor="everyone" />\n      <column id="19317" colType="5" colName="" showOnCoursePage="true" visibleFor="everyone" />\n      <column id="19319" colType="4" colName="" showOnCoursePage="true" visibleFor="everyone" />\n      <column id="19321" colType="8" colName="" showOnCoursePage="true" visibleFor="everyone" />\n      <column id="19322" colType="9" colName="" showOnCoursePage="true" visibleFor="everyone" />\n      <column id="19323" colType="12" colName="" showOnCoursePage="true" visibleFor="everyone" />\n    </lesson_columns>\n  </columns>\n  <themes xmlns="">')

	for row in csv_reader:
		if line_count == 0:
			line_count += 1
		else:
			if(len({row[0]}) >0):
				if(uge == ""):
					print(f'    <theme themeId="2667">\n      <title>Uge {row[0]}</title>\n      <lessons>')
					uge = row[0]
				if(uge != row[0]):
					print(f'      </lessons>\n    </theme>\n    <theme themeId="2667">\n      <title>Uge {row[0]}</title>\n      <lessons>')
					uge = row[0]

				print(f'        <lesson lessonId="6354">')
				print(f'          <name>{row[2]}</name>')
				print(f'          <start>{row[1]}T08:15:00</start>')
				print(f'          <stop>{row[1]}T14:00:00</stop>')
				print('        </lesson>')
			
	print('      </lessons>\n    </theme>\n  </themes>\n</plan>')