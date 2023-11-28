from panoptes_client import Panoptes, Project, SubjectSet, Subject
import sys

## This is to test the golden sample and how we can make it work for multiple choices questions

Panoptes.connect(username='XXXX', password='XXXXX')

tutorial_project = Project.find("18664")

print(tutorial_project.display_name)

subject_set = SubjectSet.find(114311)

XRT_info = []
i_XRT = 0
f_XRT = open('XRT_position.txt','r')
for line in f_XRT.readlines():
	if '#' not in line[0]:
		column = line.split('|')
		GRBname = 'GRB' + column[0].split()[1]
		RA = column[1]
		DEC = column[2]
		if ('N/A' not in RA):
			XRT_info.append([])
			XRT_info[i_XRT].append(GRBname)
			XRT_info[i_XRT].append(RA)
			XRT_info[i_XRT].append(DEC)

			i_XRT += 1
f_XRT.close

f_BATlocation = open('/Users/alien/work/Individual_study/Swift_3rdBATcatalog/event/summary_cflux/summary_general_info/summary_general.txt','r')
i_BAT = 0
BAT_info = []
for line in f_BATlocation.readlines():
	if '#' not in line[0]:
		column = line.split('|')
		GRBname = column[0].strip()
		if ('N/A' not in column[4]):
			RA = '%.4f' % float(column[4])
			DEC = '%.4f' % float(column[5])
		else:
			RA = 'N/A'
			DEC = 'N/A'

		BAT_info.append([])
		BAT_info[i_BAT].append(GRBname)
		BAT_info[i_BAT].append(RA)
		BAT_info[i_BAT].append(DEC)
		i_BAT += 1
f_BATlocation.close


#lc_dir = '/Users/alien/work/Individual_study/Citizen_science/Zooniverse/lc'
lc_dir = '/Users/alien/work/Individual_study/Citizen_science/citizen_scientist_plot/lc'
GRBcat_web = 'https://swift.gsfc.nasa.gov/results/batgrbcat/'
XRT_web = 'https://www.swift.ac.uk/xrt_live_cat/'
keys = []
values = []
f_input = open('GRB_list_test.txt','r')
for line in f_input.readlines():
        if '#' not in line[0]:
            column = line.split('_')
            GRBname = column[0]
            trigid = column[1].split('.')[0].strip()

            if(len(trigid)<7):
                trigid_XRT = '00' + trigid
            else:
                trigid_XRT = '0' + trigid

            #print(GRBname, trigid)
            keys.append(lc_dir + '/' + GRBname + '_' + trigid + '.png')

            RA = 'N/A'
            DEC = 'N/A'

            for i_BAT in range(len(BAT_info)):
                if (GRBname == BAT_info[i_XRT][0]):
                    RA = BAT_info[i_XRT][1].strip()
                    DEC = BAT_info[i_XRT][2].strip()

            #XRT_pos_SIMBAD_search = 'Location not precise enough for SIMBAD search.'   
            ## XRT position, search radius = 3 arcmin
            for i_XRT in range(len(XRT_info)):
                if (GRBname == XRT_info[i_XRT][0]):
                    RA = XRT_info[i_XRT][1].strip()
                    DEC = XRT_info[i_XRT][2].strip()
                    #we simply use GRBname for SIMBAD search
                    #XRT_pos_SIMBAD_search = 'http://simbad.u-strasbg.fr/simbad/sim-basic?Ident=' + RA_XRT + '+' + DEC_XRT + '+%28radius%3D3+arcmin%29&submit=SIMBAD+search'


            successMessage = 'Yes!'
            failureMessage = f'Missed this is a {s[0o]}. A {s[0]} is {'

            inside_dicts = {'GRB Location':'RA:' + RA + ', DEC:' + DEC,
                'BAT light curve':GRBcat_web + '/' + GRBname + '/web/' + GRBname + '.html#lc',
                'X-ray light curve':'https://www.swift.ac.uk/xrt_live_cat/' + trigid_XRT,
                'SIMBAD': 'https://simbad.u-strasbg.fr/simbad/sim-id?Ident=' + GRBname + '&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id',
                '#feedback_1_answer': str(2),
                '#feedback_1_successMessage': successMessage,
                '#feedback_1_failureMessage': failureMessage,
                '#feedback_2_answer': str(3),
                '#feedback_2_successMessage': successMessage,
                '#feedback_2_failureMessage': failureMessage
                }
            values.append(inside_dicts)

f_input.close

subject_metadata = {}

for i in range(len(keys)):
	subject_metadata[keys[i]] = values[i]

new_subjects = []

for filename, metadata in subject_metadata.items():
    subject = Subject()

    print(filename)
    print(metadata)

    subject.links.project = tutorial_project
    subject.add_location(filename)

    subject.metadata.update(metadata)

    subject.save()
    new_subjects.append(subject)

subject_set.add(new_subjects)
